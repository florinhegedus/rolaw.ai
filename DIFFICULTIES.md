# Problem #1: MongoDB Container Not Starting
## Description
The MongoDB docker container starts and exits automatically. This happened when changing the `user` and `password` in `docker-compose.yml`.
```
- MONGODB_INITDB_ROOT_USERNAME=old-user
- MONGODB_INITDB_ROOT_PASSWORD=old-pass
```

To reproduce:
```bash
make local-docker-infrastructure-stop
# update `user` and `password` in docker-compose.yml
make local-docker-infrastructure-up
docker ps  # no container running
```

To change the mongodb user and password, I followed: [stackoverflow](https://stackoverflow.com/questions/76201574/how-to-change-mongodb-password-in-docker-compose). 

```bash
# run bash inside `docker-local_dev_atlas-1` container
docker exec -it docker-local_dev_atlas-1 bash
# connect to `admin` db
mongosh admin -u old_user -p old_pass
# create user with desired username and password
db.createUser({
  user: "new_user",
  pwd: "new_pass",
  roles: [ { role: "root", db: "admin" } ]
})
```
