-- an sql script rankining country origins
-- of bandds ordered by the number of non unique fans
SELECT `origin`, SUM(`fans`) as nb_fans from metal_bands
GROUP BY origin ORDER BY nb_fans DESC;
