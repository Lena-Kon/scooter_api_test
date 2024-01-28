SELECT c.login, count(o.id)
FROM "Couriers" c
JOIN "Orders" o on (o."courierId" = c.id) AND o."inDelivery" = true
GROUP BY c.login;

SELECT c.login, count(o.id)
FROM "Couriers" c
JOIN "Orders" o on (o."courierId" = c.id) AND o."inDelivery" = true
GROUP BY c.login;
