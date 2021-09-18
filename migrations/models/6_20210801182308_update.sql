-- upgrade --
CREATE TABLE IF NOT EXISTS "profile" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "last_name" VARCHAR(100)   DEFAULT '',
    "date_join" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "last_login" TIMESTAMPTZ,
    "username_id" INT NOT NULL UNIQUE REFERENCES "user" ("id") ON DELETE CASCADE
);
COMMENT ON TABLE "profile" IS 'Model user ';
-- downgrade --
DROP TABLE IF EXISTS "profile";
