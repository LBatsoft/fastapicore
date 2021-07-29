-- upgrade --
ALTER TABLE "user" ALTER COLUMN "last_name" SET DEFAULT '';
ALTER TABLE "user" ALTER COLUMN "first_name" SET DEFAULT '';
-- downgrade --
ALTER TABLE "user" ALTER COLUMN "last_name" DROP DEFAULT;
ALTER TABLE "user" ALTER COLUMN "first_name" DROP DEFAULT;
