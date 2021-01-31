PGDMP                           y         	   deaconfig "   11.10 (Ubuntu 11.10-1.pgdg18.04+1) "   11.10 (Ubuntu 11.10-1.pgdg18.04+1) O   �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                       false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                       false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                       false            �           1262    2903456 	   deaconfig    DATABASE     s   CREATE DATABASE deaconfig WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'C.UTF-8' LC_CTYPE = 'C.UTF-8';
    DROP DATABASE deaconfig;
             postgres    false            �           0    0    DATABASE deaconfig    ACL     /   GRANT ALL ON DATABASE deaconfig TO agdc_admin;
                  postgres    false    3545                        2615    2903461    agdc    SCHEMA        CREATE SCHEMA agdc;
    DROP SCHEMA agdc;
          
   agdc_admin    false            �           0    0    SCHEMA agdc    ACL     U   GRANT USAGE ON SCHEMA agdc TO agdc_user;
GRANT CREATE ON SCHEMA agdc TO agdc_manage;
               
   agdc_admin    false    8            �           1247    2903463    float8range    TYPE     g   CREATE TYPE agdc.float8range AS RANGE (
    subtype = double precision,
    subtype_diff = float8mi
);
    DROP TYPE agdc.float8range;
       agdc    
   agdc_admin    false    8                       1255    2903462    common_timestamp(text)    FUNCTION     �   CREATE FUNCTION agdc.common_timestamp(text) RETURNS timestamp with time zone
    LANGUAGE sql IMMUTABLE STRICT
    AS $_$
select ($1)::timestamp at time zone 'utc';
$_$;
 +   DROP FUNCTION agdc.common_timestamp(text);
       agdc    
   agdc_admin    false    8            �           0    0    FUNCTION common_timestamp(text)    ACL     @   GRANT ALL ON FUNCTION agdc.common_timestamp(text) TO agdc_user;
            agdc    
   agdc_admin    false    280                       1255    2903566    set_row_update_time()    FUNCTION     �   CREATE FUNCTION agdc.set_row_update_time() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
begin
  new.updated = now();
  return new;
end;
$$;
 *   DROP FUNCTION agdc.set_row_update_time();
       agdc    
   agdc_admin    false    8            �            1259    2903504    dataset    TABLE     [  CREATE TABLE agdc.dataset (
    id uuid NOT NULL,
    metadata_type_ref smallint NOT NULL,
    dataset_type_ref smallint NOT NULL,
    metadata jsonb NOT NULL,
    archived timestamp with time zone,
    added timestamp with time zone DEFAULT now() NOT NULL,
    added_by name DEFAULT CURRENT_USER NOT NULL,
    updated timestamp with time zone
);
    DROP TABLE agdc.dataset;
       agdc      
   agdc_admin    false    8            �           0    0    TABLE dataset    ACL     d   GRANT SELECT ON TABLE agdc.dataset TO agdc_user;
GRANT INSERT ON TABLE agdc.dataset TO agdc_ingest;
            agdc    
   agdc_admin    false    201            �            1259    2903527    dataset_location    TABLE     F  CREATE TABLE agdc.dataset_location (
    id integer NOT NULL,
    dataset_ref uuid NOT NULL,
    uri_scheme character varying NOT NULL,
    uri_body character varying NOT NULL,
    added timestamp with time zone DEFAULT now() NOT NULL,
    added_by name DEFAULT CURRENT_USER NOT NULL,
    archived timestamp with time zone
);
 "   DROP TABLE agdc.dataset_location;
       agdc      
   agdc_admin    false    8            �           0    0    TABLE dataset_location    ACL     v   GRANT SELECT ON TABLE agdc.dataset_location TO agdc_user;
GRANT INSERT ON TABLE agdc.dataset_location TO agdc_ingest;
            agdc    
   agdc_admin    false    203            �            1259    2903525    dataset_location_id_seq    SEQUENCE     �   CREATE SEQUENCE agdc.dataset_location_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 ,   DROP SEQUENCE agdc.dataset_location_id_seq;
       agdc    
   agdc_admin    false    8    203            �           0    0    dataset_location_id_seq    SEQUENCE OWNED BY     O   ALTER SEQUENCE agdc.dataset_location_id_seq OWNED BY agdc.dataset_location.id;
            agdc    
   agdc_admin    false    202            �           0    0     SEQUENCE dataset_location_id_seq    ACL     L   GRANT SELECT,USAGE ON SEQUENCE agdc.dataset_location_id_seq TO agdc_ingest;
            agdc    
   agdc_admin    false    202            �            1259    2903546    dataset_source    TABLE     �   CREATE TABLE agdc.dataset_source (
    dataset_ref uuid NOT NULL,
    classifier character varying NOT NULL,
    source_dataset_ref uuid NOT NULL
);
     DROP TABLE agdc.dataset_source;
       agdc      
   agdc_admin    false    8            �           0    0    TABLE dataset_source    ACL     r   GRANT SELECT ON TABLE agdc.dataset_source TO agdc_user;
GRANT INSERT ON TABLE agdc.dataset_source TO agdc_ingest;
            agdc    
   agdc_admin    false    204            �            1259    2903485    dataset_type    TABLE     �  CREATE TABLE agdc.dataset_type (
    id smallint NOT NULL,
    name character varying NOT NULL,
    metadata jsonb NOT NULL,
    metadata_type_ref smallint NOT NULL,
    definition jsonb NOT NULL,
    added timestamp with time zone DEFAULT now() NOT NULL,
    added_by name DEFAULT CURRENT_USER NOT NULL,
    updated timestamp with time zone,
    CONSTRAINT ck_dataset_type_alphanumeric_name CHECK (((name)::text ~* '^\w+$'::text))
);
    DROP TABLE agdc.dataset_type;
       agdc      
   agdc_admin    false    8            �           0    0    TABLE dataset_type    ACL     u   GRANT SELECT ON TABLE agdc.dataset_type TO agdc_user;
GRANT INSERT,DELETE ON TABLE agdc.dataset_type TO agdc_manage;
            agdc    
   agdc_admin    false    200            �            1259    2903483    dataset_type_id_seq    SEQUENCE     �   CREATE SEQUENCE agdc.dataset_type_id_seq
    AS smallint
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE agdc.dataset_type_id_seq;
       agdc    
   agdc_admin    false    200    8            �           0    0    dataset_type_id_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE agdc.dataset_type_id_seq OWNED BY agdc.dataset_type.id;
            agdc    
   agdc_admin    false    199            �           0    0    SEQUENCE dataset_type_id_seq    ACL     H   GRANT SELECT,USAGE ON SEQUENCE agdc.dataset_type_id_seq TO agdc_ingest;
            agdc    
   agdc_admin    false    199            �            1259    2903469    metadata_type    TABLE     o  CREATE TABLE agdc.metadata_type (
    id smallint NOT NULL,
    name character varying NOT NULL,
    definition jsonb NOT NULL,
    added timestamp with time zone DEFAULT now() NOT NULL,
    added_by name DEFAULT CURRENT_USER NOT NULL,
    updated timestamp with time zone,
    CONSTRAINT ck_metadata_type_alphanumeric_name CHECK (((name)::text ~* '^\w+$'::text))
);
    DROP TABLE agdc.metadata_type;
       agdc      
   agdc_admin    false    8            �           0    0    TABLE metadata_type    ACL     w   GRANT SELECT ON TABLE agdc.metadata_type TO agdc_user;
GRANT INSERT,DELETE ON TABLE agdc.metadata_type TO agdc_manage;
            agdc    
   agdc_admin    false    198            �            1259    2903619 '   dv_aster_aloh_group_composition_dataset    VIEW     �
  CREATE VIEW agdc.dv_aster_aloh_group_composition_dataset AS
 SELECT dataset.id,
    dataset.added AS indexed_time,
    dataset.added_by AS indexed_by,
    dataset_type.name AS product,
    dataset.dataset_type_ref AS dataset_type_id,
    metadata_type.name AS metadata_type,
    dataset.metadata_type_ref AS metadata_type_id,
    dataset.metadata AS metadata_doc,
    agdc.common_timestamp((dataset.metadata #>> '{creation_dt}'::text[])) AS creation_time,
    (dataset.metadata #>> '{format,name}'::text[]) AS format,
    (dataset.metadata #>> '{ga_label}'::text[]) AS label,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text) AS lat,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text) AS lon,
    tstzrange(LEAST(agdc.common_timestamp((dataset.metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((dataset.metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), '[]'::text) AS "time",
    (dataset.metadata #>> '{platform,code}'::text[]) AS platform,
    (dataset.metadata #>> '{instrument,name}'::text[]) AS instrument,
    (dataset.metadata #>> '{product_type}'::text[]) AS product_type
   FROM ((agdc.dataset
     JOIN agdc.dataset_type ON ((dataset_type.id = dataset.dataset_type_ref)))
     JOIN agdc.metadata_type ON ((metadata_type.id = dataset_type.metadata_type_ref)))
  WHERE ((dataset.archived IS NULL) AND (dataset.dataset_type_ref = 3));
 8   DROP VIEW agdc.dv_aster_aloh_group_composition_dataset;
       agdc       africa    false    280    201    198    198    201    201    201    201    200    200    200    201    201    8    673    673            �            1259    2903628 #   dv_aster_aloh_group_content_dataset    VIEW     �
  CREATE VIEW agdc.dv_aster_aloh_group_content_dataset AS
 SELECT dataset.id,
    dataset.added AS indexed_time,
    dataset.added_by AS indexed_by,
    dataset_type.name AS product,
    dataset.dataset_type_ref AS dataset_type_id,
    metadata_type.name AS metadata_type,
    dataset.metadata_type_ref AS metadata_type_id,
    dataset.metadata AS metadata_doc,
    agdc.common_timestamp((dataset.metadata #>> '{creation_dt}'::text[])) AS creation_time,
    (dataset.metadata #>> '{format,name}'::text[]) AS format,
    (dataset.metadata #>> '{ga_label}'::text[]) AS label,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text) AS lat,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text) AS lon,
    tstzrange(LEAST(agdc.common_timestamp((dataset.metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((dataset.metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), '[]'::text) AS "time",
    (dataset.metadata #>> '{platform,code}'::text[]) AS platform,
    (dataset.metadata #>> '{instrument,name}'::text[]) AS instrument,
    (dataset.metadata #>> '{product_type}'::text[]) AS product_type
   FROM ((agdc.dataset
     JOIN agdc.dataset_type ON ((dataset_type.id = dataset.dataset_type_ref)))
     JOIN agdc.metadata_type ON ((metadata_type.id = dataset_type.metadata_type_ref)))
  WHERE ((dataset.archived IS NULL) AND (dataset.dataset_type_ref = 4));
 4   DROP VIEW agdc.dv_aster_aloh_group_content_dataset;
       agdc       africa    false    201    280    198    198    200    200    200    201    201    201    201    201    201    8    673    673            �            1259    2903637    dv_aster_false_colour_dataset    VIEW     �
  CREATE VIEW agdc.dv_aster_false_colour_dataset AS
 SELECT dataset.id,
    dataset.added AS indexed_time,
    dataset.added_by AS indexed_by,
    dataset_type.name AS product,
    dataset.dataset_type_ref AS dataset_type_id,
    metadata_type.name AS metadata_type,
    dataset.metadata_type_ref AS metadata_type_id,
    dataset.metadata AS metadata_doc,
    agdc.common_timestamp((dataset.metadata #>> '{creation_dt}'::text[])) AS creation_time,
    (dataset.metadata #>> '{format,name}'::text[]) AS format,
    (dataset.metadata #>> '{ga_label}'::text[]) AS label,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text) AS lat,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text) AS lon,
    tstzrange(LEAST(agdc.common_timestamp((dataset.metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((dataset.metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), '[]'::text) AS "time",
    (dataset.metadata #>> '{platform,code}'::text[]) AS platform,
    (dataset.metadata #>> '{instrument,name}'::text[]) AS instrument,
    (dataset.metadata #>> '{product_type}'::text[]) AS product_type
   FROM ((agdc.dataset
     JOIN agdc.dataset_type ON ((dataset_type.id = dataset.dataset_type_ref)))
     JOIN agdc.metadata_type ON ((metadata_type.id = dataset_type.metadata_type_ref)))
  WHERE ((dataset.archived IS NULL) AND (dataset.dataset_type_ref = 5));
 .   DROP VIEW agdc.dv_aster_false_colour_dataset;
       agdc       africa    false    201    201    201    201    201    201    201    200    200    200    198    198    280    673    673    8            �            1259    2903646 #   dv_aster_feoh_group_content_dataset    VIEW     �
  CREATE VIEW agdc.dv_aster_feoh_group_content_dataset AS
 SELECT dataset.id,
    dataset.added AS indexed_time,
    dataset.added_by AS indexed_by,
    dataset_type.name AS product,
    dataset.dataset_type_ref AS dataset_type_id,
    metadata_type.name AS metadata_type,
    dataset.metadata_type_ref AS metadata_type_id,
    dataset.metadata AS metadata_doc,
    agdc.common_timestamp((dataset.metadata #>> '{creation_dt}'::text[])) AS creation_time,
    (dataset.metadata #>> '{format,name}'::text[]) AS format,
    (dataset.metadata #>> '{ga_label}'::text[]) AS label,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text) AS lat,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text) AS lon,
    tstzrange(LEAST(agdc.common_timestamp((dataset.metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((dataset.metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), '[]'::text) AS "time",
    (dataset.metadata #>> '{platform,code}'::text[]) AS platform,
    (dataset.metadata #>> '{instrument,name}'::text[]) AS instrument,
    (dataset.metadata #>> '{product_type}'::text[]) AS product_type
   FROM ((agdc.dataset
     JOIN agdc.dataset_type ON ((dataset_type.id = dataset.dataset_type_ref)))
     JOIN agdc.metadata_type ON ((metadata_type.id = dataset_type.metadata_type_ref)))
  WHERE ((dataset.archived IS NULL) AND (dataset.dataset_type_ref = 6));
 4   DROP VIEW agdc.dv_aster_feoh_group_content_dataset;
       agdc       africa    false    198    201    201    201    201    201    201    201    200    200    200    280    198    8    673    673            �            1259    2903655 )   dv_aster_ferric_oxide_composition_dataset    VIEW     �
  CREATE VIEW agdc.dv_aster_ferric_oxide_composition_dataset AS
 SELECT dataset.id,
    dataset.added AS indexed_time,
    dataset.added_by AS indexed_by,
    dataset_type.name AS product,
    dataset.dataset_type_ref AS dataset_type_id,
    metadata_type.name AS metadata_type,
    dataset.metadata_type_ref AS metadata_type_id,
    dataset.metadata AS metadata_doc,
    agdc.common_timestamp((dataset.metadata #>> '{creation_dt}'::text[])) AS creation_time,
    (dataset.metadata #>> '{format,name}'::text[]) AS format,
    (dataset.metadata #>> '{ga_label}'::text[]) AS label,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text) AS lat,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text) AS lon,
    tstzrange(LEAST(agdc.common_timestamp((dataset.metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((dataset.metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), '[]'::text) AS "time",
    (dataset.metadata #>> '{platform,code}'::text[]) AS platform,
    (dataset.metadata #>> '{instrument,name}'::text[]) AS instrument,
    (dataset.metadata #>> '{product_type}'::text[]) AS product_type
   FROM ((agdc.dataset
     JOIN agdc.dataset_type ON ((dataset_type.id = dataset.dataset_type_ref)))
     JOIN agdc.metadata_type ON ((metadata_type.id = dataset_type.metadata_type_ref)))
  WHERE ((dataset.archived IS NULL) AND (dataset.dataset_type_ref = 7));
 :   DROP VIEW agdc.dv_aster_ferric_oxide_composition_dataset;
       agdc       africa    false    201    201    201    200    200    200    198    198    280    201    201    201    201    8    673    673            �            1259    2903664 %   dv_aster_ferric_oxide_content_dataset    VIEW     �
  CREATE VIEW agdc.dv_aster_ferric_oxide_content_dataset AS
 SELECT dataset.id,
    dataset.added AS indexed_time,
    dataset.added_by AS indexed_by,
    dataset_type.name AS product,
    dataset.dataset_type_ref AS dataset_type_id,
    metadata_type.name AS metadata_type,
    dataset.metadata_type_ref AS metadata_type_id,
    dataset.metadata AS metadata_doc,
    agdc.common_timestamp((dataset.metadata #>> '{creation_dt}'::text[])) AS creation_time,
    (dataset.metadata #>> '{format,name}'::text[]) AS format,
    (dataset.metadata #>> '{ga_label}'::text[]) AS label,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text) AS lat,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text) AS lon,
    tstzrange(LEAST(agdc.common_timestamp((dataset.metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((dataset.metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), '[]'::text) AS "time",
    (dataset.metadata #>> '{platform,code}'::text[]) AS platform,
    (dataset.metadata #>> '{instrument,name}'::text[]) AS instrument,
    (dataset.metadata #>> '{product_type}'::text[]) AS product_type
   FROM ((agdc.dataset
     JOIN agdc.dataset_type ON ((dataset_type.id = dataset.dataset_type_ref)))
     JOIN agdc.metadata_type ON ((metadata_type.id = dataset_type.metadata_type_ref)))
  WHERE ((dataset.archived IS NULL) AND (dataset.dataset_type_ref = 8));
 6   DROP VIEW agdc.dv_aster_ferric_oxide_content_dataset;
       agdc       africa    false    201    201    201    201    201    200    200    200    198    198    280    201    201    8    673    673            �            1259    2903673 -   dv_aster_ferrous_iron_content_in_mgoh_dataset    VIEW     �
  CREATE VIEW agdc.dv_aster_ferrous_iron_content_in_mgoh_dataset AS
 SELECT dataset.id,
    dataset.added AS indexed_time,
    dataset.added_by AS indexed_by,
    dataset_type.name AS product,
    dataset.dataset_type_ref AS dataset_type_id,
    metadata_type.name AS metadata_type,
    dataset.metadata_type_ref AS metadata_type_id,
    dataset.metadata AS metadata_doc,
    agdc.common_timestamp((dataset.metadata #>> '{creation_dt}'::text[])) AS creation_time,
    (dataset.metadata #>> '{format,name}'::text[]) AS format,
    (dataset.metadata #>> '{ga_label}'::text[]) AS label,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text) AS lat,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text) AS lon,
    tstzrange(LEAST(agdc.common_timestamp((dataset.metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((dataset.metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), '[]'::text) AS "time",
    (dataset.metadata #>> '{platform,code}'::text[]) AS platform,
    (dataset.metadata #>> '{instrument,name}'::text[]) AS instrument,
    (dataset.metadata #>> '{product_type}'::text[]) AS product_type
   FROM ((agdc.dataset
     JOIN agdc.dataset_type ON ((dataset_type.id = dataset.dataset_type_ref)))
     JOIN agdc.metadata_type ON ((metadata_type.id = dataset_type.metadata_type_ref)))
  WHERE ((dataset.archived IS NULL) AND (dataset.dataset_type_ref = 9));
 >   DROP VIEW agdc.dv_aster_ferrous_iron_content_in_mgoh_dataset;
       agdc       africa    false    201    201    200    198    280    200    201    198    201    201    201    201    200    673    673    8            �            1259    2903682 #   dv_aster_ferrous_iron_index_dataset    VIEW     �
  CREATE VIEW agdc.dv_aster_ferrous_iron_index_dataset AS
 SELECT dataset.id,
    dataset.added AS indexed_time,
    dataset.added_by AS indexed_by,
    dataset_type.name AS product,
    dataset.dataset_type_ref AS dataset_type_id,
    metadata_type.name AS metadata_type,
    dataset.metadata_type_ref AS metadata_type_id,
    dataset.metadata AS metadata_doc,
    agdc.common_timestamp((dataset.metadata #>> '{creation_dt}'::text[])) AS creation_time,
    (dataset.metadata #>> '{format,name}'::text[]) AS format,
    (dataset.metadata #>> '{ga_label}'::text[]) AS label,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text) AS lat,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text) AS lon,
    tstzrange(LEAST(agdc.common_timestamp((dataset.metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((dataset.metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), '[]'::text) AS "time",
    (dataset.metadata #>> '{platform,code}'::text[]) AS platform,
    (dataset.metadata #>> '{instrument,name}'::text[]) AS instrument,
    (dataset.metadata #>> '{product_type}'::text[]) AS product_type
   FROM ((agdc.dataset
     JOIN agdc.dataset_type ON ((dataset_type.id = dataset.dataset_type_ref)))
     JOIN agdc.metadata_type ON ((metadata_type.id = dataset_type.metadata_type_ref)))
  WHERE ((dataset.archived IS NULL) AND (dataset.dataset_type_ref = 10));
 4   DROP VIEW agdc.dv_aster_ferrous_iron_index_dataset;
       agdc       africa    false    280    198    198    200    200    200    201    201    201    201    201    201    201    673    8    673            �            1259    2903691 !   dv_aster_green_vegetation_dataset    VIEW     �
  CREATE VIEW agdc.dv_aster_green_vegetation_dataset AS
 SELECT dataset.id,
    dataset.added AS indexed_time,
    dataset.added_by AS indexed_by,
    dataset_type.name AS product,
    dataset.dataset_type_ref AS dataset_type_id,
    metadata_type.name AS metadata_type,
    dataset.metadata_type_ref AS metadata_type_id,
    dataset.metadata AS metadata_doc,
    agdc.common_timestamp((dataset.metadata #>> '{creation_dt}'::text[])) AS creation_time,
    (dataset.metadata #>> '{format,name}'::text[]) AS format,
    (dataset.metadata #>> '{ga_label}'::text[]) AS label,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text) AS lat,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text) AS lon,
    tstzrange(LEAST(agdc.common_timestamp((dataset.metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((dataset.metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), '[]'::text) AS "time",
    (dataset.metadata #>> '{platform,code}'::text[]) AS platform,
    (dataset.metadata #>> '{instrument,name}'::text[]) AS instrument,
    (dataset.metadata #>> '{product_type}'::text[]) AS product_type
   FROM ((agdc.dataset
     JOIN agdc.dataset_type ON ((dataset_type.id = dataset.dataset_type_ref)))
     JOIN agdc.metadata_type ON ((metadata_type.id = dataset_type.metadata_type_ref)))
  WHERE ((dataset.archived IS NULL) AND (dataset.dataset_type_ref = 11));
 2   DROP VIEW agdc.dv_aster_green_vegetation_dataset;
       agdc       africa    false    198    280    201    201    201    201    201    201    201    200    200    200    198    673    673    8            �            1259    2903700    dv_aster_gypsum_index_dataset    VIEW     �
  CREATE VIEW agdc.dv_aster_gypsum_index_dataset AS
 SELECT dataset.id,
    dataset.added AS indexed_time,
    dataset.added_by AS indexed_by,
    dataset_type.name AS product,
    dataset.dataset_type_ref AS dataset_type_id,
    metadata_type.name AS metadata_type,
    dataset.metadata_type_ref AS metadata_type_id,
    dataset.metadata AS metadata_doc,
    agdc.common_timestamp((dataset.metadata #>> '{creation_dt}'::text[])) AS creation_time,
    (dataset.metadata #>> '{format,name}'::text[]) AS format,
    (dataset.metadata #>> '{ga_label}'::text[]) AS label,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text) AS lat,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text) AS lon,
    tstzrange(LEAST(agdc.common_timestamp((dataset.metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((dataset.metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), '[]'::text) AS "time",
    (dataset.metadata #>> '{platform,code}'::text[]) AS platform,
    (dataset.metadata #>> '{instrument,name}'::text[]) AS instrument,
    (dataset.metadata #>> '{product_type}'::text[]) AS product_type
   FROM ((agdc.dataset
     JOIN agdc.dataset_type ON ((dataset_type.id = dataset.dataset_type_ref)))
     JOIN agdc.metadata_type ON ((metadata_type.id = dataset_type.metadata_type_ref)))
  WHERE ((dataset.archived IS NULL) AND (dataset.dataset_type_ref = 12));
 .   DROP VIEW agdc.dv_aster_gypsum_index_dataset;
       agdc       africa    false    201    200    201    201    198    198    201    201    201    201    200    200    280    673    8    673            �            1259    2903709 #   dv_aster_kaolin_group_index_dataset    VIEW     �
  CREATE VIEW agdc.dv_aster_kaolin_group_index_dataset AS
 SELECT dataset.id,
    dataset.added AS indexed_time,
    dataset.added_by AS indexed_by,
    dataset_type.name AS product,
    dataset.dataset_type_ref AS dataset_type_id,
    metadata_type.name AS metadata_type,
    dataset.metadata_type_ref AS metadata_type_id,
    dataset.metadata AS metadata_doc,
    agdc.common_timestamp((dataset.metadata #>> '{creation_dt}'::text[])) AS creation_time,
    (dataset.metadata #>> '{format,name}'::text[]) AS format,
    (dataset.metadata #>> '{ga_label}'::text[]) AS label,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text) AS lat,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text) AS lon,
    tstzrange(LEAST(agdc.common_timestamp((dataset.metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((dataset.metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), '[]'::text) AS "time",
    (dataset.metadata #>> '{platform,code}'::text[]) AS platform,
    (dataset.metadata #>> '{instrument,name}'::text[]) AS instrument,
    (dataset.metadata #>> '{product_type}'::text[]) AS product_type
   FROM ((agdc.dataset
     JOIN agdc.dataset_type ON ((dataset_type.id = dataset.dataset_type_ref)))
     JOIN agdc.metadata_type ON ((metadata_type.id = dataset_type.metadata_type_ref)))
  WHERE ((dataset.archived IS NULL) AND (dataset.dataset_type_ref = 13));
 4   DROP VIEW agdc.dv_aster_kaolin_group_index_dataset;
       agdc       africa    false    200    200    280    201    201    201    201    201    201    201    200    198    198    673    8    673            �            1259    2903718 '   dv_aster_mgoh_group_composition_dataset    VIEW     �
  CREATE VIEW agdc.dv_aster_mgoh_group_composition_dataset AS
 SELECT dataset.id,
    dataset.added AS indexed_time,
    dataset.added_by AS indexed_by,
    dataset_type.name AS product,
    dataset.dataset_type_ref AS dataset_type_id,
    metadata_type.name AS metadata_type,
    dataset.metadata_type_ref AS metadata_type_id,
    dataset.metadata AS metadata_doc,
    agdc.common_timestamp((dataset.metadata #>> '{creation_dt}'::text[])) AS creation_time,
    (dataset.metadata #>> '{format,name}'::text[]) AS format,
    (dataset.metadata #>> '{ga_label}'::text[]) AS label,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text) AS lat,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text) AS lon,
    tstzrange(LEAST(agdc.common_timestamp((dataset.metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((dataset.metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), '[]'::text) AS "time",
    (dataset.metadata #>> '{platform,code}'::text[]) AS platform,
    (dataset.metadata #>> '{instrument,name}'::text[]) AS instrument,
    (dataset.metadata #>> '{product_type}'::text[]) AS product_type
   FROM ((agdc.dataset
     JOIN agdc.dataset_type ON ((dataset_type.id = dataset.dataset_type_ref)))
     JOIN agdc.metadata_type ON ((metadata_type.id = dataset_type.metadata_type_ref)))
  WHERE ((dataset.archived IS NULL) AND (dataset.dataset_type_ref = 14));
 8   DROP VIEW agdc.dv_aster_mgoh_group_composition_dataset;
       agdc       africa    false    200    280    198    198    200    200    201    201    201    201    201    201    201    673    673    8            �            1259    2903727 #   dv_aster_mgoh_group_content_dataset    VIEW     �
  CREATE VIEW agdc.dv_aster_mgoh_group_content_dataset AS
 SELECT dataset.id,
    dataset.added AS indexed_time,
    dataset.added_by AS indexed_by,
    dataset_type.name AS product,
    dataset.dataset_type_ref AS dataset_type_id,
    metadata_type.name AS metadata_type,
    dataset.metadata_type_ref AS metadata_type_id,
    dataset.metadata AS metadata_doc,
    agdc.common_timestamp((dataset.metadata #>> '{creation_dt}'::text[])) AS creation_time,
    (dataset.metadata #>> '{format,name}'::text[]) AS format,
    (dataset.metadata #>> '{ga_label}'::text[]) AS label,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text) AS lat,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text) AS lon,
    tstzrange(LEAST(agdc.common_timestamp((dataset.metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((dataset.metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), '[]'::text) AS "time",
    (dataset.metadata #>> '{platform,code}'::text[]) AS platform,
    (dataset.metadata #>> '{instrument,name}'::text[]) AS instrument,
    (dataset.metadata #>> '{product_type}'::text[]) AS product_type
   FROM ((agdc.dataset
     JOIN agdc.dataset_type ON ((dataset_type.id = dataset.dataset_type_ref)))
     JOIN agdc.metadata_type ON ((metadata_type.id = dataset_type.metadata_type_ref)))
  WHERE ((dataset.archived IS NULL) AND (dataset.dataset_type_ref = 15));
 4   DROP VIEW agdc.dv_aster_mgoh_group_content_dataset;
       agdc       africa    false    198    200    200    280    200    201    201    201    201    201    201    201    198    673    8    673            �            1259    2903736    dv_aster_opaque_index_dataset    VIEW     �
  CREATE VIEW agdc.dv_aster_opaque_index_dataset AS
 SELECT dataset.id,
    dataset.added AS indexed_time,
    dataset.added_by AS indexed_by,
    dataset_type.name AS product,
    dataset.dataset_type_ref AS dataset_type_id,
    metadata_type.name AS metadata_type,
    dataset.metadata_type_ref AS metadata_type_id,
    dataset.metadata AS metadata_doc,
    agdc.common_timestamp((dataset.metadata #>> '{creation_dt}'::text[])) AS creation_time,
    (dataset.metadata #>> '{format,name}'::text[]) AS format,
    (dataset.metadata #>> '{ga_label}'::text[]) AS label,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text) AS lat,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text) AS lon,
    tstzrange(LEAST(agdc.common_timestamp((dataset.metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((dataset.metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), '[]'::text) AS "time",
    (dataset.metadata #>> '{platform,code}'::text[]) AS platform,
    (dataset.metadata #>> '{instrument,name}'::text[]) AS instrument,
    (dataset.metadata #>> '{product_type}'::text[]) AS product_type
   FROM ((agdc.dataset
     JOIN agdc.dataset_type ON ((dataset_type.id = dataset.dataset_type_ref)))
     JOIN agdc.metadata_type ON ((metadata_type.id = dataset_type.metadata_type_ref)))
  WHERE ((dataset.archived IS NULL) AND (dataset.dataset_type_ref = 16));
 .   DROP VIEW agdc.dv_aster_opaque_index_dataset;
       agdc       africa    false    200    198    198    280    200    201    201    201    201    201    201    201    200    8    673    673            �            1259    2903745    dv_aster_quartz_index_dataset    VIEW     �
  CREATE VIEW agdc.dv_aster_quartz_index_dataset AS
 SELECT dataset.id,
    dataset.added AS indexed_time,
    dataset.added_by AS indexed_by,
    dataset_type.name AS product,
    dataset.dataset_type_ref AS dataset_type_id,
    metadata_type.name AS metadata_type,
    dataset.metadata_type_ref AS metadata_type_id,
    dataset.metadata AS metadata_doc,
    agdc.common_timestamp((dataset.metadata #>> '{creation_dt}'::text[])) AS creation_time,
    (dataset.metadata #>> '{format,name}'::text[]) AS format,
    (dataset.metadata #>> '{ga_label}'::text[]) AS label,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text) AS lat,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text) AS lon,
    tstzrange(LEAST(agdc.common_timestamp((dataset.metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((dataset.metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), '[]'::text) AS "time",
    (dataset.metadata #>> '{platform,code}'::text[]) AS platform,
    (dataset.metadata #>> '{instrument,name}'::text[]) AS instrument,
    (dataset.metadata #>> '{product_type}'::text[]) AS product_type
   FROM ((agdc.dataset
     JOIN agdc.dataset_type ON ((dataset_type.id = dataset.dataset_type_ref)))
     JOIN agdc.metadata_type ON ((metadata_type.id = dataset_type.metadata_type_ref)))
  WHERE ((dataset.archived IS NULL) AND (dataset.dataset_type_ref = 17));
 .   DROP VIEW agdc.dv_aster_quartz_index_dataset;
       agdc       africa    false    280    198    198    200    200    200    201    201    201    201    201    201    201    673    673    8            �            1259    2903754     dv_aster_regolith_ratios_dataset    VIEW     �
  CREATE VIEW agdc.dv_aster_regolith_ratios_dataset AS
 SELECT dataset.id,
    dataset.added AS indexed_time,
    dataset.added_by AS indexed_by,
    dataset_type.name AS product,
    dataset.dataset_type_ref AS dataset_type_id,
    metadata_type.name AS metadata_type,
    dataset.metadata_type_ref AS metadata_type_id,
    dataset.metadata AS metadata_doc,
    agdc.common_timestamp((dataset.metadata #>> '{creation_dt}'::text[])) AS creation_time,
    (dataset.metadata #>> '{format,name}'::text[]) AS format,
    (dataset.metadata #>> '{ga_label}'::text[]) AS label,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text) AS lat,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text) AS lon,
    tstzrange(LEAST(agdc.common_timestamp((dataset.metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((dataset.metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), '[]'::text) AS "time",
    (dataset.metadata #>> '{platform,code}'::text[]) AS platform,
    (dataset.metadata #>> '{instrument,name}'::text[]) AS instrument,
    (dataset.metadata #>> '{product_type}'::text[]) AS product_type
   FROM ((agdc.dataset
     JOIN agdc.dataset_type ON ((dataset_type.id = dataset.dataset_type_ref)))
     JOIN agdc.metadata_type ON ((metadata_type.id = dataset_type.metadata_type_ref)))
  WHERE ((dataset.archived IS NULL) AND (dataset.dataset_type_ref = 18));
 1   DROP VIEW agdc.dv_aster_regolith_ratios_dataset;
       agdc       africa    false    201    201    201    201    200    200    200    198    198    280    201    201    201    673    673    8            �            1259    2903763    dv_aster_silica_index_dataset    VIEW     �
  CREATE VIEW agdc.dv_aster_silica_index_dataset AS
 SELECT dataset.id,
    dataset.added AS indexed_time,
    dataset.added_by AS indexed_by,
    dataset_type.name AS product,
    dataset.dataset_type_ref AS dataset_type_id,
    metadata_type.name AS metadata_type,
    dataset.metadata_type_ref AS metadata_type_id,
    dataset.metadata AS metadata_doc,
    agdc.common_timestamp((dataset.metadata #>> '{creation_dt}'::text[])) AS creation_time,
    (dataset.metadata #>> '{format,name}'::text[]) AS format,
    (dataset.metadata #>> '{ga_label}'::text[]) AS label,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text) AS lat,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text) AS lon,
    tstzrange(LEAST(agdc.common_timestamp((dataset.metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((dataset.metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), '[]'::text) AS "time",
    (dataset.metadata #>> '{platform,code}'::text[]) AS platform,
    (dataset.metadata #>> '{instrument,name}'::text[]) AS instrument,
    (dataset.metadata #>> '{product_type}'::text[]) AS product_type
   FROM ((agdc.dataset
     JOIN agdc.dataset_type ON ((dataset_type.id = dataset.dataset_type_ref)))
     JOIN agdc.metadata_type ON ((metadata_type.id = dataset_type.metadata_type_ref)))
  WHERE ((dataset.archived IS NULL) AND (dataset.dataset_type_ref = 19));
 .   DROP VIEW agdc.dv_aster_silica_index_dataset;
       agdc       africa    false    200    280    198    198    200    200    201    201    201    201    201    201    201    673    673    8            �            1259    2903771 '   dv_cemp_insar_alos_displacement_dataset    VIEW     �  CREATE VIEW agdc.dv_cemp_insar_alos_displacement_dataset AS
 SELECT dataset.id,
    dataset.added AS indexed_time,
    dataset.added_by AS indexed_by,
    dataset_type.name AS product,
    dataset.dataset_type_ref AS dataset_type_id,
    metadata_type.name AS metadata_type,
    dataset.metadata_type_ref AS metadata_type_id,
    dataset.metadata AS metadata_doc,
    agdc.common_timestamp((dataset.metadata #>> '{properties,odc:processing_datetime}'::text[])) AS creation_time,
    (dataset.metadata #>> '{properties,odc:file_format}'::text[]) AS format,
    (dataset.metadata #>> '{label}'::text[]) AS label,
    agdc.float8range(((dataset.metadata #>> '{extent,lat,begin}'::text[]))::double precision, ((dataset.metadata #>> '{extent,lat,end}'::text[]))::double precision, '[]'::text) AS lat,
    agdc.float8range(((dataset.metadata #>> '{extent,lon,begin}'::text[]))::double precision, ((dataset.metadata #>> '{extent,lon,end}'::text[]))::double precision, '[]'::text) AS lon,
    tstzrange(LEAST(agdc.common_timestamp((dataset.metadata #>> '{properties,dtr:start_datetime}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{properties,datetime}'::text[]))), GREATEST(agdc.common_timestamp((dataset.metadata #>> '{properties,dtr:end_datetime}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{properties,datetime}'::text[]))), '[]'::text) AS "time",
    (dataset.metadata #>> '{properties,eo:platform}'::text[]) AS platform,
    (dataset.metadata #>> '{properties,eo:instrument}'::text[]) AS instrument,
    (dataset.metadata #>> '{properties,odc:region_code}'::text[]) AS region_code,
    (dataset.metadata #>> '{properties,odc:product_family}'::text[]) AS product_family,
    (dataset.metadata #>> '{properties,dea:dataset_maturity}'::text[]) AS dataset_maturity
   FROM ((agdc.dataset
     JOIN agdc.dataset_type ON ((dataset_type.id = dataset.dataset_type_ref)))
     JOIN agdc.metadata_type ON ((metadata_type.id = dataset_type.metadata_type_ref)))
  WHERE ((dataset.archived IS NULL) AND (dataset.dataset_type_ref = 20));
 8   DROP VIEW agdc.dv_cemp_insar_alos_displacement_dataset;
       agdc       africa    false    201    201    201    201    201    200    200    198    200    280    198    201    201    673    8    673            �            1259    2903779 #   dv_cemp_insar_alos_velocity_dataset    VIEW     �  CREATE VIEW agdc.dv_cemp_insar_alos_velocity_dataset AS
 SELECT dataset.id,
    dataset.added AS indexed_time,
    dataset.added_by AS indexed_by,
    dataset_type.name AS product,
    dataset.dataset_type_ref AS dataset_type_id,
    metadata_type.name AS metadata_type,
    dataset.metadata_type_ref AS metadata_type_id,
    dataset.metadata AS metadata_doc,
    agdc.common_timestamp((dataset.metadata #>> '{properties,odc:processing_datetime}'::text[])) AS creation_time,
    (dataset.metadata #>> '{properties,odc:file_format}'::text[]) AS format,
    (dataset.metadata #>> '{label}'::text[]) AS label,
    agdc.float8range(((dataset.metadata #>> '{extent,lat,begin}'::text[]))::double precision, ((dataset.metadata #>> '{extent,lat,end}'::text[]))::double precision, '[]'::text) AS lat,
    agdc.float8range(((dataset.metadata #>> '{extent,lon,begin}'::text[]))::double precision, ((dataset.metadata #>> '{extent,lon,end}'::text[]))::double precision, '[]'::text) AS lon,
    tstzrange(LEAST(agdc.common_timestamp((dataset.metadata #>> '{properties,dtr:start_datetime}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{properties,datetime}'::text[]))), GREATEST(agdc.common_timestamp((dataset.metadata #>> '{properties,dtr:end_datetime}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{properties,datetime}'::text[]))), '[]'::text) AS "time",
    (dataset.metadata #>> '{properties,eo:platform}'::text[]) AS platform,
    (dataset.metadata #>> '{properties,eo:instrument}'::text[]) AS instrument,
    (dataset.metadata #>> '{properties,odc:region_code}'::text[]) AS region_code,
    (dataset.metadata #>> '{properties,odc:product_family}'::text[]) AS product_family,
    (dataset.metadata #>> '{properties,dea:dataset_maturity}'::text[]) AS dataset_maturity
   FROM ((agdc.dataset
     JOIN agdc.dataset_type ON ((dataset_type.id = dataset.dataset_type_ref)))
     JOIN agdc.metadata_type ON ((metadata_type.id = dataset_type.metadata_type_ref)))
  WHERE ((dataset.archived IS NULL) AND (dataset.dataset_type_ref = 21));
 4   DROP VIEW agdc.dv_cemp_insar_alos_velocity_dataset;
       agdc       africa    false    280    201    201    201    201    198    198    200    200    200    201    201    201    673    8    673            �            1259    2903787 *   dv_cemp_insar_envisat_displacement_dataset    VIEW       CREATE VIEW agdc.dv_cemp_insar_envisat_displacement_dataset AS
 SELECT dataset.id,
    dataset.added AS indexed_time,
    dataset.added_by AS indexed_by,
    dataset_type.name AS product,
    dataset.dataset_type_ref AS dataset_type_id,
    metadata_type.name AS metadata_type,
    dataset.metadata_type_ref AS metadata_type_id,
    dataset.metadata AS metadata_doc,
    agdc.common_timestamp((dataset.metadata #>> '{properties,odc:processing_datetime}'::text[])) AS creation_time,
    (dataset.metadata #>> '{properties,odc:file_format}'::text[]) AS format,
    (dataset.metadata #>> '{label}'::text[]) AS label,
    agdc.float8range(((dataset.metadata #>> '{extent,lat,begin}'::text[]))::double precision, ((dataset.metadata #>> '{extent,lat,end}'::text[]))::double precision, '[]'::text) AS lat,
    agdc.float8range(((dataset.metadata #>> '{extent,lon,begin}'::text[]))::double precision, ((dataset.metadata #>> '{extent,lon,end}'::text[]))::double precision, '[]'::text) AS lon,
    tstzrange(LEAST(agdc.common_timestamp((dataset.metadata #>> '{properties,dtr:start_datetime}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{properties,datetime}'::text[]))), GREATEST(agdc.common_timestamp((dataset.metadata #>> '{properties,dtr:end_datetime}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{properties,datetime}'::text[]))), '[]'::text) AS "time",
    (dataset.metadata #>> '{properties,eo:platform}'::text[]) AS platform,
    (dataset.metadata #>> '{properties,eo:instrument}'::text[]) AS instrument,
    (dataset.metadata #>> '{properties,odc:region_code}'::text[]) AS region_code,
    (dataset.metadata #>> '{properties,odc:product_family}'::text[]) AS product_family,
    (dataset.metadata #>> '{properties,dea:dataset_maturity}'::text[]) AS dataset_maturity
   FROM ((agdc.dataset
     JOIN agdc.dataset_type ON ((dataset_type.id = dataset.dataset_type_ref)))
     JOIN agdc.metadata_type ON ((metadata_type.id = dataset_type.metadata_type_ref)))
  WHERE ((dataset.archived IS NULL) AND (dataset.dataset_type_ref = 22));
 ;   DROP VIEW agdc.dv_cemp_insar_envisat_displacement_dataset;
       agdc       africa    false    200    201    201    200    201    200    198    198    280    201    201    201    201    673    8    673            �            1259    2903795 &   dv_cemp_insar_envisat_velocity_dataset    VIEW     �  CREATE VIEW agdc.dv_cemp_insar_envisat_velocity_dataset AS
 SELECT dataset.id,
    dataset.added AS indexed_time,
    dataset.added_by AS indexed_by,
    dataset_type.name AS product,
    dataset.dataset_type_ref AS dataset_type_id,
    metadata_type.name AS metadata_type,
    dataset.metadata_type_ref AS metadata_type_id,
    dataset.metadata AS metadata_doc,
    agdc.common_timestamp((dataset.metadata #>> '{properties,odc:processing_datetime}'::text[])) AS creation_time,
    (dataset.metadata #>> '{properties,odc:file_format}'::text[]) AS format,
    (dataset.metadata #>> '{label}'::text[]) AS label,
    agdc.float8range(((dataset.metadata #>> '{extent,lat,begin}'::text[]))::double precision, ((dataset.metadata #>> '{extent,lat,end}'::text[]))::double precision, '[]'::text) AS lat,
    agdc.float8range(((dataset.metadata #>> '{extent,lon,begin}'::text[]))::double precision, ((dataset.metadata #>> '{extent,lon,end}'::text[]))::double precision, '[]'::text) AS lon,
    tstzrange(LEAST(agdc.common_timestamp((dataset.metadata #>> '{properties,dtr:start_datetime}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{properties,datetime}'::text[]))), GREATEST(agdc.common_timestamp((dataset.metadata #>> '{properties,dtr:end_datetime}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{properties,datetime}'::text[]))), '[]'::text) AS "time",
    (dataset.metadata #>> '{properties,eo:platform}'::text[]) AS platform,
    (dataset.metadata #>> '{properties,eo:instrument}'::text[]) AS instrument,
    (dataset.metadata #>> '{properties,odc:region_code}'::text[]) AS region_code,
    (dataset.metadata #>> '{properties,odc:product_family}'::text[]) AS product_family,
    (dataset.metadata #>> '{properties,dea:dataset_maturity}'::text[]) AS dataset_maturity
   FROM ((agdc.dataset
     JOIN agdc.dataset_type ON ((dataset_type.id = dataset.dataset_type_ref)))
     JOIN agdc.metadata_type ON ((metadata_type.id = dataset_type.metadata_type_ref)))
  WHERE ((dataset.archived IS NULL) AND (dataset.dataset_type_ref = 23));
 7   DROP VIEW agdc.dv_cemp_insar_envisat_velocity_dataset;
       agdc       africa    false    201    201    201    201    201    200    200    200    280    198    198    201    201    8    673    673            �            1259    2903803 ,   dv_cemp_insar_radarsat2_displacement_dataset    VIEW       CREATE VIEW agdc.dv_cemp_insar_radarsat2_displacement_dataset AS
 SELECT dataset.id,
    dataset.added AS indexed_time,
    dataset.added_by AS indexed_by,
    dataset_type.name AS product,
    dataset.dataset_type_ref AS dataset_type_id,
    metadata_type.name AS metadata_type,
    dataset.metadata_type_ref AS metadata_type_id,
    dataset.metadata AS metadata_doc,
    agdc.common_timestamp((dataset.metadata #>> '{properties,odc:processing_datetime}'::text[])) AS creation_time,
    (dataset.metadata #>> '{properties,odc:file_format}'::text[]) AS format,
    (dataset.metadata #>> '{label}'::text[]) AS label,
    agdc.float8range(((dataset.metadata #>> '{extent,lat,begin}'::text[]))::double precision, ((dataset.metadata #>> '{extent,lat,end}'::text[]))::double precision, '[]'::text) AS lat,
    agdc.float8range(((dataset.metadata #>> '{extent,lon,begin}'::text[]))::double precision, ((dataset.metadata #>> '{extent,lon,end}'::text[]))::double precision, '[]'::text) AS lon,
    tstzrange(LEAST(agdc.common_timestamp((dataset.metadata #>> '{properties,dtr:start_datetime}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{properties,datetime}'::text[]))), GREATEST(agdc.common_timestamp((dataset.metadata #>> '{properties,dtr:end_datetime}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{properties,datetime}'::text[]))), '[]'::text) AS "time",
    (dataset.metadata #>> '{properties,eo:platform}'::text[]) AS platform,
    (dataset.metadata #>> '{properties,eo:instrument}'::text[]) AS instrument,
    (dataset.metadata #>> '{properties,odc:region_code}'::text[]) AS region_code,
    (dataset.metadata #>> '{properties,odc:product_family}'::text[]) AS product_family,
    (dataset.metadata #>> '{properties,dea:dataset_maturity}'::text[]) AS dataset_maturity
   FROM ((agdc.dataset
     JOIN agdc.dataset_type ON ((dataset_type.id = dataset.dataset_type_ref)))
     JOIN agdc.metadata_type ON ((metadata_type.id = dataset_type.metadata_type_ref)))
  WHERE ((dataset.archived IS NULL) AND (dataset.dataset_type_ref = 24));
 =   DROP VIEW agdc.dv_cemp_insar_radarsat2_displacement_dataset;
       agdc       africa    false    201    201    201    201    280    198    198    200    200    200    201    201    201    673    8    673            �            1259    2903811 (   dv_cemp_insar_radarsat2_velocity_dataset    VIEW        CREATE VIEW agdc.dv_cemp_insar_radarsat2_velocity_dataset AS
 SELECT dataset.id,
    dataset.added AS indexed_time,
    dataset.added_by AS indexed_by,
    dataset_type.name AS product,
    dataset.dataset_type_ref AS dataset_type_id,
    metadata_type.name AS metadata_type,
    dataset.metadata_type_ref AS metadata_type_id,
    dataset.metadata AS metadata_doc,
    agdc.common_timestamp((dataset.metadata #>> '{properties,odc:processing_datetime}'::text[])) AS creation_time,
    (dataset.metadata #>> '{properties,odc:file_format}'::text[]) AS format,
    (dataset.metadata #>> '{label}'::text[]) AS label,
    agdc.float8range(((dataset.metadata #>> '{extent,lat,begin}'::text[]))::double precision, ((dataset.metadata #>> '{extent,lat,end}'::text[]))::double precision, '[]'::text) AS lat,
    agdc.float8range(((dataset.metadata #>> '{extent,lon,begin}'::text[]))::double precision, ((dataset.metadata #>> '{extent,lon,end}'::text[]))::double precision, '[]'::text) AS lon,
    tstzrange(LEAST(agdc.common_timestamp((dataset.metadata #>> '{properties,dtr:start_datetime}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{properties,datetime}'::text[]))), GREATEST(agdc.common_timestamp((dataset.metadata #>> '{properties,dtr:end_datetime}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{properties,datetime}'::text[]))), '[]'::text) AS "time",
    (dataset.metadata #>> '{properties,eo:platform}'::text[]) AS platform,
    (dataset.metadata #>> '{properties,eo:instrument}'::text[]) AS instrument,
    (dataset.metadata #>> '{properties,odc:region_code}'::text[]) AS region_code,
    (dataset.metadata #>> '{properties,odc:product_family}'::text[]) AS product_family,
    (dataset.metadata #>> '{properties,dea:dataset_maturity}'::text[]) AS dataset_maturity
   FROM ((agdc.dataset
     JOIN agdc.dataset_type ON ((dataset_type.id = dataset.dataset_type_ref)))
     JOIN agdc.metadata_type ON ((metadata_type.id = dataset_type.metadata_type_ref)))
  WHERE ((dataset.archived IS NULL) AND (dataset.dataset_type_ref = 25));
 9   DROP VIEW agdc.dv_cemp_insar_radarsat2_velocity_dataset;
       agdc       africa    false    201    200    200    198    201    201    198    200    201    201    201    201    280    673    673    8            �            1259    2903590    dv_eo3_dataset    VIEW     �  CREATE VIEW agdc.dv_eo3_dataset AS
 SELECT dataset.id,
    dataset.added AS indexed_time,
    dataset.added_by AS indexed_by,
    dataset_type.name AS product,
    dataset.dataset_type_ref AS dataset_type_id,
    metadata_type.name AS metadata_type,
    dataset.metadata_type_ref AS metadata_type_id,
    dataset.metadata AS metadata_doc,
    agdc.common_timestamp((dataset.metadata #>> '{properties,odc:processing_datetime}'::text[])) AS creation_time,
    (dataset.metadata #>> '{properties,odc:file_format}'::text[]) AS format,
    (dataset.metadata #>> '{label}'::text[]) AS label,
    agdc.float8range(((dataset.metadata #>> '{extent,lat,begin}'::text[]))::double precision, ((dataset.metadata #>> '{extent,lat,end}'::text[]))::double precision, '[]'::text) AS lat,
    agdc.float8range(((dataset.metadata #>> '{extent,lon,begin}'::text[]))::double precision, ((dataset.metadata #>> '{extent,lon,end}'::text[]))::double precision, '[]'::text) AS lon,
    tstzrange(LEAST(agdc.common_timestamp((dataset.metadata #>> '{properties,dtr:start_datetime}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{properties,datetime}'::text[]))), GREATEST(agdc.common_timestamp((dataset.metadata #>> '{properties,dtr:end_datetime}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{properties,datetime}'::text[]))), '[]'::text) AS "time",
    (dataset.metadata #>> '{properties,eo:platform}'::text[]) AS platform,
    (dataset.metadata #>> '{properties,eo:instrument}'::text[]) AS instrument,
    (dataset.metadata #>> '{properties,odc:region_code}'::text[]) AS region_code,
    (dataset.metadata #>> '{properties,odc:product_family}'::text[]) AS product_family,
    (dataset.metadata #>> '{properties,dea:dataset_maturity}'::text[]) AS dataset_maturity
   FROM ((agdc.dataset
     JOIN agdc.dataset_type ON ((dataset_type.id = dataset.dataset_type_ref)))
     JOIN agdc.metadata_type ON ((metadata_type.id = dataset_type.metadata_type_ref)))
  WHERE ((dataset.archived IS NULL) AND (dataset.metadata_type_ref = 1));
    DROP VIEW agdc.dv_eo3_dataset;
       agdc       africa    false    200    280    198    198    200    200    201    201    201    201    201    201    201    673    673    8                       1259    2904096    dv_eo3_landsat_ard_dataset    VIEW     w  CREATE VIEW agdc.dv_eo3_landsat_ard_dataset AS
 SELECT dataset.id,
    dataset.added AS indexed_time,
    dataset.added_by AS indexed_by,
    dataset_type.name AS product,
    dataset.dataset_type_ref AS dataset_type_id,
    metadata_type.name AS metadata_type,
    dataset.metadata_type_ref AS metadata_type_id,
    dataset.metadata AS metadata_doc,
    agdc.common_timestamp((dataset.metadata #>> '{properties,odc:processing_datetime}'::text[])) AS creation_time,
    (dataset.metadata #>> '{properties,odc:file_format}'::text[]) AS format,
    (dataset.metadata #>> '{label}'::text[]) AS label,
    ((dataset.metadata #>> '{properties,eo:cloud_cover}'::text[]))::double precision AS cloud_cover,
    (dataset.metadata #>> '{properties,dea:dataset_maturity}'::text[]) AS dataset_maturity,
    ((dataset.metadata #>> '{properties,eo:gsd}'::text[]))::double precision AS eo_gsd,
    ((dataset.metadata #>> '{properties,eo:sun_azimuth}'::text[]))::double precision AS eo_sun_azimuth,
    ((dataset.metadata #>> '{properties,eo:sun_elevation}'::text[]))::double precision AS eo_sun_elevation,
    ((dataset.metadata #>> '{properties,fmask:clear}'::text[]))::double precision AS fmask_clear,
    ((dataset.metadata #>> '{properties,fmask:cloud_shadow}'::text[]))::double precision AS fmask_cloud_shadow,
    ((dataset.metadata #>> '{properties,fmask:snow}'::text[]))::double precision AS fmask_snow,
    ((dataset.metadata #>> '{properties,fmask:water}'::text[]))::double precision AS fmask_water,
    ((dataset.metadata #>> '{properties,gqa:cep90}'::text[]))::double precision AS gqa,
    ((dataset.metadata #>> '{properties,gqa:abs_iterative_mean_x}'::text[]))::double precision AS gqa_abs_iterative_mean_x,
    ((dataset.metadata #>> '{properties,gqa:abs_iterative_mean_xy}'::text[]))::double precision AS gqa_abs_iterative_mean_xy,
    ((dataset.metadata #>> '{properties,gqa:abs_iterative_mean_y}'::text[]))::double precision AS gqa_abs_iterative_mean_y,
    ((dataset.metadata #>> '{properties,gqa:abs_x}'::text[]))::double precision AS gqa_abs_x,
    ((dataset.metadata #>> '{properties,gqa:abs_xy}'::text[]))::double precision AS gqa_abs_xy,
    ((dataset.metadata #>> '{properties,gqa:abs_y}'::text[]))::double precision AS gqa_abs_y,
    ((dataset.metadata #>> '{properties,gqa:cep90}'::text[]))::double precision AS gqa_cep90,
    ((dataset.metadata #>> '{properties,gqa:iterative_mean_x}'::text[]))::double precision AS gqa_iterative_mean_x,
    ((dataset.metadata #>> '{properties,gqa:iterative_mean_xy}'::text[]))::double precision AS gqa_iterative_mean_xy,
    ((dataset.metadata #>> '{properties,gqa:iterative_mean_y}'::text[]))::double precision AS gqa_iterative_mean_y,
    ((dataset.metadata #>> '{properties,gqa:iterative_stddev_x}'::text[]))::double precision AS gqa_iterative_stddev_x,
    ((dataset.metadata #>> '{properties,gqa:iterative_stddev_xy}'::text[]))::double precision AS gqa_iterative_stddev_xy,
    ((dataset.metadata #>> '{properties,gqa:iterative_stddev_y}'::text[]))::double precision AS gqa_iterative_stddev_y,
    ((dataset.metadata #>> '{properties,gqa:mean_x}'::text[]))::double precision AS gqa_mean_x,
    ((dataset.metadata #>> '{properties,gqa:mean_xy}'::text[]))::double precision AS gqa_mean_xy,
    ((dataset.metadata #>> '{properties,gqa:mean_y}'::text[]))::double precision AS gqa_mean_y,
    ((dataset.metadata #>> '{properties,gqa:stddev_x}'::text[]))::double precision AS gqa_stddev_x,
    ((dataset.metadata #>> '{properties,gqa:stddev_xy}'::text[]))::double precision AS gqa_stddev_xy,
    ((dataset.metadata #>> '{properties,gqa:stddev_y}'::text[]))::double precision AS gqa_stddev_y,
    (dataset.metadata #>> '{properties,eo:instrument}'::text[]) AS instrument,
    agdc.float8range(((dataset.metadata #>> '{extent,lat,begin}'::text[]))::double precision, ((dataset.metadata #>> '{extent,lat,end}'::text[]))::double precision, '[]'::text) AS lat,
    agdc.float8range(((dataset.metadata #>> '{extent,lon,begin}'::text[]))::double precision, ((dataset.metadata #>> '{extent,lon,end}'::text[]))::double precision, '[]'::text) AS lon,
    (dataset.metadata #>> '{properties,eo:platform}'::text[]) AS platform,
    (dataset.metadata #>> '{properties,odc:product_family}'::text[]) AS product_family,
    (dataset.metadata #>> '{properties,odc:region_code}'::text[]) AS region_code,
    tstzrange(LEAST(agdc.common_timestamp((dataset.metadata #>> '{properties,dtr:start_datetime}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{properties,datetime}'::text[]))), GREATEST(agdc.common_timestamp((dataset.metadata #>> '{properties,dtr:end_datetime}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{properties,datetime}'::text[]))), '[]'::text) AS "time"
   FROM ((agdc.dataset
     JOIN agdc.dataset_type ON ((dataset_type.id = dataset.dataset_type_ref)))
     JOIN agdc.metadata_type ON ((metadata_type.id = dataset_type.metadata_type_ref)))
  WHERE ((dataset.archived IS NULL) AND (dataset.metadata_type_ref = 5));
 +   DROP VIEW agdc.dv_eo3_landsat_ard_dataset;
       agdc       africa    false    201    201    201    201    201    201    201    200    200    200    198    198    280    673    8    673                       1259    2904101    dv_eo3_landsat_l1_dataset    VIEW     F
  CREATE VIEW agdc.dv_eo3_landsat_l1_dataset AS
 SELECT dataset.id,
    dataset.added AS indexed_time,
    dataset.added_by AS indexed_by,
    dataset_type.name AS product,
    dataset.dataset_type_ref AS dataset_type_id,
    metadata_type.name AS metadata_type,
    dataset.metadata_type_ref AS metadata_type_id,
    dataset.metadata AS metadata_doc,
    agdc.common_timestamp((dataset.metadata #>> '{properties,odc:processing_datetime}'::text[])) AS creation_time,
    (dataset.metadata #>> '{properties,odc:file_format}'::text[]) AS format,
    (dataset.metadata #>> '{label}'::text[]) AS label,
    ((dataset.metadata #>> '{properties,eo:cloud_cover}'::text[]))::double precision AS cloud_cover,
    (dataset.metadata #>> '{properties,dea:dataset_maturity}'::text[]) AS dataset_maturity,
    ((dataset.metadata #>> '{properties,eo:gsd}'::text[]))::double precision AS eo_gsd,
    ((dataset.metadata #>> '{properties,eo:sun_azimuth}'::text[]))::double precision AS eo_sun_azimuth,
    ((dataset.metadata #>> '{properties,eo:sun_elevation}'::text[]))::double precision AS eo_sun_elevation,
    (dataset.metadata #>> '{properties,eo:instrument}'::text[]) AS instrument,
    (dataset.metadata #>> '{properties,landsat:landsat_product_id}'::text[]) AS landsat_product_id,
    (dataset.metadata #>> '{properties,landsat:landsat_scene_id}'::text[]) AS landsat_scene_id,
    agdc.float8range(((dataset.metadata #>> '{extent,lat,begin}'::text[]))::double precision, ((dataset.metadata #>> '{extent,lat,end}'::text[]))::double precision, '[]'::text) AS lat,
    agdc.float8range(((dataset.metadata #>> '{extent,lon,begin}'::text[]))::double precision, ((dataset.metadata #>> '{extent,lon,end}'::text[]))::double precision, '[]'::text) AS lon,
    (dataset.metadata #>> '{properties,eo:platform}'::text[]) AS platform,
    (dataset.metadata #>> '{properties,odc:product_family}'::text[]) AS product_family,
    (dataset.metadata #>> '{properties,odc:region_code}'::text[]) AS region_code,
    tstzrange(LEAST(agdc.common_timestamp((dataset.metadata #>> '{properties,dtr:start_datetime}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{properties,datetime}'::text[]))), GREATEST(agdc.common_timestamp((dataset.metadata #>> '{properties,dtr:end_datetime}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{properties,datetime}'::text[]))), '[]'::text) AS "time"
   FROM ((agdc.dataset
     JOIN agdc.dataset_type ON ((dataset_type.id = dataset.dataset_type_ref)))
     JOIN agdc.metadata_type ON ((metadata_type.id = dataset_type.metadata_type_ref)))
  WHERE ((dataset.archived IS NULL) AND (dataset.metadata_type_ref = 6));
 *   DROP VIEW agdc.dv_eo3_landsat_l1_dataset;
       agdc       africa    false    201    201    201    280    198    198    200    200    200    201    201    201    201    673    673    8            �            1259    2903585    dv_eo_dataset    VIEW     �
  CREATE VIEW agdc.dv_eo_dataset AS
 SELECT dataset.id,
    dataset.added AS indexed_time,
    dataset.added_by AS indexed_by,
    dataset_type.name AS product,
    dataset.dataset_type_ref AS dataset_type_id,
    metadata_type.name AS metadata_type,
    dataset.metadata_type_ref AS metadata_type_id,
    dataset.metadata AS metadata_doc,
    agdc.common_timestamp((dataset.metadata #>> '{creation_dt}'::text[])) AS creation_time,
    (dataset.metadata #>> '{format,name}'::text[]) AS format,
    (dataset.metadata #>> '{ga_label}'::text[]) AS label,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text) AS lat,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text) AS lon,
    tstzrange(LEAST(agdc.common_timestamp((dataset.metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((dataset.metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), '[]'::text) AS "time",
    (dataset.metadata #>> '{platform,code}'::text[]) AS platform,
    (dataset.metadata #>> '{instrument,name}'::text[]) AS instrument,
    (dataset.metadata #>> '{product_type}'::text[]) AS product_type
   FROM ((agdc.dataset
     JOIN agdc.dataset_type ON ((dataset_type.id = dataset.dataset_type_ref)))
     JOIN agdc.metadata_type ON ((metadata_type.id = dataset_type.metadata_type_ref)))
  WHERE ((dataset.archived IS NULL) AND (dataset.metadata_type_ref = 2));
    DROP VIEW agdc.dv_eo_dataset;
       agdc       africa    false    201    201    201    201    198    280    200    200    200    198    201    201    201    673    673    8                       1259    2904106    dv_eo_plus_dataset    VIEW     u  CREATE VIEW agdc.dv_eo_plus_dataset AS
 SELECT dataset.id,
    dataset.added AS indexed_time,
    dataset.added_by AS indexed_by,
    dataset_type.name AS product,
    dataset.dataset_type_ref AS dataset_type_id,
    metadata_type.name AS metadata_type,
    dataset.metadata_type_ref AS metadata_type_id,
    dataset.metadata AS metadata_doc,
    agdc.common_timestamp((dataset.metadata #>> '{system_information,time_processed}'::text[])) AS creation_time,
    (dataset.metadata #>> '{format,name}'::text[]) AS format,
    (dataset.metadata #>> '{ga_label}'::text[]) AS label,
    ((dataset.metadata #>> '{gqa,cep90}'::text[]))::double precision AS gqa,
    ((dataset.metadata #>> '{gqa,residual,abs_iterative_mean,xy}'::text[]))::double precision AS gqa_abs_iterative_mean_xy,
    ((dataset.metadata #>> '{gqa,residual,abs,xy}'::text[]))::double precision AS gqa_abs_xy,
    ((dataset.metadata #>> '{gqa,residual,cep90}'::text[]))::double precision AS gqa_cep90,
    (dataset.metadata #>> '{gqa,error_message}'::text[]) AS gqa_error_message,
    ((dataset.metadata #>> '{gqa,final_qa_count}'::text[]))::integer AS gqa_final_qa_count,
    ((dataset.metadata #>> '{gqa,residual,iterative_mean,xy}'::text[]))::double precision AS gqa_iterative_mean_xy,
    ((dataset.metadata #>> '{gqa,residual,iterative_stddev,xy}'::text[]))::double precision AS gqa_iterative_stddev_xy,
    ((dataset.metadata #>> '{gqa,residual,mean,xy}'::text[]))::double precision AS gqa_mean_xy,
    (dataset.metadata #>> '{gqa,ref_source}'::text[]) AS gqa_ref_source,
    ((dataset.metadata #>> '{gqa,residual,stddev,xy}'::text[]))::double precision AS gqa_stddev_xy,
    (dataset.metadata #>> '{instrument,name}'::text[]) AS instrument,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text) AS lat,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text) AS lon,
    (dataset.metadata #>> '{platform,code}'::text[]) AS platform,
    (dataset.metadata #>> '{product_type}'::text[]) AS product_type,
    (dataset.metadata #>> '{provider,reference_code}'::text[]) AS region_code,
    tstzrange(agdc.common_timestamp((dataset.metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,to_dt}'::text[])), '[]'::text) AS "time"
   FROM ((agdc.dataset
     JOIN agdc.dataset_type ON ((dataset_type.id = dataset.dataset_type_ref)))
     JOIN agdc.metadata_type ON ((metadata_type.id = dataset_type.metadata_type_ref)))
  WHERE ((dataset.archived IS NULL) AND (dataset.metadata_type_ref = 7));
 #   DROP VIEW agdc.dv_eo_plus_dataset;
       agdc       africa    false    201    201    201    201    201    280    201    200    200    198    198    200    201    673    8    673                       1259    2904090    dv_eo_s2_nrt_dataset    VIEW     
  CREATE VIEW agdc.dv_eo_s2_nrt_dataset AS
 SELECT dataset.id,
    dataset.added AS indexed_time,
    dataset.added_by AS indexed_by,
    dataset_type.name AS product,
    dataset.dataset_type_ref AS dataset_type_id,
    metadata_type.name AS metadata_type,
    dataset.metadata_type_ref AS metadata_type_id,
    dataset.metadata AS metadata_doc,
    agdc.common_timestamp((dataset.metadata #>> '{system_information,time_processed}'::text[])) AS creation_time,
    (dataset.metadata #>> '{format,name}'::text[]) AS format,
    (dataset.metadata #>> '{tile_id}'::text[]) AS label,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text) AS lat,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text) AS lon,
    tstzrange(agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[])), '[]'::text) AS "time",
    (dataset.metadata #>> '{platform,code}'::text[]) AS platform,
    (dataset.metadata #>> '{instrument,name}'::text[]) AS instrument,
    (dataset.metadata #>> '{product_type}'::text[]) AS product_type
   FROM ((agdc.dataset
     JOIN agdc.dataset_type ON ((dataset_type.id = dataset.dataset_type_ref)))
     JOIN agdc.metadata_type ON ((metadata_type.id = dataset_type.metadata_type_ref)))
  WHERE ((dataset.archived IS NULL) AND (dataset.metadata_type_ref = 4));
 %   DROP VIEW agdc.dv_eo_s2_nrt_dataset;
       agdc       africa    false    201    201    198    280    201    201    201    201    198    200    200    200    201    8    673    673            �            1259    2903818 &   dv_fc_percentile_albers_annual_dataset    VIEW     �
  CREATE VIEW agdc.dv_fc_percentile_albers_annual_dataset AS
 SELECT dataset.id,
    dataset.added AS indexed_time,
    dataset.added_by AS indexed_by,
    dataset_type.name AS product,
    dataset.dataset_type_ref AS dataset_type_id,
    metadata_type.name AS metadata_type,
    dataset.metadata_type_ref AS metadata_type_id,
    dataset.metadata AS metadata_doc,
    agdc.common_timestamp((dataset.metadata #>> '{creation_dt}'::text[])) AS creation_time,
    (dataset.metadata #>> '{format,name}'::text[]) AS format,
    (dataset.metadata #>> '{ga_label}'::text[]) AS label,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text) AS lat,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text) AS lon,
    tstzrange(LEAST(agdc.common_timestamp((dataset.metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((dataset.metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), '[]'::text) AS "time",
    (dataset.metadata #>> '{platform,code}'::text[]) AS platform,
    (dataset.metadata #>> '{instrument,name}'::text[]) AS instrument,
    (dataset.metadata #>> '{product_type}'::text[]) AS product_type
   FROM ((agdc.dataset
     JOIN agdc.dataset_type ON ((dataset_type.id = dataset.dataset_type_ref)))
     JOIN agdc.metadata_type ON ((metadata_type.id = dataset_type.metadata_type_ref)))
  WHERE ((dataset.archived IS NULL) AND (dataset.dataset_type_ref = 26));
 7   DROP VIEW agdc.dv_fc_percentile_albers_annual_dataset;
       agdc       africa    false    198    280    201    201    201    201    201    201    201    200    200    200    198    673    8    673            �            1259    2903825 (   dv_fc_percentile_albers_seasonal_dataset    VIEW     �
  CREATE VIEW agdc.dv_fc_percentile_albers_seasonal_dataset AS
 SELECT dataset.id,
    dataset.added AS indexed_time,
    dataset.added_by AS indexed_by,
    dataset_type.name AS product,
    dataset.dataset_type_ref AS dataset_type_id,
    metadata_type.name AS metadata_type,
    dataset.metadata_type_ref AS metadata_type_id,
    dataset.metadata AS metadata_doc,
    agdc.common_timestamp((dataset.metadata #>> '{creation_dt}'::text[])) AS creation_time,
    (dataset.metadata #>> '{format,name}'::text[]) AS format,
    (dataset.metadata #>> '{ga_label}'::text[]) AS label,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text) AS lat,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text) AS lon,
    tstzrange(LEAST(agdc.common_timestamp((dataset.metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((dataset.metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), '[]'::text) AS "time",
    (dataset.metadata #>> '{platform,code}'::text[]) AS platform,
    (dataset.metadata #>> '{instrument,name}'::text[]) AS instrument,
    (dataset.metadata #>> '{product_type}'::text[]) AS product_type
   FROM ((agdc.dataset
     JOIN agdc.dataset_type ON ((dataset_type.id = dataset.dataset_type_ref)))
     JOIN agdc.metadata_type ON ((metadata_type.id = dataset_type.metadata_type_ref)))
  WHERE ((dataset.archived IS NULL) AND (dataset.dataset_type_ref = 27));
 9   DROP VIEW agdc.dv_fc_percentile_albers_seasonal_dataset;
       agdc       africa    false    198    280    198    200    200    200    201    201    201    201    201    201    201    673    8    673                       1259    2904122    dv_ga_ls8c_ard_3_dataset    VIEW     u  CREATE VIEW agdc.dv_ga_ls8c_ard_3_dataset AS
 SELECT dataset.id,
    dataset.added AS indexed_time,
    dataset.added_by AS indexed_by,
    dataset_type.name AS product,
    dataset.dataset_type_ref AS dataset_type_id,
    metadata_type.name AS metadata_type,
    dataset.metadata_type_ref AS metadata_type_id,
    dataset.metadata AS metadata_doc,
    agdc.common_timestamp((dataset.metadata #>> '{properties,odc:processing_datetime}'::text[])) AS creation_time,
    (dataset.metadata #>> '{properties,odc:file_format}'::text[]) AS format,
    (dataset.metadata #>> '{label}'::text[]) AS label,
    ((dataset.metadata #>> '{properties,gqa:cep90}'::text[]))::double precision AS gqa,
    agdc.float8range(((dataset.metadata #>> '{extent,lat,begin}'::text[]))::double precision, ((dataset.metadata #>> '{extent,lat,end}'::text[]))::double precision, '[]'::text) AS lat,
    agdc.float8range(((dataset.metadata #>> '{extent,lon,begin}'::text[]))::double precision, ((dataset.metadata #>> '{extent,lon,end}'::text[]))::double precision, '[]'::text) AS lon,
    tstzrange(LEAST(agdc.common_timestamp((dataset.metadata #>> '{properties,dtr:start_datetime}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{properties,datetime}'::text[]))), GREATEST(agdc.common_timestamp((dataset.metadata #>> '{properties,dtr:end_datetime}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{properties,datetime}'::text[]))), '[]'::text) AS "time",
    ((dataset.metadata #>> '{properties,eo:gsd}'::text[]))::double precision AS eo_gsd,
    (dataset.metadata #>> '{properties,eo:platform}'::text[]) AS platform,
    ((dataset.metadata #>> '{properties,gqa:abs_x}'::text[]))::double precision AS gqa_abs_x,
    ((dataset.metadata #>> '{properties,gqa:abs_y}'::text[]))::double precision AS gqa_abs_y,
    ((dataset.metadata #>> '{properties,gqa:cep90}'::text[]))::double precision AS gqa_cep90,
    ((dataset.metadata #>> '{properties,fmask:snow}'::text[]))::double precision AS fmask_snow,
    ((dataset.metadata #>> '{properties,gqa:abs_xy}'::text[]))::double precision AS gqa_abs_xy,
    ((dataset.metadata #>> '{properties,gqa:mean_x}'::text[]))::double precision AS gqa_mean_x,
    ((dataset.metadata #>> '{properties,gqa:mean_y}'::text[]))::double precision AS gqa_mean_y,
    (dataset.metadata #>> '{properties,eo:instrument}'::text[]) AS instrument,
    ((dataset.metadata #>> '{properties,eo:cloud_cover}'::text[]))::double precision AS cloud_cover,
    ((dataset.metadata #>> '{properties,fmask:clear}'::text[]))::double precision AS fmask_clear,
    ((dataset.metadata #>> '{properties,fmask:water}'::text[]))::double precision AS fmask_water,
    ((dataset.metadata #>> '{properties,gqa:mean_xy}'::text[]))::double precision AS gqa_mean_xy,
    (dataset.metadata #>> '{properties,odc:region_code}'::text[]) AS region_code,
    ((dataset.metadata #>> '{properties,gqa:stddev_x}'::text[]))::double precision AS gqa_stddev_x,
    ((dataset.metadata #>> '{properties,gqa:stddev_y}'::text[]))::double precision AS gqa_stddev_y,
    ((dataset.metadata #>> '{properties,gqa:stddev_xy}'::text[]))::double precision AS gqa_stddev_xy,
    ((dataset.metadata #>> '{properties,eo:sun_azimuth}'::text[]))::double precision AS eo_sun_azimuth,
    (dataset.metadata #>> '{properties,odc:product_family}'::text[]) AS product_family,
    (dataset.metadata #>> '{properties,dea:dataset_maturity}'::text[]) AS dataset_maturity,
    ((dataset.metadata #>> '{properties,eo:sun_elevation}'::text[]))::double precision AS eo_sun_elevation,
    ((dataset.metadata #>> '{properties,fmask:cloud_shadow}'::text[]))::double precision AS fmask_cloud_shadow,
    ((dataset.metadata #>> '{properties,gqa:iterative_mean_x}'::text[]))::double precision AS gqa_iterative_mean_x,
    ((dataset.metadata #>> '{properties,gqa:iterative_mean_y}'::text[]))::double precision AS gqa_iterative_mean_y,
    ((dataset.metadata #>> '{properties,gqa:iterative_mean_xy}'::text[]))::double precision AS gqa_iterative_mean_xy,
    ((dataset.metadata #>> '{properties,gqa:iterative_stddev_x}'::text[]))::double precision AS gqa_iterative_stddev_x,
    ((dataset.metadata #>> '{properties,gqa:iterative_stddev_y}'::text[]))::double precision AS gqa_iterative_stddev_y,
    ((dataset.metadata #>> '{properties,gqa:iterative_stddev_xy}'::text[]))::double precision AS gqa_iterative_stddev_xy,
    ((dataset.metadata #>> '{properties,gqa:abs_iterative_mean_x}'::text[]))::double precision AS gqa_abs_iterative_mean_x,
    ((dataset.metadata #>> '{properties,gqa:abs_iterative_mean_y}'::text[]))::double precision AS gqa_abs_iterative_mean_y,
    ((dataset.metadata #>> '{properties,gqa:abs_iterative_mean_xy}'::text[]))::double precision AS gqa_abs_iterative_mean_xy
   FROM ((agdc.dataset
     JOIN agdc.dataset_type ON ((dataset_type.id = dataset.dataset_type_ref)))
     JOIN agdc.metadata_type ON ((metadata_type.id = dataset_type.metadata_type_ref)))
  WHERE ((dataset.archived IS NULL) AND (dataset.dataset_type_ref = 61));
 )   DROP VIEW agdc.dv_ga_ls8c_ard_3_dataset;
       agdc       africa    false    201    280    198    198    200    200    200    201    201    201    201    201    201    673    8    673                       1259    2904131 "   dv_ga_s2a_ard_nbar_granule_dataset    VIEW     �  CREATE VIEW agdc.dv_ga_s2a_ard_nbar_granule_dataset AS
 SELECT dataset.id,
    dataset.added AS indexed_time,
    dataset.added_by AS indexed_by,
    dataset_type.name AS product,
    dataset.dataset_type_ref AS dataset_type_id,
    metadata_type.name AS metadata_type,
    dataset.metadata_type_ref AS metadata_type_id,
    dataset.metadata AS metadata_doc,
    agdc.common_timestamp((dataset.metadata #>> '{system_information,time_processed}'::text[])) AS creation_time,
    (dataset.metadata #>> '{format,name}'::text[]) AS format,
    (dataset.metadata #>> '{ga_label}'::text[]) AS label,
    ((dataset.metadata #>> '{gqa,cep90}'::text[]))::double precision AS gqa,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text) AS lat,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text) AS lon,
    tstzrange(agdc.common_timestamp((dataset.metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,to_dt}'::text[])), '[]'::text) AS "time",
    (dataset.metadata #>> '{platform,code}'::text[]) AS platform,
    ((dataset.metadata #>> '{gqa,residual,cep90}'::text[]))::double precision AS gqa_cep90,
    ((dataset.metadata #>> '{gqa,residual,abs,xy}'::text[]))::double precision AS gqa_abs_xy,
    (dataset.metadata #>> '{instrument,name}'::text[]) AS instrument,
    ((dataset.metadata #>> '{gqa,residual,mean,xy}'::text[]))::double precision AS gqa_mean_xy,
    (dataset.metadata #>> '{provider,reference_code}'::text[]) AS region_code,
    (dataset.metadata #>> '{product_type}'::text[]) AS product_type,
    ((dataset.metadata #>> '{gqa,residual,stddev,xy}'::text[]))::double precision AS gqa_stddev_xy,
    (dataset.metadata #>> '{gqa,ref_source}'::text[]) AS gqa_ref_source,
    (dataset.metadata #>> '{gqa,error_message}'::text[]) AS gqa_error_message,
    ((dataset.metadata #>> '{gqa,final_qa_count}'::text[]))::integer AS gqa_final_qa_count,
    ((dataset.metadata #>> '{gqa,residual,iterative_mean,xy}'::text[]))::double precision AS gqa_iterative_mean_xy,
    ((dataset.metadata #>> '{gqa,residual,iterative_stddev,xy}'::text[]))::double precision AS gqa_iterative_stddev_xy,
    ((dataset.metadata #>> '{gqa,residual,abs_iterative_mean,xy}'::text[]))::double precision AS gqa_abs_iterative_mean_xy
   FROM ((agdc.dataset
     JOIN agdc.dataset_type ON ((dataset_type.id = dataset.dataset_type_ref)))
     JOIN agdc.metadata_type ON ((metadata_type.id = dataset_type.metadata_type_ref)))
  WHERE ((dataset.archived IS NULL) AND (dataset.dataset_type_ref = 62));
 3   DROP VIEW agdc.dv_ga_s2a_ard_nbar_granule_dataset;
       agdc       africa    false    198    201    201    201    201    201    201    200    200    200    198    201    280    673    673    8                       1259    2904140 "   dv_ga_s2b_ard_nbar_granule_dataset    VIEW     �  CREATE VIEW agdc.dv_ga_s2b_ard_nbar_granule_dataset AS
 SELECT dataset.id,
    dataset.added AS indexed_time,
    dataset.added_by AS indexed_by,
    dataset_type.name AS product,
    dataset.dataset_type_ref AS dataset_type_id,
    metadata_type.name AS metadata_type,
    dataset.metadata_type_ref AS metadata_type_id,
    dataset.metadata AS metadata_doc,
    agdc.common_timestamp((dataset.metadata #>> '{system_information,time_processed}'::text[])) AS creation_time,
    (dataset.metadata #>> '{format,name}'::text[]) AS format,
    (dataset.metadata #>> '{ga_label}'::text[]) AS label,
    ((dataset.metadata #>> '{gqa,cep90}'::text[]))::double precision AS gqa,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text) AS lat,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text) AS lon,
    tstzrange(agdc.common_timestamp((dataset.metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,to_dt}'::text[])), '[]'::text) AS "time",
    (dataset.metadata #>> '{platform,code}'::text[]) AS platform,
    ((dataset.metadata #>> '{gqa,residual,cep90}'::text[]))::double precision AS gqa_cep90,
    ((dataset.metadata #>> '{gqa,residual,abs,xy}'::text[]))::double precision AS gqa_abs_xy,
    (dataset.metadata #>> '{instrument,name}'::text[]) AS instrument,
    ((dataset.metadata #>> '{gqa,residual,mean,xy}'::text[]))::double precision AS gqa_mean_xy,
    (dataset.metadata #>> '{provider,reference_code}'::text[]) AS region_code,
    (dataset.metadata #>> '{product_type}'::text[]) AS product_type,
    ((dataset.metadata #>> '{gqa,residual,stddev,xy}'::text[]))::double precision AS gqa_stddev_xy,
    (dataset.metadata #>> '{gqa,ref_source}'::text[]) AS gqa_ref_source,
    (dataset.metadata #>> '{gqa,error_message}'::text[]) AS gqa_error_message,
    ((dataset.metadata #>> '{gqa,final_qa_count}'::text[]))::integer AS gqa_final_qa_count,
    ((dataset.metadata #>> '{gqa,residual,iterative_mean,xy}'::text[]))::double precision AS gqa_iterative_mean_xy,
    ((dataset.metadata #>> '{gqa,residual,iterative_stddev,xy}'::text[]))::double precision AS gqa_iterative_stddev_xy,
    ((dataset.metadata #>> '{gqa,residual,abs_iterative_mean,xy}'::text[]))::double precision AS gqa_abs_iterative_mean_xy
   FROM ((agdc.dataset
     JOIN agdc.dataset_type ON ((dataset_type.id = dataset.dataset_type_ref)))
     JOIN agdc.metadata_type ON ((metadata_type.id = dataset_type.metadata_type_ref)))
  WHERE ((dataset.archived IS NULL) AND (dataset.dataset_type_ref = 63));
 3   DROP VIEW agdc.dv_ga_s2b_ard_nbar_granule_dataset;
       agdc       africa    false    200    280    198    198    200    200    201    201    201    201    201    201    201    673    8    673            �            1259    2903834    dv_geodata_coast_100k_dataset    VIEW     �
  CREATE VIEW agdc.dv_geodata_coast_100k_dataset AS
 SELECT dataset.id,
    dataset.added AS indexed_time,
    dataset.added_by AS indexed_by,
    dataset_type.name AS product,
    dataset.dataset_type_ref AS dataset_type_id,
    metadata_type.name AS metadata_type,
    dataset.metadata_type_ref AS metadata_type_id,
    dataset.metadata AS metadata_doc,
    agdc.common_timestamp((dataset.metadata #>> '{creation_dt}'::text[])) AS creation_time,
    (dataset.metadata #>> '{format,name}'::text[]) AS format,
    (dataset.metadata #>> '{ga_label}'::text[]) AS label,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text) AS lat,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text) AS lon,
    tstzrange(LEAST(agdc.common_timestamp((dataset.metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((dataset.metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), '[]'::text) AS "time",
    (dataset.metadata #>> '{platform,code}'::text[]) AS platform,
    (dataset.metadata #>> '{instrument,name}'::text[]) AS instrument,
    (dataset.metadata #>> '{product_type}'::text[]) AS product_type
   FROM ((agdc.dataset
     JOIN agdc.dataset_type ON ((dataset_type.id = dataset.dataset_type_ref)))
     JOIN agdc.metadata_type ON ((metadata_type.id = dataset_type.metadata_type_ref)))
  WHERE ((dataset.archived IS NULL) AND (dataset.dataset_type_ref = 28));
 .   DROP VIEW agdc.dv_geodata_coast_100k_dataset;
       agdc       africa    false    201    201    201    280    198    200    200    200    201    201    201    201    198    673    673    8                       1259    2904111    dv_gqa_eo_dataset    VIEW     v  CREATE VIEW agdc.dv_gqa_eo_dataset AS
 SELECT dataset.id,
    dataset.added AS indexed_time,
    dataset.added_by AS indexed_by,
    dataset_type.name AS product,
    dataset.dataset_type_ref AS dataset_type_id,
    metadata_type.name AS metadata_type,
    dataset.metadata_type_ref AS metadata_type_id,
    dataset.metadata AS metadata_doc,
    agdc.common_timestamp((dataset.metadata #>> '{system_information,time_processed}'::text[])) AS creation_time,
    (dataset.metadata #>> '{format,name}'::text[]) AS format,
    (dataset.metadata #>> '{ga_label}'::text[]) AS label,
    ((dataset.metadata #>> '{gqa,cep90}'::text[]))::double precision AS gqa,
    ((dataset.metadata #>> '{gqa,residual,abs_iterative_mean,xy}'::text[]))::double precision AS gqa_abs_iterative_mean_xy,
    ((dataset.metadata #>> '{gqa,residual,abs,xy}'::text[]))::double precision AS gqa_abs_xy,
    ((dataset.metadata #>> '{gqa,residual,cep90}'::text[]))::double precision AS gqa_cep90,
    (dataset.metadata #>> '{gqa,error_message}'::text[]) AS gqa_error_message,
    ((dataset.metadata #>> '{gqa,final_gcp_count}'::text[]))::integer AS gqa_final_gcp_count,
    ((dataset.metadata #>> '{gqa,residual,iterative_mean,xy}'::text[]))::double precision AS gqa_iterative_mean_xy,
    ((dataset.metadata #>> '{gqa,residual,iterative_stddev,xy}'::text[]))::double precision AS gqa_iterative_stddev_xy,
    ((dataset.metadata #>> '{gqa,residual,mean,xy}'::text[]))::double precision AS gqa_mean_xy,
    (dataset.metadata #>> '{gqa,ref_source}'::text[]) AS gqa_ref_source,
    ((dataset.metadata #>> '{gqa,residual,stddev,xy}'::text[]))::double precision AS gqa_stddev_xy,
    (dataset.metadata #>> '{instrument,name}'::text[]) AS instrument,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text) AS lat,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text) AS lon,
    (dataset.metadata #>> '{platform,code}'::text[]) AS platform,
    (dataset.metadata #>> '{product_type}'::text[]) AS product_type,
    (dataset.metadata #>> '{provider,reference_code}'::text[]) AS region_code,
    tstzrange(agdc.common_timestamp((dataset.metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,to_dt}'::text[])), '[]'::text) AS "time"
   FROM ((agdc.dataset
     JOIN agdc.dataset_type ON ((dataset_type.id = dataset.dataset_type_ref)))
     JOIN agdc.metadata_type ON ((metadata_type.id = dataset_type.metadata_type_ref)))
  WHERE ((dataset.archived IS NULL) AND (dataset.metadata_type_ref = 8));
 "   DROP VIEW agdc.dv_gqa_eo_dataset;
       agdc       africa    false    200    200    201    201    201    201    201    201    201    198    280    198    200    673    8    673            �            1259    2903843    dv_high_tide_comp_20p_dataset    VIEW     �
  CREATE VIEW agdc.dv_high_tide_comp_20p_dataset AS
 SELECT dataset.id,
    dataset.added AS indexed_time,
    dataset.added_by AS indexed_by,
    dataset_type.name AS product,
    dataset.dataset_type_ref AS dataset_type_id,
    metadata_type.name AS metadata_type,
    dataset.metadata_type_ref AS metadata_type_id,
    dataset.metadata AS metadata_doc,
    agdc.common_timestamp((dataset.metadata #>> '{creation_dt}'::text[])) AS creation_time,
    (dataset.metadata #>> '{format,name}'::text[]) AS format,
    (dataset.metadata #>> '{ga_label}'::text[]) AS label,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text) AS lat,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text) AS lon,
    tstzrange(LEAST(agdc.common_timestamp((dataset.metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((dataset.metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), '[]'::text) AS "time",
    (dataset.metadata #>> '{platform,code}'::text[]) AS platform,
    (dataset.metadata #>> '{instrument,name}'::text[]) AS instrument,
    (dataset.metadata #>> '{product_type}'::text[]) AS product_type
   FROM ((agdc.dataset
     JOIN agdc.dataset_type ON ((dataset_type.id = dataset.dataset_type_ref)))
     JOIN agdc.metadata_type ON ((metadata_type.id = dataset_type.metadata_type_ref)))
  WHERE ((dataset.archived IS NULL) AND (dataset.dataset_type_ref = 29));
 .   DROP VIEW agdc.dv_high_tide_comp_20p_dataset;
       agdc       africa    false    200    200    200    201    201    201    201    201    201    201    280    198    198    673    8    673            �            1259    2903861 *   dv_historical_airborne_photography_dataset    VIEW     �
  CREATE VIEW agdc.dv_historical_airborne_photography_dataset AS
 SELECT dataset.id,
    dataset.added AS indexed_time,
    dataset.added_by AS indexed_by,
    dataset_type.name AS product,
    dataset.dataset_type_ref AS dataset_type_id,
    metadata_type.name AS metadata_type,
    dataset.metadata_type_ref AS metadata_type_id,
    dataset.metadata AS metadata_doc,
    agdc.common_timestamp((dataset.metadata #>> '{creation_dt}'::text[])) AS creation_time,
    (dataset.metadata #>> '{format,name}'::text[]) AS format,
    (dataset.metadata #>> '{ga_label}'::text[]) AS label,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text) AS lat,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text) AS lon,
    tstzrange(LEAST(agdc.common_timestamp((dataset.metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((dataset.metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), '[]'::text) AS "time",
    (dataset.metadata #>> '{platform,code}'::text[]) AS platform,
    (dataset.metadata #>> '{instrument,name}'::text[]) AS instrument,
    (dataset.metadata #>> '{product_type}'::text[]) AS product_type
   FROM ((agdc.dataset
     JOIN agdc.dataset_type ON ((dataset_type.id = dataset.dataset_type_ref)))
     JOIN agdc.metadata_type ON ((metadata_type.id = dataset_type.metadata_type_ref)))
  WHERE ((dataset.archived IS NULL) AND (dataset.dataset_type_ref = 31));
 ;   DROP VIEW agdc.dv_historical_airborne_photography_dataset;
       agdc       africa    false    200    198    198    201    201    201    201    201    201    201    280    200    200    8    673    673            �            1259    2903879    dv_item_v2_conf_dataset    VIEW     �
  CREATE VIEW agdc.dv_item_v2_conf_dataset AS
 SELECT dataset.id,
    dataset.added AS indexed_time,
    dataset.added_by AS indexed_by,
    dataset_type.name AS product,
    dataset.dataset_type_ref AS dataset_type_id,
    metadata_type.name AS metadata_type,
    dataset.metadata_type_ref AS metadata_type_id,
    dataset.metadata AS metadata_doc,
    agdc.common_timestamp((dataset.metadata #>> '{creation_dt}'::text[])) AS creation_time,
    (dataset.metadata #>> '{format,name}'::text[]) AS format,
    (dataset.metadata #>> '{ga_label}'::text[]) AS label,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text) AS lat,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text) AS lon,
    tstzrange(LEAST(agdc.common_timestamp((dataset.metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((dataset.metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), '[]'::text) AS "time",
    (dataset.metadata #>> '{platform,code}'::text[]) AS platform,
    (dataset.metadata #>> '{instrument,name}'::text[]) AS instrument,
    (dataset.metadata #>> '{product_type}'::text[]) AS product_type
   FROM ((agdc.dataset
     JOIN agdc.dataset_type ON ((dataset_type.id = dataset.dataset_type_ref)))
     JOIN agdc.metadata_type ON ((metadata_type.id = dataset_type.metadata_type_ref)))
  WHERE ((dataset.archived IS NULL) AND (dataset.dataset_type_ref = 33));
 (   DROP VIEW agdc.dv_item_v2_conf_dataset;
       agdc       africa    false    201    201    201    201    201    280    198    198    200    200    201    200    201    673    673    8            �            1259    2903870    dv_item_v2_dataset    VIEW     �
  CREATE VIEW agdc.dv_item_v2_dataset AS
 SELECT dataset.id,
    dataset.added AS indexed_time,
    dataset.added_by AS indexed_by,
    dataset_type.name AS product,
    dataset.dataset_type_ref AS dataset_type_id,
    metadata_type.name AS metadata_type,
    dataset.metadata_type_ref AS metadata_type_id,
    dataset.metadata AS metadata_doc,
    agdc.common_timestamp((dataset.metadata #>> '{creation_dt}'::text[])) AS creation_time,
    (dataset.metadata #>> '{format,name}'::text[]) AS format,
    (dataset.metadata #>> '{ga_label}'::text[]) AS label,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text) AS lat,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text) AS lon,
    tstzrange(LEAST(agdc.common_timestamp((dataset.metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((dataset.metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), '[]'::text) AS "time",
    (dataset.metadata #>> '{platform,code}'::text[]) AS platform,
    (dataset.metadata #>> '{instrument,name}'::text[]) AS instrument,
    (dataset.metadata #>> '{product_type}'::text[]) AS product_type
   FROM ((agdc.dataset
     JOIN agdc.dataset_type ON ((dataset_type.id = dataset.dataset_type_ref)))
     JOIN agdc.metadata_type ON ((metadata_type.id = dataset_type.metadata_type_ref)))
  WHERE ((dataset.archived IS NULL) AND (dataset.dataset_type_ref = 32));
 #   DROP VIEW agdc.dv_item_v2_dataset;
       agdc       africa    false    201    201    201    201    280    198    198    200    200    200    201    201    201    673    8    673            �            1259    2903886    dv_landsat_barest_earth_dataset    VIEW     �
  CREATE VIEW agdc.dv_landsat_barest_earth_dataset AS
 SELECT dataset.id,
    dataset.added AS indexed_time,
    dataset.added_by AS indexed_by,
    dataset_type.name AS product,
    dataset.dataset_type_ref AS dataset_type_id,
    metadata_type.name AS metadata_type,
    dataset.metadata_type_ref AS metadata_type_id,
    dataset.metadata AS metadata_doc,
    agdc.common_timestamp((dataset.metadata #>> '{creation_dt}'::text[])) AS creation_time,
    (dataset.metadata #>> '{format,name}'::text[]) AS format,
    (dataset.metadata #>> '{ga_label}'::text[]) AS label,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text) AS lat,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text) AS lon,
    tstzrange(LEAST(agdc.common_timestamp((dataset.metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((dataset.metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), '[]'::text) AS "time",
    (dataset.metadata #>> '{platform,code}'::text[]) AS platform,
    (dataset.metadata #>> '{instrument,name}'::text[]) AS instrument,
    (dataset.metadata #>> '{product_type}'::text[]) AS product_type
   FROM ((agdc.dataset
     JOIN agdc.dataset_type ON ((dataset_type.id = dataset.dataset_type_ref)))
     JOIN agdc.metadata_type ON ((metadata_type.id = dataset_type.metadata_type_ref)))
  WHERE ((dataset.archived IS NULL) AND (dataset.dataset_type_ref = 34));
 0   DROP VIEW agdc.dv_landsat_barest_earth_dataset;
       agdc       africa    false    201    201    201    201    280    198    201    201    201    198    200    200    200    673    8    673            �            1259    2903852    dv_low_tide_comp_20p_dataset    VIEW     �
  CREATE VIEW agdc.dv_low_tide_comp_20p_dataset AS
 SELECT dataset.id,
    dataset.added AS indexed_time,
    dataset.added_by AS indexed_by,
    dataset_type.name AS product,
    dataset.dataset_type_ref AS dataset_type_id,
    metadata_type.name AS metadata_type,
    dataset.metadata_type_ref AS metadata_type_id,
    dataset.metadata AS metadata_doc,
    agdc.common_timestamp((dataset.metadata #>> '{creation_dt}'::text[])) AS creation_time,
    (dataset.metadata #>> '{format,name}'::text[]) AS format,
    (dataset.metadata #>> '{ga_label}'::text[]) AS label,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text) AS lat,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text) AS lon,
    tstzrange(LEAST(agdc.common_timestamp((dataset.metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((dataset.metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), '[]'::text) AS "time",
    (dataset.metadata #>> '{platform,code}'::text[]) AS platform,
    (dataset.metadata #>> '{instrument,name}'::text[]) AS instrument,
    (dataset.metadata #>> '{product_type}'::text[]) AS product_type
   FROM ((agdc.dataset
     JOIN agdc.dataset_type ON ((dataset_type.id = dataset.dataset_type_ref)))
     JOIN agdc.metadata_type ON ((metadata_type.id = dataset_type.metadata_type_ref)))
  WHERE ((dataset.archived IS NULL) AND (dataset.dataset_type_ref = 30));
 -   DROP VIEW agdc.dv_low_tide_comp_20p_dataset;
       agdc       africa    false    201    198    198    200    200    200    201    280    201    201    201    201    201    673    673    8            �            1259    2903893    dv_ls5_fc_albers_dataset    VIEW     �
  CREATE VIEW agdc.dv_ls5_fc_albers_dataset AS
 SELECT dataset.id,
    dataset.added AS indexed_time,
    dataset.added_by AS indexed_by,
    dataset_type.name AS product,
    dataset.dataset_type_ref AS dataset_type_id,
    metadata_type.name AS metadata_type,
    dataset.metadata_type_ref AS metadata_type_id,
    dataset.metadata AS metadata_doc,
    agdc.common_timestamp((dataset.metadata #>> '{creation_dt}'::text[])) AS creation_time,
    (dataset.metadata #>> '{format,name}'::text[]) AS format,
    (dataset.metadata #>> '{ga_label}'::text[]) AS label,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text) AS lat,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text) AS lon,
    tstzrange(LEAST(agdc.common_timestamp((dataset.metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((dataset.metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), '[]'::text) AS "time",
    (dataset.metadata #>> '{platform,code}'::text[]) AS platform,
    (dataset.metadata #>> '{instrument,name}'::text[]) AS instrument,
    (dataset.metadata #>> '{product_type}'::text[]) AS product_type
   FROM ((agdc.dataset
     JOIN agdc.dataset_type ON ((dataset_type.id = dataset.dataset_type_ref)))
     JOIN agdc.metadata_type ON ((metadata_type.id = dataset_type.metadata_type_ref)))
  WHERE ((dataset.archived IS NULL) AND (dataset.dataset_type_ref = 35));
 )   DROP VIEW agdc.dv_ls5_fc_albers_dataset;
       agdc       africa    false    201    201    201    201    200    200    200    198    198    280    201    201    201    673    8    673            �            1259    2903603    dv_ls5_level1_usgs_dataset    VIEW     �
  CREATE VIEW agdc.dv_ls5_level1_usgs_dataset AS
 SELECT dataset.id,
    dataset.added AS indexed_time,
    dataset.added_by AS indexed_by,
    dataset_type.name AS product,
    dataset.dataset_type_ref AS dataset_type_id,
    metadata_type.name AS metadata_type,
    dataset.metadata_type_ref AS metadata_type_id,
    dataset.metadata AS metadata_doc,
    agdc.common_timestamp((dataset.metadata #>> '{creation_dt}'::text[])) AS creation_time,
    (dataset.metadata #>> '{format,name}'::text[]) AS format,
    (dataset.metadata #>> '{ga_label}'::text[]) AS label,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text) AS lat,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text) AS lon,
    tstzrange(LEAST(agdc.common_timestamp((dataset.metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((dataset.metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), '[]'::text) AS "time",
    (dataset.metadata #>> '{platform,code}'::text[]) AS platform,
    (dataset.metadata #>> '{instrument,name}'::text[]) AS instrument,
    (dataset.metadata #>> '{product_type}'::text[]) AS product_type
   FROM ((agdc.dataset
     JOIN agdc.dataset_type ON ((dataset_type.id = dataset.dataset_type_ref)))
     JOIN agdc.metadata_type ON ((metadata_type.id = dataset_type.metadata_type_ref)))
  WHERE ((dataset.archived IS NULL) AND (dataset.dataset_type_ref = 1));
 +   DROP VIEW agdc.dv_ls5_level1_usgs_dataset;
       agdc       africa    false    201    201    201    201    201    201    201    200    200    200    198    198    280    673    673    8            �            1259    2903914 %   dv_ls5_nbart_geomedian_annual_dataset    VIEW     �
  CREATE VIEW agdc.dv_ls5_nbart_geomedian_annual_dataset AS
 SELECT dataset.id,
    dataset.added AS indexed_time,
    dataset.added_by AS indexed_by,
    dataset_type.name AS product,
    dataset.dataset_type_ref AS dataset_type_id,
    metadata_type.name AS metadata_type,
    dataset.metadata_type_ref AS metadata_type_id,
    dataset.metadata AS metadata_doc,
    agdc.common_timestamp((dataset.metadata #>> '{creation_dt}'::text[])) AS creation_time,
    (dataset.metadata #>> '{format,name}'::text[]) AS format,
    (dataset.metadata #>> '{ga_label}'::text[]) AS label,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text) AS lat,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text) AS lon,
    tstzrange(LEAST(agdc.common_timestamp((dataset.metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((dataset.metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), '[]'::text) AS "time",
    (dataset.metadata #>> '{platform,code}'::text[]) AS platform,
    (dataset.metadata #>> '{instrument,name}'::text[]) AS instrument,
    (dataset.metadata #>> '{product_type}'::text[]) AS product_type
   FROM ((agdc.dataset
     JOIN agdc.dataset_type ON ((dataset_type.id = dataset.dataset_type_ref)))
     JOIN agdc.metadata_type ON ((metadata_type.id = dataset_type.metadata_type_ref)))
  WHERE ((dataset.archived IS NULL) AND (dataset.dataset_type_ref = 38));
 6   DROP VIEW agdc.dv_ls5_nbart_geomedian_annual_dataset;
       agdc       africa    false    198    280    198    200    201    201    201    201    201    201    201    200    200    673    673    8            �            1259    2903935     dv_ls5_nbart_tmad_annual_dataset    VIEW     �
  CREATE VIEW agdc.dv_ls5_nbart_tmad_annual_dataset AS
 SELECT dataset.id,
    dataset.added AS indexed_time,
    dataset.added_by AS indexed_by,
    dataset_type.name AS product,
    dataset.dataset_type_ref AS dataset_type_id,
    metadata_type.name AS metadata_type,
    dataset.metadata_type_ref AS metadata_type_id,
    dataset.metadata AS metadata_doc,
    agdc.common_timestamp((dataset.metadata #>> '{creation_dt}'::text[])) AS creation_time,
    (dataset.metadata #>> '{format,name}'::text[]) AS format,
    (dataset.metadata #>> '{ga_label}'::text[]) AS label,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text) AS lat,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text) AS lon,
    tstzrange(LEAST(agdc.common_timestamp((dataset.metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((dataset.metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), '[]'::text) AS "time",
    (dataset.metadata #>> '{platform,code}'::text[]) AS platform,
    (dataset.metadata #>> '{instrument,name}'::text[]) AS instrument,
    (dataset.metadata #>> '{product_type}'::text[]) AS product_type
   FROM ((agdc.dataset
     JOIN agdc.dataset_type ON ((dataset_type.id = dataset.dataset_type_ref)))
     JOIN agdc.metadata_type ON ((metadata_type.id = dataset_type.metadata_type_ref)))
  WHERE ((dataset.archived IS NULL) AND (dataset.dataset_type_ref = 41));
 1   DROP VIEW agdc.dv_ls5_nbart_tmad_annual_dataset;
       agdc       africa    false    200    200    200    198    198    280    201    201    201    201    201    201    201    673    673    8            �            1259    2903943    dv_ls5_usgs_l2c1_dataset    VIEW     �
  CREATE VIEW agdc.dv_ls5_usgs_l2c1_dataset AS
 SELECT dataset.id,
    dataset.added AS indexed_time,
    dataset.added_by AS indexed_by,
    dataset_type.name AS product,
    dataset.dataset_type_ref AS dataset_type_id,
    metadata_type.name AS metadata_type,
    dataset.metadata_type_ref AS metadata_type_id,
    dataset.metadata AS metadata_doc,
    agdc.common_timestamp((dataset.metadata #>> '{creation_dt}'::text[])) AS creation_time,
    (dataset.metadata #>> '{format,name}'::text[]) AS format,
    (dataset.metadata #>> '{ga_label}'::text[]) AS label,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text) AS lat,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text) AS lon,
    tstzrange(LEAST(agdc.common_timestamp((dataset.metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((dataset.metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), '[]'::text) AS "time",
    (dataset.metadata #>> '{platform,code}'::text[]) AS platform,
    (dataset.metadata #>> '{instrument,name}'::text[]) AS instrument,
    (dataset.metadata #>> '{product_type}'::text[]) AS product_type
   FROM ((agdc.dataset
     JOIN agdc.dataset_type ON ((dataset_type.id = dataset.dataset_type_ref)))
     JOIN agdc.metadata_type ON ((metadata_type.id = dataset_type.metadata_type_ref)))
  WHERE ((dataset.archived IS NULL) AND (dataset.dataset_type_ref = 42));
 )   DROP VIEW agdc.dv_ls5_usgs_l2c1_dataset;
       agdc       africa    false    201    201    201    201    201    201    201    200    200    200    198    198    280    673    673    8            �            1259    2903950    dv_ls7_fc_albers_dataset    VIEW     �
  CREATE VIEW agdc.dv_ls7_fc_albers_dataset AS
 SELECT dataset.id,
    dataset.added AS indexed_time,
    dataset.added_by AS indexed_by,
    dataset_type.name AS product,
    dataset.dataset_type_ref AS dataset_type_id,
    metadata_type.name AS metadata_type,
    dataset.metadata_type_ref AS metadata_type_id,
    dataset.metadata AS metadata_doc,
    agdc.common_timestamp((dataset.metadata #>> '{creation_dt}'::text[])) AS creation_time,
    (dataset.metadata #>> '{format,name}'::text[]) AS format,
    (dataset.metadata #>> '{ga_label}'::text[]) AS label,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text) AS lat,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text) AS lon,
    tstzrange(LEAST(agdc.common_timestamp((dataset.metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((dataset.metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), '[]'::text) AS "time",
    (dataset.metadata #>> '{platform,code}'::text[]) AS platform,
    (dataset.metadata #>> '{instrument,name}'::text[]) AS instrument,
    (dataset.metadata #>> '{product_type}'::text[]) AS product_type
   FROM ((agdc.dataset
     JOIN agdc.dataset_type ON ((dataset_type.id = dataset.dataset_type_ref)))
     JOIN agdc.metadata_type ON ((metadata_type.id = dataset_type.metadata_type_ref)))
  WHERE ((dataset.archived IS NULL) AND (dataset.dataset_type_ref = 43));
 )   DROP VIEW agdc.dv_ls7_fc_albers_dataset;
       agdc       africa    false    200    201    201    201    201    201    201    201    200    200    198    198    280    673    673    8            �            1259    2903610    dv_ls7_level1_usgs_dataset    VIEW     �
  CREATE VIEW agdc.dv_ls7_level1_usgs_dataset AS
 SELECT dataset.id,
    dataset.added AS indexed_time,
    dataset.added_by AS indexed_by,
    dataset_type.name AS product,
    dataset.dataset_type_ref AS dataset_type_id,
    metadata_type.name AS metadata_type,
    dataset.metadata_type_ref AS metadata_type_id,
    dataset.metadata AS metadata_doc,
    agdc.common_timestamp((dataset.metadata #>> '{creation_dt}'::text[])) AS creation_time,
    (dataset.metadata #>> '{format,name}'::text[]) AS format,
    (dataset.metadata #>> '{ga_label}'::text[]) AS label,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text) AS lat,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text) AS lon,
    tstzrange(LEAST(agdc.common_timestamp((dataset.metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((dataset.metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), '[]'::text) AS "time",
    (dataset.metadata #>> '{platform,code}'::text[]) AS platform,
    (dataset.metadata #>> '{instrument,name}'::text[]) AS instrument,
    (dataset.metadata #>> '{product_type}'::text[]) AS product_type
   FROM ((agdc.dataset
     JOIN agdc.dataset_type ON ((dataset_type.id = dataset.dataset_type_ref)))
     JOIN agdc.metadata_type ON ((metadata_type.id = dataset_type.metadata_type_ref)))
  WHERE ((dataset.archived IS NULL) AND (dataset.dataset_type_ref = 2));
 +   DROP VIEW agdc.dv_ls7_level1_usgs_dataset;
       agdc       africa    false    280    200    200    201    201    201    201    201    201    201    200    198    198    8    673    673            �            1259    2903907 %   dv_ls7_nbart_geomedian_annual_dataset    VIEW     �
  CREATE VIEW agdc.dv_ls7_nbart_geomedian_annual_dataset AS
 SELECT dataset.id,
    dataset.added AS indexed_time,
    dataset.added_by AS indexed_by,
    dataset_type.name AS product,
    dataset.dataset_type_ref AS dataset_type_id,
    metadata_type.name AS metadata_type,
    dataset.metadata_type_ref AS metadata_type_id,
    dataset.metadata AS metadata_doc,
    agdc.common_timestamp((dataset.metadata #>> '{creation_dt}'::text[])) AS creation_time,
    (dataset.metadata #>> '{format,name}'::text[]) AS format,
    (dataset.metadata #>> '{ga_label}'::text[]) AS label,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text) AS lat,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text) AS lon,
    tstzrange(LEAST(agdc.common_timestamp((dataset.metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((dataset.metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), '[]'::text) AS "time",
    (dataset.metadata #>> '{platform,code}'::text[]) AS platform,
    (dataset.metadata #>> '{instrument,name}'::text[]) AS instrument,
    (dataset.metadata #>> '{product_type}'::text[]) AS product_type
   FROM ((agdc.dataset
     JOIN agdc.dataset_type ON ((dataset_type.id = dataset.dataset_type_ref)))
     JOIN agdc.metadata_type ON ((metadata_type.id = dataset_type.metadata_type_ref)))
  WHERE ((dataset.archived IS NULL) AND (dataset.dataset_type_ref = 37));
 6   DROP VIEW agdc.dv_ls7_nbart_geomedian_annual_dataset;
       agdc       africa    false    200    200    201    201    201    201    201    280    201    201    198    198    200    673    673    8            �            1259    2903928     dv_ls7_nbart_tmad_annual_dataset    VIEW     �
  CREATE VIEW agdc.dv_ls7_nbart_tmad_annual_dataset AS
 SELECT dataset.id,
    dataset.added AS indexed_time,
    dataset.added_by AS indexed_by,
    dataset_type.name AS product,
    dataset.dataset_type_ref AS dataset_type_id,
    metadata_type.name AS metadata_type,
    dataset.metadata_type_ref AS metadata_type_id,
    dataset.metadata AS metadata_doc,
    agdc.common_timestamp((dataset.metadata #>> '{creation_dt}'::text[])) AS creation_time,
    (dataset.metadata #>> '{format,name}'::text[]) AS format,
    (dataset.metadata #>> '{ga_label}'::text[]) AS label,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text) AS lat,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text) AS lon,
    tstzrange(LEAST(agdc.common_timestamp((dataset.metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((dataset.metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), '[]'::text) AS "time",
    (dataset.metadata #>> '{platform,code}'::text[]) AS platform,
    (dataset.metadata #>> '{instrument,name}'::text[]) AS instrument,
    (dataset.metadata #>> '{product_type}'::text[]) AS product_type
   FROM ((agdc.dataset
     JOIN agdc.dataset_type ON ((dataset_type.id = dataset.dataset_type_ref)))
     JOIN agdc.metadata_type ON ((metadata_type.id = dataset_type.metadata_type_ref)))
  WHERE ((dataset.archived IS NULL) AND (dataset.dataset_type_ref = 40));
 1   DROP VIEW agdc.dv_ls7_nbart_tmad_annual_dataset;
       agdc       africa    false    201    280    198    198    200    200    200    201    201    201    201    201    201    673    673    8            �            1259    2903958    dv_ls7_usgs_l2c1_dataset    VIEW     �
  CREATE VIEW agdc.dv_ls7_usgs_l2c1_dataset AS
 SELECT dataset.id,
    dataset.added AS indexed_time,
    dataset.added_by AS indexed_by,
    dataset_type.name AS product,
    dataset.dataset_type_ref AS dataset_type_id,
    metadata_type.name AS metadata_type,
    dataset.metadata_type_ref AS metadata_type_id,
    dataset.metadata AS metadata_doc,
    agdc.common_timestamp((dataset.metadata #>> '{creation_dt}'::text[])) AS creation_time,
    (dataset.metadata #>> '{format,name}'::text[]) AS format,
    (dataset.metadata #>> '{ga_label}'::text[]) AS label,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text) AS lat,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text) AS lon,
    tstzrange(LEAST(agdc.common_timestamp((dataset.metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((dataset.metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), '[]'::text) AS "time",
    (dataset.metadata #>> '{platform,code}'::text[]) AS platform,
    (dataset.metadata #>> '{instrument,name}'::text[]) AS instrument,
    (dataset.metadata #>> '{product_type}'::text[]) AS product_type
   FROM ((agdc.dataset
     JOIN agdc.dataset_type ON ((dataset_type.id = dataset.dataset_type_ref)))
     JOIN agdc.metadata_type ON ((metadata_type.id = dataset_type.metadata_type_ref)))
  WHERE ((dataset.archived IS NULL) AND (dataset.dataset_type_ref = 44));
 )   DROP VIEW agdc.dv_ls7_usgs_l2c1_dataset;
       agdc       africa    false    201    201    201    201    201    201    201    280    198    198    200    200    200    673    673    8            �            1259    2903965 "   dv_ls8_barest_earth_albers_dataset    VIEW     �
  CREATE VIEW agdc.dv_ls8_barest_earth_albers_dataset AS
 SELECT dataset.id,
    dataset.added AS indexed_time,
    dataset.added_by AS indexed_by,
    dataset_type.name AS product,
    dataset.dataset_type_ref AS dataset_type_id,
    metadata_type.name AS metadata_type,
    dataset.metadata_type_ref AS metadata_type_id,
    dataset.metadata AS metadata_doc,
    agdc.common_timestamp((dataset.metadata #>> '{creation_dt}'::text[])) AS creation_time,
    (dataset.metadata #>> '{format,name}'::text[]) AS format,
    (dataset.metadata #>> '{ga_label}'::text[]) AS label,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text) AS lat,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text) AS lon,
    tstzrange(LEAST(agdc.common_timestamp((dataset.metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((dataset.metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), '[]'::text) AS "time",
    (dataset.metadata #>> '{platform,code}'::text[]) AS platform,
    (dataset.metadata #>> '{instrument,name}'::text[]) AS instrument,
    (dataset.metadata #>> '{product_type}'::text[]) AS product_type
   FROM ((agdc.dataset
     JOIN agdc.dataset_type ON ((dataset_type.id = dataset.dataset_type_ref)))
     JOIN agdc.metadata_type ON ((metadata_type.id = dataset_type.metadata_type_ref)))
  WHERE ((dataset.archived IS NULL) AND (dataset.dataset_type_ref = 45));
 3   DROP VIEW agdc.dv_ls8_barest_earth_albers_dataset;
       agdc       africa    false    201    200    200    200    198    198    280    201    201    201    201    201    201    8    673    673            �            1259    2903972    dv_ls8_fc_albers_dataset    VIEW     �
  CREATE VIEW agdc.dv_ls8_fc_albers_dataset AS
 SELECT dataset.id,
    dataset.added AS indexed_time,
    dataset.added_by AS indexed_by,
    dataset_type.name AS product,
    dataset.dataset_type_ref AS dataset_type_id,
    metadata_type.name AS metadata_type,
    dataset.metadata_type_ref AS metadata_type_id,
    dataset.metadata AS metadata_doc,
    agdc.common_timestamp((dataset.metadata #>> '{creation_dt}'::text[])) AS creation_time,
    (dataset.metadata #>> '{format,name}'::text[]) AS format,
    (dataset.metadata #>> '{ga_label}'::text[]) AS label,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text) AS lat,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text) AS lon,
    tstzrange(LEAST(agdc.common_timestamp((dataset.metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((dataset.metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), '[]'::text) AS "time",
    (dataset.metadata #>> '{platform,code}'::text[]) AS platform,
    (dataset.metadata #>> '{instrument,name}'::text[]) AS instrument,
    (dataset.metadata #>> '{product_type}'::text[]) AS product_type
   FROM ((agdc.dataset
     JOIN agdc.dataset_type ON ((dataset_type.id = dataset.dataset_type_ref)))
     JOIN agdc.metadata_type ON ((metadata_type.id = dataset_type.metadata_type_ref)))
  WHERE ((dataset.archived IS NULL) AND (dataset.dataset_type_ref = 46));
 )   DROP VIEW agdc.dv_ls8_fc_albers_dataset;
       agdc       africa    false    200    280    198    198    200    200    201    201    201    201    201    201    201    673    673    8            �            1259    2903981    dv_ls8_level1_usgs_dataset    VIEW     �
  CREATE VIEW agdc.dv_ls8_level1_usgs_dataset AS
 SELECT dataset.id,
    dataset.added AS indexed_time,
    dataset.added_by AS indexed_by,
    dataset_type.name AS product,
    dataset.dataset_type_ref AS dataset_type_id,
    metadata_type.name AS metadata_type,
    dataset.metadata_type_ref AS metadata_type_id,
    dataset.metadata AS metadata_doc,
    agdc.common_timestamp((dataset.metadata #>> '{creation_dt}'::text[])) AS creation_time,
    (dataset.metadata #>> '{format,name}'::text[]) AS format,
    (dataset.metadata #>> '{ga_label}'::text[]) AS label,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text) AS lat,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text) AS lon,
    tstzrange(LEAST(agdc.common_timestamp((dataset.metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((dataset.metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), '[]'::text) AS "time",
    (dataset.metadata #>> '{platform,code}'::text[]) AS platform,
    (dataset.metadata #>> '{instrument,name}'::text[]) AS instrument,
    (dataset.metadata #>> '{product_type}'::text[]) AS product_type
   FROM ((agdc.dataset
     JOIN agdc.dataset_type ON ((dataset_type.id = dataset.dataset_type_ref)))
     JOIN agdc.metadata_type ON ((metadata_type.id = dataset_type.metadata_type_ref)))
  WHERE ((dataset.archived IS NULL) AND (dataset.dataset_type_ref = 47));
 +   DROP VIEW agdc.dv_ls8_level1_usgs_dataset;
       agdc       africa    false    280    198    198    200    200    200    201    201    201    201    201    201    201    8    673    673            �            1259    2903900 %   dv_ls8_nbart_geomedian_annual_dataset    VIEW     �
  CREATE VIEW agdc.dv_ls8_nbart_geomedian_annual_dataset AS
 SELECT dataset.id,
    dataset.added AS indexed_time,
    dataset.added_by AS indexed_by,
    dataset_type.name AS product,
    dataset.dataset_type_ref AS dataset_type_id,
    metadata_type.name AS metadata_type,
    dataset.metadata_type_ref AS metadata_type_id,
    dataset.metadata AS metadata_doc,
    agdc.common_timestamp((dataset.metadata #>> '{creation_dt}'::text[])) AS creation_time,
    (dataset.metadata #>> '{format,name}'::text[]) AS format,
    (dataset.metadata #>> '{ga_label}'::text[]) AS label,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text) AS lat,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text) AS lon,
    tstzrange(LEAST(agdc.common_timestamp((dataset.metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((dataset.metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), '[]'::text) AS "time",
    (dataset.metadata #>> '{platform,code}'::text[]) AS platform,
    (dataset.metadata #>> '{instrument,name}'::text[]) AS instrument,
    (dataset.metadata #>> '{product_type}'::text[]) AS product_type
   FROM ((agdc.dataset
     JOIN agdc.dataset_type ON ((dataset_type.id = dataset.dataset_type_ref)))
     JOIN agdc.metadata_type ON ((metadata_type.id = dataset_type.metadata_type_ref)))
  WHERE ((dataset.archived IS NULL) AND (dataset.dataset_type_ref = 36));
 6   DROP VIEW agdc.dv_ls8_nbart_geomedian_annual_dataset;
       agdc       africa    false    201    198    198    200    200    200    201    201    201    201    201    280    201    8    673    673            �            1259    2903921     dv_ls8_nbart_tmad_annual_dataset    VIEW     �
  CREATE VIEW agdc.dv_ls8_nbart_tmad_annual_dataset AS
 SELECT dataset.id,
    dataset.added AS indexed_time,
    dataset.added_by AS indexed_by,
    dataset_type.name AS product,
    dataset.dataset_type_ref AS dataset_type_id,
    metadata_type.name AS metadata_type,
    dataset.metadata_type_ref AS metadata_type_id,
    dataset.metadata AS metadata_doc,
    agdc.common_timestamp((dataset.metadata #>> '{creation_dt}'::text[])) AS creation_time,
    (dataset.metadata #>> '{format,name}'::text[]) AS format,
    (dataset.metadata #>> '{ga_label}'::text[]) AS label,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text) AS lat,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text) AS lon,
    tstzrange(LEAST(agdc.common_timestamp((dataset.metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((dataset.metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), '[]'::text) AS "time",
    (dataset.metadata #>> '{platform,code}'::text[]) AS platform,
    (dataset.metadata #>> '{instrument,name}'::text[]) AS instrument,
    (dataset.metadata #>> '{product_type}'::text[]) AS product_type
   FROM ((agdc.dataset
     JOIN agdc.dataset_type ON ((dataset_type.id = dataset.dataset_type_ref)))
     JOIN agdc.metadata_type ON ((metadata_type.id = dataset_type.metadata_type_ref)))
  WHERE ((dataset.archived IS NULL) AND (dataset.dataset_type_ref = 39));
 1   DROP VIEW agdc.dv_ls8_nbart_tmad_annual_dataset;
       agdc       africa    false    201    201    201    201    201    201    201    280    200    200    200    198    198    673    673    8            �            1259    2903989    dv_ls8_usgs_l2c1_dataset    VIEW     �
  CREATE VIEW agdc.dv_ls8_usgs_l2c1_dataset AS
 SELECT dataset.id,
    dataset.added AS indexed_time,
    dataset.added_by AS indexed_by,
    dataset_type.name AS product,
    dataset.dataset_type_ref AS dataset_type_id,
    metadata_type.name AS metadata_type,
    dataset.metadata_type_ref AS metadata_type_id,
    dataset.metadata AS metadata_doc,
    agdc.common_timestamp((dataset.metadata #>> '{creation_dt}'::text[])) AS creation_time,
    (dataset.metadata #>> '{format,name}'::text[]) AS format,
    (dataset.metadata #>> '{ga_label}'::text[]) AS label,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text) AS lat,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text) AS lon,
    tstzrange(LEAST(agdc.common_timestamp((dataset.metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((dataset.metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), '[]'::text) AS "time",
    (dataset.metadata #>> '{platform,code}'::text[]) AS platform,
    (dataset.metadata #>> '{instrument,name}'::text[]) AS instrument,
    (dataset.metadata #>> '{product_type}'::text[]) AS product_type
   FROM ((agdc.dataset
     JOIN agdc.dataset_type ON ((dataset_type.id = dataset.dataset_type_ref)))
     JOIN agdc.metadata_type ON ((metadata_type.id = dataset_type.metadata_type_ref)))
  WHERE ((dataset.archived IS NULL) AND (dataset.dataset_type_ref = 48));
 )   DROP VIEW agdc.dv_ls8_usgs_l2c1_dataset;
       agdc       africa    false    200    280    198    198    200    200    201    201    201    201    201    201    201    673    8    673                        1259    2903996    dv_mangrove_cover_dataset    VIEW     �
  CREATE VIEW agdc.dv_mangrove_cover_dataset AS
 SELECT dataset.id,
    dataset.added AS indexed_time,
    dataset.added_by AS indexed_by,
    dataset_type.name AS product,
    dataset.dataset_type_ref AS dataset_type_id,
    metadata_type.name AS metadata_type,
    dataset.metadata_type_ref AS metadata_type_id,
    dataset.metadata AS metadata_doc,
    agdc.common_timestamp((dataset.metadata #>> '{creation_dt}'::text[])) AS creation_time,
    (dataset.metadata #>> '{format,name}'::text[]) AS format,
    (dataset.metadata #>> '{ga_label}'::text[]) AS label,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text) AS lat,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text) AS lon,
    tstzrange(LEAST(agdc.common_timestamp((dataset.metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((dataset.metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), '[]'::text) AS "time",
    (dataset.metadata #>> '{platform,code}'::text[]) AS platform,
    (dataset.metadata #>> '{instrument,name}'::text[]) AS instrument,
    (dataset.metadata #>> '{product_type}'::text[]) AS product_type
   FROM ((agdc.dataset
     JOIN agdc.dataset_type ON ((dataset_type.id = dataset.dataset_type_ref)))
     JOIN agdc.metadata_type ON ((metadata_type.id = dataset_type.metadata_type_ref)))
  WHERE ((dataset.archived IS NULL) AND (dataset.dataset_type_ref = 49));
 *   DROP VIEW agdc.dv_mangrove_cover_dataset;
       agdc       africa    false    280    198    198    200    200    200    201    201    201    201    201    201    201    8    673    673                       1259    2904005 +   dv_multi_scale_topographic_position_dataset    VIEW     �
  CREATE VIEW agdc.dv_multi_scale_topographic_position_dataset AS
 SELECT dataset.id,
    dataset.added AS indexed_time,
    dataset.added_by AS indexed_by,
    dataset_type.name AS product,
    dataset.dataset_type_ref AS dataset_type_id,
    metadata_type.name AS metadata_type,
    dataset.metadata_type_ref AS metadata_type_id,
    dataset.metadata AS metadata_doc,
    agdc.common_timestamp((dataset.metadata #>> '{creation_dt}'::text[])) AS creation_time,
    (dataset.metadata #>> '{format,name}'::text[]) AS format,
    (dataset.metadata #>> '{ga_label}'::text[]) AS label,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text) AS lat,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text) AS lon,
    tstzrange(LEAST(agdc.common_timestamp((dataset.metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((dataset.metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), '[]'::text) AS "time",
    (dataset.metadata #>> '{platform,code}'::text[]) AS platform,
    (dataset.metadata #>> '{instrument,name}'::text[]) AS instrument,
    (dataset.metadata #>> '{product_type}'::text[]) AS product_type
   FROM ((agdc.dataset
     JOIN agdc.dataset_type ON ((dataset_type.id = dataset.dataset_type_ref)))
     JOIN agdc.metadata_type ON ((metadata_type.id = dataset_type.metadata_type_ref)))
  WHERE ((dataset.archived IS NULL) AND (dataset.dataset_type_ref = 50));
 <   DROP VIEW agdc.dv_multi_scale_topographic_position_dataset;
       agdc       africa    false    201    280    198    198    200    200    200    201    201    201    201    201    201    673    8    673                       1259    2904014    dv_nidem_dataset    VIEW     �
  CREATE VIEW agdc.dv_nidem_dataset AS
 SELECT dataset.id,
    dataset.added AS indexed_time,
    dataset.added_by AS indexed_by,
    dataset_type.name AS product,
    dataset.dataset_type_ref AS dataset_type_id,
    metadata_type.name AS metadata_type,
    dataset.metadata_type_ref AS metadata_type_id,
    dataset.metadata AS metadata_doc,
    agdc.common_timestamp((dataset.metadata #>> '{creation_dt}'::text[])) AS creation_time,
    (dataset.metadata #>> '{format,name}'::text[]) AS format,
    (dataset.metadata #>> '{ga_label}'::text[]) AS label,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text) AS lat,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text) AS lon,
    tstzrange(LEAST(agdc.common_timestamp((dataset.metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((dataset.metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), '[]'::text) AS "time",
    (dataset.metadata #>> '{platform,code}'::text[]) AS platform,
    (dataset.metadata #>> '{instrument,name}'::text[]) AS instrument,
    (dataset.metadata #>> '{product_type}'::text[]) AS product_type
   FROM ((agdc.dataset
     JOIN agdc.dataset_type ON ((dataset_type.id = dataset.dataset_type_ref)))
     JOIN agdc.metadata_type ON ((metadata_type.id = dataset_type.metadata_type_ref)))
  WHERE ((dataset.archived IS NULL) AND (dataset.dataset_type_ref = 51));
 !   DROP VIEW agdc.dv_nidem_dataset;
       agdc       africa    false    201    201    201    201    201    201    201    200    200    200    198    198    280    8    673    673                       1259    2904164    dv_s2_tsmask_dataset    VIEW     w  CREATE VIEW agdc.dv_s2_tsmask_dataset AS
 SELECT dataset.id,
    dataset.added AS indexed_time,
    dataset.added_by AS indexed_by,
    dataset_type.name AS product,
    dataset.dataset_type_ref AS dataset_type_id,
    metadata_type.name AS metadata_type,
    dataset.metadata_type_ref AS metadata_type_id,
    dataset.metadata AS metadata_doc,
    agdc.common_timestamp((dataset.metadata #>> '{system_information,time_processed}'::text[])) AS creation_time,
    (dataset.metadata #>> '{format,name}'::text[]) AS format,
    (dataset.metadata #>> '{ga_label}'::text[]) AS label,
    ((dataset.metadata #>> '{gqa,cep90}'::text[]))::double precision AS gqa,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text) AS lat,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text) AS lon,
    tstzrange(agdc.common_timestamp((dataset.metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,to_dt}'::text[])), '[]'::text) AS "time",
    (dataset.metadata #>> '{platform,code}'::text[]) AS platform,
    ((dataset.metadata #>> '{gqa,residual,cep90}'::text[]))::double precision AS gqa_cep90,
    ((dataset.metadata #>> '{gqa,residual,abs,xy}'::text[]))::double precision AS gqa_abs_xy,
    (dataset.metadata #>> '{instrument,name}'::text[]) AS instrument,
    ((dataset.metadata #>> '{gqa,residual,mean,xy}'::text[]))::double precision AS gqa_mean_xy,
    (dataset.metadata #>> '{provider,reference_code}'::text[]) AS region_code,
    (dataset.metadata #>> '{product_type}'::text[]) AS product_type,
    ((dataset.metadata #>> '{gqa,residual,stddev,xy}'::text[]))::double precision AS gqa_stddev_xy,
    (dataset.metadata #>> '{gqa,ref_source}'::text[]) AS gqa_ref_source,
    (dataset.metadata #>> '{gqa,error_message}'::text[]) AS gqa_error_message,
    ((dataset.metadata #>> '{gqa,final_qa_count}'::text[]))::integer AS gqa_final_qa_count,
    ((dataset.metadata #>> '{gqa,residual,iterative_mean,xy}'::text[]))::double precision AS gqa_iterative_mean_xy,
    ((dataset.metadata #>> '{gqa,residual,iterative_stddev,xy}'::text[]))::double precision AS gqa_iterative_stddev_xy,
    ((dataset.metadata #>> '{gqa,residual,abs_iterative_mean,xy}'::text[]))::double precision AS gqa_abs_iterative_mean_xy
   FROM ((agdc.dataset
     JOIN agdc.dataset_type ON ((dataset_type.id = dataset.dataset_type_ref)))
     JOIN agdc.metadata_type ON ((metadata_type.id = dataset_type.metadata_type_ref)))
  WHERE ((dataset.archived IS NULL) AND (dataset.dataset_type_ref = 66));
 %   DROP VIEW agdc.dv_s2_tsmask_dataset;
       agdc       africa    false    201    198    200    200    200    198    280    201    201    201    201    201    201    8    673    673                       1259    2904148    dv_s2a_nrt_granule_dataset    VIEW     
  CREATE VIEW agdc.dv_s2a_nrt_granule_dataset AS
 SELECT dataset.id,
    dataset.added AS indexed_time,
    dataset.added_by AS indexed_by,
    dataset_type.name AS product,
    dataset.dataset_type_ref AS dataset_type_id,
    metadata_type.name AS metadata_type,
    dataset.metadata_type_ref AS metadata_type_id,
    dataset.metadata AS metadata_doc,
    agdc.common_timestamp((dataset.metadata #>> '{system_information,time_processed}'::text[])) AS creation_time,
    (dataset.metadata #>> '{format,name}'::text[]) AS format,
    (dataset.metadata #>> '{tile_id}'::text[]) AS label,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text) AS lat,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text) AS lon,
    tstzrange(agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[])), '[]'::text) AS "time",
    (dataset.metadata #>> '{platform,code}'::text[]) AS platform,
    (dataset.metadata #>> '{instrument,name}'::text[]) AS instrument,
    (dataset.metadata #>> '{product_type}'::text[]) AS product_type
   FROM ((agdc.dataset
     JOIN agdc.dataset_type ON ((dataset_type.id = dataset.dataset_type_ref)))
     JOIN agdc.metadata_type ON ((metadata_type.id = dataset_type.metadata_type_ref)))
  WHERE ((dataset.archived IS NULL) AND (dataset.dataset_type_ref = 64));
 +   DROP VIEW agdc.dv_s2a_nrt_granule_dataset;
       agdc       africa    false    201    201    201    201    200    200    201    201    280    198    198    200    201    673    8    673                       1259    2904156    dv_s2b_nrt_granule_dataset    VIEW     
  CREATE VIEW agdc.dv_s2b_nrt_granule_dataset AS
 SELECT dataset.id,
    dataset.added AS indexed_time,
    dataset.added_by AS indexed_by,
    dataset_type.name AS product,
    dataset.dataset_type_ref AS dataset_type_id,
    metadata_type.name AS metadata_type,
    dataset.metadata_type_ref AS metadata_type_id,
    dataset.metadata AS metadata_doc,
    agdc.common_timestamp((dataset.metadata #>> '{system_information,time_processed}'::text[])) AS creation_time,
    (dataset.metadata #>> '{format,name}'::text[]) AS format,
    (dataset.metadata #>> '{tile_id}'::text[]) AS label,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text) AS lat,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text) AS lon,
    tstzrange(agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[])), '[]'::text) AS "time",
    (dataset.metadata #>> '{platform,code}'::text[]) AS platform,
    (dataset.metadata #>> '{instrument,name}'::text[]) AS instrument,
    (dataset.metadata #>> '{product_type}'::text[]) AS product_type
   FROM ((agdc.dataset
     JOIN agdc.dataset_type ON ((dataset_type.id = dataset.dataset_type_ref)))
     JOIN agdc.metadata_type ON ((metadata_type.id = dataset_type.metadata_type_ref)))
  WHERE ((dataset.archived IS NULL) AND (dataset.dataset_type_ref = 65));
 +   DROP VIEW agdc.dv_s2b_nrt_granule_dataset;
       agdc       africa    false    198    280    201    201    201    201    201    201    201    200    200    200    198    673    673    8                       1259    2904022    dv_sentinel2_wofs_nrt_dataset    VIEW     �
  CREATE VIEW agdc.dv_sentinel2_wofs_nrt_dataset AS
 SELECT dataset.id,
    dataset.added AS indexed_time,
    dataset.added_by AS indexed_by,
    dataset_type.name AS product,
    dataset.dataset_type_ref AS dataset_type_id,
    metadata_type.name AS metadata_type,
    dataset.metadata_type_ref AS metadata_type_id,
    dataset.metadata AS metadata_doc,
    agdc.common_timestamp((dataset.metadata #>> '{creation_dt}'::text[])) AS creation_time,
    (dataset.metadata #>> '{format,name}'::text[]) AS format,
    (dataset.metadata #>> '{ga_label}'::text[]) AS label,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text) AS lat,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text) AS lon,
    tstzrange(LEAST(agdc.common_timestamp((dataset.metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((dataset.metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), '[]'::text) AS "time",
    (dataset.metadata #>> '{platform,code}'::text[]) AS platform,
    (dataset.metadata #>> '{instrument,name}'::text[]) AS instrument,
    (dataset.metadata #>> '{product_type}'::text[]) AS product_type
   FROM ((agdc.dataset
     JOIN agdc.dataset_type ON ((dataset_type.id = dataset.dataset_type_ref)))
     JOIN agdc.metadata_type ON ((metadata_type.id = dataset_type.metadata_type_ref)))
  WHERE ((dataset.archived IS NULL) AND (dataset.dataset_type_ref = 52));
 .   DROP VIEW agdc.dv_sentinel2_wofs_nrt_dataset;
       agdc       africa    false    198    198    200    200    200    201    201    201    201    201    201    201    280    8    673    673            �            1259    2903595    dv_telemetry_dataset    VIEW     �  CREATE VIEW agdc.dv_telemetry_dataset AS
 SELECT dataset.id,
    dataset.added AS indexed_time,
    dataset.added_by AS indexed_by,
    dataset_type.name AS product,
    dataset.dataset_type_ref AS dataset_type_id,
    metadata_type.name AS metadata_type,
    dataset.metadata_type_ref AS metadata_type_id,
    dataset.metadata AS metadata_doc,
    agdc.common_timestamp((dataset.metadata #>> '{creation_dt}'::text[])) AS creation_time,
    (dataset.metadata #>> '{format,name}'::text[]) AS format,
    (dataset.metadata #>> '{ga_label}'::text[]) AS label,
    (dataset.metadata #>> '{acquisition,groundstation,code}'::text[]) AS gsi,
    tstzrange(agdc.common_timestamp((dataset.metadata #>> '{acquisition,aos}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{acquisition,los}'::text[])), '[]'::text) AS "time",
    ((dataset.metadata #>> '{acquisition,platform_orbit}'::text[]))::integer AS orbit,
    numrange((((dataset.metadata #>> '{image,satellite_ref_point_start,y}'::text[]))::integer)::numeric, (GREATEST(((dataset.metadata #>> '{image,satellite_ref_point_end,y}'::text[]))::integer, ((dataset.metadata #>> '{image,satellite_ref_point_start,y}'::text[]))::integer))::numeric, '[]'::text) AS sat_row,
    (dataset.metadata #>> '{platform,code}'::text[]) AS platform,
    numrange((((dataset.metadata #>> '{image,satellite_ref_point_start,x}'::text[]))::integer)::numeric, (GREATEST(((dataset.metadata #>> '{image,satellite_ref_point_end,x}'::text[]))::integer, ((dataset.metadata #>> '{image,satellite_ref_point_start,x}'::text[]))::integer))::numeric, '[]'::text) AS sat_path,
    (dataset.metadata #>> '{instrument,name}'::text[]) AS instrument,
    (dataset.metadata #>> '{product_type}'::text[]) AS product_type
   FROM ((agdc.dataset
     JOIN agdc.dataset_type ON ((dataset_type.id = dataset.dataset_type_ref)))
     JOIN agdc.metadata_type ON ((metadata_type.id = dataset_type.metadata_type_ref)))
  WHERE ((dataset.archived IS NULL) AND (dataset.metadata_type_ref = 3));
 %   DROP VIEW agdc.dv_telemetry_dataset;
       agdc       africa    false    201    201    201    280    198    198    201    200    200    200    201    201    201    8                       1259    2904031    dv_water_bodies_dataset    VIEW     �
  CREATE VIEW agdc.dv_water_bodies_dataset AS
 SELECT dataset.id,
    dataset.added AS indexed_time,
    dataset.added_by AS indexed_by,
    dataset_type.name AS product,
    dataset.dataset_type_ref AS dataset_type_id,
    metadata_type.name AS metadata_type,
    dataset.metadata_type_ref AS metadata_type_id,
    dataset.metadata AS metadata_doc,
    agdc.common_timestamp((dataset.metadata #>> '{creation_dt}'::text[])) AS creation_time,
    (dataset.metadata #>> '{format,name}'::text[]) AS format,
    (dataset.metadata #>> '{ga_label}'::text[]) AS label,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text) AS lat,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text) AS lon,
    tstzrange(LEAST(agdc.common_timestamp((dataset.metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((dataset.metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), '[]'::text) AS "time",
    (dataset.metadata #>> '{platform,code}'::text[]) AS platform,
    (dataset.metadata #>> '{instrument,name}'::text[]) AS instrument,
    (dataset.metadata #>> '{product_type}'::text[]) AS product_type
   FROM ((agdc.dataset
     JOIN agdc.dataset_type ON ((dataset_type.id = dataset.dataset_type_ref)))
     JOIN agdc.metadata_type ON ((metadata_type.id = dataset_type.metadata_type_ref)))
  WHERE ((dataset.archived IS NULL) AND (dataset.dataset_type_ref = 53));
 (   DROP VIEW agdc.dv_water_bodies_dataset;
       agdc       africa    false    198    198    200    200    200    201    201    201    201    201    201    201    280    673    673    8                       1259    2904038    dv_weathering_intensity_dataset    VIEW     �
  CREATE VIEW agdc.dv_weathering_intensity_dataset AS
 SELECT dataset.id,
    dataset.added AS indexed_time,
    dataset.added_by AS indexed_by,
    dataset_type.name AS product,
    dataset.dataset_type_ref AS dataset_type_id,
    metadata_type.name AS metadata_type,
    dataset.metadata_type_ref AS metadata_type_id,
    dataset.metadata AS metadata_doc,
    agdc.common_timestamp((dataset.metadata #>> '{creation_dt}'::text[])) AS creation_time,
    (dataset.metadata #>> '{format,name}'::text[]) AS format,
    (dataset.metadata #>> '{ga_label}'::text[]) AS label,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text) AS lat,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text) AS lon,
    tstzrange(LEAST(agdc.common_timestamp((dataset.metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((dataset.metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), '[]'::text) AS "time",
    (dataset.metadata #>> '{platform,code}'::text[]) AS platform,
    (dataset.metadata #>> '{instrument,name}'::text[]) AS instrument,
    (dataset.metadata #>> '{product_type}'::text[]) AS product_type
   FROM ((agdc.dataset
     JOIN agdc.dataset_type ON ((dataset_type.id = dataset.dataset_type_ref)))
     JOIN agdc.metadata_type ON ((metadata_type.id = dataset_type.metadata_type_ref)))
  WHERE ((dataset.archived IS NULL) AND (dataset.dataset_type_ref = 54));
 0   DROP VIEW agdc.dv_weathering_intensity_dataset;
       agdc       africa    false    201    201    201    201    201    200    200    200    198    198    280    201    201    673    673    8                       1259    2904049    dv_wofs_albers_dataset    VIEW     �
  CREATE VIEW agdc.dv_wofs_albers_dataset AS
 SELECT dataset.id,
    dataset.added AS indexed_time,
    dataset.added_by AS indexed_by,
    dataset_type.name AS product,
    dataset.dataset_type_ref AS dataset_type_id,
    metadata_type.name AS metadata_type,
    dataset.metadata_type_ref AS metadata_type_id,
    dataset.metadata AS metadata_doc,
    agdc.common_timestamp((dataset.metadata #>> '{creation_dt}'::text[])) AS creation_time,
    (dataset.metadata #>> '{format,name}'::text[]) AS format,
    (dataset.metadata #>> '{ga_label}'::text[]) AS label,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text) AS lat,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text) AS lon,
    tstzrange(LEAST(agdc.common_timestamp((dataset.metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((dataset.metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), '[]'::text) AS "time",
    (dataset.metadata #>> '{platform,code}'::text[]) AS platform,
    (dataset.metadata #>> '{instrument,name}'::text[]) AS instrument,
    (dataset.metadata #>> '{product_type}'::text[]) AS product_type
   FROM ((agdc.dataset
     JOIN agdc.dataset_type ON ((dataset_type.id = dataset.dataset_type_ref)))
     JOIN agdc.metadata_type ON ((metadata_type.id = dataset_type.metadata_type_ref)))
  WHERE ((dataset.archived IS NULL) AND (dataset.dataset_type_ref = 55));
 '   DROP VIEW agdc.dv_wofs_albers_dataset;
       agdc       africa    false    201    201    201    201    201    201    280    198    198    200    200    200    201    8    673    673                       1259    2904056    dv_wofs_annual_summary_dataset    VIEW     �
  CREATE VIEW agdc.dv_wofs_annual_summary_dataset AS
 SELECT dataset.id,
    dataset.added AS indexed_time,
    dataset.added_by AS indexed_by,
    dataset_type.name AS product,
    dataset.dataset_type_ref AS dataset_type_id,
    metadata_type.name AS metadata_type,
    dataset.metadata_type_ref AS metadata_type_id,
    dataset.metadata AS metadata_doc,
    agdc.common_timestamp((dataset.metadata #>> '{creation_dt}'::text[])) AS creation_time,
    (dataset.metadata #>> '{format,name}'::text[]) AS format,
    (dataset.metadata #>> '{ga_label}'::text[]) AS label,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text) AS lat,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text) AS lon,
    tstzrange(LEAST(agdc.common_timestamp((dataset.metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((dataset.metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), '[]'::text) AS "time",
    (dataset.metadata #>> '{platform,code}'::text[]) AS platform,
    (dataset.metadata #>> '{instrument,name}'::text[]) AS instrument,
    (dataset.metadata #>> '{product_type}'::text[]) AS product_type
   FROM ((agdc.dataset
     JOIN agdc.dataset_type ON ((dataset_type.id = dataset.dataset_type_ref)))
     JOIN agdc.metadata_type ON ((metadata_type.id = dataset_type.metadata_type_ref)))
  WHERE ((dataset.archived IS NULL) AND (dataset.dataset_type_ref = 56));
 /   DROP VIEW agdc.dv_wofs_annual_summary_dataset;
       agdc       africa    false    201    280    198    198    200    200    200    201    201    201    201    201    201    673    673    8                       1259    2904063    dv_wofs_apr_oct_summary_dataset    VIEW     �
  CREATE VIEW agdc.dv_wofs_apr_oct_summary_dataset AS
 SELECT dataset.id,
    dataset.added AS indexed_time,
    dataset.added_by AS indexed_by,
    dataset_type.name AS product,
    dataset.dataset_type_ref AS dataset_type_id,
    metadata_type.name AS metadata_type,
    dataset.metadata_type_ref AS metadata_type_id,
    dataset.metadata AS metadata_doc,
    agdc.common_timestamp((dataset.metadata #>> '{creation_dt}'::text[])) AS creation_time,
    (dataset.metadata #>> '{format,name}'::text[]) AS format,
    (dataset.metadata #>> '{ga_label}'::text[]) AS label,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text) AS lat,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text) AS lon,
    tstzrange(LEAST(agdc.common_timestamp((dataset.metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((dataset.metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), '[]'::text) AS "time",
    (dataset.metadata #>> '{platform,code}'::text[]) AS platform,
    (dataset.metadata #>> '{instrument,name}'::text[]) AS instrument,
    (dataset.metadata #>> '{product_type}'::text[]) AS product_type
   FROM ((agdc.dataset
     JOIN agdc.dataset_type ON ((dataset_type.id = dataset.dataset_type_ref)))
     JOIN agdc.metadata_type ON ((metadata_type.id = dataset_type.metadata_type_ref)))
  WHERE ((dataset.archived IS NULL) AND (dataset.dataset_type_ref = 57));
 0   DROP VIEW agdc.dv_wofs_apr_oct_summary_dataset;
       agdc       africa    false    280    198    198    200    200    200    201    201    201    201    201    201    201    8    673    673            	           1259    2904070     dv_wofs_filtered_summary_dataset    VIEW     �
  CREATE VIEW agdc.dv_wofs_filtered_summary_dataset AS
 SELECT dataset.id,
    dataset.added AS indexed_time,
    dataset.added_by AS indexed_by,
    dataset_type.name AS product,
    dataset.dataset_type_ref AS dataset_type_id,
    metadata_type.name AS metadata_type,
    dataset.metadata_type_ref AS metadata_type_id,
    dataset.metadata AS metadata_doc,
    agdc.common_timestamp((dataset.metadata #>> '{creation_dt}'::text[])) AS creation_time,
    (dataset.metadata #>> '{format,name}'::text[]) AS format,
    (dataset.metadata #>> '{ga_label}'::text[]) AS label,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text) AS lat,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text) AS lon,
    tstzrange(LEAST(agdc.common_timestamp((dataset.metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((dataset.metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), '[]'::text) AS "time",
    (dataset.metadata #>> '{platform,code}'::text[]) AS platform,
    (dataset.metadata #>> '{instrument,name}'::text[]) AS instrument,
    (dataset.metadata #>> '{product_type}'::text[]) AS product_type
   FROM ((agdc.dataset
     JOIN agdc.dataset_type ON ((dataset_type.id = dataset.dataset_type_ref)))
     JOIN agdc.metadata_type ON ((metadata_type.id = dataset_type.metadata_type_ref)))
  WHERE ((dataset.archived IS NULL) AND (dataset.dataset_type_ref = 58));
 1   DROP VIEW agdc.dv_wofs_filtered_summary_dataset;
       agdc       africa    false    201    198    198    200    201    201    200    280    201    200    201    201    201    8    673    673            
           1259    2904077    dv_wofs_nov_mar_summary_dataset    VIEW     �
  CREATE VIEW agdc.dv_wofs_nov_mar_summary_dataset AS
 SELECT dataset.id,
    dataset.added AS indexed_time,
    dataset.added_by AS indexed_by,
    dataset_type.name AS product,
    dataset.dataset_type_ref AS dataset_type_id,
    metadata_type.name AS metadata_type,
    dataset.metadata_type_ref AS metadata_type_id,
    dataset.metadata AS metadata_doc,
    agdc.common_timestamp((dataset.metadata #>> '{creation_dt}'::text[])) AS creation_time,
    (dataset.metadata #>> '{format,name}'::text[]) AS format,
    (dataset.metadata #>> '{ga_label}'::text[]) AS label,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text) AS lat,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text) AS lon,
    tstzrange(LEAST(agdc.common_timestamp((dataset.metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((dataset.metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), '[]'::text) AS "time",
    (dataset.metadata #>> '{platform,code}'::text[]) AS platform,
    (dataset.metadata #>> '{instrument,name}'::text[]) AS instrument,
    (dataset.metadata #>> '{product_type}'::text[]) AS product_type
   FROM ((agdc.dataset
     JOIN agdc.dataset_type ON ((dataset_type.id = dataset.dataset_type_ref)))
     JOIN agdc.metadata_type ON ((metadata_type.id = dataset_type.metadata_type_ref)))
  WHERE ((dataset.archived IS NULL) AND (dataset.dataset_type_ref = 59));
 0   DROP VIEW agdc.dv_wofs_nov_mar_summary_dataset;
       agdc       africa    false    200    200    201    201    201    201    201    201    280    198    198    201    200    673    8    673                       1259    2904084    dv_wofs_summary_dataset    VIEW     �
  CREATE VIEW agdc.dv_wofs_summary_dataset AS
 SELECT dataset.id,
    dataset.added AS indexed_time,
    dataset.added_by AS indexed_by,
    dataset_type.name AS product,
    dataset.dataset_type_ref AS dataset_type_id,
    metadata_type.name AS metadata_type,
    dataset.metadata_type_ref AS metadata_type_id,
    dataset.metadata AS metadata_doc,
    agdc.common_timestamp((dataset.metadata #>> '{creation_dt}'::text[])) AS creation_time,
    (dataset.metadata #>> '{format,name}'::text[]) AS format,
    (dataset.metadata #>> '{ga_label}'::text[]) AS label,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text) AS lat,
    agdc.float8range(LEAST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((dataset.metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((dataset.metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text) AS lon,
    tstzrange(LEAST(agdc.common_timestamp((dataset.metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((dataset.metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((dataset.metadata #>> '{extent,center_dt}'::text[]))), '[]'::text) AS "time",
    (dataset.metadata #>> '{platform,code}'::text[]) AS platform,
    (dataset.metadata #>> '{instrument,name}'::text[]) AS instrument,
    (dataset.metadata #>> '{product_type}'::text[]) AS product_type
   FROM ((agdc.dataset
     JOIN agdc.dataset_type ON ((dataset_type.id = dataset.dataset_type_ref)))
     JOIN agdc.metadata_type ON ((metadata_type.id = dataset_type.metadata_type_ref)))
  WHERE ((dataset.archived IS NULL) AND (dataset.dataset_type_ref = 60));
 (   DROP VIEW agdc.dv_wofs_summary_dataset;
       agdc       africa    false    201    280    198    198    200    200    200    201    201    201    201    201    201    673    673    8            �            1259    2903467    metadata_type_id_seq    SEQUENCE     �   CREATE SEQUENCE agdc.metadata_type_id_seq
    AS smallint
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE agdc.metadata_type_id_seq;
       agdc    
   agdc_admin    false    198    8            �           0    0    metadata_type_id_seq    SEQUENCE OWNED BY     I   ALTER SEQUENCE agdc.metadata_type_id_seq OWNED BY agdc.metadata_type.id;
            agdc    
   agdc_admin    false    197            �           0    0    SEQUENCE metadata_type_id_seq    ACL     I   GRANT SELECT,USAGE ON SEQUENCE agdc.metadata_type_id_seq TO agdc_ingest;
            agdc    
   agdc_admin    false    197            !           2604    2903530    dataset_location id    DEFAULT     v   ALTER TABLE ONLY agdc.dataset_location ALTER COLUMN id SET DEFAULT nextval('agdc.dataset_location_id_seq'::regclass);
 @   ALTER TABLE agdc.dataset_location ALTER COLUMN id DROP DEFAULT;
       agdc    
   agdc_admin    false    203    202    203                       2604    2903488    dataset_type id    DEFAULT     n   ALTER TABLE ONLY agdc.dataset_type ALTER COLUMN id SET DEFAULT nextval('agdc.dataset_type_id_seq'::regclass);
 <   ALTER TABLE agdc.dataset_type ALTER COLUMN id DROP DEFAULT;
       agdc    
   agdc_admin    false    199    200    200                       2604    2903472    metadata_type id    DEFAULT     p   ALTER TABLE ONLY agdc.metadata_type ALTER COLUMN id SET DEFAULT nextval('agdc.metadata_type_id_seq'::regclass);
 =   ALTER TABLE agdc.metadata_type ALTER COLUMN id DROP DEFAULT;
       agdc    
   agdc_admin    false    198    197    198            �          0    2903504    dataset 
   TABLE DATA               v   COPY agdc.dataset (id, metadata_type_ref, dataset_type_ref, metadata, archived, added, added_by, updated) FROM stdin;
    agdc    
   agdc_admin    false    201   ��      �          0    2903527    dataset_location 
   TABLE DATA               j   COPY agdc.dataset_location (id, dataset_ref, uri_scheme, uri_body, added, added_by, archived) FROM stdin;
    agdc    
   agdc_admin    false    203   ��      �          0    2903546    dataset_source 
   TABLE DATA               S   COPY agdc.dataset_source (dataset_ref, classifier, source_dataset_ref) FROM stdin;
    agdc    
   agdc_admin    false    204   ��      �          0    2903485    dataset_type 
   TABLE DATA               q   COPY agdc.dataset_type (id, name, metadata, metadata_type_ref, definition, added, added_by, updated) FROM stdin;
    agdc    
   agdc_admin    false    200   �      �          0    2903469    metadata_type 
   TABLE DATA               U   COPY agdc.metadata_type (id, name, definition, added, added_by, updated) FROM stdin;
    agdc    
   agdc_admin    false    198   υ      �           0    0    dataset_location_id_seq    SEQUENCE SET     D   SELECT pg_catalog.setval('agdc.dataset_location_id_seq', 1, false);
            agdc    
   agdc_admin    false    202            �           0    0    dataset_type_id_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('agdc.dataset_type_id_seq', 66, true);
            agdc    
   agdc_admin    false    199            �           0    0    metadata_type_id_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('agdc.metadata_type_id_seq', 8, true);
            agdc    
   agdc_admin    false    197            �           2606    2903513    dataset pk_dataset 
   CONSTRAINT     N   ALTER TABLE ONLY agdc.dataset
    ADD CONSTRAINT pk_dataset PRIMARY KEY (id);
 :   ALTER TABLE ONLY agdc.dataset DROP CONSTRAINT pk_dataset;
       agdc      
   agdc_admin    false    201            �           2606    2903537 $   dataset_location pk_dataset_location 
   CONSTRAINT     `   ALTER TABLE ONLY agdc.dataset_location
    ADD CONSTRAINT pk_dataset_location PRIMARY KEY (id);
 L   ALTER TABLE ONLY agdc.dataset_location DROP CONSTRAINT pk_dataset_location;
       agdc      
   agdc_admin    false    203            �           2606    2903553     dataset_source pk_dataset_source 
   CONSTRAINT     q   ALTER TABLE ONLY agdc.dataset_source
    ADD CONSTRAINT pk_dataset_source PRIMARY KEY (dataset_ref, classifier);
 H   ALTER TABLE ONLY agdc.dataset_source DROP CONSTRAINT pk_dataset_source;
       agdc      
   agdc_admin    false    204    204            )           2606    2903496    dataset_type pk_dataset_type 
   CONSTRAINT     X   ALTER TABLE ONLY agdc.dataset_type
    ADD CONSTRAINT pk_dataset_type PRIMARY KEY (id);
 D   ALTER TABLE ONLY agdc.dataset_type DROP CONSTRAINT pk_dataset_type;
       agdc      
   agdc_admin    false    200            %           2606    2903480    metadata_type pk_metadata_type 
   CONSTRAINT     Z   ALTER TABLE ONLY agdc.metadata_type
    ADD CONSTRAINT pk_metadata_type PRIMARY KEY (id);
 F   ALTER TABLE ONLY agdc.metadata_type DROP CONSTRAINT pk_metadata_type;
       agdc      
   agdc_admin    false    198            �           2606    2903539 /   dataset_location uq_dataset_location_uri_scheme 
   CONSTRAINT     �   ALTER TABLE ONLY agdc.dataset_location
    ADD CONSTRAINT uq_dataset_location_uri_scheme UNIQUE (uri_scheme, uri_body, dataset_ref);
 W   ALTER TABLE ONLY agdc.dataset_location DROP CONSTRAINT uq_dataset_location_uri_scheme;
       agdc      
   agdc_admin    false    203    203    203            �           2606    2903555 3   dataset_source uq_dataset_source_source_dataset_ref 
   CONSTRAINT     �   ALTER TABLE ONLY agdc.dataset_source
    ADD CONSTRAINT uq_dataset_source_source_dataset_ref UNIQUE (source_dataset_ref, dataset_ref);
 [   ALTER TABLE ONLY agdc.dataset_source DROP CONSTRAINT uq_dataset_source_source_dataset_ref;
       agdc      
   agdc_admin    false    204    204            +           2606    2903498 !   dataset_type uq_dataset_type_name 
   CONSTRAINT     Z   ALTER TABLE ONLY agdc.dataset_type
    ADD CONSTRAINT uq_dataset_type_name UNIQUE (name);
 I   ALTER TABLE ONLY agdc.dataset_type DROP CONSTRAINT uq_dataset_type_name;
       agdc      
   agdc_admin    false    200            '           2606    2903482 #   metadata_type uq_metadata_type_name 
   CONSTRAINT     \   ALTER TABLE ONLY agdc.metadata_type
    ADD CONSTRAINT uq_metadata_type_name UNIQUE (name);
 K   ALTER TABLE ONLY agdc.metadata_type DROP CONSTRAINT uq_metadata_type_name;
       agdc      
   agdc_admin    false    198            ,           1259    2903618 +   dix_aster_aloh_group_composition_instrument    INDEX     �   CREATE INDEX dix_aster_aloh_group_composition_instrument ON agdc.dataset USING btree (((metadata #>> '{instrument,name}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 3));
 =   DROP INDEX agdc.dix_aster_aloh_group_composition_instrument;
       agdc      
   agdc_admin    false    201    201    201    201            -           1259    2903615 -   dix_aster_aloh_group_composition_lat_lon_time    INDEX     ^  CREATE INDEX dix_aster_aloh_group_composition_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 3));
 ?   DROP INDEX agdc.dix_aster_aloh_group_composition_lat_lon_time;
       agdc      
   agdc_admin    false    201    201    201    280    201            .           1259    2903617 )   dix_aster_aloh_group_composition_platform    INDEX     �   CREATE INDEX dix_aster_aloh_group_composition_platform ON agdc.dataset USING btree (((metadata #>> '{platform,code}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 3));
 ;   DROP INDEX agdc.dix_aster_aloh_group_composition_platform;
       agdc      
   agdc_admin    false    201    201    201    201            /           1259    2903616 -   dix_aster_aloh_group_composition_time_lat_lon    INDEX     ^  CREATE INDEX dix_aster_aloh_group_composition_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 3));
 ?   DROP INDEX agdc.dix_aster_aloh_group_composition_time_lat_lon;
       agdc      
   agdc_admin    false    201    201    280    201    201            0           1259    2903627 '   dix_aster_aloh_group_content_instrument    INDEX     �   CREATE INDEX dix_aster_aloh_group_content_instrument ON agdc.dataset USING btree (((metadata #>> '{instrument,name}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 4));
 9   DROP INDEX agdc.dix_aster_aloh_group_content_instrument;
       agdc      
   agdc_admin    false    201    201    201    201            1           1259    2903624 )   dix_aster_aloh_group_content_lat_lon_time    INDEX     Z  CREATE INDEX dix_aster_aloh_group_content_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 4));
 ;   DROP INDEX agdc.dix_aster_aloh_group_content_lat_lon_time;
       agdc      
   agdc_admin    false    201    201    280    201    201            2           1259    2903626 %   dix_aster_aloh_group_content_platform    INDEX     �   CREATE INDEX dix_aster_aloh_group_content_platform ON agdc.dataset USING btree (((metadata #>> '{platform,code}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 4));
 7   DROP INDEX agdc.dix_aster_aloh_group_content_platform;
       agdc      
   agdc_admin    false    201    201    201    201            3           1259    2903625 )   dix_aster_aloh_group_content_time_lat_lon    INDEX     Z  CREATE INDEX dix_aster_aloh_group_content_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 4));
 ;   DROP INDEX agdc.dix_aster_aloh_group_content_time_lat_lon;
       agdc      
   agdc_admin    false    201    201    201    201    280            4           1259    2903636 !   dix_aster_false_colour_instrument    INDEX     �   CREATE INDEX dix_aster_false_colour_instrument ON agdc.dataset USING btree (((metadata #>> '{instrument,name}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 5));
 3   DROP INDEX agdc.dix_aster_false_colour_instrument;
       agdc      
   agdc_admin    false    201    201    201    201            5           1259    2903633 #   dix_aster_false_colour_lat_lon_time    INDEX     T  CREATE INDEX dix_aster_false_colour_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 5));
 5   DROP INDEX agdc.dix_aster_false_colour_lat_lon_time;
       agdc      
   agdc_admin    false    201    201    201    201    280            6           1259    2903635    dix_aster_false_colour_platform    INDEX     �   CREATE INDEX dix_aster_false_colour_platform ON agdc.dataset USING btree (((metadata #>> '{platform,code}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 5));
 1   DROP INDEX agdc.dix_aster_false_colour_platform;
       agdc      
   agdc_admin    false    201    201    201    201            7           1259    2903634 #   dix_aster_false_colour_time_lat_lon    INDEX     T  CREATE INDEX dix_aster_false_colour_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 5));
 5   DROP INDEX agdc.dix_aster_false_colour_time_lat_lon;
       agdc      
   agdc_admin    false    201    201    280    201    201            8           1259    2903645 '   dix_aster_feoh_group_content_instrument    INDEX     �   CREATE INDEX dix_aster_feoh_group_content_instrument ON agdc.dataset USING btree (((metadata #>> '{instrument,name}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 6));
 9   DROP INDEX agdc.dix_aster_feoh_group_content_instrument;
       agdc      
   agdc_admin    false    201    201    201    201            9           1259    2903642 )   dix_aster_feoh_group_content_lat_lon_time    INDEX     Z  CREATE INDEX dix_aster_feoh_group_content_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 6));
 ;   DROP INDEX agdc.dix_aster_feoh_group_content_lat_lon_time;
       agdc      
   agdc_admin    false    201    201    201    280    201            :           1259    2903644 %   dix_aster_feoh_group_content_platform    INDEX     �   CREATE INDEX dix_aster_feoh_group_content_platform ON agdc.dataset USING btree (((metadata #>> '{platform,code}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 6));
 7   DROP INDEX agdc.dix_aster_feoh_group_content_platform;
       agdc      
   agdc_admin    false    201    201    201    201            ;           1259    2903643 )   dix_aster_feoh_group_content_time_lat_lon    INDEX     Z  CREATE INDEX dix_aster_feoh_group_content_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 6));
 ;   DROP INDEX agdc.dix_aster_feoh_group_content_time_lat_lon;
       agdc      
   agdc_admin    false    201    201    201    201    280            <           1259    2903654 -   dix_aster_ferric_oxide_composition_instrument    INDEX     �   CREATE INDEX dix_aster_ferric_oxide_composition_instrument ON agdc.dataset USING btree (((metadata #>> '{instrument,name}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 7));
 ?   DROP INDEX agdc.dix_aster_ferric_oxide_composition_instrument;
       agdc      
   agdc_admin    false    201    201    201    201            =           1259    2903651 /   dix_aster_ferric_oxide_composition_lat_lon_time    INDEX     `  CREATE INDEX dix_aster_ferric_oxide_composition_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 7));
 A   DROP INDEX agdc.dix_aster_ferric_oxide_composition_lat_lon_time;
       agdc      
   agdc_admin    false    201    201    201    201    280            >           1259    2903653 +   dix_aster_ferric_oxide_composition_platform    INDEX     �   CREATE INDEX dix_aster_ferric_oxide_composition_platform ON agdc.dataset USING btree (((metadata #>> '{platform,code}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 7));
 =   DROP INDEX agdc.dix_aster_ferric_oxide_composition_platform;
       agdc      
   agdc_admin    false    201    201    201    201            ?           1259    2903652 /   dix_aster_ferric_oxide_composition_time_lat_lon    INDEX     `  CREATE INDEX dix_aster_ferric_oxide_composition_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 7));
 A   DROP INDEX agdc.dix_aster_ferric_oxide_composition_time_lat_lon;
       agdc      
   agdc_admin    false    201    201    201    201    280            @           1259    2903663 )   dix_aster_ferric_oxide_content_instrument    INDEX     �   CREATE INDEX dix_aster_ferric_oxide_content_instrument ON agdc.dataset USING btree (((metadata #>> '{instrument,name}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 8));
 ;   DROP INDEX agdc.dix_aster_ferric_oxide_content_instrument;
       agdc      
   agdc_admin    false    201    201    201    201            A           1259    2903660 +   dix_aster_ferric_oxide_content_lat_lon_time    INDEX     \  CREATE INDEX dix_aster_ferric_oxide_content_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 8));
 =   DROP INDEX agdc.dix_aster_ferric_oxide_content_lat_lon_time;
       agdc      
   agdc_admin    false    201    201    201    201    280            B           1259    2903662 '   dix_aster_ferric_oxide_content_platform    INDEX     �   CREATE INDEX dix_aster_ferric_oxide_content_platform ON agdc.dataset USING btree (((metadata #>> '{platform,code}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 8));
 9   DROP INDEX agdc.dix_aster_ferric_oxide_content_platform;
       agdc      
   agdc_admin    false    201    201    201    201            C           1259    2903661 +   dix_aster_ferric_oxide_content_time_lat_lon    INDEX     \  CREATE INDEX dix_aster_ferric_oxide_content_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 8));
 =   DROP INDEX agdc.dix_aster_ferric_oxide_content_time_lat_lon;
       agdc      
   agdc_admin    false    280    201    201    201    201            D           1259    2903672 1   dix_aster_ferrous_iron_content_in_mgoh_instrument    INDEX     �   CREATE INDEX dix_aster_ferrous_iron_content_in_mgoh_instrument ON agdc.dataset USING btree (((metadata #>> '{instrument,name}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 9));
 C   DROP INDEX agdc.dix_aster_ferrous_iron_content_in_mgoh_instrument;
       agdc      
   agdc_admin    false    201    201    201    201            E           1259    2903669 3   dix_aster_ferrous_iron_content_in_mgoh_lat_lon_time    INDEX     d  CREATE INDEX dix_aster_ferrous_iron_content_in_mgoh_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 9));
 E   DROP INDEX agdc.dix_aster_ferrous_iron_content_in_mgoh_lat_lon_time;
       agdc      
   agdc_admin    false    201    201    201    280    201            F           1259    2903671 /   dix_aster_ferrous_iron_content_in_mgoh_platform    INDEX     �   CREATE INDEX dix_aster_ferrous_iron_content_in_mgoh_platform ON agdc.dataset USING btree (((metadata #>> '{platform,code}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 9));
 A   DROP INDEX agdc.dix_aster_ferrous_iron_content_in_mgoh_platform;
       agdc      
   agdc_admin    false    201    201    201    201            G           1259    2903670 3   dix_aster_ferrous_iron_content_in_mgoh_time_lat_lon    INDEX     d  CREATE INDEX dix_aster_ferrous_iron_content_in_mgoh_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 9));
 E   DROP INDEX agdc.dix_aster_ferrous_iron_content_in_mgoh_time_lat_lon;
       agdc      
   agdc_admin    false    280    201    201    201    201            H           1259    2903681 '   dix_aster_ferrous_iron_index_instrument    INDEX     �   CREATE INDEX dix_aster_ferrous_iron_index_instrument ON agdc.dataset USING btree (((metadata #>> '{instrument,name}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 10));
 9   DROP INDEX agdc.dix_aster_ferrous_iron_index_instrument;
       agdc      
   agdc_admin    false    201    201    201    201            I           1259    2903678 )   dix_aster_ferrous_iron_index_lat_lon_time    INDEX     [  CREATE INDEX dix_aster_ferrous_iron_index_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 10));
 ;   DROP INDEX agdc.dix_aster_ferrous_iron_index_lat_lon_time;
       agdc      
   agdc_admin    false    201    280    201    201    201            J           1259    2903680 %   dix_aster_ferrous_iron_index_platform    INDEX     �   CREATE INDEX dix_aster_ferrous_iron_index_platform ON agdc.dataset USING btree (((metadata #>> '{platform,code}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 10));
 7   DROP INDEX agdc.dix_aster_ferrous_iron_index_platform;
       agdc      
   agdc_admin    false    201    201    201    201            K           1259    2903679 )   dix_aster_ferrous_iron_index_time_lat_lon    INDEX     [  CREATE INDEX dix_aster_ferrous_iron_index_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 10));
 ;   DROP INDEX agdc.dix_aster_ferrous_iron_index_time_lat_lon;
       agdc      
   agdc_admin    false    201    201    280    201    201            L           1259    2903690 %   dix_aster_green_vegetation_instrument    INDEX     �   CREATE INDEX dix_aster_green_vegetation_instrument ON agdc.dataset USING btree (((metadata #>> '{instrument,name}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 11));
 7   DROP INDEX agdc.dix_aster_green_vegetation_instrument;
       agdc      
   agdc_admin    false    201    201    201    201            M           1259    2903687 '   dix_aster_green_vegetation_lat_lon_time    INDEX     Y  CREATE INDEX dix_aster_green_vegetation_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 11));
 9   DROP INDEX agdc.dix_aster_green_vegetation_lat_lon_time;
       agdc      
   agdc_admin    false    280    201    201    201    201            N           1259    2903689 #   dix_aster_green_vegetation_platform    INDEX     �   CREATE INDEX dix_aster_green_vegetation_platform ON agdc.dataset USING btree (((metadata #>> '{platform,code}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 11));
 5   DROP INDEX agdc.dix_aster_green_vegetation_platform;
       agdc      
   agdc_admin    false    201    201    201    201            O           1259    2903688 '   dix_aster_green_vegetation_time_lat_lon    INDEX     Y  CREATE INDEX dix_aster_green_vegetation_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 11));
 9   DROP INDEX agdc.dix_aster_green_vegetation_time_lat_lon;
       agdc      
   agdc_admin    false    201    201    201    201    280            P           1259    2903699 !   dix_aster_gypsum_index_instrument    INDEX     �   CREATE INDEX dix_aster_gypsum_index_instrument ON agdc.dataset USING btree (((metadata #>> '{instrument,name}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 12));
 3   DROP INDEX agdc.dix_aster_gypsum_index_instrument;
       agdc      
   agdc_admin    false    201    201    201    201            Q           1259    2903696 #   dix_aster_gypsum_index_lat_lon_time    INDEX     U  CREATE INDEX dix_aster_gypsum_index_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 12));
 5   DROP INDEX agdc.dix_aster_gypsum_index_lat_lon_time;
       agdc      
   agdc_admin    false    201    201    280    201    201            R           1259    2903698    dix_aster_gypsum_index_platform    INDEX     �   CREATE INDEX dix_aster_gypsum_index_platform ON agdc.dataset USING btree (((metadata #>> '{platform,code}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 12));
 1   DROP INDEX agdc.dix_aster_gypsum_index_platform;
       agdc      
   agdc_admin    false    201    201    201    201            S           1259    2903697 #   dix_aster_gypsum_index_time_lat_lon    INDEX     U  CREATE INDEX dix_aster_gypsum_index_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 12));
 5   DROP INDEX agdc.dix_aster_gypsum_index_time_lat_lon;
       agdc      
   agdc_admin    false    280    201    201    201    201            T           1259    2903708 '   dix_aster_kaolin_group_index_instrument    INDEX     �   CREATE INDEX dix_aster_kaolin_group_index_instrument ON agdc.dataset USING btree (((metadata #>> '{instrument,name}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 13));
 9   DROP INDEX agdc.dix_aster_kaolin_group_index_instrument;
       agdc      
   agdc_admin    false    201    201    201    201            U           1259    2903705 )   dix_aster_kaolin_group_index_lat_lon_time    INDEX     [  CREATE INDEX dix_aster_kaolin_group_index_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 13));
 ;   DROP INDEX agdc.dix_aster_kaolin_group_index_lat_lon_time;
       agdc      
   agdc_admin    false    201    201    280    201    201            V           1259    2903707 %   dix_aster_kaolin_group_index_platform    INDEX     �   CREATE INDEX dix_aster_kaolin_group_index_platform ON agdc.dataset USING btree (((metadata #>> '{platform,code}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 13));
 7   DROP INDEX agdc.dix_aster_kaolin_group_index_platform;
       agdc      
   agdc_admin    false    201    201    201    201            W           1259    2903706 )   dix_aster_kaolin_group_index_time_lat_lon    INDEX     [  CREATE INDEX dix_aster_kaolin_group_index_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 13));
 ;   DROP INDEX agdc.dix_aster_kaolin_group_index_time_lat_lon;
       agdc      
   agdc_admin    false    201    201    201    280    201            X           1259    2903717 +   dix_aster_mgoh_group_composition_instrument    INDEX     �   CREATE INDEX dix_aster_mgoh_group_composition_instrument ON agdc.dataset USING btree (((metadata #>> '{instrument,name}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 14));
 =   DROP INDEX agdc.dix_aster_mgoh_group_composition_instrument;
       agdc      
   agdc_admin    false    201    201    201    201            Y           1259    2903714 -   dix_aster_mgoh_group_composition_lat_lon_time    INDEX     _  CREATE INDEX dix_aster_mgoh_group_composition_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 14));
 ?   DROP INDEX agdc.dix_aster_mgoh_group_composition_lat_lon_time;
       agdc      
   agdc_admin    false    201    201    201    280    201            Z           1259    2903716 )   dix_aster_mgoh_group_composition_platform    INDEX     �   CREATE INDEX dix_aster_mgoh_group_composition_platform ON agdc.dataset USING btree (((metadata #>> '{platform,code}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 14));
 ;   DROP INDEX agdc.dix_aster_mgoh_group_composition_platform;
       agdc      
   agdc_admin    false    201    201    201    201            [           1259    2903715 -   dix_aster_mgoh_group_composition_time_lat_lon    INDEX     _  CREATE INDEX dix_aster_mgoh_group_composition_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 14));
 ?   DROP INDEX agdc.dix_aster_mgoh_group_composition_time_lat_lon;
       agdc      
   agdc_admin    false    201    280    201    201    201            \           1259    2903726 '   dix_aster_mgoh_group_content_instrument    INDEX     �   CREATE INDEX dix_aster_mgoh_group_content_instrument ON agdc.dataset USING btree (((metadata #>> '{instrument,name}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 15));
 9   DROP INDEX agdc.dix_aster_mgoh_group_content_instrument;
       agdc      
   agdc_admin    false    201    201    201    201            ]           1259    2903723 )   dix_aster_mgoh_group_content_lat_lon_time    INDEX     [  CREATE INDEX dix_aster_mgoh_group_content_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 15));
 ;   DROP INDEX agdc.dix_aster_mgoh_group_content_lat_lon_time;
       agdc      
   agdc_admin    false    201    201    201    280    201            ^           1259    2903725 %   dix_aster_mgoh_group_content_platform    INDEX     �   CREATE INDEX dix_aster_mgoh_group_content_platform ON agdc.dataset USING btree (((metadata #>> '{platform,code}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 15));
 7   DROP INDEX agdc.dix_aster_mgoh_group_content_platform;
       agdc      
   agdc_admin    false    201    201    201    201            _           1259    2903724 )   dix_aster_mgoh_group_content_time_lat_lon    INDEX     [  CREATE INDEX dix_aster_mgoh_group_content_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 15));
 ;   DROP INDEX agdc.dix_aster_mgoh_group_content_time_lat_lon;
       agdc      
   agdc_admin    false    280    201    201    201    201            `           1259    2903735 !   dix_aster_opaque_index_instrument    INDEX     �   CREATE INDEX dix_aster_opaque_index_instrument ON agdc.dataset USING btree (((metadata #>> '{instrument,name}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 16));
 3   DROP INDEX agdc.dix_aster_opaque_index_instrument;
       agdc      
   agdc_admin    false    201    201    201    201            a           1259    2903732 #   dix_aster_opaque_index_lat_lon_time    INDEX     U  CREATE INDEX dix_aster_opaque_index_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 16));
 5   DROP INDEX agdc.dix_aster_opaque_index_lat_lon_time;
       agdc      
   agdc_admin    false    201    280    201    201    201            b           1259    2903734    dix_aster_opaque_index_platform    INDEX     �   CREATE INDEX dix_aster_opaque_index_platform ON agdc.dataset USING btree (((metadata #>> '{platform,code}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 16));
 1   DROP INDEX agdc.dix_aster_opaque_index_platform;
       agdc      
   agdc_admin    false    201    201    201    201            c           1259    2903733 #   dix_aster_opaque_index_time_lat_lon    INDEX     U  CREATE INDEX dix_aster_opaque_index_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 16));
 5   DROP INDEX agdc.dix_aster_opaque_index_time_lat_lon;
       agdc      
   agdc_admin    false    201    201    201    280    201            d           1259    2903744 !   dix_aster_quartz_index_instrument    INDEX     �   CREATE INDEX dix_aster_quartz_index_instrument ON agdc.dataset USING btree (((metadata #>> '{instrument,name}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 17));
 3   DROP INDEX agdc.dix_aster_quartz_index_instrument;
       agdc      
   agdc_admin    false    201    201    201    201            e           1259    2903741 #   dix_aster_quartz_index_lat_lon_time    INDEX     U  CREATE INDEX dix_aster_quartz_index_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 17));
 5   DROP INDEX agdc.dix_aster_quartz_index_lat_lon_time;
       agdc      
   agdc_admin    false    201    201    201    280    201            f           1259    2903743    dix_aster_quartz_index_platform    INDEX     �   CREATE INDEX dix_aster_quartz_index_platform ON agdc.dataset USING btree (((metadata #>> '{platform,code}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 17));
 1   DROP INDEX agdc.dix_aster_quartz_index_platform;
       agdc      
   agdc_admin    false    201    201    201    201            g           1259    2903742 #   dix_aster_quartz_index_time_lat_lon    INDEX     U  CREATE INDEX dix_aster_quartz_index_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 17));
 5   DROP INDEX agdc.dix_aster_quartz_index_time_lat_lon;
       agdc      
   agdc_admin    false    280    201    201    201    201            h           1259    2903753 $   dix_aster_regolith_ratios_instrument    INDEX     �   CREATE INDEX dix_aster_regolith_ratios_instrument ON agdc.dataset USING btree (((metadata #>> '{instrument,name}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 18));
 6   DROP INDEX agdc.dix_aster_regolith_ratios_instrument;
       agdc      
   agdc_admin    false    201    201    201    201            i           1259    2903750 &   dix_aster_regolith_ratios_lat_lon_time    INDEX     X  CREATE INDEX dix_aster_regolith_ratios_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 18));
 8   DROP INDEX agdc.dix_aster_regolith_ratios_lat_lon_time;
       agdc      
   agdc_admin    false    201    280    201    201    201            j           1259    2903752 "   dix_aster_regolith_ratios_platform    INDEX     �   CREATE INDEX dix_aster_regolith_ratios_platform ON agdc.dataset USING btree (((metadata #>> '{platform,code}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 18));
 4   DROP INDEX agdc.dix_aster_regolith_ratios_platform;
       agdc      
   agdc_admin    false    201    201    201    201            k           1259    2903751 &   dix_aster_regolith_ratios_time_lat_lon    INDEX     X  CREATE INDEX dix_aster_regolith_ratios_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 18));
 8   DROP INDEX agdc.dix_aster_regolith_ratios_time_lat_lon;
       agdc      
   agdc_admin    false    201    280    201    201    201            l           1259    2903762 !   dix_aster_silica_index_instrument    INDEX     �   CREATE INDEX dix_aster_silica_index_instrument ON agdc.dataset USING btree (((metadata #>> '{instrument,name}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 19));
 3   DROP INDEX agdc.dix_aster_silica_index_instrument;
       agdc      
   agdc_admin    false    201    201    201    201            m           1259    2903759 #   dix_aster_silica_index_lat_lon_time    INDEX     U  CREATE INDEX dix_aster_silica_index_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 19));
 5   DROP INDEX agdc.dix_aster_silica_index_lat_lon_time;
       agdc      
   agdc_admin    false    201    201    280    201    201            n           1259    2903761    dix_aster_silica_index_platform    INDEX     �   CREATE INDEX dix_aster_silica_index_platform ON agdc.dataset USING btree (((metadata #>> '{platform,code}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 19));
 1   DROP INDEX agdc.dix_aster_silica_index_platform;
       agdc      
   agdc_admin    false    201    201    201    201            o           1259    2903760 #   dix_aster_silica_index_time_lat_lon    INDEX     U  CREATE INDEX dix_aster_silica_index_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 19));
 5   DROP INDEX agdc.dix_aster_silica_index_time_lat_lon;
       agdc      
   agdc_admin    false    201    201    201    280    201            p           1259    2903768 -   dix_cemp_insar_alos_displacement_lat_lon_time    INDEX     !  CREATE INDEX dix_cemp_insar_alos_displacement_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(((metadata #>> '{extent,lat,begin}'::text[]))::double precision, ((metadata #>> '{extent,lat,end}'::text[]))::double precision, '[]'::text), agdc.float8range(((metadata #>> '{extent,lon,begin}'::text[]))::double precision, ((metadata #>> '{extent,lon,end}'::text[]))::double precision, '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{properties,dtr:start_datetime}'::text[])), agdc.common_timestamp((metadata #>> '{properties,datetime}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{properties,dtr:end_datetime}'::text[])), agdc.common_timestamp((metadata #>> '{properties,datetime}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 20));
 ?   DROP INDEX agdc.dix_cemp_insar_alos_displacement_lat_lon_time;
       agdc      
   agdc_admin    false    201    201    201    201    280            q           1259    2903770 ,   dix_cemp_insar_alos_displacement_region_code    INDEX     �   CREATE INDEX dix_cemp_insar_alos_displacement_region_code ON agdc.dataset USING btree (((metadata #>> '{properties,odc:region_code}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 20));
 >   DROP INDEX agdc.dix_cemp_insar_alos_displacement_region_code;
       agdc      
   agdc_admin    false    201    201    201    201            r           1259    2903769 -   dix_cemp_insar_alos_displacement_time_lat_lon    INDEX     !  CREATE INDEX dix_cemp_insar_alos_displacement_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{properties,dtr:start_datetime}'::text[])), agdc.common_timestamp((metadata #>> '{properties,datetime}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{properties,dtr:end_datetime}'::text[])), agdc.common_timestamp((metadata #>> '{properties,datetime}'::text[]))), '[]'::text), agdc.float8range(((metadata #>> '{extent,lat,begin}'::text[]))::double precision, ((metadata #>> '{extent,lat,end}'::text[]))::double precision, '[]'::text), agdc.float8range(((metadata #>> '{extent,lon,begin}'::text[]))::double precision, ((metadata #>> '{extent,lon,end}'::text[]))::double precision, '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 20));
 ?   DROP INDEX agdc.dix_cemp_insar_alos_displacement_time_lat_lon;
       agdc      
   agdc_admin    false    201    201    201    280    201            s           1259    2903776 )   dix_cemp_insar_alos_velocity_lat_lon_time    INDEX       CREATE INDEX dix_cemp_insar_alos_velocity_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(((metadata #>> '{extent,lat,begin}'::text[]))::double precision, ((metadata #>> '{extent,lat,end}'::text[]))::double precision, '[]'::text), agdc.float8range(((metadata #>> '{extent,lon,begin}'::text[]))::double precision, ((metadata #>> '{extent,lon,end}'::text[]))::double precision, '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{properties,dtr:start_datetime}'::text[])), agdc.common_timestamp((metadata #>> '{properties,datetime}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{properties,dtr:end_datetime}'::text[])), agdc.common_timestamp((metadata #>> '{properties,datetime}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 21));
 ;   DROP INDEX agdc.dix_cemp_insar_alos_velocity_lat_lon_time;
       agdc      
   agdc_admin    false    201    201    201    280    201            t           1259    2903778 (   dix_cemp_insar_alos_velocity_region_code    INDEX     �   CREATE INDEX dix_cemp_insar_alos_velocity_region_code ON agdc.dataset USING btree (((metadata #>> '{properties,odc:region_code}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 21));
 :   DROP INDEX agdc.dix_cemp_insar_alos_velocity_region_code;
       agdc      
   agdc_admin    false    201    201    201    201            u           1259    2903777 )   dix_cemp_insar_alos_velocity_time_lat_lon    INDEX       CREATE INDEX dix_cemp_insar_alos_velocity_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{properties,dtr:start_datetime}'::text[])), agdc.common_timestamp((metadata #>> '{properties,datetime}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{properties,dtr:end_datetime}'::text[])), agdc.common_timestamp((metadata #>> '{properties,datetime}'::text[]))), '[]'::text), agdc.float8range(((metadata #>> '{extent,lat,begin}'::text[]))::double precision, ((metadata #>> '{extent,lat,end}'::text[]))::double precision, '[]'::text), agdc.float8range(((metadata #>> '{extent,lon,begin}'::text[]))::double precision, ((metadata #>> '{extent,lon,end}'::text[]))::double precision, '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 21));
 ;   DROP INDEX agdc.dix_cemp_insar_alos_velocity_time_lat_lon;
       agdc      
   agdc_admin    false    201    280    201    201    201            v           1259    2903784 0   dix_cemp_insar_envisat_displacement_lat_lon_time    INDEX     $  CREATE INDEX dix_cemp_insar_envisat_displacement_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(((metadata #>> '{extent,lat,begin}'::text[]))::double precision, ((metadata #>> '{extent,lat,end}'::text[]))::double precision, '[]'::text), agdc.float8range(((metadata #>> '{extent,lon,begin}'::text[]))::double precision, ((metadata #>> '{extent,lon,end}'::text[]))::double precision, '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{properties,dtr:start_datetime}'::text[])), agdc.common_timestamp((metadata #>> '{properties,datetime}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{properties,dtr:end_datetime}'::text[])), agdc.common_timestamp((metadata #>> '{properties,datetime}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 22));
 B   DROP INDEX agdc.dix_cemp_insar_envisat_displacement_lat_lon_time;
       agdc      
   agdc_admin    false    280    201    201    201    201            w           1259    2903786 /   dix_cemp_insar_envisat_displacement_region_code    INDEX     �   CREATE INDEX dix_cemp_insar_envisat_displacement_region_code ON agdc.dataset USING btree (((metadata #>> '{properties,odc:region_code}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 22));
 A   DROP INDEX agdc.dix_cemp_insar_envisat_displacement_region_code;
       agdc      
   agdc_admin    false    201    201    201    201            x           1259    2903785 0   dix_cemp_insar_envisat_displacement_time_lat_lon    INDEX     $  CREATE INDEX dix_cemp_insar_envisat_displacement_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{properties,dtr:start_datetime}'::text[])), agdc.common_timestamp((metadata #>> '{properties,datetime}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{properties,dtr:end_datetime}'::text[])), agdc.common_timestamp((metadata #>> '{properties,datetime}'::text[]))), '[]'::text), agdc.float8range(((metadata #>> '{extent,lat,begin}'::text[]))::double precision, ((metadata #>> '{extent,lat,end}'::text[]))::double precision, '[]'::text), agdc.float8range(((metadata #>> '{extent,lon,begin}'::text[]))::double precision, ((metadata #>> '{extent,lon,end}'::text[]))::double precision, '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 22));
 B   DROP INDEX agdc.dix_cemp_insar_envisat_displacement_time_lat_lon;
       agdc      
   agdc_admin    false    201    201    201    201    280            y           1259    2903792 ,   dix_cemp_insar_envisat_velocity_lat_lon_time    INDEX        CREATE INDEX dix_cemp_insar_envisat_velocity_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(((metadata #>> '{extent,lat,begin}'::text[]))::double precision, ((metadata #>> '{extent,lat,end}'::text[]))::double precision, '[]'::text), agdc.float8range(((metadata #>> '{extent,lon,begin}'::text[]))::double precision, ((metadata #>> '{extent,lon,end}'::text[]))::double precision, '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{properties,dtr:start_datetime}'::text[])), agdc.common_timestamp((metadata #>> '{properties,datetime}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{properties,dtr:end_datetime}'::text[])), agdc.common_timestamp((metadata #>> '{properties,datetime}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 23));
 >   DROP INDEX agdc.dix_cemp_insar_envisat_velocity_lat_lon_time;
       agdc      
   agdc_admin    false    201    201    201    280    201            z           1259    2903794 +   dix_cemp_insar_envisat_velocity_region_code    INDEX     �   CREATE INDEX dix_cemp_insar_envisat_velocity_region_code ON agdc.dataset USING btree (((metadata #>> '{properties,odc:region_code}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 23));
 =   DROP INDEX agdc.dix_cemp_insar_envisat_velocity_region_code;
       agdc      
   agdc_admin    false    201    201    201    201            {           1259    2903793 ,   dix_cemp_insar_envisat_velocity_time_lat_lon    INDEX        CREATE INDEX dix_cemp_insar_envisat_velocity_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{properties,dtr:start_datetime}'::text[])), agdc.common_timestamp((metadata #>> '{properties,datetime}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{properties,dtr:end_datetime}'::text[])), agdc.common_timestamp((metadata #>> '{properties,datetime}'::text[]))), '[]'::text), agdc.float8range(((metadata #>> '{extent,lat,begin}'::text[]))::double precision, ((metadata #>> '{extent,lat,end}'::text[]))::double precision, '[]'::text), agdc.float8range(((metadata #>> '{extent,lon,begin}'::text[]))::double precision, ((metadata #>> '{extent,lon,end}'::text[]))::double precision, '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 23));
 >   DROP INDEX agdc.dix_cemp_insar_envisat_velocity_time_lat_lon;
       agdc      
   agdc_admin    false    201    201    280    201    201            |           1259    2903800 2   dix_cemp_insar_radarsat2_displacement_lat_lon_time    INDEX     &  CREATE INDEX dix_cemp_insar_radarsat2_displacement_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(((metadata #>> '{extent,lat,begin}'::text[]))::double precision, ((metadata #>> '{extent,lat,end}'::text[]))::double precision, '[]'::text), agdc.float8range(((metadata #>> '{extent,lon,begin}'::text[]))::double precision, ((metadata #>> '{extent,lon,end}'::text[]))::double precision, '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{properties,dtr:start_datetime}'::text[])), agdc.common_timestamp((metadata #>> '{properties,datetime}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{properties,dtr:end_datetime}'::text[])), agdc.common_timestamp((metadata #>> '{properties,datetime}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 24));
 D   DROP INDEX agdc.dix_cemp_insar_radarsat2_displacement_lat_lon_time;
       agdc      
   agdc_admin    false    201    280    201    201    201            }           1259    2903802 1   dix_cemp_insar_radarsat2_displacement_region_code    INDEX     �   CREATE INDEX dix_cemp_insar_radarsat2_displacement_region_code ON agdc.dataset USING btree (((metadata #>> '{properties,odc:region_code}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 24));
 C   DROP INDEX agdc.dix_cemp_insar_radarsat2_displacement_region_code;
       agdc      
   agdc_admin    false    201    201    201    201            ~           1259    2903801 2   dix_cemp_insar_radarsat2_displacement_time_lat_lon    INDEX     &  CREATE INDEX dix_cemp_insar_radarsat2_displacement_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{properties,dtr:start_datetime}'::text[])), agdc.common_timestamp((metadata #>> '{properties,datetime}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{properties,dtr:end_datetime}'::text[])), agdc.common_timestamp((metadata #>> '{properties,datetime}'::text[]))), '[]'::text), agdc.float8range(((metadata #>> '{extent,lat,begin}'::text[]))::double precision, ((metadata #>> '{extent,lat,end}'::text[]))::double precision, '[]'::text), agdc.float8range(((metadata #>> '{extent,lon,begin}'::text[]))::double precision, ((metadata #>> '{extent,lon,end}'::text[]))::double precision, '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 24));
 D   DROP INDEX agdc.dix_cemp_insar_radarsat2_displacement_time_lat_lon;
       agdc      
   agdc_admin    false    201    201    280    201    201                       1259    2903808 .   dix_cemp_insar_radarsat2_velocity_lat_lon_time    INDEX     "  CREATE INDEX dix_cemp_insar_radarsat2_velocity_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(((metadata #>> '{extent,lat,begin}'::text[]))::double precision, ((metadata #>> '{extent,lat,end}'::text[]))::double precision, '[]'::text), agdc.float8range(((metadata #>> '{extent,lon,begin}'::text[]))::double precision, ((metadata #>> '{extent,lon,end}'::text[]))::double precision, '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{properties,dtr:start_datetime}'::text[])), agdc.common_timestamp((metadata #>> '{properties,datetime}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{properties,dtr:end_datetime}'::text[])), agdc.common_timestamp((metadata #>> '{properties,datetime}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 25));
 @   DROP INDEX agdc.dix_cemp_insar_radarsat2_velocity_lat_lon_time;
       agdc      
   agdc_admin    false    201    280    201    201    201            �           1259    2903810 -   dix_cemp_insar_radarsat2_velocity_region_code    INDEX     �   CREATE INDEX dix_cemp_insar_radarsat2_velocity_region_code ON agdc.dataset USING btree (((metadata #>> '{properties,odc:region_code}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 25));
 ?   DROP INDEX agdc.dix_cemp_insar_radarsat2_velocity_region_code;
       agdc      
   agdc_admin    false    201    201    201    201            �           1259    2903809 .   dix_cemp_insar_radarsat2_velocity_time_lat_lon    INDEX     "  CREATE INDEX dix_cemp_insar_radarsat2_velocity_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{properties,dtr:start_datetime}'::text[])), agdc.common_timestamp((metadata #>> '{properties,datetime}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{properties,dtr:end_datetime}'::text[])), agdc.common_timestamp((metadata #>> '{properties,datetime}'::text[]))), '[]'::text), agdc.float8range(((metadata #>> '{extent,lat,begin}'::text[]))::double precision, ((metadata #>> '{extent,lat,end}'::text[]))::double precision, '[]'::text), agdc.float8range(((metadata #>> '{extent,lon,begin}'::text[]))::double precision, ((metadata #>> '{extent,lon,end}'::text[]))::double precision, '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 25));
 @   DROP INDEX agdc.dix_cemp_insar_radarsat2_velocity_time_lat_lon;
       agdc      
   agdc_admin    false    280    201    201    201    201            �           1259    2903816 ,   dix_fc_percentile_albers_annual_lat_lon_time    INDEX     ^  CREATE INDEX dix_fc_percentile_albers_annual_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 26));
 >   DROP INDEX agdc.dix_fc_percentile_albers_annual_lat_lon_time;
       agdc      
   agdc_admin    false    201    201    201    280    201            �           1259    2903817 ,   dix_fc_percentile_albers_annual_time_lat_lon    INDEX     ^  CREATE INDEX dix_fc_percentile_albers_annual_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 26));
 >   DROP INDEX agdc.dix_fc_percentile_albers_annual_time_lat_lon;
       agdc      
   agdc_admin    false    201    201    201    201    280            �           1259    2903823 .   dix_fc_percentile_albers_seasonal_lat_lon_time    INDEX     `  CREATE INDEX dix_fc_percentile_albers_seasonal_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 27));
 @   DROP INDEX agdc.dix_fc_percentile_albers_seasonal_lat_lon_time;
       agdc      
   agdc_admin    false    201    201    201    280    201            �           1259    2903824 .   dix_fc_percentile_albers_seasonal_time_lat_lon    INDEX     `  CREATE INDEX dix_fc_percentile_albers_seasonal_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 27));
 @   DROP INDEX agdc.dix_fc_percentile_albers_seasonal_time_lat_lon;
       agdc      
   agdc_admin    false    201    201    201    280    201            �           1259    2904119    dix_ga_ls8c_ard_3_cloud_cover    INDEX     �   CREATE INDEX dix_ga_ls8c_ard_3_cloud_cover ON agdc.dataset USING btree ((((metadata #>> '{properties,eo:cloud_cover}'::text[]))::double precision)) WHERE ((archived IS NULL) AND (dataset_type_ref = 61));
 /   DROP INDEX agdc.dix_ga_ls8c_ard_3_cloud_cover;
       agdc      
   agdc_admin    false    201    201    201    201            �           1259    2904121 "   dix_ga_ls8c_ard_3_dataset_maturity    INDEX     �   CREATE INDEX dix_ga_ls8c_ard_3_dataset_maturity ON agdc.dataset USING btree (((metadata #>> '{properties,dea:dataset_maturity}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 61));
 4   DROP INDEX agdc.dix_ga_ls8c_ard_3_dataset_maturity;
       agdc      
   agdc_admin    false    201    201    201    201            �           1259    2904118    dix_ga_ls8c_ard_3_gqa    INDEX     �   CREATE INDEX dix_ga_ls8c_ard_3_gqa ON agdc.dataset USING btree ((((metadata #>> '{properties,gqa:cep90}'::text[]))::double precision)) WHERE ((archived IS NULL) AND (dataset_type_ref = 61));
 '   DROP INDEX agdc.dix_ga_ls8c_ard_3_gqa;
       agdc      
   agdc_admin    false    201    201    201    201            �           1259    2904116    dix_ga_ls8c_ard_3_lat_lon_time    INDEX       CREATE INDEX dix_ga_ls8c_ard_3_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(((metadata #>> '{extent,lat,begin}'::text[]))::double precision, ((metadata #>> '{extent,lat,end}'::text[]))::double precision, '[]'::text), agdc.float8range(((metadata #>> '{extent,lon,begin}'::text[]))::double precision, ((metadata #>> '{extent,lon,end}'::text[]))::double precision, '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{properties,dtr:start_datetime}'::text[])), agdc.common_timestamp((metadata #>> '{properties,datetime}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{properties,dtr:end_datetime}'::text[])), agdc.common_timestamp((metadata #>> '{properties,datetime}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 61));
 0   DROP INDEX agdc.dix_ga_ls8c_ard_3_lat_lon_time;
       agdc      
   agdc_admin    false    280    201    201    201    201            �           1259    2904120    dix_ga_ls8c_ard_3_region_code    INDEX     �   CREATE INDEX dix_ga_ls8c_ard_3_region_code ON agdc.dataset USING btree (((metadata #>> '{properties,odc:region_code}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 61));
 /   DROP INDEX agdc.dix_ga_ls8c_ard_3_region_code;
       agdc      
   agdc_admin    false    201    201    201    201            �           1259    2904117    dix_ga_ls8c_ard_3_time_lat_lon    INDEX       CREATE INDEX dix_ga_ls8c_ard_3_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{properties,dtr:start_datetime}'::text[])), agdc.common_timestamp((metadata #>> '{properties,datetime}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{properties,dtr:end_datetime}'::text[])), agdc.common_timestamp((metadata #>> '{properties,datetime}'::text[]))), '[]'::text), agdc.float8range(((metadata #>> '{extent,lat,begin}'::text[]))::double precision, ((metadata #>> '{extent,lat,end}'::text[]))::double precision, '[]'::text), agdc.float8range(((metadata #>> '{extent,lon,begin}'::text[]))::double precision, ((metadata #>> '{extent,lon,end}'::text[]))::double precision, '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 61));
 0   DROP INDEX agdc.dix_ga_ls8c_ard_3_time_lat_lon;
       agdc      
   agdc_admin    false    201    201    201    201    280            �           1259    2904128 (   dix_ga_s2a_ard_nbar_granule_lat_lon_time    INDEX     �  CREATE INDEX dix_ga_s2a_ard_nbar_granule_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 62));
 :   DROP INDEX agdc.dix_ga_s2a_ard_nbar_granule_lat_lon_time;
       agdc      
   agdc_admin    false    201    280    201    201    201            �           1259    2904130 '   dix_ga_s2a_ard_nbar_granule_region_code    INDEX     �   CREATE INDEX dix_ga_s2a_ard_nbar_granule_region_code ON agdc.dataset USING btree (((metadata #>> '{provider,reference_code}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 62));
 9   DROP INDEX agdc.dix_ga_s2a_ard_nbar_granule_region_code;
       agdc      
   agdc_admin    false    201    201    201    201            �           1259    2904129 (   dix_ga_s2a_ard_nbar_granule_time_lat_lon    INDEX     �  CREATE INDEX dix_ga_s2a_ard_nbar_granule_time_lat_lon ON agdc.dataset USING gist (tstzrange(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 62));
 :   DROP INDEX agdc.dix_ga_s2a_ard_nbar_granule_time_lat_lon;
       agdc      
   agdc_admin    false    201    201    280    201    201            �           1259    2904137 (   dix_ga_s2b_ard_nbar_granule_lat_lon_time    INDEX     �  CREATE INDEX dix_ga_s2b_ard_nbar_granule_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 63));
 :   DROP INDEX agdc.dix_ga_s2b_ard_nbar_granule_lat_lon_time;
       agdc      
   agdc_admin    false    201    201    280    201    201            �           1259    2904139 '   dix_ga_s2b_ard_nbar_granule_region_code    INDEX     �   CREATE INDEX dix_ga_s2b_ard_nbar_granule_region_code ON agdc.dataset USING btree (((metadata #>> '{provider,reference_code}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 63));
 9   DROP INDEX agdc.dix_ga_s2b_ard_nbar_granule_region_code;
       agdc      
   agdc_admin    false    201    201    201    201            �           1259    2904138 (   dix_ga_s2b_ard_nbar_granule_time_lat_lon    INDEX     �  CREATE INDEX dix_ga_s2b_ard_nbar_granule_time_lat_lon ON agdc.dataset USING gist (tstzrange(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 63));
 :   DROP INDEX agdc.dix_ga_s2b_ard_nbar_granule_time_lat_lon;
       agdc      
   agdc_admin    false    201    280    201    201    201            �           1259    2903832 #   dix_geodata_coast_100k_lat_lon_time    INDEX     U  CREATE INDEX dix_geodata_coast_100k_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 28));
 5   DROP INDEX agdc.dix_geodata_coast_100k_lat_lon_time;
       agdc      
   agdc_admin    false    201    201    201    280    201            �           1259    2903833 #   dix_geodata_coast_100k_time_lat_lon    INDEX     U  CREATE INDEX dix_geodata_coast_100k_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 28));
 5   DROP INDEX agdc.dix_geodata_coast_100k_time_lat_lon;
       agdc      
   agdc_admin    false    201    201    201    280    201            �           1259    2903842 !   dix_high_tide_comp_20p_instrument    INDEX     �   CREATE INDEX dix_high_tide_comp_20p_instrument ON agdc.dataset USING btree (((metadata #>> '{instrument,name}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 29));
 3   DROP INDEX agdc.dix_high_tide_comp_20p_instrument;
       agdc      
   agdc_admin    false    201    201    201    201            �           1259    2903839 #   dix_high_tide_comp_20p_lat_lon_time    INDEX     U  CREATE INDEX dix_high_tide_comp_20p_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 29));
 5   DROP INDEX agdc.dix_high_tide_comp_20p_lat_lon_time;
       agdc      
   agdc_admin    false    201    201    201    280    201            �           1259    2903841    dix_high_tide_comp_20p_platform    INDEX     �   CREATE INDEX dix_high_tide_comp_20p_platform ON agdc.dataset USING btree (((metadata #>> '{platform,code}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 29));
 1   DROP INDEX agdc.dix_high_tide_comp_20p_platform;
       agdc      
   agdc_admin    false    201    201    201    201            �           1259    2903840 #   dix_high_tide_comp_20p_time_lat_lon    INDEX     U  CREATE INDEX dix_high_tide_comp_20p_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 29));
 5   DROP INDEX agdc.dix_high_tide_comp_20p_time_lat_lon;
       agdc      
   agdc_admin    false    280    201    201    201    201            �           1259    2903860 .   dix_historical_airborne_photography_instrument    INDEX     �   CREATE INDEX dix_historical_airborne_photography_instrument ON agdc.dataset USING btree (((metadata #>> '{instrument,name}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 31));
 @   DROP INDEX agdc.dix_historical_airborne_photography_instrument;
       agdc      
   agdc_admin    false    201    201    201    201            �           1259    2903857 0   dix_historical_airborne_photography_lat_lon_time    INDEX     b  CREATE INDEX dix_historical_airborne_photography_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 31));
 B   DROP INDEX agdc.dix_historical_airborne_photography_lat_lon_time;
       agdc      
   agdc_admin    false    280    201    201    201    201            �           1259    2903859 ,   dix_historical_airborne_photography_platform    INDEX     �   CREATE INDEX dix_historical_airborne_photography_platform ON agdc.dataset USING btree (((metadata #>> '{platform,code}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 31));
 >   DROP INDEX agdc.dix_historical_airborne_photography_platform;
       agdc      
   agdc_admin    false    201    201    201    201            �           1259    2903858 0   dix_historical_airborne_photography_time_lat_lon    INDEX     b  CREATE INDEX dix_historical_airborne_photography_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 31));
 B   DROP INDEX agdc.dix_historical_airborne_photography_time_lat_lon;
       agdc      
   agdc_admin    false    201    280    201    201    201            �           1259    2903878    dix_item_v2_conf_instrument    INDEX     �   CREATE INDEX dix_item_v2_conf_instrument ON agdc.dataset USING btree (((metadata #>> '{instrument,name}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 33));
 -   DROP INDEX agdc.dix_item_v2_conf_instrument;
       agdc      
   agdc_admin    false    201    201    201    201            �           1259    2903875    dix_item_v2_conf_lat_lon_time    INDEX     O  CREATE INDEX dix_item_v2_conf_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 33));
 /   DROP INDEX agdc.dix_item_v2_conf_lat_lon_time;
       agdc      
   agdc_admin    false    201    201    201    201    280            �           1259    2903877    dix_item_v2_conf_platform    INDEX     �   CREATE INDEX dix_item_v2_conf_platform ON agdc.dataset USING btree (((metadata #>> '{platform,code}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 33));
 +   DROP INDEX agdc.dix_item_v2_conf_platform;
       agdc      
   agdc_admin    false    201    201    201    201            �           1259    2903876    dix_item_v2_conf_time_lat_lon    INDEX     O  CREATE INDEX dix_item_v2_conf_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 33));
 /   DROP INDEX agdc.dix_item_v2_conf_time_lat_lon;
       agdc      
   agdc_admin    false    201    201    280    201    201            �           1259    2903869    dix_item_v2_instrument    INDEX     �   CREATE INDEX dix_item_v2_instrument ON agdc.dataset USING btree (((metadata #>> '{instrument,name}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 32));
 (   DROP INDEX agdc.dix_item_v2_instrument;
       agdc      
   agdc_admin    false    201    201    201    201            �           1259    2903866    dix_item_v2_lat_lon_time    INDEX     J  CREATE INDEX dix_item_v2_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 32));
 *   DROP INDEX agdc.dix_item_v2_lat_lon_time;
       agdc      
   agdc_admin    false    280    201    201    201    201            �           1259    2903868    dix_item_v2_platform    INDEX     �   CREATE INDEX dix_item_v2_platform ON agdc.dataset USING btree (((metadata #>> '{platform,code}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 32));
 &   DROP INDEX agdc.dix_item_v2_platform;
       agdc      
   agdc_admin    false    201    201    201    201            �           1259    2903867    dix_item_v2_time_lat_lon    INDEX     J  CREATE INDEX dix_item_v2_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 32));
 *   DROP INDEX agdc.dix_item_v2_time_lat_lon;
       agdc      
   agdc_admin    false    201    201    201    280    201            �           1259    2903884 %   dix_landsat_barest_earth_lat_lon_time    INDEX     W  CREATE INDEX dix_landsat_barest_earth_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 34));
 7   DROP INDEX agdc.dix_landsat_barest_earth_lat_lon_time;
       agdc      
   agdc_admin    false    201    201    201    201    280            �           1259    2903885 %   dix_landsat_barest_earth_time_lat_lon    INDEX     W  CREATE INDEX dix_landsat_barest_earth_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 34));
 7   DROP INDEX agdc.dix_landsat_barest_earth_time_lat_lon;
       agdc      
   agdc_admin    false    201    201    201    280    201            �           1259    2903851     dix_low_tide_comp_20p_instrument    INDEX     �   CREATE INDEX dix_low_tide_comp_20p_instrument ON agdc.dataset USING btree (((metadata #>> '{instrument,name}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 30));
 2   DROP INDEX agdc.dix_low_tide_comp_20p_instrument;
       agdc      
   agdc_admin    false    201    201    201    201            �           1259    2903848 "   dix_low_tide_comp_20p_lat_lon_time    INDEX     T  CREATE INDEX dix_low_tide_comp_20p_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 30));
 4   DROP INDEX agdc.dix_low_tide_comp_20p_lat_lon_time;
       agdc      
   agdc_admin    false    201    201    201    201    280            �           1259    2903850    dix_low_tide_comp_20p_platform    INDEX     �   CREATE INDEX dix_low_tide_comp_20p_platform ON agdc.dataset USING btree (((metadata #>> '{platform,code}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 30));
 0   DROP INDEX agdc.dix_low_tide_comp_20p_platform;
       agdc      
   agdc_admin    false    201    201    201    201            �           1259    2903849 "   dix_low_tide_comp_20p_time_lat_lon    INDEX     T  CREATE INDEX dix_low_tide_comp_20p_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 30));
 4   DROP INDEX agdc.dix_low_tide_comp_20p_time_lat_lon;
       agdc      
   agdc_admin    false    201    201    201    280    201            �           1259    2903891    dix_ls5_fc_albers_lat_lon_time    INDEX     P  CREATE INDEX dix_ls5_fc_albers_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 35));
 0   DROP INDEX agdc.dix_ls5_fc_albers_lat_lon_time;
       agdc      
   agdc_admin    false    201    201    201    280    201            �           1259    2903892    dix_ls5_fc_albers_time_lat_lon    INDEX     P  CREATE INDEX dix_ls5_fc_albers_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 35));
 0   DROP INDEX agdc.dix_ls5_fc_albers_time_lat_lon;
       agdc      
   agdc_admin    false    201    201    280    201    201            �           1259    2903601     dix_ls5_level1_usgs_lat_lon_time    INDEX     Q  CREATE INDEX dix_ls5_level1_usgs_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 1));
 2   DROP INDEX agdc.dix_ls5_level1_usgs_lat_lon_time;
       agdc      
   agdc_admin    false    201    201    201    280    201            �           1259    2903602     dix_ls5_level1_usgs_time_lat_lon    INDEX     Q  CREATE INDEX dix_ls5_level1_usgs_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 1));
 2   DROP INDEX agdc.dix_ls5_level1_usgs_time_lat_lon;
       agdc      
   agdc_admin    false    201    201    201    280    201            �           1259    2903912 +   dix_ls5_nbart_geomedian_annual_lat_lon_time    INDEX     ]  CREATE INDEX dix_ls5_nbart_geomedian_annual_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 38));
 =   DROP INDEX agdc.dix_ls5_nbart_geomedian_annual_lat_lon_time;
       agdc      
   agdc_admin    false    201    201    280    201    201            �           1259    2903913 +   dix_ls5_nbart_geomedian_annual_time_lat_lon    INDEX     ]  CREATE INDEX dix_ls5_nbart_geomedian_annual_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 38));
 =   DROP INDEX agdc.dix_ls5_nbart_geomedian_annual_time_lat_lon;
       agdc      
   agdc_admin    false    201    201    201    280    201            �           1259    2903933 &   dix_ls5_nbart_tmad_annual_lat_lon_time    INDEX     X  CREATE INDEX dix_ls5_nbart_tmad_annual_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 41));
 8   DROP INDEX agdc.dix_ls5_nbart_tmad_annual_lat_lon_time;
       agdc      
   agdc_admin    false    201    201    201    280    201            �           1259    2903934 &   dix_ls5_nbart_tmad_annual_time_lat_lon    INDEX     X  CREATE INDEX dix_ls5_nbart_tmad_annual_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 41));
 8   DROP INDEX agdc.dix_ls5_nbart_tmad_annual_time_lat_lon;
       agdc      
   agdc_admin    false    201    201    201    280    201            �           1259    2903941    dix_ls5_usgs_l2c1_lat_lon_time    INDEX     P  CREATE INDEX dix_ls5_usgs_l2c1_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 42));
 0   DROP INDEX agdc.dix_ls5_usgs_l2c1_lat_lon_time;
       agdc      
   agdc_admin    false    201    201    201    280    201            �           1259    2903942    dix_ls5_usgs_l2c1_time_lat_lon    INDEX     P  CREATE INDEX dix_ls5_usgs_l2c1_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 42));
 0   DROP INDEX agdc.dix_ls5_usgs_l2c1_time_lat_lon;
       agdc      
   agdc_admin    false    201    201    201    280    201            �           1259    2903948    dix_ls7_fc_albers_lat_lon_time    INDEX     P  CREATE INDEX dix_ls7_fc_albers_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 43));
 0   DROP INDEX agdc.dix_ls7_fc_albers_lat_lon_time;
       agdc      
   agdc_admin    false    201    201    201    280    201            �           1259    2903949    dix_ls7_fc_albers_time_lat_lon    INDEX     P  CREATE INDEX dix_ls7_fc_albers_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 43));
 0   DROP INDEX agdc.dix_ls7_fc_albers_time_lat_lon;
       agdc      
   agdc_admin    false    201    201    201    280    201            �           1259    2903608     dix_ls7_level1_usgs_lat_lon_time    INDEX     Q  CREATE INDEX dix_ls7_level1_usgs_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 2));
 2   DROP INDEX agdc.dix_ls7_level1_usgs_lat_lon_time;
       agdc      
   agdc_admin    false    280    201    201    201    201            �           1259    2903609     dix_ls7_level1_usgs_time_lat_lon    INDEX     Q  CREATE INDEX dix_ls7_level1_usgs_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 2));
 2   DROP INDEX agdc.dix_ls7_level1_usgs_time_lat_lon;
       agdc      
   agdc_admin    false    201    201    280    201    201            �           1259    2903905 +   dix_ls7_nbart_geomedian_annual_lat_lon_time    INDEX     ]  CREATE INDEX dix_ls7_nbart_geomedian_annual_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 37));
 =   DROP INDEX agdc.dix_ls7_nbart_geomedian_annual_lat_lon_time;
       agdc      
   agdc_admin    false    280    201    201    201    201            �           1259    2903906 +   dix_ls7_nbart_geomedian_annual_time_lat_lon    INDEX     ]  CREATE INDEX dix_ls7_nbart_geomedian_annual_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 37));
 =   DROP INDEX agdc.dix_ls7_nbart_geomedian_annual_time_lat_lon;
       agdc      
   agdc_admin    false    201    201    201    280    201            �           1259    2903926 &   dix_ls7_nbart_tmad_annual_lat_lon_time    INDEX     X  CREATE INDEX dix_ls7_nbart_tmad_annual_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 40));
 8   DROP INDEX agdc.dix_ls7_nbart_tmad_annual_lat_lon_time;
       agdc      
   agdc_admin    false    201    201    280    201    201            �           1259    2903927 &   dix_ls7_nbart_tmad_annual_time_lat_lon    INDEX     X  CREATE INDEX dix_ls7_nbart_tmad_annual_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 40));
 8   DROP INDEX agdc.dix_ls7_nbart_tmad_annual_time_lat_lon;
       agdc      
   agdc_admin    false    201    201    280    201    201            �           1259    2903956    dix_ls7_usgs_l2c1_lat_lon_time    INDEX     P  CREATE INDEX dix_ls7_usgs_l2c1_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 44));
 0   DROP INDEX agdc.dix_ls7_usgs_l2c1_lat_lon_time;
       agdc      
   agdc_admin    false    201    201    201    280    201            �           1259    2903957    dix_ls7_usgs_l2c1_time_lat_lon    INDEX     P  CREATE INDEX dix_ls7_usgs_l2c1_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 44));
 0   DROP INDEX agdc.dix_ls7_usgs_l2c1_time_lat_lon;
       agdc      
   agdc_admin    false    201    201    201    280    201            �           1259    2903963 (   dix_ls8_barest_earth_albers_lat_lon_time    INDEX     Z  CREATE INDEX dix_ls8_barest_earth_albers_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 45));
 :   DROP INDEX agdc.dix_ls8_barest_earth_albers_lat_lon_time;
       agdc      
   agdc_admin    false    201    201    280    201    201            �           1259    2903964 (   dix_ls8_barest_earth_albers_time_lat_lon    INDEX     Z  CREATE INDEX dix_ls8_barest_earth_albers_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 45));
 :   DROP INDEX agdc.dix_ls8_barest_earth_albers_time_lat_lon;
       agdc      
   agdc_admin    false    201    201    280    201    201            �           1259    2903970    dix_ls8_fc_albers_lat_lon_time    INDEX     P  CREATE INDEX dix_ls8_fc_albers_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 46));
 0   DROP INDEX agdc.dix_ls8_fc_albers_lat_lon_time;
       agdc      
   agdc_admin    false    280    201    201    201    201            �           1259    2903971    dix_ls8_fc_albers_time_lat_lon    INDEX     P  CREATE INDEX dix_ls8_fc_albers_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 46));
 0   DROP INDEX agdc.dix_ls8_fc_albers_time_lat_lon;
       agdc      
   agdc_admin    false    201    201    201    280    201            �           1259    2903980    dix_ls8_level1_usgs_instrument    INDEX     �   CREATE INDEX dix_ls8_level1_usgs_instrument ON agdc.dataset USING btree (((metadata #>> '{instrument,name}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 47));
 0   DROP INDEX agdc.dix_ls8_level1_usgs_instrument;
       agdc      
   agdc_admin    false    201    201    201    201            �           1259    2903977     dix_ls8_level1_usgs_lat_lon_time    INDEX     R  CREATE INDEX dix_ls8_level1_usgs_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 47));
 2   DROP INDEX agdc.dix_ls8_level1_usgs_lat_lon_time;
       agdc      
   agdc_admin    false    201    201    201    280    201            �           1259    2903979    dix_ls8_level1_usgs_platform    INDEX     �   CREATE INDEX dix_ls8_level1_usgs_platform ON agdc.dataset USING btree (((metadata #>> '{platform,code}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 47));
 .   DROP INDEX agdc.dix_ls8_level1_usgs_platform;
       agdc      
   agdc_admin    false    201    201    201    201            �           1259    2903978     dix_ls8_level1_usgs_time_lat_lon    INDEX     R  CREATE INDEX dix_ls8_level1_usgs_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 47));
 2   DROP INDEX agdc.dix_ls8_level1_usgs_time_lat_lon;
       agdc      
   agdc_admin    false    201    201    201    280    201            �           1259    2903898 +   dix_ls8_nbart_geomedian_annual_lat_lon_time    INDEX     ]  CREATE INDEX dix_ls8_nbart_geomedian_annual_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 36));
 =   DROP INDEX agdc.dix_ls8_nbart_geomedian_annual_lat_lon_time;
       agdc      
   agdc_admin    false    201    201    201    201    280            �           1259    2903899 +   dix_ls8_nbart_geomedian_annual_time_lat_lon    INDEX     ]  CREATE INDEX dix_ls8_nbart_geomedian_annual_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 36));
 =   DROP INDEX agdc.dix_ls8_nbart_geomedian_annual_time_lat_lon;
       agdc      
   agdc_admin    false    201    280    201    201    201            �           1259    2903919 &   dix_ls8_nbart_tmad_annual_lat_lon_time    INDEX     X  CREATE INDEX dix_ls8_nbart_tmad_annual_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 39));
 8   DROP INDEX agdc.dix_ls8_nbart_tmad_annual_lat_lon_time;
       agdc      
   agdc_admin    false    201    201    201    280    201            �           1259    2903920 &   dix_ls8_nbart_tmad_annual_time_lat_lon    INDEX     X  CREATE INDEX dix_ls8_nbart_tmad_annual_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 39));
 8   DROP INDEX agdc.dix_ls8_nbart_tmad_annual_time_lat_lon;
       agdc      
   agdc_admin    false    201    201    201    201    280            �           1259    2903987    dix_ls8_usgs_l2c1_lat_lon_time    INDEX     P  CREATE INDEX dix_ls8_usgs_l2c1_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 48));
 0   DROP INDEX agdc.dix_ls8_usgs_l2c1_lat_lon_time;
       agdc      
   agdc_admin    false    201    201    280    201    201            �           1259    2903988    dix_ls8_usgs_l2c1_time_lat_lon    INDEX     P  CREATE INDEX dix_ls8_usgs_l2c1_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 48));
 0   DROP INDEX agdc.dix_ls8_usgs_l2c1_time_lat_lon;
       agdc      
   agdc_admin    false    201    201    280    201    201            �           1259    2903994    dix_mangrove_cover_lat_lon_time    INDEX     Q  CREATE INDEX dix_mangrove_cover_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 49));
 1   DROP INDEX agdc.dix_mangrove_cover_lat_lon_time;
       agdc      
   agdc_admin    false    201    201    201    280    201            �           1259    2903995    dix_mangrove_cover_time_lat_lon    INDEX     Q  CREATE INDEX dix_mangrove_cover_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 49));
 1   DROP INDEX agdc.dix_mangrove_cover_time_lat_lon;
       agdc      
   agdc_admin    false    201    280    201    201    201            �           1259    2904004 /   dix_multi_scale_topographic_position_instrument    INDEX     �   CREATE INDEX dix_multi_scale_topographic_position_instrument ON agdc.dataset USING btree (((metadata #>> '{instrument,name}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 50));
 A   DROP INDEX agdc.dix_multi_scale_topographic_position_instrument;
       agdc      
   agdc_admin    false    201    201    201    201            �           1259    2904001 1   dix_multi_scale_topographic_position_lat_lon_time    INDEX     c  CREATE INDEX dix_multi_scale_topographic_position_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 50));
 C   DROP INDEX agdc.dix_multi_scale_topographic_position_lat_lon_time;
       agdc      
   agdc_admin    false    280    201    201    201    201            �           1259    2904003 -   dix_multi_scale_topographic_position_platform    INDEX     �   CREATE INDEX dix_multi_scale_topographic_position_platform ON agdc.dataset USING btree (((metadata #>> '{platform,code}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 50));
 ?   DROP INDEX agdc.dix_multi_scale_topographic_position_platform;
       agdc      
   agdc_admin    false    201    201    201    201            �           1259    2904002 1   dix_multi_scale_topographic_position_time_lat_lon    INDEX     c  CREATE INDEX dix_multi_scale_topographic_position_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 50));
 C   DROP INDEX agdc.dix_multi_scale_topographic_position_time_lat_lon;
       agdc      
   agdc_admin    false    201    201    201    280    201            �           1259    2904013    dix_nidem_instrument    INDEX     �   CREATE INDEX dix_nidem_instrument ON agdc.dataset USING btree (((metadata #>> '{instrument,name}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 51));
 &   DROP INDEX agdc.dix_nidem_instrument;
       agdc      
   agdc_admin    false    201    201    201    201            �           1259    2904010    dix_nidem_lat_lon_time    INDEX     H  CREATE INDEX dix_nidem_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 51));
 (   DROP INDEX agdc.dix_nidem_lat_lon_time;
       agdc      
   agdc_admin    false    201    201    201    201    280            �           1259    2904012    dix_nidem_platform    INDEX     �   CREATE INDEX dix_nidem_platform ON agdc.dataset USING btree (((metadata #>> '{platform,code}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 51));
 $   DROP INDEX agdc.dix_nidem_platform;
       agdc      
   agdc_admin    false    201    201    201    201            �           1259    2904011    dix_nidem_time_lat_lon    INDEX     H  CREATE INDEX dix_nidem_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 51));
 (   DROP INDEX agdc.dix_nidem_time_lat_lon;
       agdc      
   agdc_admin    false    201    201    280    201    201            �           1259    2904161    dix_s2_tsmask_lat_lon_time    INDEX     �  CREATE INDEX dix_s2_tsmask_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 66));
 ,   DROP INDEX agdc.dix_s2_tsmask_lat_lon_time;
       agdc      
   agdc_admin    false    201    201    280    201    201            �           1259    2904163    dix_s2_tsmask_region_code    INDEX     �   CREATE INDEX dix_s2_tsmask_region_code ON agdc.dataset USING btree (((metadata #>> '{provider,reference_code}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 66));
 +   DROP INDEX agdc.dix_s2_tsmask_region_code;
       agdc      
   agdc_admin    false    201    201    201    201            �           1259    2904162    dix_s2_tsmask_time_lat_lon    INDEX     �  CREATE INDEX dix_s2_tsmask_time_lat_lon ON agdc.dataset USING gist (tstzrange(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 66));
 ,   DROP INDEX agdc.dix_s2_tsmask_time_lat_lon;
       agdc      
   agdc_admin    false    201    201    280    201    201            �           1259    2904146     dix_s2a_nrt_granule_lat_lon_time    INDEX     �  CREATE INDEX dix_s2a_nrt_granule_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[])), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 64));
 2   DROP INDEX agdc.dix_s2a_nrt_granule_lat_lon_time;
       agdc      
   agdc_admin    false    201    201    201    280    201            �           1259    2904147     dix_s2a_nrt_granule_time_lat_lon    INDEX     �  CREATE INDEX dix_s2a_nrt_granule_time_lat_lon ON agdc.dataset USING gist (tstzrange(agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[])), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 64));
 2   DROP INDEX agdc.dix_s2a_nrt_granule_time_lat_lon;
       agdc      
   agdc_admin    false    201    201    201    201    280            �           1259    2904154     dix_s2b_nrt_granule_lat_lon_time    INDEX     �  CREATE INDEX dix_s2b_nrt_granule_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[])), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 65));
 2   DROP INDEX agdc.dix_s2b_nrt_granule_lat_lon_time;
       agdc      
   agdc_admin    false    280    201    201    201    201            �           1259    2904155     dix_s2b_nrt_granule_time_lat_lon    INDEX     �  CREATE INDEX dix_s2b_nrt_granule_time_lat_lon ON agdc.dataset USING gist (tstzrange(agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[])), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 65));
 2   DROP INDEX agdc.dix_s2b_nrt_granule_time_lat_lon;
       agdc      
   agdc_admin    false    280    201    201    201    201            �           1259    2904019 #   dix_sentinel2_wofs_nrt_lat_lon_time    INDEX     U  CREATE INDEX dix_sentinel2_wofs_nrt_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 52));
 5   DROP INDEX agdc.dix_sentinel2_wofs_nrt_lat_lon_time;
       agdc      
   agdc_admin    false    280    201    201    201    201            �           1259    2904021    dix_sentinel2_wofs_nrt_platform    INDEX     �   CREATE INDEX dix_sentinel2_wofs_nrt_platform ON agdc.dataset USING btree (((metadata #>> '{platform,code}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 52));
 1   DROP INDEX agdc.dix_sentinel2_wofs_nrt_platform;
       agdc      
   agdc_admin    false    201    201    201    201            �           1259    2904020 #   dix_sentinel2_wofs_nrt_time_lat_lon    INDEX     U  CREATE INDEX dix_sentinel2_wofs_nrt_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 52));
 5   DROP INDEX agdc.dix_sentinel2_wofs_nrt_time_lat_lon;
       agdc      
   agdc_admin    false    280    201    201    201    201            �           1259    2904030    dix_water_bodies_instrument    INDEX     �   CREATE INDEX dix_water_bodies_instrument ON agdc.dataset USING btree (((metadata #>> '{instrument,name}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 53));
 -   DROP INDEX agdc.dix_water_bodies_instrument;
       agdc      
   agdc_admin    false    201    201    201    201            �           1259    2904027    dix_water_bodies_lat_lon_time    INDEX     O  CREATE INDEX dix_water_bodies_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 53));
 /   DROP INDEX agdc.dix_water_bodies_lat_lon_time;
       agdc      
   agdc_admin    false    280    201    201    201    201            �           1259    2904029    dix_water_bodies_platform    INDEX     �   CREATE INDEX dix_water_bodies_platform ON agdc.dataset USING btree (((metadata #>> '{platform,code}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 53));
 +   DROP INDEX agdc.dix_water_bodies_platform;
       agdc      
   agdc_admin    false    201    201    201    201            �           1259    2904028    dix_water_bodies_time_lat_lon    INDEX     O  CREATE INDEX dix_water_bodies_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 53));
 /   DROP INDEX agdc.dix_water_bodies_time_lat_lon;
       agdc      
   agdc_admin    false    201    201    201    280    201            �           1259    2904036 %   dix_weathering_intensity_lat_lon_time    INDEX     W  CREATE INDEX dix_weathering_intensity_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 54));
 7   DROP INDEX agdc.dix_weathering_intensity_lat_lon_time;
       agdc      
   agdc_admin    false    201    201    201    280    201            �           1259    2904037 %   dix_weathering_intensity_time_lat_lon    INDEX     W  CREATE INDEX dix_weathering_intensity_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 54));
 7   DROP INDEX agdc.dix_weathering_intensity_time_lat_lon;
       agdc      
   agdc_admin    false    201    201    280    201    201            �           1259    2904048    dix_wofs_albers_instrument    INDEX     �   CREATE INDEX dix_wofs_albers_instrument ON agdc.dataset USING btree (((metadata #>> '{instrument,name}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 55));
 ,   DROP INDEX agdc.dix_wofs_albers_instrument;
       agdc      
   agdc_admin    false    201    201    201    201            �           1259    2904045    dix_wofs_albers_lat_lon_time    INDEX     N  CREATE INDEX dix_wofs_albers_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 55));
 .   DROP INDEX agdc.dix_wofs_albers_lat_lon_time;
       agdc      
   agdc_admin    false    201    201    201    201    280            �           1259    2904047    dix_wofs_albers_platform    INDEX     �   CREATE INDEX dix_wofs_albers_platform ON agdc.dataset USING btree (((metadata #>> '{platform,code}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 55));
 *   DROP INDEX agdc.dix_wofs_albers_platform;
       agdc      
   agdc_admin    false    201    201    201    201            �           1259    2904046    dix_wofs_albers_time_lat_lon    INDEX     N  CREATE INDEX dix_wofs_albers_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 55));
 .   DROP INDEX agdc.dix_wofs_albers_time_lat_lon;
       agdc      
   agdc_admin    false    201    201    201    280    201            �           1259    2904054 $   dix_wofs_annual_summary_lat_lon_time    INDEX     V  CREATE INDEX dix_wofs_annual_summary_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 56));
 6   DROP INDEX agdc.dix_wofs_annual_summary_lat_lon_time;
       agdc      
   agdc_admin    false    280    201    201    201    201            �           1259    2904055 $   dix_wofs_annual_summary_time_lat_lon    INDEX     V  CREATE INDEX dix_wofs_annual_summary_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 56));
 6   DROP INDEX agdc.dix_wofs_annual_summary_time_lat_lon;
       agdc      
   agdc_admin    false    201    201    201    280    201            �           1259    2904061 %   dix_wofs_apr_oct_summary_lat_lon_time    INDEX     W  CREATE INDEX dix_wofs_apr_oct_summary_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 57));
 7   DROP INDEX agdc.dix_wofs_apr_oct_summary_lat_lon_time;
       agdc      
   agdc_admin    false    280    201    201    201    201            �           1259    2904062 %   dix_wofs_apr_oct_summary_time_lat_lon    INDEX     W  CREATE INDEX dix_wofs_apr_oct_summary_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 57));
 7   DROP INDEX agdc.dix_wofs_apr_oct_summary_time_lat_lon;
       agdc      
   agdc_admin    false    201    280    201    201    201            �           1259    2904068 &   dix_wofs_filtered_summary_lat_lon_time    INDEX     X  CREATE INDEX dix_wofs_filtered_summary_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 58));
 8   DROP INDEX agdc.dix_wofs_filtered_summary_lat_lon_time;
       agdc      
   agdc_admin    false    280    201    201    201    201            �           1259    2904069 &   dix_wofs_filtered_summary_time_lat_lon    INDEX     X  CREATE INDEX dix_wofs_filtered_summary_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 58));
 8   DROP INDEX agdc.dix_wofs_filtered_summary_time_lat_lon;
       agdc      
   agdc_admin    false    201    201    280    201    201            �           1259    2904075 %   dix_wofs_nov_mar_summary_lat_lon_time    INDEX     W  CREATE INDEX dix_wofs_nov_mar_summary_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 59));
 7   DROP INDEX agdc.dix_wofs_nov_mar_summary_lat_lon_time;
       agdc      
   agdc_admin    false    201    201    201    280    201            �           1259    2904076 %   dix_wofs_nov_mar_summary_time_lat_lon    INDEX     W  CREATE INDEX dix_wofs_nov_mar_summary_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 59));
 7   DROP INDEX agdc.dix_wofs_nov_mar_summary_time_lat_lon;
       agdc      
   agdc_admin    false    201    201    201    280    201            �           1259    2904082    dix_wofs_summary_lat_lon_time    INDEX     O  CREATE INDEX dix_wofs_summary_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 60));
 /   DROP INDEX agdc.dix_wofs_summary_lat_lon_time;
       agdc      
   agdc_admin    false    201    201    201    201    280            �           1259    2904083    dix_wofs_summary_time_lat_lon    INDEX     O  CREATE INDEX dix_wofs_summary_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 60));
 /   DROP INDEX agdc.dix_wofs_summary_time_lat_lon;
       agdc      
   agdc_admin    false    201    201    201    280    201            �           1259    2903524     ix_agdc_dataset_dataset_type_ref    INDEX     ^   CREATE INDEX ix_agdc_dataset_dataset_type_ref ON agdc.dataset USING btree (dataset_type_ref);
 2   DROP INDEX agdc.ix_agdc_dataset_dataset_type_ref;
       agdc      
   agdc_admin    false    201            �           1259    2903545 $   ix_agdc_dataset_location_dataset_ref    INDEX     f   CREATE INDEX ix_agdc_dataset_location_dataset_ref ON agdc.dataset_location USING btree (dataset_ref);
 6   DROP INDEX agdc.ix_agdc_dataset_location_dataset_ref;
       agdc      
   agdc_admin    false    203                       2620    2903569    dataset row_update_time_dataset    TRIGGER     �   CREATE TRIGGER row_update_time_dataset BEFORE UPDATE ON agdc.dataset FOR EACH ROW EXECUTE PROCEDURE agdc.set_row_update_time();
 6   DROP TRIGGER row_update_time_dataset ON agdc.dataset;
       agdc    
   agdc_admin    false    279    201                       2620    2903568 )   dataset_type row_update_time_dataset_type    TRIGGER     �   CREATE TRIGGER row_update_time_dataset_type BEFORE UPDATE ON agdc.dataset_type FOR EACH ROW EXECUTE PROCEDURE agdc.set_row_update_time();
 @   DROP TRIGGER row_update_time_dataset_type ON agdc.dataset_type;
       agdc    
   agdc_admin    false    200    279                       2620    2903567 +   metadata_type row_update_time_metadata_type    TRIGGER     �   CREATE TRIGGER row_update_time_metadata_type BEFORE UPDATE ON agdc.metadata_type FOR EACH ROW EXECUTE PROCEDURE agdc.set_row_update_time();
 B   DROP TRIGGER row_update_time_metadata_type ON agdc.metadata_type;
       agdc    
   agdc_admin    false    198    279                       2606    2903519 0   dataset fk_dataset_dataset_type_ref_dataset_type    FK CONSTRAINT     �   ALTER TABLE ONLY agdc.dataset
    ADD CONSTRAINT fk_dataset_dataset_type_ref_dataset_type FOREIGN KEY (dataset_type_ref) REFERENCES agdc.dataset_type(id);
 X   ALTER TABLE ONLY agdc.dataset DROP CONSTRAINT fk_dataset_dataset_type_ref_dataset_type;
       agdc    
   agdc_admin    false    200    3113    201                       2606    2903540 8   dataset_location fk_dataset_location_dataset_ref_dataset    FK CONSTRAINT     �   ALTER TABLE ONLY agdc.dataset_location
    ADD CONSTRAINT fk_dataset_location_dataset_ref_dataset FOREIGN KEY (dataset_ref) REFERENCES agdc.dataset(id);
 `   ALTER TABLE ONLY agdc.dataset_location DROP CONSTRAINT fk_dataset_location_dataset_ref_dataset;
       agdc    
   agdc_admin    false    203    3318    201                       2606    2903514 2   dataset fk_dataset_metadata_type_ref_metadata_type    FK CONSTRAINT     �   ALTER TABLE ONLY agdc.dataset
    ADD CONSTRAINT fk_dataset_metadata_type_ref_metadata_type FOREIGN KEY (metadata_type_ref) REFERENCES agdc.metadata_type(id);
 Z   ALTER TABLE ONLY agdc.dataset DROP CONSTRAINT fk_dataset_metadata_type_ref_metadata_type;
       agdc    
   agdc_admin    false    201    3109    198                       2606    2903556 4   dataset_source fk_dataset_source_dataset_ref_dataset    FK CONSTRAINT     �   ALTER TABLE ONLY agdc.dataset_source
    ADD CONSTRAINT fk_dataset_source_dataset_ref_dataset FOREIGN KEY (dataset_ref) REFERENCES agdc.dataset(id);
 \   ALTER TABLE ONLY agdc.dataset_source DROP CONSTRAINT fk_dataset_source_dataset_ref_dataset;
       agdc    
   agdc_admin    false    3318    204    201                       2606    2903561 ;   dataset_source fk_dataset_source_source_dataset_ref_dataset    FK CONSTRAINT     �   ALTER TABLE ONLY agdc.dataset_source
    ADD CONSTRAINT fk_dataset_source_source_dataset_ref_dataset FOREIGN KEY (source_dataset_ref) REFERENCES agdc.dataset(id);
 c   ALTER TABLE ONLY agdc.dataset_source DROP CONSTRAINT fk_dataset_source_source_dataset_ref_dataset;
       agdc    
   agdc_admin    false    204    201    3318                        2606    2903499 <   dataset_type fk_dataset_type_metadata_type_ref_metadata_type    FK CONSTRAINT     �   ALTER TABLE ONLY agdc.dataset_type
    ADD CONSTRAINT fk_dataset_type_metadata_type_ref_metadata_type FOREIGN KEY (metadata_type_ref) REFERENCES agdc.metadata_type(id);
 d   ALTER TABLE ONLY agdc.dataset_type DROP CONSTRAINT fk_dataset_type_metadata_type_ref_metadata_type;
       agdc    
   agdc_admin    false    3109    200    198            �      x������ � �      �      x������ � �      �      x������ � �      �      x��ms$�q.���WL0�R���R�%�f�D�Z�7N�*���XX��	��[���3���b|���]�ݕOefeee�7��b���BN_�|y���������g��j�?�<{�_>����g�_|��_O6��8��Kp�ӫg��w}��'}v�q����������}*���\_={���������韞����ɯ�ÿ~>X[<܇�����ٳ��3P�qu\�l{��������%Ο]>�9���^���>�F6�����>Ջ��_�ɣ�>��{�����[���h��|~�r�W<�[�_�J�_^^���E���bg<��o�pvq~v��?�s��@����;|y��^>�-�^f���q�}�0w�z�Rۧy~�0�.����|s~-s������s�����ϗ���o�u�������~��g�[�qr߿�8��������AƆ�kW/����F�?�^��ـ�~_��g7���6cn��_�N\_�x�}v�����{���H��n� �z����7��O��O�.�ػ��mY����O�n7���n���_�r��������_>����/�_~uLt<7��O�n��������r|��������7����(�_����9��bzT�/�n3���j�?��H����Ͽ�<�]����~�{�7�?݌���ݞ��F	oHG���{�{7�'���v!��P�g�r��ٳ�;��'��C������������P���OO��zy}6G��X8��c/vyu���#��|��(�w�_�������n��n��'�����*��W㭞�]~�Qav��~{6��N���׿�y���y{�����"��lB��R~���ے��僳/���>��>��0z�=�u���oc�����y�g}��Sߛ=�͞�f�{������yo��XfOΏ�ˇR�͞����`�����W�_^_�|1����ثm�O~�ۣV��X4���͛�{��l���g���V�?Mb���Co�{�(����U�o���+��cX�����1��v�ǃ0����v��3���y3�?��[����d��x�!�ߖe�4�2k�a��-z�5��i��x�`7
~�C󟦝��7�v��7���\��K͵�}�����d�]J��w��������xƅ�=�%h�:w�v��C�!���轂�����X��G�y34=n%���ڎ3���]Zo����������>��}��W/oNϯ�.��O�/O�y�ջ0�U4_��W6x0ƾ��~�n�k�+re9����g��z���ws�.{x��?k���qi��ٚ��[~z�ʏ��F1�G{Po��?�]4�1�}�Ov�t���/�כ_|��_����˳�oo�o6ܞ=�v��.��<��<ݚ���H��>5���N!�@M2����i�����	x�����{N6�d�M=��yvv��ͳ���v�����2�|�2_�������f�/t������U��<�.��x���o��x=Ǝ�����|L�o�_ݜ^�8{z_'�1W��ٟ�<���x��m��?/�Oo��.�v��yq5��z<vߏe�<��c�?
��b�����;�jv��d�Į$��;;�4i�j���X�t�F�&P���w�ׅ�p>Ǝ�iɸK��9��-�XJA��pY����3�R숇�1�QM�~�v�Z7�-�X��Ѝ֬���=[Xx̸�E���ߒ�H�v�a3�J����}���Rо��s�c��!6;6kc�c�v����n�ɮ/��^��_�ѯ��Z��f��ǋ��Xڛ�b���>Yc��=�Q0"dxb�ѭo[1�`��sF��25�c�X��<� 4Ce"o�4�р ��/�<�u��b�����9��9K��/)��aSY{�7tvY�X
�5{�1�ǔP�eK�Pl��8s`g�I��89|�����������ۯT�$g��q�����IY�t�&�I;'鳤�-�)h�J�.��"3�%eo
�"j흤]��CR�
���')Z�r1%m�8�HHI[$m���J��#/)^S�Y[dm�/����.H�,�vJ������"$m��H��he��Tj$EHR����S�*�0^R�U[�HU[(6��=���~h��-Tz$�s��Tl&EcRh��-���ᓺ�Pn��-T>%�PR||I�K^����C��"&���:��ʜ��>+ϳ�<+ϳ�<+ϳ�<+ϳ�<+ϳ�<+ϳ�<+ϳ��6+�!���<+ϳ�<+ϳ��%+ϳ�<+ϳ�<+ϳ�<+ϳ�<+ϳ�<+ϳ�<+ϳ�<+�!���<+ϳ�<���}��c��ý��T�TzK����B9��y�҃�?�q�a?Gʬ�(s�4�q�4��{��$Py�C��1�B�S��<9���)Ƹ1Q��"6-���S����0(�%WS�5��fA]ĕ���(&ړY�dX-��j���ue���C^�l
�ʔr�Q�5-�Y��7���,�V�]W�)���Ք�֍\'K�b]�����l^n�ޗ��*�*6�L���yLu�5�P��1�K�%`�S��'�t�;T>T3~�V��F����2��1u���v��'��?Q݋a��n������hgK������L����J��l�E���h.6�����b� .4&���N-�8��b��@��mjT�T���D�]��Q���J��~/�!��C[h�f����&kwf����;��Ί���;��l �`V͝�Yќ��Y5wV0gex�A�u�e��Y����SV��Usg��YE'����;+볎���Q���Y57Q	ђu�e`V�u�fEy^��Ey^��Ey^��Ey�(ϋ�(ϋ�(ϋ�(ϋ���(ϋ�(ϋ�(ϋ��}Q�C��yQ��yQ��9�CQ^�[�ˁ~}ظ>j�x���OQ+%��X9D9��ʕ
��+F��%�Ԗb�cL]�m�����''	Vg�6҇�M`������c��>��#�o���.5�>Ө�3���L|�|h�=��e��K�v�����Tnmqil�uJ|�	:��댓3�U�Q]eWsl�ڎ���£�~(kl�>&��<	�'��Z�d��^�����1�伓�ݮ䧾�&��+p�Ǥ֞���s��3_-��]g=���Pav4�Z��ls�d�4��[�\��.�z��[ݝ���:����vY��9�zN%�}é� ��ח)��*o��v4�=Eu�� �1EuLQh�1�K�B��(��v��*�
�E�RQ��1EuLю-�c��(���XT�eq�!^T��1E;�(��vn�WOp$�1E�DQSt�eRQASE�VQS��`}Q~��:��(�V\E!U��Eu\UE�Z��1EuLQ�ST��f���������*/�ꘪ`�*��ª���_���|�ʣ����P�?l�5~���w�>��C�Ce̳l������ȑ��ۑ^�r��F�6)ƀ��h�A܎��&tV;�3�l�>�3�H/c4q+����.Qڏ�i�@W��1m�L��>_��R�Sj7��4�J[3���D�D�K�K�KaJqW��G�];�d�ϯsN�v}|�o�I�S�$��Υz�yGr�K�T��R�
��K�*s
�^O�Z���:�GNf���N�<F��&������G���~���|i>��dA?��ң����sp�.���5�9�
1d�����Oǎ��J"��hn^p���<��f��iu4��4�[�f`K�=��귡U�.yNK[��á�9�'��g�U#������ؤ�q����G��L�����6'�6�+�5q� vZn����JQQ��ʳ!My������1�;�ݎ�FN�ԅ+.R��Ri(Dw#�;��L��ȣԻ&����&(����jC�U���k�Y]BTU�!k��*�
BՇ���U߶�*�:���\F�VU�U;�f�?TqUn�1UUUZ.U%OU�@tW~�`.�J���,����h�ړ�T�lU�
���*m: `�7U� ~SV�jl�������zŘh*��є!>MLSLb����T��t�7MD���h�,��	�{Sa|a�@s4U�/��U�    ��o�K8���Ǧ�D����HS�Ҕ�Myޔ�gp�4�9dCS�c8c��)ϛ���)�a���Ҕ�My�ߔ�My9Д�MyS3��<��<DMyޔ�Myޔ�My��)��dj�sh��<��k��<o�s���ڬ)ϛ�+�!��+ϻ�n=�r੃ߴ+ϻ�KH]y�V���+��וoX�ʏ1���yf&W�����,L)2����E(�O/�Rl4�s�Do���y6��^�u^2�i��UF��D�v39���PMyE*�ȉ\�>Ht��dVG�p�Y���\�S�p�6��2�V�g�<�sE��{��M>�]h�p�+��[����ng��^bz�{���҆��W�>紜���k�</nܱ�t���;�i����e>u�>�&u�o�'��������xj�%sڻ���ӽ�+��9���i�v2�gwk�H;�o;=n�����᝖�[i�{�V͟^I�����4�/_̗�3}�KdZ�����L�eڌ�Vr��qk?�F��\:h�6]��ĥ����+�4������ �|t�@�D|��(0� DN�8x��%_����6yN:���X��-�%q��;�zC~Q0qr�$
2_}G<!7���.��P�;t��g.��L�,8�4��\�8�}'��\so��.��䊀��'�z<�O���-�r`"�n䂠Wnm�K[����nl�[�x}��e-pW\�w��E-pO\����E$�	�B���$�	�@Y%���'��<>�")/���xw��WG���T��8p���F��Ԃɢ�Q#p�4��1#p�2g� i�&��.����"��,e#�|+��gg����R �n�r� �G0���k�+��k��
\�2�8�p�ר�P�a��.0����(�x�1.0�F�� ��[�M�@
�@�	l�qm~�Q-0�ƴ���Z`<g��,0�I`(�b��ػV`�
lM��8&ه~��\ofT� �x�G;����:�N��VT8rp��r��M��?�O_11i�i_��2���6��&����0�LG�-\[�ՒL:ӕ�iE�qs�i΄j�(ڹ B^�c��y��0�
WFd�J�o:5��� .��:��g��������?SW�)Z��b$w~؏��.����҇Q���Pw	;E;e�Wޚ?�ֻ��s��_&;��J�=�i��{���)e�d�{Oz��E�Yi���׌!�~d�o�ϑ#=<�è�y��#;�����0�맯_yh�}ځ��+����#��&��4��۵��C��tS��v;�R~�Xw����~Qw�7��K8�X���N���; h���cPl�
�	��aKn�,`I1d��^}lj{Ғ�����qrɹ�I36����]c/,j��� Z�3�������*�PPx̈l��g#�F���A!�~��	g�&��8�A!�B�����-8[@��B�
��+�V�m8�p��l���;�w��8�J2zj#`>>>>���
�
�
΢��D�m������ـ�g#΢�$�B��	��'�M8�q��������	����-8�ޓ
*�WЯ8[q��l�Y������;�w��8�q��� �!p! b(`i9�^@�a �C�P�:,a,��OP@�a�O������:��}�^@��^ 개0>q6�YP@��^@��. u�@]@��^@��^@�@] �P�:�X�W' �1�i�k����8��C$a�<�f	���{�����	
轈ދ轈ދ�=L�C�"z�y���{��{��=D�,E��0��"z�͐�p����	�轈ދ�=$�O�E�E�UZ��cY���{����F�V�n.ڞ]��E�7�wn5���h�5*��;ىƉ��'ί�_���<#x���g痛��O/^��N)���˗7�
���������G6G!�տ}tgo������os�����B϶:}�?#�B��
v)&4é��>����+I�v{ys�=��.���~^w��an�3ݝ����A����n���{"���~;�o~�l�Qs��?��#2������_����b�ix��z5&���
�Px7Bq��F(MB���I(��2	�w#T'��������a��n�r(�.d������󳋲蕟�b(�7w�ؔ��a�R����kq�{�������w���v�n|�̃_}ٟ�K����30<00 ���fc�ŕ6�-1�}݃i�
���r�&lz�P��Ix;��"��h(�?�|�v}`���]6׌���P�������b\y�\,t��-�7�HG7�V��
��h.���P�ŽTt0-���p����a#v�qQ��-5��chj�N��0�ƀ�F�4�[H��Ѧ����6ѝ*��w#͸_�^��q��C��/q��/�ą��AS�g��|���a��j��WB'���>�u�����UTF'w�u�}o�^��f�F��*j!�R�<s����Cv�M�i.�Ewڸ��}.����s�/m.���t5>&!�����a��J�S�K���q���v�jg]����/y]���;���)\7-���qq�`�9G�Rw�f d$Ժ�����n&�2�gv~��
J~b+y, 1��Z�=��=��*_��Z��WrW�Ğ��K�E��+q�4������5`�<�ç�Z�!���摋�u�n{��@��xB��0?;�,��ekg�h��ķ��=ސK��uѩ�<��q��{X���-���v��`^�#�B�}��wa�#7�e�m��m��M|�D\FvB,憌��.�~̛q��PN�f

�#�F�D�BO��DK�E����w�Dn"�X"i<d/t*q�M���q��ݠ���t����fcp��m	���	�gZ*����ea��\\��c��;�����ց�3,p����!�!�!�!ۡءڡ����Q�"FE��1*bTĨ�Q��J0*����J0*����J0*ѨD��J4*ѨD��J4*ѨD���J2*ɨ$���J2*ɨ$���J2*٨d�����&,��d���J6*!�X(�bk��-�/Ũ�R�J1*�޾���b+�K1*ըT�bk݋-g/�n�T�R�J5*ըT�ҌJ3*���2�b���-/���R�ҌJ3*ݨt�ҍJ7*ݨt�ҍJ7*ݨvŰ+�]1�aW�b�îvŰ+�]1�aW�b�îvŰ+�]1�aW�b�îvŰ+�]1�aW�b�îvŰ+�]1�aW�b�îvŰ+�]1�aW�b�îvŰ+�]1�aW��a��vŰ+�]F�0���*LîvŰ+�]Ɗ0(��b�îv��P�\�aW�b�îvŰ+�]�10��1b`�İ+�]1�aW�b�îvŰ+�]1�a���A�����P�P���`T���3FŰk�1b�.�`T��X2FŰk+bK�`T���0FŰk�b��u;�n0�{^�?FŰk�s1_�;�n0��n0��n0��n0��n0��n0���<1�p0�p0�p0�p0�p0�p0�p0�p0�p0�p0�p0�p0�p0�p0�p0�p0�p0��0itI⍳ܵ_��8�1��	��	���tMJ���	��Mx�7L`w�[�u�����y0�T���������Kr��qN�^�0\ڻ�ϛC�qV��A^�/gW�L,�Nl�K�(��\� ,;v��7���=d�/���h���qjG��K���z��7#�cՏ�p�c�|���w)}70%�����9�4*v�D��s^\�����ܾ��ܥq�[{<��o���P�X�p8�����<����wc�.��ڻ�A�˟7����C^�z���۷_�b��5)_�cd����a՝����?�<Lʺ� �p��En�/�O�&!viE����[��0w�ǥ/�L������s5�o�P)�����͋��    �x���왽�{]�����7���Koq��\��ǿ����'�q�������7w��*fm��c�Wg�1�����y�o�����՗����Ϯ�9������A�������]?{����-^<Э�E�o�
<�c��Z�j��e����ۋ+�=��`�˿����M����w�w�?|�����ov�w���^�ݱ|�Wz@�1á����^~}�����Z��G/�'�_q�ׂ�ck�^`�m
���Ř�^�x�o.�[���Vr������{,�4�\4�z���:�bY� \��{J���^��W4�'�_y��b��l�(���Po�K\���V�ǡ���n�7���
{Sh�����-���E_KK�R�|�����k��v~�3�Ϸ�7�g��/�.���>����7�}�{'���o��e�N>�������h�����S�6����^(�ul}q}�T�~vq���k�q9�������Ϯ�=���?�\]�}��׻�>�Ó�U��]�]��������o�g�9�ok�_�a��*��;��[\oo�.^�-Bz����G!c���ҝ��W��p���x�=����}�W�gι��+.�v���Z�oV���܌~�ޞh����F<�|��F7h��]n>�7�n��G�۳�x�����/&����'����,{#��7�ϵ?�eOn����ЧF��-?Ի= �O���[�w{ B���{�-�q��������	7�:��`���.��
��}t����V�N�	넟5�~��`��;���Sz�N�?�W)��}����J��wW���=�Wj�7#uՐǚ�:4�_nAq�1:�������_.u��	�{ɡtx>�\H��vg&��=���>����y6㾫z�h���{x�u���:�L��0MǑ�㝷G���h�?����~'-��);�o�]�x����%~8~����y�ft�'�����! �����Rf��������#8���ky<t�q�M,�����V�}ƻ]��u�'������g��oο<�Ǐ/�_[&��+�ǃ=���Bt������ۨ��>��q��,qΡ����_����"�4,/����Jٻ�������v���g�D S�^1�w��<8���K����<}�s�i��2��㙣�_F������Z`����3�t?͞���7�}���Y8�i3� �_?ބ���C��-��t��
�oK�����9,���t�V�xJ�)�GID�_ہ���W���%��bwT�g{qr��F��;�ڑ���7�%�{I�zIR��X$��D�<�g�ן_]_nO_|uu{���ً��}�P�#T�X���gKo��4�?��#6����1~�Qǃ��q��+j1|0�0��w��qφ�����O>����~4���s;����K7��������ގ�����2��ody|��{�jM���1:�u��o���[���k�gߜ�
x��.��-�"䣯��&m�y�E��o�_��l�P�'x��?��X��}�R�XWb���\ԧ�X��ܞnϮo����T;��3���.y��_y1A��G��[�ߚZ���_n�m�	d6+��m�V��ָ~�u�;���^���$M�{x���a̾��+���	�J9X�����|��S.����z�@y���C��x��Q�ʃ��+e�&�]&���F�j	��=���ÿ?�c���C��������~c������~S��縤Cs6�nt��r{N��������2J���r\�)�A{�������3� O� ����m�_-#����o�׶r�������ɋ3+��j��
o>Y}sv]��1�v�99�!�۩��nO��l��|��y���~�{��uz���b�������3_�?oK�'��G�5��qm��ge�������{���xG�4��{��9�!��[J�����1�J2��%��%ӏ���%�{��p���Tef�o'��d��C��W��߰h�Q���dz/�L2i5�p(���|���ٳ��Tn�����^9��y��ɡ��ֺ�^����-\�|�9zg����P����o~z��{�q�D>��T�1��&�$M��T�������!F������?N���?�a����ᰖ�Y�=��e��fPy��A�ct��!��I���M�P��o�F��zw���w?P��b��]�/x��^���q����0�_�|ysz�ʫ���_|O0�ݓ�?=��'����#c{>ۇo8�~�'}�`���+�f�6�}�Ϩ���0�?\��cg�Ϳ�(��G��&.61�C-]�>��z��݋�O2���;d,���쟝]�e�l���f�v����_��mn�:{v�l[Q<{��t�mn�6�r������P�]������d��A�яg�ϯn���� {���Ng������3�<��������?�˪[AW�{j�hŪ��.���oYXj�햹�z�-�&n�=���U�eIq��ڬdo��̵���[up+��X������Y�7�\b�[�߬��Wf��f�z�[ف%Ǜ�f�d/���V����Z8ϱ��ΧE��ڻ�Y�8�]~�=+A��2�1��>��"�����.q�D法��kVd�X$�!�b�خ�X���bE��]?��EsQ�0i�v�^F�����N��$U?�~�(`�TI˃'����Ps0i���Mʡ�e�Q�0iQ��:�IK���-����&NQ[($Q1i]�0IZ:%m�HMZ�r:i)kTPLZM:)˒�X�B�I��IY�b�5(����p����Iy�Iq�t�%-G�tH�.c�*ũj��Hʳ��M�%TO�Z�pDm�œ��=)��B#�䤀O:JP�1ie��7)��B+)��"iY�HN
1��:��ܬ/���*P�<��Z�;+$PC2+ϳ�<+ϳ�<+ϳ�<+ϳ�<+�Qn2+ϳ�<���}��v>G%vؑ��>{������O��Cd��"^���'؁u��I�V7��]�Vz�K���q6�QL����g�������%�I_��!��J�����ĆWF7�L���=K�'�2��{�Q����c�k�s���)�H��þP���'>kݕ�|�w�مi�n�r�����<����+tYw��L�2|
�'��.=vnܕԮ���f߬y��Q��A(�!��D�a� V4]��N�"��ZLq-��{��ka1xB9�D;K��/Ni������b�N`��,���j��Z��-TQe}���*+ϲ**��ͪ���3kf�Z��������OYJ�fY�=��Ί�`�ʵ��/k�fUT�ΛÐYGUVDemVgEqVVe0(�u�g�tV�dUTYGUց�UQekY1���YUVa�\ ZVE�Ue�NVI�U�<p���UQeElVE�YUVE�u�dUT�$�UQeUTY�QV4eDY�@VE�UQe�(:\��Ey^��Ey�(ϋ�(ϋ�����(ϋ�(ϋ�(ϋ�(ϋ���!s��(ϋ�(ϋ�(ϋ�(�Q��(Q��(�J^���D#�nqG���c>2U����eo(E����t�b"LL*�h�Y���3�Z�	O1(�y��N6�j ��^����L����+�i��*v�M�O=�#�����q~@%������v��|_����^S�I���9������A�U:� �.q�e�M6A4nf�Xlh�{��5,������ ���7�l�r- �ӗ)�:浅�`Q9_TΛЗ.
Ǣ�+�O�m��^�E����EGJQ9_�G��^T���E;���/F[��/
Ǣr�֋��(��򱨜/*����r�(�bUً"�(+���(C`s�PQ9_��(�^T��@Q�cZYT���E�|Q�$j�iQ�oQ�EsQDhQ� (_U�KU�RU�W�/��W�%
�W�j��t(t�&���M;B7���]��oѠ2vQ�������y���L0-�6[���r��yĄ��~6Ƃ�`fZ09�d�<� ��3v�br��Qdvr5��]C&8*}0Ʉ���tf,�s��:~8��O�q��սCߕZq�²׺�Վ    �νMv�����%��ӕd�6���A��uE<�d�{ʯ��O�MF8=�K��9WW{ҟ���ۭ��v{޻<�6���q��ʎ��>������Wm{���K{��ޡ�Q�;:��] �"�W�n��#�D����9�k���i�5�8�酣G�ƓM�LDcY���Dl���.f�,����(L([���H��y����lMȪ��	�V�������R�
�Y3��"���� �������(U�&�U�T�.�
��0�ڃ�lTURU�GU%UUIU�U%ZU%U�ê�N��J����*V�JŪ�jWVURU�l̪J�����8��"�*�����P����*��*��܃���`�����v�Ѵ�aK5U\ MSä�aҔcMe<<�MEHS�pj���~���������X��m:r���<jj�4H��AS�55L���\��)/�Z8����؛
���IS��T|4�yS�7�9�>�ݔ�My�E��<o��<��	�00��)���o�s���<o�s(��<�,�)�����AS�Õ�~S���ߔ�p�@5�yS�7�9���)ϛ��<o�s,C4�9�b诮<�j$?�T�CW�cu:Z�+ϡ�����s���<��_�ۮ|Ü�+?z����Œ5f�1�����7�}�M2�ԡ��L���K�h39gF#�im:M�'ӕ��w6]�M��FŴ^�z�=�;��N��̈́e��&�+]l��.�Tv%'I��I����.Izb������cݽ�4��v�9m
�[n�P�S����v�Xޟ��'�u�S~GZxo9o䌑Z��͛��>-�����y�̅+Z/nQ�S}Ӝ�W��U�V΅i)���j��^��4vͧݞ��s��X{�j�VM�3�����%��!/p���OϬ�G���<�t���6=��ؕ>o���4 8R9�0Z���]�A�e�Y.V�{U�ZL3.U�OU�O�R~T�U�?�N~S��T�4���/p�
����9*p�
�����*p�
�����)�~
<�����)�;<�/���)�+	����)�f
Ė�S!�`
��ϥ�k)�^����Y!pT���9!pL����!pD���� p<���`b'p4�߂�� �)�	_��� �!�߁�o ��_��O �\���% p\7�� �����9�����Y�Y�
Kb�S������Y�R�� 0c�'��*pU�+���g΢�*z	����X��V`�
�Z�E+�f����X��U`�
�V��*�V���JX��T iV��"X�KT`�
,P��)�<V���X�KS`V
���`��N`�	0F�;��Ҏ�!u���v���>��@?Z�*S�=ڑ���E$W|����ݙ�1yL_�y�IY��1U(�+r�z1��h��h
"�4O��M�c�G�C����&L3�s�Ƀ�k\!6��x�Y;�d�JJ�m�٬����me���T�9�Y;���g��$�����Hf9�F��Wڅvhu�Ծ���JlUw	;E;E���揼��o��=���|4�X��Oc�qS���i(�$��{&>��vVڽ"�5���]�����9Ҳ�|Z��!^y�Gv(������qsY?��\@���}�42�;�O.�s~?T��Y����_����j�*��Z�ޚ���h��M��4��N�ز��w
w^��Ɋ=?ó�=��>���$�����#�mE��i+�=i�_�k� z���ul�'׏��^XԼ	����P
��7
���l�@A�0��!�8q6�l��
"�'�O��p6�l�ٌ�2(d�Ϡ_@��l�ق�
(TP��_A��l�ن�g�6Ph��A��~����$�O����Y�mEpVpVpVp�'
*l�g�g�'���8q�&"�'�O��@?�l�ٌ��=ɠ�A!�~���g΢���B�
��+�V�m8�p��ؕ�	��;�w��8�q��� ��. uX������L�,�Ի�. u�����轀�� ��8��.��z/����z/ u���w|�YP@��^@�a��4g�:�J�'(��z/��B�Y�. u�@�>�'��z/��"z/��"z/��"z/��"z6��T���{��)���^D�E�^D�E�>!{��{X����ދ轈ދ�^�"z/��"z�� sj|�,z/��"z/�� `CD�aY{|�,z/��"�*-�ưn�9�a��� ����8��؉�g�g���\���n��1�s;@Y�����϶������DÉ���7g�+��<��������Ӌ�7��o�����H8�?����;�ٿ�����p���R$��&��>���v����o���o�7��7�X6��ל?C�Af�~����	�K0N����ۗ׶���dn���0	�w#'��n��$�ލP���*�Py7Bu��@���Y�<?����P�x��ۯ����.
J�|~g@ysg �׽E� ��*�Z��ri���S��9=�㜞�L k�)�飁,���l: ����(\�6��v�ȝ6K6I�B��-s�|���@tڝ�qF�)WݙJq`o~ĵ�{:d����<��gdqoFƵ��7[{��7t�yw��<`���1��[��9�Gv�uӅ�H��t�t���}�I\��	.gی�h|�֝\6J������@_�Ϭ���Ssw�p�w��g#�މ2~�y9������B��ఖt�T(���~�~ࡠ�>��:7�8ɝ|��>���(����������SF��B߉�����q4�W|�TɳJ^Vz%*=�8��6p�Sf����Ъ��N�P���Q@_��S��kHu10T"�.|,Fv[�*�%�f�
]r��R���M�l�(�:�Dch1��P����J(��xPxC��bR�0\8S�1�*s=57wtp���t6�.�ɥ��&�1"�_&۸�Ea^i=If-.{��\��4v��s�osi�.��vɛ[&�r��u�n&�����*q�����M����h/l�=C֕��a�m�V�z_����,҈j���å�k����h���]i�q��G�ہ���S�or�����3J��$��������,E.pO���!�!�!�!ۡءڡ�K{�1*bTĨ�Q�"FE��1*����J0*����J0*����J4*ѨD��J4*ѨD��J4*ɨ$���J2*ɨ$���J2*ɨ$���J6*٨�B�b+�K6*٨d�b멋-�.�B��R�R�J1*Ũ�b���-C.�޸�R�J5*�2����b�|K5*ըT�R�J5*ͨ4�b+g�-�-�j�ز�b�f�-�-ͨ4�ҍJ7*ݨt�ҍJ7*ݨt�ҍJ1�aW�b�îvŰ+�]1�aW�b�îvŰ+�]1�aW�b�îvŰ+�]1�aW�b�îvŰ+�]1�aW�b�îvŰ+�]1�aW�b�îvŰ+�]1�aW�b��.�m �]1�a�� \���>��Ű+�]1�a�+�\B�Z�vŰ+�]�js�+�b�îvŰ+�]1�a���\��/�|���E_1�aW�b�îvŰ+�]1�aW�bصe�q;;D;$;d;;T;4;î�����v�y-��b�5��8î�����`T���b�5��/U�n�b��]sf�y-���v��(�Yԡb�b���`���`���`���`���`���`؝#f�`�`�`�`�`�`�`�`�`�`�`�`�`�`�`�`�`���}��$����A�ܸ�u�&M�%r}Eٶ��y~usv��Hj�#O}��{?�$�?�ev�G�}I��)��&Ew
�Y�$���P)�k(�~����]���������J	�i���N��&q�頂o��ۯ���|o�.�Pi�񑡹C�މ�^q����~�nd@���H6c=�(z-P�^���j1����������P���� ���-�#�������;$    ���?؆k�QRj~ u}�hd����A#�Ao�/�.�~u}��s+��ݿ��W<̽:��ܿ�ì	ۘĊ��]<�D�&�:��]�Yn�o��w�|���'��x����HG�:�8��������!���������T�j�H�Z�r,l�ӫ��o�����Z�{Ƅ��B�֡	�_>���r���"�O���ᓧ�!�=�g�����\\}���_,�b��ߝl����!�G����6��ՠ9~*�Ѱy~�wN���KX8E<�^X���ԟn��4ǩ>����n���t�z�a���{S��~��|����������=��Ex=���7�v�k��`����މ�n�k�����1z�_'Q8cΞ��6���w?3;և�W���s�(̞��������X��q��f'�Hoy��޾S?5�6_�|~v��F�4�o�;���h��X��q)-/��3,�J��������n�S.�z�����:&`g��ꯛO��������/1>���'�c�<L�͓1��W��=Y�h������c���������f���;q�C�������d�\��ln�Fs,KL�f�\�αE�vl�IN�R�{����}i����L8�r�so�2t�3��R��ob�������2#΂o��;�t}��`R.�7(Z�C%q_gP�K�ȁ�=�Rn��2^���-L�6����d7��'">�I��������nkΙ�3����-2�rY�E�(z37%�t���&V߮Y��l(����47bD��`�q�P�zd�O���-Wf��)pS�����r��q�U�'���tG�u��h���jM�4ׄ-c�T��������K���VD|�`cБF�1
0���S`����JK��0�� ���s�уcP2�l|k�a�a�`�T/�7��}m��<�y���0^��a���J���<Vk�_jd���̌;:���������01p�BM:���M�?w��/˅=P�0�E�]8Iȑ�*�&����ܤ/52SC���.6ύ����P<��r���A��yKs 1�^8�9�e�Y-��z�aX���������_�y��ˣ�v�f��� ��LW��䨍���F/�3K%��֜H�ܗ:ĳ߂a����C�Ƹ��7ꝱ�C�s�~]W�>�;*d���!��\�0�r��y�����T��UO�יݨ�P��4C�{~��]���g�r���1���u��B�,§�&�	��o(��-6���zv���=�ȸ��3�wɏ7`�9��Wfҿ���&r��鍧����
7$�����W�L�Sj���=1
ts0����#Dچ���������[�Gg����>�>s�i[O�%�R�S�&� ����yr���m��|c;�d4v%��Юe_ʺ�o�d&R�3ݧBz�W+�p9��'�v�����O��m������ͯ�~�¯R�d�}�K�N.��+��ۥ�uغ
	�UZw�U����B� ��,������2��4a�n:��i�y�l�d^sf_�k��(��HI�BwH���V$�j��Ʒ4�Uϓ;l^��*"(�s�߲��12�� $��P���j�83�O�\��B/.���=��!*i�� �^������m�=W��VqM23�u~�f�)j�+����~�&+?��ԠW�F�������gf��Y(�d�1�U��x��>��׶~͓XZ%f:&&�g�L��W��K�I��R�v�A!U�����\X-Ջn-LU���$�N��Su3aH�9g*���_�[�cZԙ(&E�N�9����r�!���ܦJ�����{F�>�ˍ��<�Lu�"��[G~�;�WO�To���|/��F�&*LY>�)w�'��R���榫���xy�ºj��r��l�X�QI7~r�_�Íah$�ԗ�\��ټRSn�2S
��]�j��7�Sv	�g�a����6�ݥ�>A���՗&s��Nr�4��]I�>���F����[v�؛o���"�PqcJ�:m��kN�S�y:�j^��>��Y��2�$|+�0�
9�l�9�L����'H��u)TE�^��޽me�v��{��w��/,��e�|���+��Oݶ<� ͹1Cc�a(r��2��Bn�q�d���M�������u�3�na}��\\���Ӭ�!'�=g�,Y�m�op�nI��c^�i���^��M�c.V�o��&�ƭ��)�w0H�vꜸ�Y7��'-�t~cB6�Ĺ�`��1�/'�@Ǳ�3)-�=�������;UB�d]�~�S���/1i�~K�φ�)F�l�2����т��u��=ʐ�|�A�ޟ1����yX����*�!�S%d�zWT���v�ݰ��;Vw�����Vd����:`�PǄ/���,ܔ?��s��؏�2��0"�$�\�V.}���[��{c��.�� !��!4�eD��7�P������
��XK90BWw�5�}5B����>3/�4�Q�(���Eh,H�-6�>0��B��Ok�QXFpc�0��[|�_�_:�'cVɤ�c�b�7f�ܣ=nk 
�f[��ݖ6Λ�%/6a�=N�ԆaB�kܭ��W��^u)TOR���X)��4O�yբ��3mս��wrc��&�,����&-���0���\��j�ۙ9�ǔ���Bv�+�,�߲���v�x6ץ���R\1,y�2�ej����>�	�Ibղ>��z<���5�W��5��r�&�'k:�tr��m-�5�5{�k�e�k�e�k�e�k����H����v/	6�26�2!6�2-6�296�2E6�2Q6�2]6�2i6�2u6�2�6�2�6�2�6�2�6��%�F[��F[&�F[K���4�pm�vm�|m��m-7�'{:n�eRn�ejn�e�n�Ū�d3Y���)��ɚ�;�����L��˞�m1��h���h��h�D�h�t�hˤ�h���h��h�4�h�d�h˔�h���h���h�$�h�T�h˄�h˴�h���h��h�D�h�t�h\yjq������G[&G[�G[&G[K?\yr�e*r�eBr�eZr�������(G[&*G[�+G[��S��-��-Ә�-���-S��m�?�4�n����K���>��eiHS���˜�)���{˺��5����W�E~t}����֌P���($w��/wd�~2V�&q��w��3\��iD�߆�C*��-Z�ꗽ����ģ	�u�%�.Ţ��l��Ȭ�ſe�ҙ�+ZZ�5���ε[���f	�M�4:M�j�*R�Y���f��'f��vk�"��)㹊)S䚏��:�!LYj��O�˞(�bDM�Pi��4�ut�$�w.fO��B�=���g(7��Nc�h
�	�x��N�K����ٺ��B+���o������Dm1����mS�=��)��yZ&>gcJ�e�e��4G57�}���z �K�����[�^XE|�T--�E��jV��o�6׸u.��S��ï�e�M�yJ��ۥ�#Rd�r�/|���W�V����L��J��y�'f�̵e�Gy��h��
YD|�4C�8�͊�T��l<�@mt.��rK��-.�8۸(p��L�h������[�^�;���˨C}J�7S�w����4}�M��sr���xDWl�t]*�Ѝ��av��s�|o����ѐ��-T�;�(�]��J�u3)#�"+D��<�*V�Di(�3�d��f�a=�	$��>c�t}��H)�b�~�a�U��Y���
�"7,2C�lo@�9j�����u1L�2w�0���aRF'̘îkQ$��5���N}N"�ע�����{�����Z�^�p�j�C.Ꜣ��x_A,sE�Ff�p�8C.< ���t��������~��JŅ��#��]�%����谽�L�+�v)��PPv������1�_���#��=>�f���r ��Ԙ}``.j���t�ɲ{,��.�zTb�\�S���e֮ʋ����ʬ�� ��X�{���\�i.Y5j�Ѡ��k'Cl^���P}Jӟ��`İ��1�h�'Z�Y]�N�jٺ���<�C�B�[�Қ[;��i�1��/h��(
��:ga    &�!�|�v�*����؃;M�h*9DO�n�_j֗��ذsX�mQ��Z��a�4��0�tQ�!}��+�J���s3䫻��=�������M[�}߹���ӕ��6��5�>z����U�n�i��0���俉[�-m�9Nc�è=�����f�7�K�pqRP�¸��-�ryY��B8V����Z�a9Y�2���:C:Yk4���Rڲ^��Um@[�n@[Vp@[�〜�^�mY�mY�m��;�-�<�-k=�-+>�-�>�-�?�-k@�-+A�-�A��^U����q�"Жu"Ж�"Ж5#ж��^�9Y�Hē��D>Y+JԓYW���ڲ�ڲ���՛@[V�@[֞@[V�@[֡@[V�@[֤@[V�@[֧@۽*hk�*�+�X���[���^���a��V��گg���j���m���p���s���v���y��{�/���_ W^mYmYmYm�:p�52�v�Rڲ^ڲjڲvڲ�ڲ�ڲ�ڲ�ڲ��r���'k��t���('kōvrXwmY}mY�mY�m�p�U9�v�6�W�u:Ж�:Ж5;Ж�;Ж�;ЖU<Ж�<�v��ڲ�ڲ��Z���+}�-�}�-�~�-k��^�e�e5�eM�ee�e}�e��ݫ�����V7���!h�"h�J"h�z"hkUE�+�-��{FЖuFЖ�FЖ5G����H8Y돤��
I9Yk���Ê$h˺$h��$h�%hk�J�+�W��{UKЖ�KЖLЖuLЖ�LЖ5MЖ�MЖ�M�v��	ڲ�	ڲ�	ڲ�	�Z���k��-+����Cy_��}u���I�W'y_���2�XA�1��������g�^]g��}N����s}����#|ߡ��v�)�Ֆk���Y�o�s}G7�N�����ϰ��I��_-�Q�-�9��m��̭����:��Ű�/U�;6Yׅ|&�%���5��9��[:�I���=fl;��;�ʪ�yMK��;,��v�|��~�2��5�/^˺WMw����V��&�^&�R���v����F|���֗�zX��U�A�O��磵,�Ef�h�!���fs�s)mL��t8(L�������m2e���u�;W6��b��I��A|����GK�F����D.aB$�ad���=��������`�*�S��cJ�/Xc�we����g d\7Y�ou o�쳖en�UG��i�ͱѦOL���Z�棭��¢-�^f����?K���}����Y��:h�d�VGYeȲ�ݯ�p-K\q0=d�zi;=�b�O����SNRb����V�X�.��4���Mt�ϗ���g>��X���v�e]�Nz>f�4�a�^�b`b<1�Fk�xV-;�ᦉ��ͬ�x'����2r?�F��}���Z��j�!=�Q�^bc��+�3�5w�"uF�0��5Hr�o���a��ݵC
pX�<��h��1 �{��z��N�ѫ�J�%�D:k_(�5�lI��--tN��r3.Ǣ��F�zI`�#�t�����p1�6�=�P�&)ʐ�ޯ5d�ՅK]G���z��1�4�ߜ�Z5*��i:|g"u��J�9�qsjO�0&v�1�C�-��K/��s|�3�C
�s��J��CF{��k�^Bz ��M�w����>$md4p�\���/�l�{�����+c��p�sѡƵU6����%���:���}s��C�"^�|��40ja_�*���w��9.W�t����40���އ-�=t5���D���Z�*^/�����j����K
�U���\5��Q�E�Lĕ<WO������)ٳ1�]L�r�b]�A����xZ�Z����Cؗ�rS��x�00�jR�r�8溸�Ւ�k �瑏Ne�w?#p��HjK�N�AZCT4�����"�`�6@d��̓��8���f�ɐ����.ǻY��dϜ��H�!H��������ڡ[RM�(oK�}F��]sv���q⑫1�
bخ��987ai��"��(j���ś������#s���]��N�z�u�ݧZu��U8NK�����t�jjC�g�	F;y�߇p)��\Sk��D��g֐qu~Os��rY��H�m=�G�z�<�|.�i��i[�^��Zm!�q@/䴚ԫ�eZ�e����2�L**��
��3~���&q��ݣ��ҕ���~�	����6���Wu���~un����-M;lXa�X�u5�Îa��iLIy��=��;�B��Lmn����S}�4�7�ag����{ܱ�{Zg1�`�ߌ%�2q��6-ʡ�$N��me�7�Ǐ;��(u�'�������,K�m��Ѳ$N�c��Q'Ͻ����[����=�كsu��B?�S����Mۿ���uj3���iQ[=KߙE/��ٙ|ξlqN�u��0���9
e�,�
D�w��uu����{���:Ŝ�.�2�?l�0���l�p.��g+�uu��ds[3#�N�!������{Y/����"i%�N�42Ϳ�eN���*Y��	�:!�ӅPv&���j^����6����5��՟��TW��e�au�u_��84�0�#��)�kܙ텕��ƾ���kG�4���|�>�{5�t��.�c�4eG���&��z��W���D����Op��$N�UW:m�Di��9�v<c�3�˘�U9�u�ǲ�(��fL���׼Fiuh�k�ﱬ}�����Ki�	���K�f�&auԲ���L������w����v�q��W�4��ꌪi�W�mN�l������
þ�(�ʷFgb���:Vѭ*���^+�wb_���[��־Z��u'�ڏSyP�kꔅM�^N��^����W�e�+�w2 ha�����u�}��.qe�v��ժڪ���i�^�F�e�_�:>[\�Km}Nu_��);ϙv��k����H�U��%�gh��m��aC}����q�:
�uu�u�t��t�t��t�t��t�t��t�t�ztmt�_tRt�Dt7t�)tt�tt,�w,�w,�w,�w,{w,`w,Ew,*w,w,�v,�v��(��Q����[G����o��:�vd��Ȱב5�#^Gv���uY�:2�ulB��Nֱ1�c�W�f��mW�:�Bulj�؞ԱѨc�P�柎m<r:��tl�����Q֭��[GQ���n%�:*�ut���Qέ��[G1��Zn��:�t���бǿc�~�^����%�:�v� �(A�Q��� aG������\��E_�}}_��}���E_O�}=�T��v�W��a7v�a7v�a7v�a7v�a7v�a7v�a7v�a7v�a7v�a7v�a7v�a7v�a7v�a7v�a7v�a7v�a7v�a7v�a7v�a7v�a7v�a7v�a7v�a7v�a7v�a7v�a7v�a7v�a7v�a7v�a7v�a7v�a7v�a7v�a7v�a7v�a7v�a7v�a7v�a7v�a7v�a7v�a7v�a7v�a7v�a7v�a7v�a7v�a7v�a7v�a7v�a7v�a7v�aw��0����b8��*R�+3�y��g��{\�5�=�ߧ�5�9-�T�m�[�>����t���0��[枚���=������R|־�Zr�����͹��]���43\fϧ��q��N�����Mt��ߤ-�z��f۶nLJ;��l���#��r���M�Jw��R���Ip��ݩ�i���V�;AWd���������RS��KM��x��D/5�?d�;л�N3�����un��j���}qi�{�56۽a�If�i�:��5��+��C�����] ����-���Zdvx]�\<��U�f�k���-��)]���N%SV~fǚnB�.T[��g�-��G��tNV&I�+VZY�a��@���S�N���p�k��b3]N3�:���6胭��:y����S,��>�>O��bd���	�ɺ�n�����D�PW��R]2�5�L���~�:��n�ҧZ�N���=���2k���8}?;\d���9Lt�>�;T�:z5`M#9�t��2GMJs�Uw���g�k���Mf�K�%��k4q�fa��@_!��dK��f���֒0��=���IyY��    �e>��s:�<����C�띿���%L�֡��_EP�ф��ɵ���;㪮�H�\�Q����t��ui��	�
4߰��}�񕺻�N��:b@,�__�r�J�U��V7;��u�9YXJ]ui����au�
)�
��&)����)����ۺBW�z��������\�}�+s�J��mg�d.�������k����\�Jy]OսG��(k�p��iOS�-�x��F���a6�yM�^p5}gB�aܮB&Ϥ�j	O6��k۰ҙk�
�5NC7�O!���Z�VYz���K�jR�tTN���@T|�U·:W�Ǽ �Ԝ��q�[�gi�.�}R�,���t��f@ȅ6P�w�$^iѴ]��jN$�^�HG��zЉn�r^]����Q�%W�	�Kn9���e4UCv�J㾪���\\�h�r��f.Y<�J�U���:�pyH`f�Ӽa��J��� /Ie\�n���S"C��O6]�ev�eR>��ή��d�i ӂ��=aϼ�I��iWb�X���Kg~��{��Zҁ1��C�i�|�:�2�>L�!�a�z$W�}ьjC�1
��K2ף�-�[|�no��I�	�D�<KH��9<�:��ZJ��c��Y��c ���jd�*��F���Q�h���#��U.{> M��E��^<L�$6n�^g�MHj�v�l]d�oj�X�Mzc?u����1�5ib������P����l����,C��b٭�����S�*�j�&�c��aPGV��U����ի���BY��$�a��aed���F��jP�W{�M��ޥ��^�k:/
8�ֳ�����E4���B�z����:`��={ҍ�}�8߹������V�ǙeA�Y{x��$)E�$�d�,�0���=���<{ ��2up�V��TN�V��u��V����"��ٳi~q�D�Q�^�F�v�U�q�}@<{њ���xۮ��X��j�&&�5>��$4�7ҶG�-�)#�_���&&wn��LDMhf`i����*L66�;��Tͺ�bK�掷�PQ���(�4���p^�S�b�
i��l��5U�-�k�`���L��%����R�Yg� �y<#!��#7,���N��"�kC�:�4�"О�`����o[��:�|���BOєf�/z�l�G��c)���,J�p(����\�W�* R �&i�}�u���Ν��+��=�f+#?HXEB=A7b3$> �{�,ِь���Ǫ�UQd���i��� �'C�x�a��i�NY�r��X�Y���G�:�EF��/�^=0|� ��m�M�>�����1Qְ2�}ލu C����v���38D�D+�����Ӡ�}c���$��Z\1�a)L�߸xa-�	���.Oԇ]`%XG��N�<O|,Cf��%g ��i����!���e�v�L��*iztqVBq��~�0=a�?:�5cr���t��ip� l�v{��2��0��U���(}7�i��rb۹�i/��&�|H~�O��Z��eڧ5̡1ϛ�.��O8M�]��A�W�a��}���;d�����8w�Ś�Z�G ��4�Q���"�I?kDx�^�l
�,a�g��`Ay�5ϖ���;/��=a�q�,K��Gu�����[��3��<o���@�.���
�s7�������k�=�5�]��k������mB�E��.�h�#[�!%/������e��/�ⲽ8�<OG4u�vתu�(�G���N�\م����Z��	KqI� �$���V��
�ZAR�W���$�xI=^AR�W���$���AR�^l�S��N����o�D�O��4�M���y�hR+��8��������G��7�?zqz�����ۓ���z�ߟ<��zq�(�X�����/�T*���O�<�|����7����w'���չ�t����r�����晿������_��_��_]>{�t�O3�n��EƎ��>ڝ��hG��������+���߾��ϑ���������������O���'n�j{}y�r"����s<�Ӑ���L�y'�W���7[��>��d�O��o{KO�1���e_���oq��͓���ѝ�^l�������܍�'W�Ӎ\��n�*����@��^lO�_^mq�
�����Ӌ˟�:n�������à��o<ɽl��\^>;?�xv�P�%�7��9�:��7��*9`V��������
�|��W��vI�v����D���z9�-��o�r�͗���������;��x�}�V�;��&�s���}}��?�+�g�m���ы�������SQ��O�?\�����ӓ�.�U�~���5����B&��m���+�\:�e��o��/��pW���9[^�~��'�?����7dP��h�!�|�w~�ۃ5����=������w����|��蕪�j��yz��\L�!�� ː�Ջ����e���:�|�f7��	�?+�u�oM��HYmO��|v��~����=�r����b��_���nu~[a��hu��B�|���ק?�Z������ẍ�ƗG̯�"ڎ�_�-�� �"nѭo���=]~�^�]�p�e���//����W �~���[�ޡ[{�0�^�w7t[����;��w�F��|����n�֣_)�7����痧��U��n�wk}~��6tk.�Ӓ�_.�_����yXd��.���=3Z�ޖ������zvu�������_⟟�(�Q��N39s0ƞ��oԇ�P}�׾ɻr�����d���\L]� sCC�������J~|�y~u�b��O�O_�O6�_m	���gW�a��2aد�U����j�h�\oo����z~z~�z������vy���~����v��/o�>����8�x���)ݯv���T�l=Ϗg?�xr}~��v�\�n�ɹ6�\�OHƿw����n���\<�Cᇗ�/�������O��|��esy������mή7/ή�1��������y>�Ǉ ��r�Sn{�C�7|X��a=ۜ^o������Ue�l���F�n�{fw�?'痿��^�p~�c�7���س`�����FN�u���K������w�4�m .2/O�O�_�xqzu�}��"�A��ޠ́<���<�W�g�Z��_�}.�=�扎�|��O��������._^,'X�쉁��-����$oz��W���r{������<d&�ϲ��ޚ���'Qd�M>��x�N�[��s�H����񧫳��r�����R��uZ�?-�g)��ּlc^>?;��}�^'������xhj�9f��G{����ɸ׶jc�}���s��Y�?���w7��g�r��D�c�]\�|"��/�����,�}�:Ɏ��:ž��>Y�>�z���?1
�Z�7'fqcb~�ߵ}�W{��l|���W�uޜ�A�	u��'������u{zrz��$�X�����7���o{����mA�5�����pz�������������ɟ~�x�O6��<?'"&��+_|/���婈������R�҃I��DC�9@t^gխ�}��u��\"��W����]�&�q��]��쁓�UWȇ�p������{@�{�r�Eάv�Eꡋ�tz��GQr�۞�R����w1]�/��3o���-k-6��7=硋m6-6��q�C�;��Zlf����ॎ4��b8VNy�RǛj��5�Q������+e�-6����i���r�Y	i��7/~yz�\��_�u-�ݭ�3�z8��?�Yog^�16kg_��]�g�nm���^�#[}�0��P�_y)\�5i��]�o���Wu8M���$�?�rܧX��c���ً�ˏ���k\��@���oN���ֳ�=�y�;���"͎z�y�;~z�������K��$�-��}g�sy�f����o�����=�z�Nx�W[��~��>�%������/9Nx���l��ϖc>��s��?�m9�5��w/��1������m�ǻOw�b���j=�[^j�d�b����p��J�q�}�<��J��vF�����T]p���/Ϸo_����|��7���Ix�H���� }�q�O���ɟ><�*:��|����;�y�z3�p�    9��!>���k�|��~}��3m~�E��-�!�O78������/����~)�3����"o�80__�6�����k޳.��?�����U���^��Պ���Z��v�;p��-vo�ҽ�z��Y�]���[�p�^�����m��&����v�/���ܷwr_���o�2��	�^��?x±f���9�������}��nb�'#8����niv�3{��R٘}Soe8���+Y=
�ŃH�Z�����`��ώ􎥃�{軩'�=�1�4���\�{Ɔ�L�OGJ�^C#7+���\�d�C������F�Y�H��-x��Y���!��M�2%@H`��f�	'U�6e�Tz�JBe-�fʕ�@��p	ϫ�� R���\I����*$���Cm��$l	��Ǘr���u���Ɉ:S���
�vm���L��:+'1}�$�q�p�0�1�I����1�7w��ͨw-i'�7*;p������O�`�Uƿ��uHZ,�t�Qu�a���D��8_Rr~����У:J�ҁ{`0��.��Z2Hf���" Fw���Z*Y2��(�C�Z`H��m��,�c���~�%���s5�g���f�f�Q�{�"�ب;�HB@Qew�Z`ς#�+'Ϭ2x�  vk�7��F�u0��[�ͥ�,Ze�����u�Бs�ѽ��TՉ�� ��]nxh(���+�Q�W4������ˤ)��}l�����Ⱥ�I���[wZ�#������`���P|;H��^:�{��w|�%{�w����o�2s>�XgGgc�DB���vH�#��F@+���8'ȡ�'p$+�r���T����J?���3��3�l5��R�(=��F	��T�0m���x'H��%'|A��	�N����&az%|��EQyx��X�*\[�k����͘�?#C	f�yj�����K���*'C.3>�ҫk��`��}��\�x��[Yu2Xk�TW�`���� �X3�d��g�+���־MJߪt��X�LU�qQ*����f�OF���L�����3��K$s+:���En��I��go�,�F$���W�F��&����_�Dٌk4P��ɔt0��I�E��YTy�K5�^#)ˣ� ö)�ڦ��x�3��Mo��=��r,i��<~,�K���JT��~h��6�U{�9�թ@;I4�}��֦����6[	�sEM���!V?�E*�Z��%r~Wɘ�a�����9ڰJ�D���.4:G�qm����J+���:'C�h�4����C��<����V�2>C��V*]���\ɚ3tN����9JV�f�
C�������s�M���t��V��A��Cs똨���\��J7fVz��
�C$�<x�A�?̜b-��v$��^!?aHm�E��)���j}@���e�X�$�F{�B#A�4�h��Cbш�Sv��|�1a�n�v�u^�����q�ͳ)Gl�Pm�k���Ǭ���%�WV=Ν�<t�/+�_�^&_9s�&ߕ]���Ί������^���L;\N �vMR��
��Q�$�@е=���+x��"�KM�]��k�SSK��V]{;z�'*t�XS �J�V�N�<*PIb�#�'�g?l�t:!�cH~�!��a����J~H�|I~t�$شF�F��e�-��wr��F��Joӄݩ�=CD-�N{P��I&�x+�T�ѣ���ᭀ�y�2�B> ?P��_p�gХJ��yƊ��Ԇ]Ɗ2��+��
cEk���S�I���x ����.7>py��gؽb�;� �w;�J��Y���C*�95G��@�*��F�6�h�4�&�>ܺi��}/�aE~�0��8�c�c"�p������Ϡд��Z�c��n��fW��r*}�ZZ��V��k���
S�bj���񈟴�}�z�և�Y렀������ËU2~M�|�[zb� Q��!�����1�t��B��٨ƉΧqWM?��0'YvƂ%K\2c�}���]f�@¼M��g�*�dr���/-Bix9,��[��F"��ve�������+t�6Q��W�D�_���B�k��
��:*'MTh�
�T�"ʝY�:��6#��:�z�B�~H�.�
�=�4�X�!c�a�F���X�[3�8?����ځ�BCK[LK���C���솗�[��-�?�7��fy��(��6��,CNsc�I1��$*Xo������;��3S�3!kU1�(�щmM'0<s%c�ҎN�<sf�U����W��@Ä��\��sea]���"���7k���B(6�|�j����,z�����ˈ߸FkR�A��b�Q����[�(��ʰ]�q\�6K=[�-�ƩݶF�q�ν�6��sT�=�f��7,3��8DK��f3�"f�H\36�ku��>��S+lҌ8uZ�+v��č%�j+�qO�=��55�:�̍��y���xbt�wW���x9�C3N�|�&�s�"�L�5�{ò����T�9�5��Wf���8�2�\l�Iz`/�,F?��Y,�SR\f�LyýZ�4��7v�-����b��R<�rc.�O)ţ����عg�	���1�A�X��s0�A+�!����7ZÌ)�9ɀq��A#�3%���������@�>V�Px��@g����
F>;#� ����GOW��Egw�V,@�o��#�X(��6T�S��w��6L6mɥ��Y��?���S�AӪ��`��Vm�ޠ�U%)StC�N�jo.�4�Iu�U"�gU5��Ҫ&��F{�Gw6����VCja(��
N�e�-5��0��O�r֯�큔�Z@Σ�������J�l���HY�����A�P/\oj7���^���+�6p��J�^�`i˿�o���ԅj��ʕ�g�y�7�vp߼�7|sm��]ԕV[�(5|sU�ڷS�|�N���q���;�i"mA�������C�}�>���L{��E��a�<y��k͆ag0��ذ*��\����lD�|�E*�)L.E�rG4��Ag�6�5�t���-�z*���l.Kf`Qt�uk�lk��V��,�O��9�Œ�h�3֨ƅ>�	<V+4d�3Z�0�����F�7�[�N�h�{WU},s搰�������-������ʍ=�I�~cn��v�Z�9o���ܾ�6�ukq�hj�mkuVf�Ak��l�El��8�f>-K���ʦ��[�4�dr5���}F�/�M!�<�2E٧�������*�jv-2��[*VFfxS|;����v���(��+z��5�9Lw�
f*����KΠGɳ,m��[C�-f�!{�h�}����$�*b��7(��t/�e^s�B��qd*D�S���ʞ��bnf����̌�����נZq��K ��KwE�v����(�M�Ẇ��'U��n^G;^��뢨��x> ��o��Cf����ʼ�|���(�d�f�Z�hZ��h�ʛ��&�g�C��p����ݤ��A^�I�{��;�q�3�.{-�F��is� �<��*�/F>+��w��;zb�>�,%ɼU���f�����,����+�ؿ�%�dyOw�7�kɍ):)�T�H\��-�� �uQ����.�hz<Z�pA��L8�h���њa���Ӳ-޺���񱛢��F����E���=?AM�F^W9����^�n썥�7��7����V�k����~����PKSp^sp^�p^�p^�p^�p^q�s���c.M�y��yM�y��yM�y��yU�^�ի�u���F��kbΫ��55�577
��Uӱߗ����ӫ��U�{Px�6��ئc��զ,��خc���:��خc���:�,;�H�W�9�M�ͺ-���m�ձ�D�hKE&�V�j��(�V�z�u����tJбA�jI}S�=��Z^�v{]�d�c�]��^/��بc���:6�بcU�Fמ�rUT���UQ�**W�������wa�55s������^�^^#\^�^^ó^_^3_�˦�/����`����������f�����.�l�Y0�i0�y0��0��0�Ư�\��d��l;�i>x�{��#���d    �߄�����\���̄�5E&���l��}�f��6[x�3� &p��@�65$u�ώ
F�j1F��
�N��@Tr�Fm��^��8�Z+{�{���3jXm��vG�v8*�W5���*1�QL���	�?+�`e�����M�A��zː(�8rƢ�ʈj��'*j�N��b�uKtA�xl�[�\��b7�Ef
>����+��(`0HMh��{�B�k��.��IBJZ��}��X-rҶ�tf��V���*1$��Sl��T�?1h-g��9ZR������;.&s�s��ke�73��FhOHѲ�=p��a�4��r�ý>�ԁPb����b�U�=¿ѶW��K�f���pU��l`�!�<�A\;ڭsDd<U�Fog�4�]I��D�vô����˽�̳�|A@	q���J�vh�ʛ���'�=�h�!�ν��nj%�[�Ga�C�-,Q��Kv��Ցm����������iG��{�G��z�t;L�	��OB"�^�H0�"4�{ś��%T��b��3b��yzw�>��-j1a�F{��6b���%��h��a���Q�z�(љK&� �ްd�������6��,�C�4S�bǘoW#���if��r������P�(��x1D��o�>�<}�b��5���3��j�g�P3Zo�6����m҈j�3!潄<�Љܑ��󭊨1K��7�X�N�b�6�3�ƠX"ح�_`��O����8QCʁ�^<�|����EPa"J��B�Tfz�I�F��%L�1^a��{25<����ra15Q]�~98�D)��)>g)\��	�)r��� 8��'ځ�I>���0��(#��O�5ѓy�C�t�4�ߎ�y��#h�$����N�]�9����󝋣ƥ ������(�8t��0��aJ�S�֙�Re���E�,�ׁ cP�m�6�l�n�n�n�n�n�n�nulӱ]�v�ulױ]�v�ulױ]��U�>�������M�ͺ-���m�ձ^�z�u�ױ^�z�u�ױ^�ztlбA�tlбA�tlбQ�FulԱQ�FulԱQ�F�tlұI�&�tlұI�&�tlұY�f�ulֱY�f�ulֱY�f[tlѱE�[tlѱE�[tlѱU�V[ulձU�V[ulձ*W�����j���U��*W�d�cU��ʕ.y��r�%Q�:V�J�A��lu�ʕW��j�љY�^�A�Q�I�Y�E�U�M�:V�J�,�ձ*WA�JßA���ח��U��>�H��VǪ\iA�lu��UP�Ҹ�lu�ʕb�d�cU�4&[�r��*��7�M�M��VǪ\�+͙�VǪ\i�hQ4������I
j�|�lu�ʕ����U�
*W��
c���U�R�`�J��;(�]�:V�*�\�+5e��u�cU��qP�lu�ʕF�`)�VǪ\i�T�:V�J�������U�
*WZ�([�r����ڕA�V�F�&�f��V�6��X���rU�Ԏ���U��*W���(����'?���>�f���֚o�Y��f����,�xlw���l���[�c��be����+���f��Y�l+���f��,\��V�����,�
wz���fn4��%: ��;�5)bU3��_P��?���O����2JH~͕������7+˭̠AD�.�{�?'���e�f`$S|�Xs �mgl��SǄMKU\�E �� .A#��8�~Q���� N'��"�>5�q�?\���H�G����R@�i������%9�3���4�QG�Әh9�F��C�}���"��p�8@J��Q^��0���%$C�:�z�>���8\�%	nB����$(�EA5:Jx��3��L�:5N����3��T��F�,�A��|L�"1~�	ʻ���AfԎ�C$��ω8F�`��V�8�Ul"����k�{,w�d�x�G�y"@&11�8�X�G6D%@�a@���B���L�H#�9�,ԑ
�=]�.��!�K �|�2�\ג��6K�̉�3[�W�����J�2�����U���ш-d�L��].h����AAҀ�W���j�쭖�@>T�f� 6k�j�� ere���+�H�����iZ%Z�(=�+�_��-�W`6N�E4,���[a�Q�#,EY|�0�i偍  X�T�������E7S}��l���$6Z�;��Q�����Uԕh��w��  6z�$N�Afޢ"�o����ƗU
Ę�A�&XB���W��v�0��b��"�7�~}��������@.?@�X �aE�P�$@�k,��(r[U­�B�@����t2�w��0Qxr���Z���/��j�O#�/�|)fl3��;bƊ�LK^,�`P�W$;����YYm�fEtAD��0/���4@f�!J�w��Wb��G��1Q��r�DA2��\qD�5"�Q{6 �"pY����fd:1�)��0�0�Y�н��&��֬JQ.M�P���,k��@�r(��Z������'�6%i0SYk{Ʉ����@4b7�9t���0ל,G�UOȰ
�)�׭ȳ��k�E�xZ2PL|�m�X?�@0!V<��aP8�(�T�����A�6@�Љ��e�)˭Ӳ	�ը��
�R���gh��Q����ʻ�򮌓��+� �+�䏍|�.�2]<d�V�&�Hb�M�A=y^ c "h�Y����v&��m��t�ͺ��a*��t5Ē��.K�#��u���%*^t�0�ţ���HI�BbJ��6�9W�T�L�����!1|��-ؼ����p�`J`�����8#����2i��B k%ƚ9�ZyM�"0�H����Ҕ��1�j �(2Mֺ��d �/ĝ� 
�э��W	����AHx9]*�L���b}��{G�/��0A�3�
�H��5)De�pT����" �H��e�PqqI�U@���$P�鰘�p��*�l�F���@) yi��ޔ%���X4�٣�X?��U�-�ѫEn�IQ�7�X`+�Q%�"���
O��RC<�����*�?�����Q@�,�X-�D��CWވh��5��k�b�zߜ2�Ll�&�o�TL�ٛ)�韆X�6����D��¡�
���C�@������%#��SC�A���:^"
I'!���ZBfg���P�Y�ſ:�U,�@��L�$d�N����"sBo��p��i���f��,�uF5P���* ���A�DښI�aK��j.S��@��d`
:�qoc'�H04Ǣ`X� cn�Q��J�6����-�
��sf�JQQ"�
/��u)2P��̒�g`8M|P��E h���E���,� �)�eqa#�ܰ��P;5�k�f��C26T7i�{���{e���9��J��gtR��rYblA�,_��dy�1�X�qU��̢y��E�m�+�e;�qˇ��Z�=<�TdQe�d�lg��Qa恓Z>�B��ԯ�;G0��D�[�a����R��s�\B)��)�ҋG��L��pJ�V��L�xP�f}�;#�YXu�����&�`	�O��l�dÒ"�GYzȢ#��6��AꟌT@�#"�"tO�+��e0"���J����f�M��y��T�us�A��E�w�{��! �%�!��u=<����`9k�<���eV��PBT�m*�I&�C}����H$3=�Mc�c�~4�@LH�{0��(~&�?�p�1��x��SIn��>��^����~,�QQ�4�.�"(Ë��"/p�N���F-�4�%�dw ��7� ��k�%�,',�ド���KX0�\1�yH\��^M3����4H?d���=+}O=DE�����|d�=�[E��HE��f��L���yQ�԰�dLRӟ�W�V�mtK���޳hM�B
ef�D�XL��nL�x��D���j��B��|V�Հ�aR�a(�X�a8:ψ�W�S�	���5<��P9��>��u�K¨`h2�H=�eQ�ų$T��ʯaG��I�������P X�,��(����`
~lD@    �B��c�:HW��J����iR\��:�(4j��1�9�8�;ʌZf���n��=�ظ��Xq�U��Ed�N�*�Q	���Ŗ~��3�F����1�$�����:`���%(D�(V�PX�+�&cE,X��sad�:	s��E,�M�Ì0�#{s\��-�
�����#��ug�3}8�P�D��VE
ϐ��+���́�:�Z�nx\C��юH?Yq�["6�j�L"�%C�\�3]��@a�D[�b:IY�Zi@yq���h���q��Ô򇇉�Œ,��!$>���
�ID_	š%:Swb��BZ�
{��Y����b̫�A+N-���0&�▞�DQʰ�M�g�����ī8�XN8@�R�`q$%70R�"R;N������J`��#�RE�cl�f�h	�
��<|2����zV����d}��@dr�`g&�UG��)��	���%#_�
h2@���̀�4f�������W�� YP�L#���`��+���9v^&�Q���$�n��4�-�fP�i��b�52���X���bI0���g����U��?��& �L��5D�={Ա3�(~�=�AU�ܭqRC\�����䂵A�������P�Hv�9Q$�>�E��,)���!G&ѸI2�@�@���7��xT[
|Oc�ڪ���P�q��5�c2ˠ��Ih��"��=s�g��'^��;��7f(R��Aw�t�mD�ޓNM)��l��lC�٘ AX9�VN����(�L�Q���n�Ӡt��Z�@T�u��;�"���?�I��xG�x4� ��!�T�s�e�d�q�f�Ŧ�w𼚣�+��3�
j��h�'t&$ë��TPUM|��r%�y��D[��$�	<��U#���$.z��nf_F<,Q0�E-��A􄃆ڬU��+�<4�H��,�$߽��bC8.;��O`�2�2�q�z1ܬ����=@E�1�8���H,�����u\vg��d)�Q��DF����i𘸄"q�i�6�'�95u���wDkiDdſ�C�?ygirt�2�~p��1�F�_@�	�-����Ua��s�
�'H쓁��3�4A��}�O�cH-9A�9��}bn�X1b�0݄@�<4���D���03H��hN��|hY��z����k�[�9�O�\e��f���KIƙ����0��dM��>3���M�ar�������k<OY$�[�:�Ć��T��5	G��ֈ��fu"
�R�� dX-M�MF���R��x��QH�Z���&��\D"�LF�*�2�YA�C��8b�9s����z�~�	i���yM ���;�yj�ڱ�_ �O�g�pe��ħ!R`�3�A�����G�

��0+mQH�HѪuk�?�d�.3��P6��X��9�&J�u�м�x��%�� 30���C�g�ԈV5| ����L`�lFm�Ǧ�n|�S� !�N隌I&P"��=oU�#q��d�Ss@���w�_|06.�w�� �3{��AJT����Ȥz�ɕ9x�8J�Y���p��9��xX����v#
;�8)����e�[h�\5�����j4�j6u�:�W�;HuwC����w�+R��Ѝ���|�7���fzH���C�O�AZ���"I��@�Lɰ�'Uax��(B1�1�E���Ǵ{}96� C͕�9#ef�JB�L��I̙h�rH�� 4��*1�W��F7ي�1k�s���������5`��4�ai�x��ދ���Ra�ޖ5�_����c(|�l���Q�5�����Xp�6W��	=BuO�|TΓ��.����:-zh�1�ѰM�F=ʗ�a<�%�����#]��ld4Tua���Q36��`0��G�l�:�]��3�*\�	]����A��7�~?d��ԉ��X��� ]!���G�a��c��*@��FG0C�g��!��ٰ̊��&��F0NԎ���sѪv�~9S���z��`�����Uu���I*B�e��!�0%�ѐp�٠!e�vl��G�A�Q]jd�t�c���)��J8����c+��J8���coF&f�X^���ң�pzrq�������_C���MȲN�����+�ݺ�_K�����.ʎ���|���?}g�^�|��|�,_+����|�,_+�כV�����#�T��{�Ǩ�mL�Y��!��'j�F�7`E%;�X>F�'e�-tķ�P%U��Q�x����	U��`�g��T���~\' ��O�c�Hñ�7k;]�l�;�N���`�R"���Z*�W�MpF(��M�n�aB�9�|�0�-[�>z4φ�����Y�]tyo���U�F_߬�%>)3�-��@rD����ΐdD/��C�2t�0$�q#Ҙ��a�R�/��UFym`�Dd�LFN������ſe��"���k��F��}^�lQA�'p�[����3�؍���׈L���ߜc���~�P�(�#C���*JR�LrR��4&,�,H�������fl�u�0��g({�� Z�&G1��j4�c�N���q�\�6r��:4Z���@Ej�J�
�����|H��Sg�p`��a��uTw�Y!�H����**s(-�!���T�;�;XkД1R�F(A�����[k�v��!�R+�#Q+a�XŴ�w��D��4^��D�Q"�c��އ�N���\�1R�uB#?A�	n����XϨT�01v?Gp�,5��21���)��4��tJ-��@���(-�AX�g��6��z�7W.YE#D�4.����s%�޸ve�hB3����c+_dW��Aa �mr����0��((s��ʟ`�nM��H&��9?D�TW;i�N���N��h�D��0 �IyB�Z�q���j[���[��`H��&����ؠ�������B����*������	��}y�G�����2ᘢ�X>V���F/x�_5z��������3�1�{֊��n���z�Ӱ"?}��7�E�U�}�#���wB\��Ax���^�F-�"��)53�]v�fO�y�w�7�n�pfĜҩ[{�T��Ca%���Ή��5��D7�{�[��l �b! �Þ�Be��Ϊ�u��-�{%bI�"tњ�W�-
4wDY�����/t��࣢Jֻ�vgn��b:��F�CK[LK��1��RVp�/=7c�B�)�s�),:�>��$�)�v�3	Q�V�
\$��ŉ_�b4F�p��C�蝁�3�h0�v6  ����֞L� K�!zێ_-��&kl(��<�a[!^�%�b�za����T+ݦP&��V�W�Y���1*%{���߸����+�v-0 �q5�,�q�8����ŀj��	@y7F�@�-/�3{D���lW�lg`,�`�`3rz**���L��b��Z�<L3�ɷ�8���\?3�.�t��du�<}���l]+��'.�jb�H�n�o$C��H�XȗQ�<�@�t-��[�@1�	-�H�"�zh��ʾ�bh�t��L��%VF���Y/�B�FA	<�Y� �4����H��z�rV�����p�Q��a��"��8��g���8�6�X	�
�1a�,�����I2�.�y��!>[ŋ�L	]��� <�XYF�;� ��ʟ詑|���� Ռ��P=*�����Q'���yo��Jz�A3n<�0Ho�9���o����]�N�@��荳F����u�@�iz�h4������z\���� �=�z1[C4+�M���Z�Fs��E���|'(�M0>x�Ə���u:ֳ��׮�q�O�(����B�����;��qj�p�?�9�Q�L
��=�I��I���3�GC��1�l�q��a�� ��󳓈�*��C�6J�4�cV�b��fŵ�V���(�6�\eݖ���N4�B�y&\�/��%T����F���m�"[�����+�)1p�i֊���c��5�9Lw�
f*����cУX|"f�f��b�J� ��-    ����k.���Xb��+Ve�?�2�JL:Ԁ'!Xm�O�[�S˓[|���65�̌�����נZqq��p�F3������*��7�MR��gES0�YB��[�Țl��cJG,p���d�5a��F�ȢD�:�����%�2��Ә�FFz�k���>��Ic�	Coy���־�#�iV�g������SO����!Ƴ#j�k�5*=N׬1>^��"�����m�Ĳ"��yYX$7m�ޖ�� ����͵�ƀ
���X�F�T�F��[��IYb�j�@����&hq��{�T6%$Ʋ`�bg$I��ꦨ|�peK�[�����4�2b��= ɿ��(+?�q�Q�U��|�BcJ��Ln����:�J��j�hG���r*�Y��7���А��1;jH(�a��%�+$��V��dUbt�C=��X��wݑ�Z36��װ��+�p�pTǞx�;�JLj�r<t���J2XYB��n"z��I1��=ZFȦ4������9!v\�D�aK�H��wJ��	��G|<�E�H�Q�` �
R�FкA�xe�1�"-id�ê�Q}��7�l2-�j�DP�!YZ6�n�R���q@k	8Kҹ̚}q�xX��֊�MBT��ae1~nD��L6u�XO�̾��jӰj�YO�C�.\�RB���c\��Me��G�7�6.[��K�'=2�E�����9���E��xjGe��9Z��h+���iM7>��gw�ӟ��#hs:.,�$o����Y�1��6	^׷=��E	�ft=��0�J�F�������A�l5:�rsϢ���X�<Oǰ�Tᛠ�(�Ɉ6Œ�W�<I���E;33�1ƀ�o�'~F��8O�N��r�V2Ԁk�/t��x��dXͱ0��?
P����x#����He�3R8b:|ӦF���:�0j��v5Z�l�;���p��/�޺^����%�P�����X�)[t�����Y=@��U��x�H���pFjԣM�^��O��޹*䨇[C�9
qJ�:[ �MG1V#�,�l�z1�n�%���◟P�~0<�1*��D�N�TK���|����EPa"Jԟ̉��g����:3���o��aO��b ��,+��I�~�9��Jy�M�q{p��&*��� 8��'%��$�z�q�FD��-�:��GC����D�8�`��{A�x:G�x�,I��&��5:�}z���Fe)��X�P	����(�8t��Q��fJ�SkI��U'T[�6�ΛEb�:d\)$V
��Bb��X)$ޖBB�I�Y�E�U�M�:V�*�\i��v�lu�ʕ�Y���ӂz"��,��ŭ˻�n]n��.����Z�:̹���h����e��uY�\�"׵�u-r]�\�Y�\��U�.��\��:�e-t]]��
]�cU�.�K]��Z�e-v��Z��A�.G�v]n��.����Z��>
^�#W�.�K^����e-z���.G�z]n��.�u��Z���\����u�]���׾.k�Gk��Z��Y�_��׵���Z���!����u9^��r��uٯ]�ص ���+`��%��~���E�k�Z���E�:v-�]�`�"�_Y��
v�]����.k!�Z�®��k!�Z�®��k!�Z�x-�]a�Bصv-�}x!�}ۯ�����?�E�K�?n�lϏ���G����ߩg���g�;{�������_�=�מ�k���g�ڳ}����Jk���lw��Z�Ӌ�K�4*|�I�K��Oq�,���5G.��$ELf������b�;|	1�A<Z������"� �v3]Q�f`����"�%sρ��v̺,�S�cVd����Uy�☍i��_�" �%*D\�GP�!D6a�Ę]DP�fCsNt�Kޢ�9�h1;���(p
h���2���`�$'w��_��f���-�ֈw(��@]d���hV.����V\�d�X�Z�Y����8\�#	>@���(�EQ3Jx��2��Lp)5���2��T|����AP�b�=��mn�}j�7ai�[�O�E��2�v"��X�M�!0��Sh�:Y�T�E�'C�c`%�s(*=
3H6�	��	���?��&����Ŵ ��d�XD}�Yd��<p����rvq��]��#NY亖�����Y�LM����F�|[V攡D�ﭤՎ�l!�dj06�rA�zLFu�
2��r��& Sfo��2�r6;D�YpU[u��+#��D�h�Dޔ��fgBNs&Ѫ%E��\��(o�= �Sm�/�)`ٕw�
S�Za���c HIN+l�  ��j ]ާ���(��� �eKdd�	�B���h�j��d�ª܀3���G�?�	�
fh*�2�az�����4��PƜ�0��>�@��4�[)�����`���#W�R�lr��b������R&� �Zc	L�F��B,n-� :H|H�+��+T!�	���6��`$�[�H�0�da!{Y��K1��&�3Vd��X�bA3���"���oLI�jJ+B"����y9,M()��2+�J�Ce�2��?f�C�ѨSn3����o��!�$3���GT[#�Ef� +B��P�X_k6�@�S��s�e�{@&i"�j��#\�фT v�L!� �����4�"j�Js���L�xy"d`��#����L�jA͚�D#vC�C����c��Ѐ%X�����25݊<;��Y���%r�������R�b�smn����O�0h�h���_&�ʴl5��<�C�T:4����C|+eG��OF�r,Ε۔+��++�
m8^l%\�7�l�+ە��t��|C�ĸ⁅`=��1d�LS$��&㠞�/�1�4�,Z�k;��u"2`\��f�Hr�Y�`�I��t%���|�:���/�h��Q�BE$B!1%�H�Ȝ+t*c`ՂI�a��s�l�����6m�>k��I[<(X�#k<Έ4jb�L��'�� R��f��X����#>k�4%�t��p�L���f3 �qg2��ktc��U�0���^NG�Ás�5CJ�@G��h^�����+���͘v�.�/�x!&Xy�|B�Y{<�&��+0�+uT�T9=�¶�).�#ۀ|�
|מ�Tc�#�WV��MۈW�(`/-�ӛ������<{T���X��j�E>z��m3)j���$��DUB$Y X�	�y�h��r�RE�G�T��<*# ������H����mv ��@~U�[�@澖��\�ڞȶ"�@���**V�f-���7S�?�m6�*7��)WC!�6#���^�7�	��#KFѧ�ڂ�.�u*�DT�7B$����
�>�Ύ�;�ܲx�u��d@�����Iȸ�\u��E��ZCe�Ѩ�����@-*�r�HK7U�;�كx��5��Öґ�\�0� �Q����r�-
���N�Y	�`h4�E��������8w��lD[@33Z��=�/��"
Ԛ���^�Nd����%!��p���(.��ͮ��	0�Y��9r0��.�F�a1��vj�X�໇dT�"n<����U!��0�s2m+�H�]7���;|��Ђ7Y�!���cD�"�$�*ٙE�x#�$�Wkr�E=^�{x
�ȢʊȚ��Ɨ��$��)�|(V}_W�_��v�d3�3�`����j	8�/r����� I�R��S��->��	�Fg����8��7�4�>4wF����:� ��M�����ٔ���B"����.G�5Rm����?��PG.D^E�TV�k��`DF���D�	���<�e󤧩`��z� ��|�����'C@�K�C�}k' z*x�3j)<��rV��<���e���5BTilJ��&�C}�A���$3��Mc�c5~�3�/&�6?YTT7��P��N<UΩ$7��RD/�z|�E?���es�u����U�8^'��C��d�;�n�@�Z�5�4�� t  ���DUFv��)�y���<$.ji���\��i��BW������y��yz�3����8y��yތ��xK`��;k�݌��XI�a��"/��V���Ij�3�J��
:�n�69�{V��\H���h�	"�ލ*�LVۂ�|Z�2�#[H����*�P0L��>e��!G�Q�jyJ1!]`�1�@Ǜ*�އ�"�nqIMf���<��,�x�{�q]P�5�hQ2)�"�Z�0��+��7�x �L�{;)Q��2��Bi=���[�a�;�
�S)s��!� M�Ug��Fͳ�=�u�gǉQ��8�Q�mÑ�g�Rˉ�R);�h�l���Q�@0� �����ow&�(�sU`;Ɛ�2� �P�K�P�\�U���C���qA�d,w�p#���Z'#�����)~��xdo��ؾ�H@��	xdҸ�YF�P(\(d"Z\�"�g�Y���ɊI�b����@O-V7<.�!N�hGӣ��7�-�k�W&�!X.4����s�0y�-R1��4K�4����Gft��Wȸ��a����DO�bIy����w{ �������;1@C!oR�=m�,C��T1�Uт���Έ�Q�,qK�d�(e����3�\�� �Y�Uf,' D)|��8+�(�Y��&dei{�l��Q�o���ٱȵ�;��
Y��l��Z��G>DeTY+�T������` 29�5��3�˪#q�����gn񈒂�+u4� �a�f�{��%{$�J�+�{�,�q��׊E��v��V���;/�˨��P	��7w���u��v3���ˈG��Q�k4\�@����3B��Ҫ���Z�l&�ɉ"���=��M�� *R��9�!.A���rr�z����xh�x��
(N$uF���(�	~�5��Je���
�b��#�hܤ�N ��Cٛۊl<ʇ-B��
x�S�*^��8i�ꇱ� �e���$4�F�`�9ųMF���3)@Ѡ�P:�6"e�ɗ�v~�EC�!ՃtK� ��K+��J�tҥ{��#�������9?�^	�(�EP7$aPN�R�V ��:����}@��b�������<�ZP�@*ֶ	3c�?�8�P��bS�;x^����Йj}J��Z��U��F���&>m���Gk���Y������R{q�PT7�1���(��"�vC� z�ACm֫O��Z�Z�ˇF
�����k�!��r�'0B�}��7�C�nV��f����hb����`$�LT���:��3YO��⨲W�"����4xL\B���}����:)p�;��4"��߆�!ϟ��49Zz1?�5B㘈tD#�/� ����Iժ0����|�$z��S˙C�`i��Z���1��������>17E��q�nB X���b�"X�i�$rd<�Y� >�,�b=��G��ԭ���'5�2��`�Ffx�ť$#��l^D	z�r�?��mx��J�&� �0	}B��M��5�,��-Iqb�~c�X����"�Jk��a�:x)VtS�2��&�&�O��~)�}A�uG����d�Jш]���Kg."�N�"��H�ﬠ�[3�ޜ�\�k�=Y��ń��E���&�!K�ߍ5Gm��/��'�3��i����J~��)0
یn� �go�p��y@Y��D����(�[��hU���v��2Y��y(��,� �v%��bh^S<R���6o�	��l�!˂3ljD_> �rO�� &0���6�aS�7�N�����L�tM�$(����*Ñ�T��f���9���G��/>��;VL��MtAw�� %�� ��kdR��ʜ<�ެ�	�]�j��Uq<�fh�N;��U���ڑ���2�-��E�	VQx_5�u5��r�ԫ�����F�$���k)v`�F�[`>ٛF�C3=�XO�!�� -H�Y�$�[ H�d���0�\A����"Tp��cڽ���������d%�E&��$�L��P�#�d0�����+ύZ#���lEr�5@���Z�Iqn�ZoPΉ
�M��0���Z<�f�E��u��k���	o�:D���e%�1>a�ME�(�ԂCAx�{,8�E����}����'f>��I`a��Ob�=4ɘ��P�Q#��K�0�`��ofn6�.HR62���0B
���IMPW�#J6K�.��u�.z�����n� �	B�N���E
�Dnb��bp�e���磇����/��T���V� ~gG#���3@�V��X�D�vXi#'jKn�j�hU�远��P� ��x0@Y��h�:� �$Ϡ6�|�����hH8h�lА�l;��Σ�Ӡ}��.5�M�ձ��㔝ge[��V6��Mle{K6������� ˻�Yns�,�� ������� wv��h� �m~�e� dYBV���iV���!ĭ!+C�?C�r<���6GȲO��,!+K��R���&d�����,+Sm9^le
��)d92U�r�+d�'YV����-d92]�r�/d�'YVƐ�1d92e�r�3d�'YV֐�5�h�!��hC�ۼ!�>qȲ2���!+s���2���!+s�����9de9s�r<��6wȲO���!+{ȇ���>d�����,+��� �2��"+��� �2��?V��+��� �!3�,G�Yns�,�$"��"����,"+���"����,"+���"����,"+���"��,"+���"���|�,"P�/��)�C'D�^�\����哿=!��:�i�r��}�<���vD��ŹG�ϯΞ�>��7�)呌Y�_�^�������Ջ�EC�����w_}��2~�t~����<����7�}����p�<����.����/�7����_��]]>{�t�O�m8��N���#OQ�����d�����M�%F����vs��:�^o��_�|�+�ػ�����/�g�e��o�N7�ʥ�.�矆'z���/6�/���>�n����e����M|��?_���]��O��Ϟ㊧������zsy��\>�,?n�2�痿�]� {/�6OO������7�����v>�=�smO���}|��q��EN�ֶxk�ܽ7���z�qܸ{nn��MYn�2�n#?�i�^w-ψ��
�>���{���v����9&h_,��ϟ��7����E7�      �   |	  x��\[o�:~Na`qRl���Ď�`� ms��[{ ��pW]�J����!��%+�$;��*�:g���I��GXw�G��3��|k���%D�������xL\�����M�a��9�.)Js�����
(�`>��Y���S҈[A�B�ڜ`I�g9�	�' KPo�8��0
�9�Ա����x ��b+�~F��9�Od�6�ܾ�&����zq�я\ε��]rȱgF4��M&F�_�4�B���֡� �T�N�|�1�R��:D؜�5r��=�H�A��ţ[*�΂�e.�M����$�S�8��;� \b��h�����sYBbj�C��OU_�"Z�&O�{=�DJ:a��Pɧ�CD�������g@�l明�'$��R���
i��n"z�=��ä�M��s�S�J�����H�Ʉp��D�
M8�!yG���Mt�8z�=G`�V�"*F�&cy�8�>���C��?~Z]����4nh_ ��?�@�$�`���\D������H#i�MA8�aF�G���f�� ���8 p��{�)8�w�RH���F�Ɓ��D!1ˆ3Ƿ�5�3�.7k8E_ldx�`�@I>�rC���5�B���l�	:D�a�o�I���o�K��!$pP�G�����ú�2��+��m}�0�C�/$���E?�uZ��a�}�m�N{pt:h5�Nڭ���Z{x©���~|Ӂ��E#�[�A0�j�[F���;�mt�>V����f3�������j����w7ʈ)�c���zʸ�Fe&>o�9�Fn,���_��d$q��� C�/���Q!n3��l#?��ke��2��J˪g+�1�!*�r:��mY�Pe f��KH����X~�e�UL�����!qЌH��T�������&>�o��9������0�
"&���a �Nʹ�{���7m6{wM����g�� w��a��h��S����I���$.�oɗ+Q*zV)X�0������Y���m��|=����1u�֬hdx�M�}�iG÷UM;�e"ۈSt8�+b���i2��U5%�u=��Ж-ß�ۭj@�?�,�$��Y}=��(5 n�TRsk΀�Ru!4-���%�UU@���R�k�3�`p��Jm�>ؽ�e���Fo�\������~�E�_W�/�����T8��J�D�<+�ڌ�>Y�"�B��E=#6pa�Z�~q�J��d^]��V2���
�I�e� ��l����w!È���~���:@�<��z[WBja�)��h�A?}F�M�Q LśΠ}<����^��?Mƛcu.�N,̝��jK���M���������e`��i+k=\�{��)�}sD8g\%8cB��i��&�S���*�
Rȩp�.L���L�.�l+ӡ0ȉT�N�xޣ20(����b���Pϟo/n�_�Y��e����z_ƽg��*ӻ�2�OfX��^jG�@��s�9���%�����E5�/V�a«��β [
@%�� x�j�e�c�c�
�m�;å��fsƋ�QeƐ��/��n��ZY��@�EoX˯zͷjw�!:T�`X�c�|�_}�U0���엻���.-��q�}5����,��J�x+�X�����c����B߳����O�i��e�$Y�~��-[�c�烸�UV����D�g� ���S5AKH��b�؊((�ޓ-2�5em*-�Qx�l}MƖ�ko�*��5	Y��R�c\�(km[�r�Y���ݠ�j�S�(,�vaՙr��g�[wFk��qk+����]a�X�fY}���ۮ��G�OQ�|�\�춢���uop�k�����z�M�Ħ��~d��m�[��+���O�y<z�ǿ��կ�e�
_�x��|�{(`@`�.�U���p�b�����ee���E/�:�j
�k\�0��7Ҧvs� �}Y+|�@��F��Kߓ{��v�8���H�;nu;�d�S7��/���ԓ�i���ʮ��ޠ��P��&�[��r����w�^�gz[)_�KIʀ��v_�����DP�7��˽����-�c�'"�v}�'
{�//d�V�Qt'g8��e +D%��iۓ]�,u`�1^�[f����T�WE��1p�Bg�h�GJ�Of(�p�Q�
ws]�{j��k_��br���#pA�"V�Np��K��1���B%B��4�A����2�R.��^���)��(�G�C��H�%)�	��	t�g�	�K����#�cy&(0�����q���l�D)?��b/~�K}����.)�����|���NN��R����{��?�u��2��S^g����{��B�.��B�.��B��*�.�W��Y�M�y�J/f,�C������*�Vy�V�"�^�J����R�z_�o޼�?n-��     