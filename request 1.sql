SELECT c.login, COUNT(*)
FROM "Couriers"
      AS c INNER JOIN "Orders"
      AS o ON o."courierId" = c.id
   WHERE o."inDelivery" = true
GROUP BY c.login;