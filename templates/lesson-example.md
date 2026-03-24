# Snowflake Recursive CTEs Reject Correlated Subqueries

**Discovered**: March 2026
**Context**: Snowflake SQL, recursive CTEs, org hierarchy queries

## The Problem

You need to walk a parent-child tree (like an org hierarchy) from a flat table with `uuid` and `manager_uuid` columns. You write a recursive CTE and try to look up the manager's name with a correlated subquery — Snowflake rejects it.

## What You'll See

```sql
-- This correlated subquery FAILS in Snowflake recursive CTEs:
SELECT (SELECT name FROM employees WHERE uuid = org_tree.manager_uuid) AS manager_name
FROM org_tree
-- Error: Unsupported subquery type cannot be evaluated
```

## The Fix

Use a LEFT JOIN after the CTE instead of a correlated subquery:

```sql
WITH base AS (
    SELECT uuid FROM employees
    WHERE mail = 'manager@example.com' LIMIT 1
),
org_tree AS (
    SELECT p.uuid, p.name, p.manager_uuid, 0 AS level,
           CAST(p.uuid AS VARCHAR) AS path
    FROM employees p JOIN base b ON p.uuid = b.uuid
    UNION ALL
    SELECT e.uuid, e.name, e.manager_uuid, t.level + 1,
           t.path || '>' || e.uuid
    FROM org_tree t JOIN employees e ON e.manager_uuid = t.uuid
    WHERE e.uuid != e.manager_uuid  -- prevent self-referencing loops
      AND t.level < 8               -- depth limit
      AND t.path NOT LIKE '%' || e.uuid || '%'  -- cycle detection
)
SELECT o.name, o.level,
       COALESCE(m.name, '') AS manager_name
FROM org_tree o
LEFT JOIN employees m ON m.uuid = o.manager_uuid  -- JOIN, not subquery
ORDER BY o.level, o.name
```

Three safeguards to always include:
- `e.uuid != e.manager_uuid` — prevents infinite loops from self-managers
- `t.level < 8` — hard depth limit
- `t.path NOT LIKE '%' || e.uuid || '%'` — cycle detection via path tracking

## Why This Happens

Snowflake's SQL compiler doesn't support correlated subqueries in recursive CTE output positions. The workaround is always to JOIN after the CTE completes. Cycle detection is necessary because real org data can have circular references during reorgs.

## Recommendation

Always use LEFT JOIN for lookups against the source table in recursive CTEs, never correlated subqueries. Include all three cycle-protection safeguards.

<!-- QUIRK: Snowflake rejects correlated subqueries in recursive CTE output -->
<!-- WHEN: Trying to look up a parent/manager name inside a recursive CTE -->
<!-- WRONG: SELECT (SELECT name FROM table WHERE uuid = cte.manager_uuid) FROM cte -->
<!-- RIGHT: SELECT o.name, m.name FROM cte o LEFT JOIN table m ON m.uuid = o.manager_uuid -->
<!-- WHY: Snowflake's SQL compiler doesn't support correlated subqueries in this position -->
<!-- TAGS: snowflake, sql, recursive-cte -->

<!-- QUIRK: Recursive CTEs need three-layer cycle protection -->
<!-- WHEN: Walking org hierarchies or any parent-child tree in Snowflake -->
<!-- WRONG: Only checking t.level < N without self-ref or path checks -->
<!-- RIGHT: Check e.uuid != e.manager_uuid AND t.level < 8 AND t.path NOT LIKE '%' || e.uuid || '%' -->
<!-- WHY: Real org data can have self-referencing managers and circular reorg artifacts -->
<!-- TAGS: snowflake, sql, recursive-cte -->
