set schema 'snomedct';

DROP VIEW IF EXISTS view_concept;
CREATE VIEW view_concept AS 
select 
  -- row_number() over() as id,
  id as _id,
  effectivetime,
  active,
  moduleid,
  definitionstatusid 
from concept_f tbl 
where 
  tbl.effectiveTime = (
    select max(sub.effectiveTime) from concept_f sub where sub.id = tbl.id
  );

INSERT INTO public.django_snomed_conceptf     
 (_id,
  effectivetime,
  active,
  moduleid,
  definitionstatusid )
  SELECT * FROM snomedct.view_concept;

DROP VIEW IF EXISTS view_description;
CREATE VIEW view_description AS 
select 
  -- row_number() over() as id,
  id as _id,
  effectivetime,
  active,
  moduleid,
  conceptid,
  languagecode,
  typeid,
  term,
  casesignificanceid 
from description_f tbl 
where 
  tbl.effectiveTime = (
    select max(sub.effectiveTime) from description_f sub where sub.id = tbl.id
  );

INSERT INTO public.django_snomed_descriptionf   
 (_id,
  effectivetime,
  active,
  moduleid,
  conceptid,
  languagecode,
  typeid,
  term,
  casesignificanceid )
  SELECT * FROM snomedct.view_description;



DROP VIEW IF EXISTS view_relationship;
CREATE VIEW view_relationship AS 
select
  -- row_number() over() as id,
  id as _id,
  effectivetime,
  active,
  moduleid,
  sourceid,
  destinationid,
  relationshipgroup,
  typeid,
  characteristictypeid,
  modifierid
from relationship_f tbl 
where 
  tbl.effectiveTime = (
    select max(sub.effectiveTime) from relationship_f sub where sub.id = tbl.id
  );

INSERT INTO public.django_snomed_relationshipf (_id,
  effectivetime,
  active,
  moduleid,
  sourceid,
  destinationid,
  relationshipgroup,
  typeid,
  characteristictypeid,
  modifierid)
  SELECT * FROM snomedct.view_relationship;

/*
select
  COUNT(*),
  MAX(effectivetime),
  id
from 
description_f
where
  languagecode='es'
group by id
order by 1 desc,3
LIMIT 10;

select  
  *
from description_f
where id = '1056432019';
*/
