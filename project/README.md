# nd064_C1
[My forked repository](https://github.com/Heshmatkhah/nd064_course_1)

- **I have changed the Vagrant IP address to `192.168.7.230` due to conflict with my local network**.
- The health check endpoint check for the database existence of a table.
- The helm chart uses `service.port` value if no value is provided for `service.targetPort`.
- I have added `information` table to the database to store the total connection count. 
    This table was designed to be a generic key-value store. o store total connection count. this table designed to be a generic key-value store.
