SELECT c.login, COUNT(*)
FROM "Couriers"
    c INNER JOIN "Orders" o ON (o."courierId" = c.id)
    AND o."inDelivery" = true
GROUP BY c.login;
