let admin = db.getSiblingDB("admin");

admin.auth();
admin.createUser({
  user: "testUser",
  pwd: "testPass",
  roles: [
    {
      role: "root",
      db: "admin",
    },
  ],
});
