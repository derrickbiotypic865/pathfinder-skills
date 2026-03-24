# Snowflake -- Technical Quirks

triggers: [snowflake, snow, snowflake-connector, recursive CTE, SHOW GRANTS, externalbrowser]
updated: 2026-03-24
count: 2

---

### Correlated subqueries fail in recursive CTE output
**When:** Trying to look up a parent/manager name inside a recursive CTE in Snowflake
**Wrong:** `SELECT (SELECT name FROM table WHERE uuid = cte.manager_uuid) FROM cte`
**Right:** `SELECT o.name, m.name FROM cte o LEFT JOIN table m ON m.uuid = o.manager_uuid`
**Why:** Snowflake's SQL compiler doesn't support correlated subqueries in this position — use a LEFT JOIN after the CTE
*Source: recursive-cte-org-chart.md*

### Recursive CTEs need three-layer cycle protection
**When:** Walking org hierarchies or any parent-child tree in Snowflake
**Wrong:** Only checking `t.level < N` without self-ref or path checks
**Right:** Check `e.uuid != e.manager_uuid AND t.level < 8 AND t.path NOT LIKE '%' || e.uuid || '%'`
**Why:** Real org data can have self-referencing managers and circular reorg artifacts
*Source: recursive-cte-org-chart.md*
