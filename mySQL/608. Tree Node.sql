# Write your MySQL query statement below
SELECT id, "Root" AS type FROM tree WHERE p_id is null
UNION
SELECT id, "Inner" AS type FROM tree WHERE p_id IS NOT null AND id IN (SELECT p_id FROM tree WHERE p_id IS NOT null)
UNION
SELECT id, "Leaf" AS type FROM tree WHERE p_id IS NOT null AND id NOT IN (SELECT p_id FROM tree WHERE p_id IS NOT null)
ORDER BY id