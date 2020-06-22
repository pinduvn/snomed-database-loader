#!/bin/sh
cat create-database-postgres.pgsql | docker exec -i django-snomed_db_1 psql -U postgres
cat environment-postgresql.pgsql | docker exec -i django-snomed_db_1 psql -U postgres
cat indexing-postgres.pgsql | docker exec -i django-snomed_db_1 psql -U postgres
cat load-postgresql.pgsql | docker exec -i django-snomed_db_1 psql -U postgres
cat create-views.pgsql | docker exec -i django-snomed_db_1 psql -U postgres