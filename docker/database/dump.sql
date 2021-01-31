--
-- PostgreSQL database dump
--

-- Dumped from database version 11.10 (Ubuntu 11.10-1.pgdg18.04+1)
-- Dumped by pg_dump version 11.10 (Ubuntu 11.10-1.pgdg18.04+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: agdc; Type: SCHEMA; Schema: -; Owner: agdc_admin
--

CREATE SCHEMA agdc;


ALTER SCHEMA agdc OWNER TO agdc_admin;

--
-- Name: float8range; Type: TYPE; Schema: agdc; Owner: agdc_admin
--

CREATE TYPE agdc.float8range AS RANGE (
    subtype = double precision,
    subtype_diff = float8mi
);


ALTER TYPE agdc.float8range OWNER TO agdc_admin;

--
-- Name: common_timestamp(text); Type: FUNCTION; Schema: agdc; Owner: agdc_admin
--

CREATE FUNCTION agdc.common_timestamp(text) RETURNS timestamp with time zone
    LANGUAGE sql IMMUTABLE STRICT
    AS $_$
select ($1)::timestamp at time zone 'utc';
$_$;


ALTER FUNCTION agdc.common_timestamp(text) OWNER TO agdc_admin;

--
-- Name: set_row_update_time(); Type: FUNCTION; Schema: agdc; Owner: agdc_admin
--

CREATE FUNCTION agdc.set_row_update_time() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
begin
  new.updated = now();
  return new;
end;
$$;


ALTER FUNCTION agdc.set_row_update_time() OWNER TO agdc_admin;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: dataset; Type: TABLE; Schema: agdc; Owner: agdc_admin
--

CREATE TABLE agdc.dataset (
    id uuid NOT NULL,
    metadata_type_ref smallint NOT NULL,
    dataset_type_ref smallint NOT NULL,
    metadata jsonb NOT NULL,
    archived timestamp with time zone,
    added timestamp with time zone DEFAULT now() NOT NULL,
    added_by name DEFAULT CURRENT_USER NOT NULL,
    updated timestamp with time zone
);


ALTER TABLE agdc.dataset OWNER TO agdc_admin;

--
-- Name: dataset_location; Type: TABLE; Schema: agdc; Owner: agdc_admin
--

CREATE TABLE agdc.dataset_location (
    id integer NOT NULL,
    dataset_ref uuid NOT NULL,
    uri_scheme character varying NOT NULL,
    uri_body character varying NOT NULL,
    added timestamp with time zone DEFAULT now() NOT NULL,
    added_by name DEFAULT CURRENT_USER NOT NULL,
    archived timestamp with time zone
);


ALTER TABLE agdc.dataset_location OWNER TO agdc_admin;

--
-- Name: dataset_location_id_seq; Type: SEQUENCE; Schema: agdc; Owner: agdc_admin
--

CREATE SEQUENCE agdc.dataset_location_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE agdc.dataset_location_id_seq OWNER TO agdc_admin;

--
-- Name: dataset_location_id_seq; Type: SEQUENCE OWNED BY; Schema: agdc; Owner: agdc_admin
--

ALTER SEQUENCE agdc.dataset_location_id_seq OWNED BY agdc.dataset_location.id;


--
-- Name: dataset_source; Type: TABLE; Schema: agdc; Owner: agdc_admin
--

CREATE TABLE agdc.dataset_source (
    dataset_ref uuid NOT NULL,
    classifier character varying NOT NULL,
    source_dataset_ref uuid NOT NULL
);


ALTER TABLE agdc.dataset_source OWNER TO agdc_admin;

--
-- Name: dataset_type; Type: TABLE; Schema: agdc; Owner: agdc_admin
--

CREATE TABLE agdc.dataset_type (
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


ALTER TABLE agdc.dataset_type OWNER TO agdc_admin;

--
-- Name: dataset_type_id_seq; Type: SEQUENCE; Schema: agdc; Owner: agdc_admin
--

CREATE SEQUENCE agdc.dataset_type_id_seq
    AS smallint
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE agdc.dataset_type_id_seq OWNER TO agdc_admin;

--
-- Name: dataset_type_id_seq; Type: SEQUENCE OWNED BY; Schema: agdc; Owner: agdc_admin
--

ALTER SEQUENCE agdc.dataset_type_id_seq OWNED BY agdc.dataset_type.id;


--
-- Name: metadata_type; Type: TABLE; Schema: agdc; Owner: agdc_admin
--

CREATE TABLE agdc.metadata_type (
    id smallint NOT NULL,
    name character varying NOT NULL,
    definition jsonb NOT NULL,
    added timestamp with time zone DEFAULT now() NOT NULL,
    added_by name DEFAULT CURRENT_USER NOT NULL,
    updated timestamp with time zone,
    CONSTRAINT ck_metadata_type_alphanumeric_name CHECK (((name)::text ~* '^\w+$'::text))
);


ALTER TABLE agdc.metadata_type OWNER TO agdc_admin;

--
-- Name: dv_aster_aloh_group_composition_dataset; Type: VIEW; Schema: agdc; Owner: africa
--

CREATE VIEW agdc.dv_aster_aloh_group_composition_dataset AS
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


ALTER TABLE agdc.dv_aster_aloh_group_composition_dataset OWNER TO africa;

--
-- Name: dv_aster_aloh_group_content_dataset; Type: VIEW; Schema: agdc; Owner: africa
--

CREATE VIEW agdc.dv_aster_aloh_group_content_dataset AS
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


ALTER TABLE agdc.dv_aster_aloh_group_content_dataset OWNER TO africa;

--
-- Name: dv_aster_false_colour_dataset; Type: VIEW; Schema: agdc; Owner: africa
--

CREATE VIEW agdc.dv_aster_false_colour_dataset AS
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


ALTER TABLE agdc.dv_aster_false_colour_dataset OWNER TO africa;

--
-- Name: dv_aster_feoh_group_content_dataset; Type: VIEW; Schema: agdc; Owner: africa
--

CREATE VIEW agdc.dv_aster_feoh_group_content_dataset AS
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


ALTER TABLE agdc.dv_aster_feoh_group_content_dataset OWNER TO africa;

--
-- Name: dv_aster_ferric_oxide_composition_dataset; Type: VIEW; Schema: agdc; Owner: africa
--

CREATE VIEW agdc.dv_aster_ferric_oxide_composition_dataset AS
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


ALTER TABLE agdc.dv_aster_ferric_oxide_composition_dataset OWNER TO africa;

--
-- Name: dv_aster_ferric_oxide_content_dataset; Type: VIEW; Schema: agdc; Owner: africa
--

CREATE VIEW agdc.dv_aster_ferric_oxide_content_dataset AS
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


ALTER TABLE agdc.dv_aster_ferric_oxide_content_dataset OWNER TO africa;

--
-- Name: dv_aster_ferrous_iron_content_in_mgoh_dataset; Type: VIEW; Schema: agdc; Owner: africa
--

CREATE VIEW agdc.dv_aster_ferrous_iron_content_in_mgoh_dataset AS
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


ALTER TABLE agdc.dv_aster_ferrous_iron_content_in_mgoh_dataset OWNER TO africa;

--
-- Name: dv_aster_ferrous_iron_index_dataset; Type: VIEW; Schema: agdc; Owner: africa
--

CREATE VIEW agdc.dv_aster_ferrous_iron_index_dataset AS
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


ALTER TABLE agdc.dv_aster_ferrous_iron_index_dataset OWNER TO africa;

--
-- Name: dv_aster_green_vegetation_dataset; Type: VIEW; Schema: agdc; Owner: africa
--

CREATE VIEW agdc.dv_aster_green_vegetation_dataset AS
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


ALTER TABLE agdc.dv_aster_green_vegetation_dataset OWNER TO africa;

--
-- Name: dv_aster_gypsum_index_dataset; Type: VIEW; Schema: agdc; Owner: africa
--

CREATE VIEW agdc.dv_aster_gypsum_index_dataset AS
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


ALTER TABLE agdc.dv_aster_gypsum_index_dataset OWNER TO africa;

--
-- Name: dv_aster_kaolin_group_index_dataset; Type: VIEW; Schema: agdc; Owner: africa
--

CREATE VIEW agdc.dv_aster_kaolin_group_index_dataset AS
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


ALTER TABLE agdc.dv_aster_kaolin_group_index_dataset OWNER TO africa;

--
-- Name: dv_aster_mgoh_group_composition_dataset; Type: VIEW; Schema: agdc; Owner: africa
--

CREATE VIEW agdc.dv_aster_mgoh_group_composition_dataset AS
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


ALTER TABLE agdc.dv_aster_mgoh_group_composition_dataset OWNER TO africa;

--
-- Name: dv_aster_mgoh_group_content_dataset; Type: VIEW; Schema: agdc; Owner: africa
--

CREATE VIEW agdc.dv_aster_mgoh_group_content_dataset AS
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


ALTER TABLE agdc.dv_aster_mgoh_group_content_dataset OWNER TO africa;

--
-- Name: dv_aster_opaque_index_dataset; Type: VIEW; Schema: agdc; Owner: africa
--

CREATE VIEW agdc.dv_aster_opaque_index_dataset AS
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


ALTER TABLE agdc.dv_aster_opaque_index_dataset OWNER TO africa;

--
-- Name: dv_aster_quartz_index_dataset; Type: VIEW; Schema: agdc; Owner: africa
--

CREATE VIEW agdc.dv_aster_quartz_index_dataset AS
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


ALTER TABLE agdc.dv_aster_quartz_index_dataset OWNER TO africa;

--
-- Name: dv_aster_regolith_ratios_dataset; Type: VIEW; Schema: agdc; Owner: africa
--

CREATE VIEW agdc.dv_aster_regolith_ratios_dataset AS
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


ALTER TABLE agdc.dv_aster_regolith_ratios_dataset OWNER TO africa;

--
-- Name: dv_aster_silica_index_dataset; Type: VIEW; Schema: agdc; Owner: africa
--

CREATE VIEW agdc.dv_aster_silica_index_dataset AS
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


ALTER TABLE agdc.dv_aster_silica_index_dataset OWNER TO africa;

--
-- Name: dv_cemp_insar_alos_displacement_dataset; Type: VIEW; Schema: agdc; Owner: africa
--

CREATE VIEW agdc.dv_cemp_insar_alos_displacement_dataset AS
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


ALTER TABLE agdc.dv_cemp_insar_alos_displacement_dataset OWNER TO africa;

--
-- Name: dv_cemp_insar_alos_velocity_dataset; Type: VIEW; Schema: agdc; Owner: africa
--

CREATE VIEW agdc.dv_cemp_insar_alos_velocity_dataset AS
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


ALTER TABLE agdc.dv_cemp_insar_alos_velocity_dataset OWNER TO africa;

--
-- Name: dv_cemp_insar_envisat_displacement_dataset; Type: VIEW; Schema: agdc; Owner: africa
--

CREATE VIEW agdc.dv_cemp_insar_envisat_displacement_dataset AS
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


ALTER TABLE agdc.dv_cemp_insar_envisat_displacement_dataset OWNER TO africa;

--
-- Name: dv_cemp_insar_envisat_velocity_dataset; Type: VIEW; Schema: agdc; Owner: africa
--

CREATE VIEW agdc.dv_cemp_insar_envisat_velocity_dataset AS
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


ALTER TABLE agdc.dv_cemp_insar_envisat_velocity_dataset OWNER TO africa;

--
-- Name: dv_cemp_insar_radarsat2_displacement_dataset; Type: VIEW; Schema: agdc; Owner: africa
--

CREATE VIEW agdc.dv_cemp_insar_radarsat2_displacement_dataset AS
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


ALTER TABLE agdc.dv_cemp_insar_radarsat2_displacement_dataset OWNER TO africa;

--
-- Name: dv_cemp_insar_radarsat2_velocity_dataset; Type: VIEW; Schema: agdc; Owner: africa
--

CREATE VIEW agdc.dv_cemp_insar_radarsat2_velocity_dataset AS
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


ALTER TABLE agdc.dv_cemp_insar_radarsat2_velocity_dataset OWNER TO africa;

--
-- Name: dv_eo3_dataset; Type: VIEW; Schema: agdc; Owner: africa
--

CREATE VIEW agdc.dv_eo3_dataset AS
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


ALTER TABLE agdc.dv_eo3_dataset OWNER TO africa;

--
-- Name: dv_eo3_landsat_ard_dataset; Type: VIEW; Schema: agdc; Owner: africa
--

CREATE VIEW agdc.dv_eo3_landsat_ard_dataset AS
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


ALTER TABLE agdc.dv_eo3_landsat_ard_dataset OWNER TO africa;

--
-- Name: dv_eo3_landsat_l1_dataset; Type: VIEW; Schema: agdc; Owner: africa
--

CREATE VIEW agdc.dv_eo3_landsat_l1_dataset AS
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


ALTER TABLE agdc.dv_eo3_landsat_l1_dataset OWNER TO africa;

--
-- Name: dv_eo_dataset; Type: VIEW; Schema: agdc; Owner: africa
--

CREATE VIEW agdc.dv_eo_dataset AS
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


ALTER TABLE agdc.dv_eo_dataset OWNER TO africa;

--
-- Name: dv_eo_plus_dataset; Type: VIEW; Schema: agdc; Owner: africa
--

CREATE VIEW agdc.dv_eo_plus_dataset AS
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


ALTER TABLE agdc.dv_eo_plus_dataset OWNER TO africa;

--
-- Name: dv_eo_s2_nrt_dataset; Type: VIEW; Schema: agdc; Owner: africa
--

CREATE VIEW agdc.dv_eo_s2_nrt_dataset AS
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


ALTER TABLE agdc.dv_eo_s2_nrt_dataset OWNER TO africa;

--
-- Name: dv_fc_percentile_albers_annual_dataset; Type: VIEW; Schema: agdc; Owner: africa
--

CREATE VIEW agdc.dv_fc_percentile_albers_annual_dataset AS
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


ALTER TABLE agdc.dv_fc_percentile_albers_annual_dataset OWNER TO africa;

--
-- Name: dv_fc_percentile_albers_seasonal_dataset; Type: VIEW; Schema: agdc; Owner: africa
--

CREATE VIEW agdc.dv_fc_percentile_albers_seasonal_dataset AS
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


ALTER TABLE agdc.dv_fc_percentile_albers_seasonal_dataset OWNER TO africa;

--
-- Name: dv_ga_ls8c_ard_3_dataset; Type: VIEW; Schema: agdc; Owner: africa
--

CREATE VIEW agdc.dv_ga_ls8c_ard_3_dataset AS
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


ALTER TABLE agdc.dv_ga_ls8c_ard_3_dataset OWNER TO africa;

--
-- Name: dv_ga_s2a_ard_nbar_granule_dataset; Type: VIEW; Schema: agdc; Owner: africa
--

CREATE VIEW agdc.dv_ga_s2a_ard_nbar_granule_dataset AS
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


ALTER TABLE agdc.dv_ga_s2a_ard_nbar_granule_dataset OWNER TO africa;

--
-- Name: dv_ga_s2b_ard_nbar_granule_dataset; Type: VIEW; Schema: agdc; Owner: africa
--

CREATE VIEW agdc.dv_ga_s2b_ard_nbar_granule_dataset AS
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


ALTER TABLE agdc.dv_ga_s2b_ard_nbar_granule_dataset OWNER TO africa;

--
-- Name: dv_geodata_coast_100k_dataset; Type: VIEW; Schema: agdc; Owner: africa
--

CREATE VIEW agdc.dv_geodata_coast_100k_dataset AS
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


ALTER TABLE agdc.dv_geodata_coast_100k_dataset OWNER TO africa;

--
-- Name: dv_gqa_eo_dataset; Type: VIEW; Schema: agdc; Owner: africa
--

CREATE VIEW agdc.dv_gqa_eo_dataset AS
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


ALTER TABLE agdc.dv_gqa_eo_dataset OWNER TO africa;

--
-- Name: dv_high_tide_comp_20p_dataset; Type: VIEW; Schema: agdc; Owner: africa
--

CREATE VIEW agdc.dv_high_tide_comp_20p_dataset AS
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


ALTER TABLE agdc.dv_high_tide_comp_20p_dataset OWNER TO africa;

--
-- Name: dv_historical_airborne_photography_dataset; Type: VIEW; Schema: agdc; Owner: africa
--

CREATE VIEW agdc.dv_historical_airborne_photography_dataset AS
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


ALTER TABLE agdc.dv_historical_airborne_photography_dataset OWNER TO africa;

--
-- Name: dv_item_v2_conf_dataset; Type: VIEW; Schema: agdc; Owner: africa
--

CREATE VIEW agdc.dv_item_v2_conf_dataset AS
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


ALTER TABLE agdc.dv_item_v2_conf_dataset OWNER TO africa;

--
-- Name: dv_item_v2_dataset; Type: VIEW; Schema: agdc; Owner: africa
--

CREATE VIEW agdc.dv_item_v2_dataset AS
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


ALTER TABLE agdc.dv_item_v2_dataset OWNER TO africa;

--
-- Name: dv_landsat_barest_earth_dataset; Type: VIEW; Schema: agdc; Owner: africa
--

CREATE VIEW agdc.dv_landsat_barest_earth_dataset AS
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


ALTER TABLE agdc.dv_landsat_barest_earth_dataset OWNER TO africa;

--
-- Name: dv_low_tide_comp_20p_dataset; Type: VIEW; Schema: agdc; Owner: africa
--

CREATE VIEW agdc.dv_low_tide_comp_20p_dataset AS
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


ALTER TABLE agdc.dv_low_tide_comp_20p_dataset OWNER TO africa;

--
-- Name: dv_ls5_fc_albers_dataset; Type: VIEW; Schema: agdc; Owner: africa
--

CREATE VIEW agdc.dv_ls5_fc_albers_dataset AS
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


ALTER TABLE agdc.dv_ls5_fc_albers_dataset OWNER TO africa;

--
-- Name: dv_ls5_level1_usgs_dataset; Type: VIEW; Schema: agdc; Owner: africa
--

CREATE VIEW agdc.dv_ls5_level1_usgs_dataset AS
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


ALTER TABLE agdc.dv_ls5_level1_usgs_dataset OWNER TO africa;

--
-- Name: dv_ls5_nbart_geomedian_annual_dataset; Type: VIEW; Schema: agdc; Owner: africa
--

CREATE VIEW agdc.dv_ls5_nbart_geomedian_annual_dataset AS
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


ALTER TABLE agdc.dv_ls5_nbart_geomedian_annual_dataset OWNER TO africa;

--
-- Name: dv_ls5_nbart_tmad_annual_dataset; Type: VIEW; Schema: agdc; Owner: africa
--

CREATE VIEW agdc.dv_ls5_nbart_tmad_annual_dataset AS
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


ALTER TABLE agdc.dv_ls5_nbart_tmad_annual_dataset OWNER TO africa;

--
-- Name: dv_ls5_usgs_l2c1_dataset; Type: VIEW; Schema: agdc; Owner: africa
--

CREATE VIEW agdc.dv_ls5_usgs_l2c1_dataset AS
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


ALTER TABLE agdc.dv_ls5_usgs_l2c1_dataset OWNER TO africa;

--
-- Name: dv_ls7_fc_albers_dataset; Type: VIEW; Schema: agdc; Owner: africa
--

CREATE VIEW agdc.dv_ls7_fc_albers_dataset AS
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


ALTER TABLE agdc.dv_ls7_fc_albers_dataset OWNER TO africa;

--
-- Name: dv_ls7_level1_usgs_dataset; Type: VIEW; Schema: agdc; Owner: africa
--

CREATE VIEW agdc.dv_ls7_level1_usgs_dataset AS
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


ALTER TABLE agdc.dv_ls7_level1_usgs_dataset OWNER TO africa;

--
-- Name: dv_ls7_nbart_geomedian_annual_dataset; Type: VIEW; Schema: agdc; Owner: africa
--

CREATE VIEW agdc.dv_ls7_nbart_geomedian_annual_dataset AS
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


ALTER TABLE agdc.dv_ls7_nbart_geomedian_annual_dataset OWNER TO africa;

--
-- Name: dv_ls7_nbart_tmad_annual_dataset; Type: VIEW; Schema: agdc; Owner: africa
--

CREATE VIEW agdc.dv_ls7_nbart_tmad_annual_dataset AS
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


ALTER TABLE agdc.dv_ls7_nbart_tmad_annual_dataset OWNER TO africa;

--
-- Name: dv_ls7_usgs_l2c1_dataset; Type: VIEW; Schema: agdc; Owner: africa
--

CREATE VIEW agdc.dv_ls7_usgs_l2c1_dataset AS
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


ALTER TABLE agdc.dv_ls7_usgs_l2c1_dataset OWNER TO africa;

--
-- Name: dv_ls8_barest_earth_albers_dataset; Type: VIEW; Schema: agdc; Owner: africa
--

CREATE VIEW agdc.dv_ls8_barest_earth_albers_dataset AS
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


ALTER TABLE agdc.dv_ls8_barest_earth_albers_dataset OWNER TO africa;

--
-- Name: dv_ls8_fc_albers_dataset; Type: VIEW; Schema: agdc; Owner: africa
--

CREATE VIEW agdc.dv_ls8_fc_albers_dataset AS
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


ALTER TABLE agdc.dv_ls8_fc_albers_dataset OWNER TO africa;

--
-- Name: dv_ls8_level1_usgs_dataset; Type: VIEW; Schema: agdc; Owner: africa
--

CREATE VIEW agdc.dv_ls8_level1_usgs_dataset AS
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


ALTER TABLE agdc.dv_ls8_level1_usgs_dataset OWNER TO africa;

--
-- Name: dv_ls8_nbart_geomedian_annual_dataset; Type: VIEW; Schema: agdc; Owner: africa
--

CREATE VIEW agdc.dv_ls8_nbart_geomedian_annual_dataset AS
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


ALTER TABLE agdc.dv_ls8_nbart_geomedian_annual_dataset OWNER TO africa;

--
-- Name: dv_ls8_nbart_tmad_annual_dataset; Type: VIEW; Schema: agdc; Owner: africa
--

CREATE VIEW agdc.dv_ls8_nbart_tmad_annual_dataset AS
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


ALTER TABLE agdc.dv_ls8_nbart_tmad_annual_dataset OWNER TO africa;

--
-- Name: dv_ls8_usgs_l2c1_dataset; Type: VIEW; Schema: agdc; Owner: africa
--

CREATE VIEW agdc.dv_ls8_usgs_l2c1_dataset AS
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


ALTER TABLE agdc.dv_ls8_usgs_l2c1_dataset OWNER TO africa;

--
-- Name: dv_mangrove_cover_dataset; Type: VIEW; Schema: agdc; Owner: africa
--

CREATE VIEW agdc.dv_mangrove_cover_dataset AS
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


ALTER TABLE agdc.dv_mangrove_cover_dataset OWNER TO africa;

--
-- Name: dv_multi_scale_topographic_position_dataset; Type: VIEW; Schema: agdc; Owner: africa
--

CREATE VIEW agdc.dv_multi_scale_topographic_position_dataset AS
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


ALTER TABLE agdc.dv_multi_scale_topographic_position_dataset OWNER TO africa;

--
-- Name: dv_nidem_dataset; Type: VIEW; Schema: agdc; Owner: africa
--

CREATE VIEW agdc.dv_nidem_dataset AS
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


ALTER TABLE agdc.dv_nidem_dataset OWNER TO africa;

--
-- Name: dv_s2_tsmask_dataset; Type: VIEW; Schema: agdc; Owner: africa
--

CREATE VIEW agdc.dv_s2_tsmask_dataset AS
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


ALTER TABLE agdc.dv_s2_tsmask_dataset OWNER TO africa;

--
-- Name: dv_s2a_nrt_granule_dataset; Type: VIEW; Schema: agdc; Owner: africa
--

CREATE VIEW agdc.dv_s2a_nrt_granule_dataset AS
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


ALTER TABLE agdc.dv_s2a_nrt_granule_dataset OWNER TO africa;

--
-- Name: dv_s2b_nrt_granule_dataset; Type: VIEW; Schema: agdc; Owner: africa
--

CREATE VIEW agdc.dv_s2b_nrt_granule_dataset AS
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


ALTER TABLE agdc.dv_s2b_nrt_granule_dataset OWNER TO africa;

--
-- Name: dv_sentinel2_wofs_nrt_dataset; Type: VIEW; Schema: agdc; Owner: africa
--

CREATE VIEW agdc.dv_sentinel2_wofs_nrt_dataset AS
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


ALTER TABLE agdc.dv_sentinel2_wofs_nrt_dataset OWNER TO africa;

--
-- Name: dv_telemetry_dataset; Type: VIEW; Schema: agdc; Owner: africa
--

CREATE VIEW agdc.dv_telemetry_dataset AS
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


ALTER TABLE agdc.dv_telemetry_dataset OWNER TO africa;

--
-- Name: dv_water_bodies_dataset; Type: VIEW; Schema: agdc; Owner: africa
--

CREATE VIEW agdc.dv_water_bodies_dataset AS
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


ALTER TABLE agdc.dv_water_bodies_dataset OWNER TO africa;

--
-- Name: dv_weathering_intensity_dataset; Type: VIEW; Schema: agdc; Owner: africa
--

CREATE VIEW agdc.dv_weathering_intensity_dataset AS
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


ALTER TABLE agdc.dv_weathering_intensity_dataset OWNER TO africa;

--
-- Name: dv_wofs_albers_dataset; Type: VIEW; Schema: agdc; Owner: africa
--

CREATE VIEW agdc.dv_wofs_albers_dataset AS
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


ALTER TABLE agdc.dv_wofs_albers_dataset OWNER TO africa;

--
-- Name: dv_wofs_annual_summary_dataset; Type: VIEW; Schema: agdc; Owner: africa
--

CREATE VIEW agdc.dv_wofs_annual_summary_dataset AS
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


ALTER TABLE agdc.dv_wofs_annual_summary_dataset OWNER TO africa;

--
-- Name: dv_wofs_apr_oct_summary_dataset; Type: VIEW; Schema: agdc; Owner: africa
--

CREATE VIEW agdc.dv_wofs_apr_oct_summary_dataset AS
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


ALTER TABLE agdc.dv_wofs_apr_oct_summary_dataset OWNER TO africa;

--
-- Name: dv_wofs_filtered_summary_dataset; Type: VIEW; Schema: agdc; Owner: africa
--

CREATE VIEW agdc.dv_wofs_filtered_summary_dataset AS
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


ALTER TABLE agdc.dv_wofs_filtered_summary_dataset OWNER TO africa;

--
-- Name: dv_wofs_nov_mar_summary_dataset; Type: VIEW; Schema: agdc; Owner: africa
--

CREATE VIEW agdc.dv_wofs_nov_mar_summary_dataset AS
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


ALTER TABLE agdc.dv_wofs_nov_mar_summary_dataset OWNER TO africa;

--
-- Name: dv_wofs_summary_dataset; Type: VIEW; Schema: agdc; Owner: africa
--

CREATE VIEW agdc.dv_wofs_summary_dataset AS
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


ALTER TABLE agdc.dv_wofs_summary_dataset OWNER TO africa;

--
-- Name: metadata_type_id_seq; Type: SEQUENCE; Schema: agdc; Owner: agdc_admin
--

CREATE SEQUENCE agdc.metadata_type_id_seq
    AS smallint
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE agdc.metadata_type_id_seq OWNER TO agdc_admin;

--
-- Name: metadata_type_id_seq; Type: SEQUENCE OWNED BY; Schema: agdc; Owner: agdc_admin
--

ALTER SEQUENCE agdc.metadata_type_id_seq OWNED BY agdc.metadata_type.id;


--
-- Name: dataset_location id; Type: DEFAULT; Schema: agdc; Owner: agdc_admin
--

ALTER TABLE ONLY agdc.dataset_location ALTER COLUMN id SET DEFAULT nextval('agdc.dataset_location_id_seq'::regclass);


--
-- Name: dataset_type id; Type: DEFAULT; Schema: agdc; Owner: agdc_admin
--

ALTER TABLE ONLY agdc.dataset_type ALTER COLUMN id SET DEFAULT nextval('agdc.dataset_type_id_seq'::regclass);


--
-- Name: metadata_type id; Type: DEFAULT; Schema: agdc; Owner: agdc_admin
--

ALTER TABLE ONLY agdc.metadata_type ALTER COLUMN id SET DEFAULT nextval('agdc.metadata_type_id_seq'::regclass);


--
-- Data for Name: dataset; Type: TABLE DATA; Schema: agdc; Owner: agdc_admin
--

COPY agdc.dataset (id, metadata_type_ref, dataset_type_ref, metadata, archived, added, added_by, updated) FROM stdin;
\.


--
-- Data for Name: dataset_location; Type: TABLE DATA; Schema: agdc; Owner: agdc_admin
--

COPY agdc.dataset_location (id, dataset_ref, uri_scheme, uri_body, added, added_by, archived) FROM stdin;
\.


--
-- Data for Name: dataset_source; Type: TABLE DATA; Schema: agdc; Owner: agdc_admin
--

COPY agdc.dataset_source (dataset_ref, classifier, source_dataset_ref) FROM stdin;
\.


--
-- Data for Name: dataset_type; Type: TABLE DATA; Schema: agdc; Owner: agdc_admin
--

COPY agdc.dataset_type (id, name, metadata, metadata_type_ref, definition, added, added_by, updated) FROM stdin;
1	ls5_level1_usgs	{"format": {"name": "GeoTiff"}, "platform": {"code": "LANDSAT_5"}, "instrument": {"name": "TM"}, "product_type": "LS_USGS_L1C1"}	2	{"name": "ls5_level1_usgs", "metadata": {"format": {"name": "GeoTiff"}, "platform": {"code": "LANDSAT_5"}, "instrument": {"name": "TM"}, "product_type": "LS_USGS_L1C1"}, "description": "Landsat 5 USGS Level 1 Collection-1 OLI-TIRS", "measurements": [{"name": "blue", "dtype": "int16", "units": "1", "nodata": -9999, "aliases": ["band_1", "blue"]}, {"name": "green", "dtype": "int16", "units": "1", "nodata": -9999, "aliases": ["band_2", "green"]}, {"name": "red", "dtype": "int16", "units": "1", "nodata": -9999, "aliases": ["band_3", "red"]}, {"name": "nir", "dtype": "int16", "units": "1", "nodata": -9999, "aliases": ["band_4", "nir"]}, {"name": "swir1", "dtype": "int16", "units": "1", "nodata": -9999, "aliases": ["band_5", "swir1"]}, {"name": "swir2", "dtype": "int16", "units": "1", "nodata": -9999, "aliases": ["band_7", "swir2"]}, {"name": "quality", "dtype": "int16", "units": "1", "nodata": 0, "aliases": ["QUALITY", "quality"], "flags_definition": {"cloud": {"bits": [4], "values": {"0": false, "1": true}, "description": "Cloud"}, "dropped_pixel": {"bits": [1], "values": {"0": false, "1": true}, "description": "Dropped Pixel"}, "snow_ice_conf": {"bits": [9, 10], "values": {"0": "Not Determined", "1": "Low", "2": "Medium", "3": "High"}, "description": "Snow/Ice Confidence with low =(0-33)%, medium =(34-66)% and high =(67-100)%"}, "designated_fill": {"bits": [0], "values": {"0": false, "1": true}, "description": "Used to identify fill values"}, "cloud_confidence": {"bits": [5, 6], "values": {"0": "Not Determined", "1": "Low", "2": "Medium", "3": "High"}, "description": "Cloud Confidence with low =(0-33)%, medium =(34-66)% and high =(67-100)%"}, "cloud_shadow_conf": {"bits": [7, 8], "values": {"0": "Not Determined", "1": "Low", "2": "Medium", "3": "High"}, "description": "Cloud Shadow Confidence with low =(0-33)%, medium =(34-66)% and high =(67-100)%"}, "radiometric_saturation": {"bits": [2, 3], "values": {"0": "none", "1": "1-2", "2": "3-4", "3": "<=5"}, "description": "Radiometric saturation bits, represents how many bands contains saturation"}}}], "metadata_type": "eo"}	2021-01-31 22:06:45.258041+00	africa	\N
2	ls7_level1_usgs	{"format": {"name": "GeoTiff"}, "platform": {"code": "LANDSAT_7"}, "instrument": {"name": "ETM"}, "product_type": "LS_USGS_L1C1"}	2	{"name": "ls7_level1_usgs", "metadata": {"format": {"name": "GeoTiff"}, "platform": {"code": "LANDSAT_7"}, "instrument": {"name": "ETM"}, "product_type": "LS_USGS_L1C1"}, "description": "Landsat 7 USGS Level 1 Collection-1 OLI-TIRS", "measurements": [{"name": "blue", "dtype": "int16", "units": "1", "nodata": -9999, "aliases": ["band_1", "blue"]}, {"name": "green", "dtype": "int16", "units": "1", "nodata": -9999, "aliases": ["band_2", "green"]}, {"name": "red", "dtype": "int16", "units": "1", "nodata": -9999, "aliases": ["band_3", "red"]}, {"name": "nir", "dtype": "int16", "units": "1", "nodata": -9999, "aliases": ["band_4", "nir"]}, {"name": "swir1", "dtype": "int16", "units": "1", "nodata": -9999, "aliases": ["band_5", "swir1"]}, {"name": "swir2", "dtype": "int16", "units": "1", "nodata": -9999, "aliases": ["band_7", "swir2"]}, {"name": "quality", "dtype": "int16", "units": "1", "nodata": 0, "aliases": ["QUALITY", "quality"], "flags_definition": {"cloud": {"bits": [4], "values": {"0": false, "1": true}, "description": "Cloud"}, "dropped_pixel": {"bits": [1], "values": {"0": false, "1": true}, "description": "Dropped Pixel"}, "snow_ice_conf": {"bits": [9, 10], "values": {"0": "Not Determined", "1": "Low", "2": "Medium", "3": "High"}, "description": "Snow/Ice Confidence with low =(0-33)%, medium =(34-66)% and high =(67-100)%"}, "designated_fill": {"bits": [0], "values": {"0": false, "1": true}, "description": "Used to identify fill values"}, "cloud_confidence": {"bits": [5, 6], "values": {"0": "Not Determined", "1": "Low", "2": "Medium", "3": "High"}, "description": "Cloud Confidence with low =(0-33)%, medium =(34-66)% and high =(67-100)%"}, "cloud_shadow_conf": {"bits": [7, 8], "values": {"0": "Not Determined", "1": "Low", "2": "Medium", "3": "High"}, "description": "Cloud Shadow Confidence with low =(0-33)%, medium =(34-66)% and high =(67-100)%"}, "radiometric_saturation": {"bits": [2, 3], "values": {"0": "none", "1": "1-2", "2": "3-4", "3": "<=5"}, "description": "Radiometric saturation bits, represents how many bands contains saturation"}}}], "metadata_type": "eo"}	2021-01-31 22:06:55.100266+00	africa	\N
3	aster_aloh_group_composition	{"format": {"name": "GeoTIFF"}, "product_type": "aster_aloh_group_composition"}	2	{"name": "aster_aloh_group_composition", "metadata": {"format": {"name": "GeoTIFF"}, "product_type": "aster_aloh_group_composition"}, "description": "ASTER", "measurements": [{"name": "Band_1", "dtype": "uint8", "units": "1", "nodata": 0, "aliases": ["band_01", "B01", "Band1"]}], "metadata_type": "eo"}	2021-01-31 22:07:17.320094+00	africa	\N
4	aster_aloh_group_content	{"format": {"name": "GeoTIFF"}, "product_type": "aster_aloh_group_content"}	2	{"name": "aster_aloh_group_content", "metadata": {"format": {"name": "GeoTIFF"}, "product_type": "aster_aloh_group_content"}, "description": "ASTER", "measurements": [{"name": "Band_1", "dtype": "uint8", "units": "1", "nodata": 0, "aliases": ["band_01", "B01", "Band1"]}], "metadata_type": "eo"}	2021-01-31 22:07:19.189883+00	africa	\N
5	aster_false_colour	{"format": {"name": "GeoTIFF"}, "product_type": "aster_false_colour"}	2	{"name": "aster_false_colour", "metadata": {"format": {"name": "GeoTIFF"}, "product_type": "aster_false_colour"}, "description": "ASTER", "measurements": [{"name": "Band_1", "dtype": "uint8", "units": "1", "nodata": 0, "aliases": ["band_01", "B01", "Band1"]}, {"name": "Band_2", "dtype": "uint8", "units": "1", "nodata": 0, "aliases": ["band_02", "B02", "Band2"]}, {"name": "Band_3", "dtype": "uint8", "units": "1", "nodata": 0, "aliases": ["band_03", "B03", "Band3"]}], "metadata_type": "eo"}	2021-01-31 22:07:21.075779+00	africa	\N
6	aster_feoh_group_content	{"format": {"name": "GeoTIFF"}, "product_type": "aster_feoh_group_content"}	2	{"name": "aster_feoh_group_content", "metadata": {"format": {"name": "GeoTIFF"}, "product_type": "aster_feoh_group_content"}, "description": "ASTER", "measurements": [{"name": "Band_1", "dtype": "uint8", "units": "1", "nodata": 0, "aliases": ["band_01", "B01", "Band1"]}], "metadata_type": "eo"}	2021-01-31 22:07:22.958036+00	africa	\N
7	aster_ferric_oxide_composition	{"format": {"name": "GeoTIFF"}, "product_type": "aster_ferric_oxide_composition"}	2	{"name": "aster_ferric_oxide_composition", "metadata": {"format": {"name": "GeoTIFF"}, "product_type": "aster_ferric_oxide_composition"}, "description": "ASTER", "measurements": [{"name": "Band_1", "dtype": "uint8", "units": "1", "nodata": 0, "aliases": ["band_01", "B01", "Band1"]}], "metadata_type": "eo"}	2021-01-31 22:07:24.864488+00	africa	\N
8	aster_ferric_oxide_content	{"format": {"name": "GeoTIFF"}, "product_type": "aster_ferric_oxide_content"}	2	{"name": "aster_ferric_oxide_content", "metadata": {"format": {"name": "GeoTIFF"}, "product_type": "aster_ferric_oxide_content"}, "description": "ASTER", "measurements": [{"name": "Band_1", "dtype": "uint8", "units": "1", "nodata": 0, "aliases": ["band_01", "B01", "Band1"]}], "metadata_type": "eo"}	2021-01-31 22:07:26.798833+00	africa	\N
9	aster_ferrous_iron_content_in_mgoh	{"format": {"name": "GeoTIFF"}, "product_type": "aster_ferrous_iron_content_in_mgoh"}	2	{"name": "aster_ferrous_iron_content_in_mgoh", "metadata": {"format": {"name": "GeoTIFF"}, "product_type": "aster_ferrous_iron_content_in_mgoh"}, "description": "ASTER", "measurements": [{"name": "Band_1", "dtype": "uint8", "units": "1", "nodata": 0, "aliases": ["band_01", "B01", "Band1"]}], "metadata_type": "eo"}	2021-01-31 22:07:28.748036+00	africa	\N
10	aster_ferrous_iron_index	{"format": {"name": "GeoTIFF"}, "product_type": "aster_ferrous_iron_index"}	2	{"name": "aster_ferrous_iron_index", "metadata": {"format": {"name": "GeoTIFF"}, "product_type": "aster_ferrous_iron_index"}, "description": "ASTER", "measurements": [{"name": "Band_1", "dtype": "uint8", "units": "1", "nodata": 0, "aliases": ["band_01", "B01", "Band1"]}], "metadata_type": "eo"}	2021-01-31 22:07:30.685868+00	africa	\N
42	ls5_usgs_l2c1	{"format": {"name": "GeoTiff"}, "platform": {"code": "LANDSAT_5"}, "instrument": {"name": "TM"}, "product_type": "LS_USGS_L2C1"}	2	{"name": "ls5_usgs_l2c1", "metadata": {"format": {"name": "GeoTiff"}, "platform": {"code": "LANDSAT_5"}, "instrument": {"name": "TM"}, "product_type": "LS_USGS_L2C1"}, "description": "Landsat 5 Thematic Mapper (TM) USGS Analysis Ready Data 30m scene", "measurements": [{"name": "sr_cloud_qa", "dtype": "uint8", "units": "1", "nodata": 255, "aliases": ["cloud_qa"], "flags_definition": {"pixelqa": {"bits": [0, 1, 2, 3, 4, 5, 6, 7], "values": {"0": "dark dense vegetation", "1": "cloud", "2": "cloud shadow", "3": "adjacent to cloud", "4": "snow", "5": "land/water"}, "description": "cloud_qa"}}}, {"name": "sr_atmos_opacity", "dtype": "int16", "units": "1", "nodata": -9999, "aliases": ["opacity"]}, {"name": "blue", "dtype": "int16", "units": "1", "nodata": -9999, "aliases": ["band_1", "sr_band1"], "spectral_definition": {"response": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0007, 0.0008, 0.0008, 0.0009, 0.0009, 0.001, 0.0013, 0.0016, 0.002, 0.0023, 0.0027, 0.0042, 0.006, 0.0086, 0.0113, 0.0141, 0.017, 0.0216, 0.0268, 0.0321, 0.037, 0.042, 0.0471, 0.0524, 0.0577, 0.0633, 0.0746, 0.1097, 0.1564, 0.2483, 0.3391, 0.4058, 0.4741, 0.5366, 0.5856, 0.6667, 0.688, 0.6993, 0.7095, 0.7165, 0.72, 0.7326, 0.7475, 0.7583, 0.7714, 0.7847, 0.7924, 0.8002, 0.808, 0.8156, 0.8206, 0.8257, 0.8308, 0.8359, 0.8421, 0.8526, 0.8642, 0.8724, 0.8824, 0.8925, 0.9026, 0.9069, 0.9111, 0.9154, 0.9196, 0.9238, 0.9285, 0.9332, 0.9379, 0.9425, 0.9472, 0.9548, 0.9623, 0.9698, 0.9761, 0.9775, 0.9788, 0.9802, 0.9815, 0.9837, 0.9891, 0.9935, 0.9978, 1.0, 0.9952, 0.9828, 0.9524, 0.9219, 0.8914, 0.8607, 0.8293, 0.8021, 0.7877, 0.7732, 0.7565, 0.7339, 0.6859, 0.5784, 0.4813, 0.4002, 0.3187, 0.2367, 0.1324, 0.1018, 0.0911, 0.0804, 0.0696, 0.0588, 0.0532, 0.0498, 0.0465, 0.0431, 0.0397, 0.0364, 0.033, 0.0296, 0.0261, 0.0227, 0.0205, 0.0184, 0.0162, 0.014, 0.0119, 0.0105, 0.0093, 0.0081, 0.0069, 0.0058, 0.0056, 0.0054, 0.0052, 0.0, 0.0], "wavelength": [410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552]}}, {"name": "green", "dtype": "int16", "units": "1", "nodata": -9999, "aliases": ["band_2", "sr_band2"], "spectral_definition": {"response": [0.0, 0.0007, 0.0021, 0.0036, 0.0032, 0.0065, 0.0089, 0.0139, 0.0164, 0.019, 0.0233, 0.0261, 0.029, 0.0318, 0.0347, 0.0377, 0.0544, 0.0713, 0.0982, 0.1297, 0.1635, 0.2055, 0.2479, 0.2908, 0.3341, 0.3779, 0.419, 0.4593, 0.4999, 0.5409, 0.5718, 0.5967, 0.6142, 0.6286, 0.6431, 0.6578, 0.6722, 0.6868, 0.7015, 0.7163, 0.7312, 0.7416, 0.752, 0.7625, 0.773, 0.7836, 0.7941, 0.8047, 0.8153, 0.826, 0.8367, 0.8425, 0.8483, 0.8541, 0.8594, 0.8646, 0.8695, 0.8743, 0.8792, 0.8841, 0.889, 0.8937, 0.8983, 0.9029, 0.9044, 0.9044, 0.905, 0.9056, 0.9063, 0.9068, 0.9074, 0.9073, 0.9072, 0.907, 0.9069, 0.9067, 0.9057, 0.9047, 0.9073, 0.9098, 0.9124, 0.9155, 0.9186, 0.9218, 0.9392, 0.95, 0.9591, 0.9683, 0.9768, 0.9819, 0.9871, 0.9913, 0.9967, 0.9999, 1.0, 0.9978, 0.9961, 0.992, 0.9757, 0.9592, 0.9428, 0.9199, 0.887, 0.854, 0.821, 0.7878, 0.7387, 0.6647, 0.5901, 0.5153, 0.4616, 0.4083, 0.3547, 0.3007, 0.2464, 0.2039, 0.1796, 0.1552, 0.1306, 0.1072, 0.0969, 0.0865, 0.076, 0.0655, 0.0549, 0.0517, 0.0485, 0.0454, 0.0422, 0.0389, 0.0357, 0.0207, 0.0115, 0.0058, 0.0], "wavelength": [500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 635, 640, 645, 650]}}, {"name": "red", "dtype": "int16", "units": "1", "nodata": -9999, "aliases": ["band_3", "sr_band3"], "spectral_definition": {"response": [0.0018, 0.002, 0.0079, 0.0205, 0.0375, 0.0409, 0.0555, 0.073, 0.0906, 0.1082, 0.1262, 0.1444, 0.1626, 0.2169, 0.2958, 0.3759, 0.4086, 0.4293, 0.4503, 0.4715, 0.4923, 0.5132, 0.5343, 0.5555, 0.5774, 0.6031, 0.6374, 0.6848, 0.7325, 0.7482, 0.7642, 0.7802, 0.7947, 0.8065, 0.8184, 0.8304, 0.8424, 0.8545, 0.8614, 0.8678, 0.8743, 0.8809, 0.8875, 0.8971, 0.9008, 0.9017, 0.9026, 0.9035, 0.9044, 0.9052, 0.9055, 0.9058, 0.906, 0.9062, 0.9064, 0.9104, 0.9143, 0.9195, 0.9266, 0.9338, 0.9412, 0.9488, 0.9563, 0.964, 0.9699, 0.9749, 0.9799, 0.9847, 0.9895, 0.9932, 0.9966, 1.0, 0.9995, 0.9989, 0.9983, 0.9784, 0.9806, 0.9827, 0.9732, 0.9558, 0.9384, 0.9209, 0.885, 0.8364, 0.7874, 0.7, 0.6052, 0.5144, 0.4413, 0.3678, 0.2942, 0.2277, 0.1916, 0.1552, 0.1186, 0.1079, 0.0972, 0.0864, 0.0756, 0.0646, 0.0464, 0.0309, 0.02, 0.0123, 0.0062, 0.0031], "wavelength": [580, 590, 600, 605, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 683, 684, 685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704, 705, 710, 715, 720, 725, 730, 740]}}, {"name": "nir", "dtype": "int16", "units": "1", "nodata": -9999, "aliases": ["band_4", "sr_band4"], "spectral_definition": {"response": [0.0023, 0.0046, 0.007, 0.0093, 0.0186, 0.0214, 0.0242, 0.027, 0.0298, 0.0326, 0.0402, 0.0478, 0.0554, 0.063, 0.0706, 0.0784, 0.0862, 0.094, 0.1152, 0.1364, 0.1577, 0.1791, 0.2069, 0.2409, 0.2752, 0.3095, 0.344, 0.3786, 0.4133, 0.4482, 0.4833, 0.5259, 0.5683, 0.6108, 0.6534, 0.6963, 0.7393, 0.7745, 0.8017, 0.829, 0.8564, 0.8838, 0.8992, 0.9146, 0.93, 0.9418, 0.9499, 0.958, 0.9661, 0.9743, 0.9794, 0.9845, 0.9897, 0.9948, 1.0, 0.9982, 0.9964, 0.9946, 0.9928, 0.991, 0.9889, 0.9868, 0.9846, 0.9825, 0.9804, 0.9758, 0.9712, 0.9666, 0.962, 0.9574, 0.9529, 0.9483, 0.9442, 0.94, 0.9359, 0.9313, 0.9268, 0.9223, 0.9178, 0.9161, 0.916, 0.9164, 0.9167, 0.917, 0.9173, 0.9176, 0.9178, 0.9181, 0.9183, 0.9185, 0.9188, 0.919, 0.9192, 0.9194, 0.9196, 0.9202, 0.9208, 0.9214, 0.922, 0.9226, 0.9232, 0.9237, 0.9243, 0.9249, 0.9254, 0.9217, 0.9179, 0.9141, 0.9104, 0.9067, 0.9029, 0.8992, 0.8947, 0.8901, 0.8856, 0.8831, 0.8815, 0.881, 0.8804, 0.8811, 0.8818, 0.8824, 0.8831, 0.8838, 0.8844, 0.8858, 0.8871, 0.8853, 0.8832, 0.881, 0.8768, 0.8725, 0.8683, 0.8641, 0.8599, 0.853, 0.8451, 0.8372, 0.8294, 0.8217, 0.8139, 0.8063, 0.7986, 0.791, 0.7835, 0.7835, 0.7836, 0.7787, 0.769, 0.7592, 0.7495, 0.7398, 0.7302, 0.7208, 0.7152, 0.671, 0.6299, 0.5891, 0.5299, 0.4664, 0.4033, 0.3405, 0.2945, 0.2528, 0.2114, 0.1702, 0.143, 0.1195, 0.0962, 0.0772, 0.0314, 0.0154, 0.0075, 0.0055, 0.0035, 0.0017], "wavelength": [730, 735, 740, 745, 750, 751, 752, 753, 754, 755, 756, 757, 758, 759, 760, 761, 762, 763, 764, 765, 766, 767, 768, 769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784, 785, 786, 787, 788, 789, 790, 791, 792, 793, 794, 795, 796, 797, 798, 799, 800, 801, 802, 803, 804, 805, 806, 807, 808, 809, 810, 811, 812, 813, 814, 815, 816, 817, 818, 819, 820, 821, 822, 823, 824, 825, 826, 827, 828, 829, 830, 831, 832, 833, 834, 835, 836, 837, 838, 839, 840, 841, 842, 843, 844, 845, 846, 847, 848, 849, 850, 851, 852, 853, 854, 855, 856, 857, 858, 859, 860, 861, 862, 863, 864, 865, 866, 867, 868, 869, 870, 871, 872, 873, 874, 875, 876, 877, 878, 879, 880, 881, 882, 883, 884, 885, 886, 887, 888, 889, 890, 891, 892, 893, 894, 895, 896, 897, 898, 899, 900, 901, 902, 903, 904, 905, 906, 907, 908, 909, 910, 911, 912, 913, 914, 915, 920, 925, 930, 935, 940, 945]}}, {"name": "swir1", "dtype": "int16", "units": "1", "nodata": -9999, "aliases": ["band_5", "sr_band5"], "spectral_definition": {"response": [0.0012, 0.0013, 0.0014, 0.0016, 0.0024, 0.0039, 0.0054, 0.0061, 0.0077, 0.0093, 0.0116, 0.014, 0.0165, 0.019, 0.0216, 0.0351, 0.0419, 0.0557, 0.0696, 0.0837, 0.1104, 0.1497, 0.1894, 0.2295, 0.2701, 0.3179, 0.3732, 0.4294, 0.4865, 0.5446, 0.5989, 0.6239, 0.6746, 0.726, 0.7781, 0.8308, 0.8553, 0.88, 0.905, 0.9301, 0.9555, 0.9526, 0.9497, 0.9467, 0.9438, 0.9409, 0.9415, 0.9421, 0.9428, 0.9434, 0.944, 0.9519, 0.9572, 0.9625, 0.9677, 0.9718, 0.9747, 0.9777, 0.9806, 0.9835, 0.9842, 0.9827, 0.9813, 0.9798, 0.9783, 0.9763, 0.9737, 0.9711, 0.9686, 0.966, 0.9661, 0.9687, 0.9727, 0.9753, 0.978, 0.979, 0.98, 0.981, 0.982, 0.983, 0.9837, 0.9844, 0.985, 0.9857, 0.9864, 0.9844, 0.9825, 0.9796, 0.9776, 0.9784, 0.982, 0.9857, 0.9893, 0.9926, 0.9953, 0.9963, 0.9974, 0.9985, 0.9995, 0.9997, 0.9988, 0.9981, 0.9975, 0.9968, 0.9922, 0.9877, 0.9854, 0.9831, 0.9785, 0.974, 0.9706, 0.9671, 0.9637, 0.9603, 0.9569, 0.9555, 0.9542, 0.9523, 0.9509, 0.9505, 0.9508, 0.9512, 0.9516, 0.9519, 0.946, 0.9339, 0.9219, 0.9098, 0.8915, 0.8651, 0.8124, 0.7597, 0.7069, 0.6542, 0.5968, 0.535, 0.4732, 0.4114, 0.3497, 0.3026, 0.2698, 0.2369, 0.204, 0.171, 0.1462, 0.1294, 0.1127, 0.096, 0.0794, 0.0684, 0.0629, 0.0574, 0.0463, 0.0326, 0.0217, 0.0129, 0.0086, 0.0043, 0.0032, 0.0021], "wavelength": [1514, 1515, 1517, 1519, 1521, 1523, 1525, 1526, 1528, 1530, 1532, 1534, 1536, 1538, 1540, 1542, 1543, 1545, 1547, 1549, 1551, 1553, 1555, 1557, 1559, 1561, 1563, 1565, 1567, 1569, 1571, 1572, 1574, 1576, 1578, 1580, 1582, 1584, 1586, 1588, 1590, 1592, 1594, 1596, 1598, 1600, 1602, 1604, 1606, 1608, 1610, 1613, 1615, 1617, 1619, 1621, 1623, 1625, 1627, 1629, 1631, 1633, 1635, 1637, 1639, 1641, 1643, 1645, 1647, 1649, 1651, 1653, 1656, 1658, 1660, 1662, 1664, 1666, 1668, 1670, 1672, 1674, 1676, 1678, 1680, 1682, 1684, 1687, 1689, 1691, 1693, 1695, 1697, 1699, 1701, 1703, 1705, 1707, 1709, 1711, 1714, 1716, 1718, 1720, 1722, 1724, 1725, 1726, 1728, 1730, 1732, 1734, 1736, 1738, 1740, 1742, 1744, 1747, 1749, 1751, 1753, 1755, 1757, 1759, 1761, 1763, 1765, 1767, 1769, 1771, 1773, 1775, 1777, 1779, 1781, 1783, 1785, 1787, 1789, 1791, 1793, 1795, 1797, 1799, 1801, 1803, 1805, 1807, 1809, 1811, 1813, 1815, 1820, 1825, 1830, 1840, 1850, 1860, 1870, 1880]}}, {"name": "swir2", "dtype": "int16", "units": "1", "nodata": -9999, "aliases": ["band_7", "sr_band7"], "spectral_definition": {"response": [0.0, 0.003, -0.002, 0.003, -0.001, 0.0, 0.004, -0.004, 0.002, 0.002, 0.002, 0.012, 0.009, 0.007, 0.011, 0.02, 0.017, 0.03, 0.035, 0.037, 0.044, 0.051, 0.065, 0.08, 0.088, 0.102, 0.133, 0.165, 0.188, 0.22, 0.264, 0.316, 0.367, 0.421, 0.484, 0.554, 0.59, 0.67, 0.683, 0.73, 0.756, 0.767, 0.794, 0.774, 0.776, 0.789, 0.775, 0.784, 0.778, 0.768, 0.762, 0.761, 0.775, 0.775, 0.764, 0.784, 0.792, 0.814, 0.794, 0.825, 0.817, 0.806, 0.819, 0.821, 0.852, 0.832, 0.836, 0.85, 0.855, 0.862, 0.853, 0.871, 0.848, 0.882, 0.875, 0.86, 0.856, 0.887, 0.85, 0.872, 0.879, 0.857, 0.865, 0.867, 0.871, 0.882, 0.87, 0.869, 0.873, 0.877, 0.868, 0.88, 0.877, 0.87, 0.878, 0.88, 0.868, 0.881, 0.87, 0.856, 0.863, 0.863, 0.857, 0.844, 0.859, 0.857, 0.852, 0.866, 0.868, 0.856, 0.856, 0.847, 0.861, 0.862, 0.84, 0.856, 0.838, 0.856, 0.837, 0.842, 0.826, 0.844, 0.827, 0.842, 0.822, 0.843, 0.823, 0.854, 0.839, 0.853, 0.854, 0.865, 0.873, 0.869, 0.865, 0.893, 0.89, 0.89, 0.906, 0.924, 0.92, 0.922, 0.939, 0.916, 0.94, 0.93, 0.942, 0.957, 0.954, 0.951, 0.954, 0.966, 0.975, 0.985, 0.971, 0.973, 0.97, 0.993, 0.996, 0.983, 0.972, 1.0, 0.998, 0.971, 0.968, 0.967, 0.962, 0.949, 0.923, 0.929, 0.917, 0.934, 0.903, 0.926, 0.916, 0.942, 0.924, 0.92, 0.863, 0.824, 0.775, 0.684, 0.583, 0.48, 0.378, 0.275, 0.233, 0.171, 0.131, 0.111, 0.081, 0.069, 0.046, 0.029, 0.038, -0.002, 0.029, 0.016, 0.009, 0.017, 0.003, 0.015, 0.0, -0.009, 0.007, 0.0, 0.0, 0.0], "wavelength": [2000, 2001, 2003, 2005, 2007, 2009, 2011, 2013, 2015, 2017, 2018, 2020, 2022, 2024, 2026, 2028, 2030, 2032, 2034, 2035, 2037, 2039, 2041, 2043, 2045, 2047, 2049, 2051, 2052, 2054, 2056, 2058, 2060, 2062, 2064, 2066, 2067, 2069, 2071, 2073, 2075, 2077, 2079, 2081, 2083, 2085, 2086, 2088, 2090, 2092, 2094, 2096, 2099, 2100, 2102, 2104, 2106, 2108, 2110, 2112, 2114, 2116, 2117, 2119, 2121, 2123, 2125, 2127, 2129, 2131, 2133, 2135, 2136, 2138, 2140, 2142, 2144, 2146, 2148, 2150, 2151, 2153, 2155, 2157, 2159, 2161, 2163, 2165, 2166, 2168, 2170, 2172, 2174, 2176, 2178, 2180, 2182, 2183, 2185, 2187, 2189, 2191, 2193, 2195, 2197, 2199, 2201, 2203, 2205, 2207, 2209, 2210, 2212, 2214, 2216, 2218, 2220, 2222, 2223, 2226, 2227, 2229, 2231, 2233, 2235, 2237, 2239, 2241, 2242, 2244, 2246, 2248, 2250, 2252, 2254, 2256, 2258, 2259, 2261, 2263, 2265, 2267, 2269, 2271, 2273, 2274, 2276, 2278, 2280, 2282, 2284, 2286, 2288, 2290, 2292, 2293, 2295, 2297, 2299, 2301, 2303, 2305, 2307, 2309, 2310, 2312, 2314, 2316, 2318, 2320, 2322, 2323, 2325, 2327, 2329, 2331, 2333, 2335, 2337, 2339, 2340, 2342, 2344, 2346, 2348, 2350, 2352, 2354, 2355, 2357, 2359, 2361, 2363, 2365, 2367, 2369, 2371, 2373, 2374, 2376, 2378, 2380, 2382, 2384, 2386, 2390, 2395, 2400]}}, {"name": "quality", "dtype": "uint8", "units": "1", "nodata": 255, "aliases": ["pixel_qa"], "flags_definition": {"pixelqa": {"bits": [0, 1, 2, 3, 4, 5, 6, 7], "values": {"0": "fill", "1": "clear", "2": "water", "3": "cloud shadow", "4": "snow", "5": "cloud", "6": "cloud confidence", "7": "cloud confidence", "8": "cirrus confidence", "9": "cirrus confidence", "10": "terrain occlusion", "11": "unused", "12": "unused", "13": "unused", "14": "unused", "15": "unused"}, "description": "PixelQA"}}}, {"name": "solar_zenith_band4", "dtype": "int16", "units": "degrees", "nodata": -32768, "aliases": ["solar_zenith"]}, {"name": "solar_azimuth_band4", "dtype": "int16", "units": "degrees", "nodata": -32768, "aliases": ["solar_azimuth"]}, {"name": "sensor_zenith_band4", "dtype": "int16", "units": "degrees", "nodata": -32768, "aliases": ["sensor_zenith"]}, {"name": "sensor_azimuth_band4", "dtype": "int16", "units": "degrees", "nodata": -32768, "aliases": ["sensor_azimuth"]}, {"name": "radsat_qa", "dtype": "uint8", "units": "1", "nodata": 255, "aliases": ["radasat"], "flags_definition": {"radsatqa": {"bits": [0, 1, 2, 3, 4, 5, 6, 7], "values": {"0": "Data Fill Flag (0 = valid data, 1 = invalid data)", "1": "Band 1 Data Saturation Flag (0 = valid data, 1 = saturated data)", "2": "Band 2 Data Saturation Flag (0 = valid data, 1 = saturated data)", "3": "Band 3 Data Saturation Flag (0 = valid data, 1 = saturated data)", "4": "Band 4 Data Saturation Flag (0 = valid data, 1 = saturated data)", "5": "Band 5 Data Saturation Flag (0 = valid data, 1 = saturated data)", "6": "Band 6 Data Saturation Flag (0 = valid data, 1 = saturated data)", "7": "Band 7 Data Saturation Flag (0 = valid data, 1 = saturated data)"}, "description": "saturation mask"}}}, {"name": "lwir1", "dtype": "int16", "units": "1", "nodata": -9999, "aliases": ["thermal60", "bt_band6"], "spectral_definition": {"response": [0, 0.0058, 0.0066, 0.0073, 0.0081, 0.0088, 0.0096, 0.0104, 0.0112, 0.012, 0.0128, 0.0136, 0.015, 0.0165, 0.0018, 0.0195, 0.021, 0.0226, 0.0241, 0.0256, 0.0272, 0.0288, 0.0334, 0.0381, 0.0428, 0.0476, 0.0524, 0.0572, 0.0621, 0.067, 0.0719, 0.0769, 0.1011, 0.1256, 0.1502, 0.1751, 0.2002, 0.2256, 0.2511, 0.2769, 0.3029, 0.3292, 0.3633, 0.3974, 0.4317, 0.4661, 0.5005, 0.535, 0.5696, 0.6043, 0.6391, 0.6739, 0.6839, 0.694, 0.7042, 0.7145, 0.725, 0.7355, 0.7461, 0.7566, 0.7671, 0.7703, 0.7736, 0.7768, 0.7801, 0.7833, 0.7845, 0.7858, 0.787, 0.7883, 0.7895, 0.7908, 0.7958, 0.8008, 0.8058, 0.8108, 0.8158, 0.8209, 0.826, 0.8311, 0.8362, 0.8413, 0.8479, 0.8545, 0.8611, 0.8677, 0.8743, 0.8811, 0.8878, 0.8946, 0.9013, 0.9081, 0.9147, 0.9213, 0.928, 0.9346, 0.9412, 0.948, 0.9548, 0.9615, 0.9683, 0.9751, 0.9759, 0.9768, 0.9776, 0.9785, 0.9793, 0.9801, 0.9809, 0.9818, 0.9826, 0.9834, 0.9806, 0.9778, 0.9749, 0.9721, 0.9693, 0.9665, 0.9637, 0.9608, 0.958, 0.9552, 0.9579, 0.9606, 0.9634, 0.9661, 0.9688, 0.9715, 0.9743, 0.9771, 0.9798, 0.9808, 0.9818, 0.9829, 0.9839, 0.9849, 0.9858, 0.9868, 0.9877, 0.9887, 0.9896, 0.9903, 0.9909, 0.9916, 0.9922, 0.9929, 0.9941, 0.9953, 0.9965, 0.9977, 0.9989, 0.9928, 0.9866, 0.9805, 0.9743, 0.9682, 0.9604, 0.9525, 0.9447, 0.9368, 0.929, 0.9293, 0.9296, 0.9299, 0.9302, 0.9332, 0.9361, 0.9391, 0.942, 0.945, 0.9478, 0.9506, 0.9533, 0.9561, 0.9589, 0.9615, 0.9642, 0.9668, 0.9695, 0.9721, 0.9736, 0.9751, 0.9767, 0.9782, 0.9787, 0.9792, 0.9796, 0.9801, 0.9806, 0.9807, 0.9809, 0.981, 0.9812, 0.9813, 0.9809, 0.9805, 0.9801, 0.9797, 0.9791, 0.9786, 0.978, 0.9775, 0.9769, 0.9759, 0.9749, 0.9739, 0.9729, 0.9719, 0.9708, 0.9698, 0.9688, 0.9677, 0.9665, 0.9653, 0.964, 0.9627, 0.9615, 0.9602, 0.9589, 0.9577, 0.9564, 0.9551, 0.9481, 0.9412, 0.9343, 0.9274, 0.9205, 0.9136, 0.9067, 0.8999, 0.893, 0.8861, 0.8568, 0.8275, 0.7982, 0.769, 0.7398, 0.7136, 0.6814, 0.6523, 0.6232, 0.594, 0.5614, 0.5286, 0.4957, 0.4627, 0.4296, 0.3964, 0.3631, 0.3297, 0.2962, 0.2627, 0.2403, 0.2181, 0.196, 0.1741, 0.1741, 0.1523, 0.1307, 0.1092, 0.0879, 0.0667, 0.0458, 0.0433, 0.0409, 0.0385, 0.0361, 0.0337, 0.0314, 0.0291, 0.0268, 0.0245, 0.0223, 0.0209, 0.0195, 0.0182, 0.0168, 0.0155, 0.0141, 0.0128, 0.0115, 0.0101, 0.0088, 0.0085, 0.0081, 0.0078, 0.0074, 0.0071, 0.0068, 0.0064, 0.0061, 0.0058, 0.0054, 0], "wavelength": [9990, 10000, 10010, 10020, 10030, 10040, 10050, 10060, 10070, 10080, 10090, 10100, 10110, 10120, 10130, 10140, 10150, 10160, 10170, 10180, 10190, 10200, 10210, 10220, 10230, 10240, 10250, 10260, 10270, 10280, 10290, 10300, 10310, 10320, 10330, 10340, 10350, 10360, 10370, 10380, 10390, 10400, 10410, 10420, 10430, 10440, 10450, 10460, 10470, 10480, 10490, 10500, 10510, 10520, 10530, 10540, 10550, 10560, 10570, 10580, 10590, 10600, 10610, 10620, 10630, 10640, 10650, 10660, 10670, 10680, 10690, 10700, 10710, 10720, 10730, 10740, 10750, 10760, 10770, 10780, 10790, 10800, 10810, 10820, 10830, 10840, 10850, 10860, 10870, 10880, 10890, 10900, 10910, 10920, 10930, 10940, 10950, 10960, 10970, 10980, 10990, 11000, 11010, 11020, 11030, 11040, 11050, 11060, 11070, 11080, 11090, 11100, 11110, 11120, 11130, 11140, 11150, 11160, 11170, 11180, 11190, 11200, 11210, 11220, 11230, 11240, 11250, 11260, 11270, 11280, 11290, 11300, 11310, 11320, 11330, 11340, 11350, 11360, 11370, 11380, 11390, 11400, 11410, 11420, 11430, 11440, 11450, 11460, 11470, 11480, 11490, 11500, 11510, 11520, 11530, 11540, 11550, 11560, 11570, 11580, 11590, 11600, 11610, 11620, 11630, 11640, 11650, 11660, 11670, 11680, 11690, 11700, 11710, 11720, 11730, 11740, 11750, 11760, 11770, 11780, 11790, 11800, 11810, 11820, 11830, 11840, 11850, 11860, 11870, 11880, 11890, 11900, 11910, 11920, 11930, 11940, 11950, 11960, 11970, 11980, 11990, 12000, 12010, 12020, 12030, 12040, 12050, 12060, 12070, 12080, 12090, 12100, 12110, 12120, 12130, 12140, 12150, 12160, 12170, 12180, 12190, 12200, 12210, 12220, 12230, 12240, 12250, 12260, 12270, 12280, 12290, 12300, 12310, 12320, 12330, 12340, 12350, 12360, 12370, 12380, 12390, 12400, 12410, 12420, 12430, 12440, 12450, 12460, 12470, 12480, 12490, 12500, 12510, 12520, 12530, 12540, 12540, 12550, 12560, 12570, 12580, 12590, 12600, 12610, 12620, 12630, 12640, 12650, 12660, 12670, 12680, 12690, 12700, 12710, 12720, 12730, 12740, 12750, 12760, 12770, 12780, 12790, 12800, 12810, 12820, 12830, 12840, 12850, 12860, 12870, 12880, 12890, 12900, 12910]}}], "metadata_type": "eo"}	2021-01-31 22:08:32.388262+00	africa	\N
11	aster_green_vegetation	{"format": {"name": "GeoTIFF"}, "product_type": "aster_green_vegetation"}	2	{"name": "aster_green_vegetation", "metadata": {"format": {"name": "GeoTIFF"}, "product_type": "aster_green_vegetation"}, "description": "ASTER", "measurements": [{"name": "Band_1", "dtype": "uint8", "units": "1", "nodata": 0, "aliases": ["band_01", "B01", "Band1"]}], "metadata_type": "eo"}	2021-01-31 22:07:32.582691+00	africa	\N
12	aster_gypsum_index	{"format": {"name": "GeoTIFF"}, "product_type": "aster_gypsum_index"}	2	{"name": "aster_gypsum_index", "metadata": {"format": {"name": "GeoTIFF"}, "product_type": "aster_gypsum_index"}, "description": "ASTER", "measurements": [{"name": "Band_1", "dtype": "uint8", "units": "1", "nodata": 0, "aliases": ["band_01", "B01", "Band1"]}], "metadata_type": "eo"}	2021-01-31 22:07:34.51044+00	africa	\N
13	aster_kaolin_group_index	{"format": {"name": "GeoTIFF"}, "product_type": "aster_kaolin_group_index"}	2	{"name": "aster_kaolin_group_index", "metadata": {"format": {"name": "GeoTIFF"}, "product_type": "aster_kaolin_group_index"}, "description": "ASTER", "measurements": [{"name": "Band_1", "dtype": "uint8", "units": "1", "nodata": 0, "aliases": ["band_01", "B01", "Band1"]}], "metadata_type": "eo"}	2021-01-31 22:07:36.38928+00	africa	\N
14	aster_mgoh_group_composition	{"format": {"name": "GeoTIFF"}, "product_type": "aster_mgoh_group_composition"}	2	{"name": "aster_mgoh_group_composition", "metadata": {"format": {"name": "GeoTIFF"}, "product_type": "aster_mgoh_group_composition"}, "description": "ASTER", "measurements": [{"name": "Band_1", "dtype": "uint8", "units": "1", "nodata": 0, "aliases": ["band_01", "B01", "Band1"]}], "metadata_type": "eo"}	2021-01-31 22:07:38.288064+00	africa	\N
15	aster_mgoh_group_content	{"format": {"name": "GeoTIFF"}, "product_type": "aster_mgoh_group_content"}	2	{"name": "aster_mgoh_group_content", "metadata": {"format": {"name": "GeoTIFF"}, "product_type": "aster_mgoh_group_content"}, "description": "ASTER", "measurements": [{"name": "Band_1", "dtype": "uint8", "units": "1", "nodata": 0, "aliases": ["band_01", "B01", "Band1"]}], "metadata_type": "eo"}	2021-01-31 22:07:40.168005+00	africa	\N
16	aster_opaque_index	{"format": {"name": "GeoTIFF"}, "product_type": "aster_opaque_index"}	2	{"name": "aster_opaque_index", "metadata": {"format": {"name": "GeoTIFF"}, "product_type": "aster_opaque_index"}, "description": "ASTER", "measurements": [{"name": "Band_1", "dtype": "uint8", "units": "1", "nodata": 0, "aliases": ["band_01", "B01", "Band1"]}], "metadata_type": "eo"}	2021-01-31 22:07:42.04624+00	africa	\N
17	aster_quartz_index	{"format": {"name": "GeoTIFF"}, "product_type": "aster_quartz_index"}	2	{"name": "aster_quartz_index", "metadata": {"format": {"name": "GeoTIFF"}, "product_type": "aster_quartz_index"}, "description": "ASTER", "measurements": [{"name": "Band_1", "dtype": "uint8", "units": "1", "nodata": 0, "aliases": ["band_01", "B01", "Band1"]}], "metadata_type": "eo"}	2021-01-31 22:07:43.918774+00	africa	\N
18	aster_regolith_ratios	{"format": {"name": "GeoTIFF"}, "product_type": "aster_regolith_ratios"}	2	{"name": "aster_regolith_ratios", "metadata": {"format": {"name": "GeoTIFF"}, "product_type": "aster_regolith_ratios"}, "description": "ASTER", "measurements": [{"name": "Band_1", "dtype": "uint8", "units": "1", "nodata": 0, "aliases": ["band_01", "B01", "Band1"]}, {"name": "Band_2", "dtype": "uint8", "units": "1", "nodata": 0, "aliases": ["band_02", "B02", "Band2"]}, {"name": "Band_3", "dtype": "uint8", "units": "1", "nodata": 0, "aliases": ["band_03", "B03", "Band3"]}], "metadata_type": "eo"}	2021-01-31 22:07:45.798151+00	africa	\N
19	aster_silica_index	{"format": {"name": "GeoTIFF"}, "product_type": "aster_silica_index"}	2	{"name": "aster_silica_index", "metadata": {"format": {"name": "GeoTIFF"}, "product_type": "aster_silica_index"}, "description": "ASTER", "measurements": [{"name": "Band_1", "dtype": "uint8", "units": "1", "nodata": 0, "aliases": ["band_01", "B01", "Band1"]}], "metadata_type": "eo"}	2021-01-31 22:07:47.690282+00	africa	\N
20	cemp_insar_alos_displacement	{"product": {"name": "cemp_insar_alos_displacement"}}	1	{"name": "cemp_insar_alos_displacement", "metadata": {"product": {"name": "cemp_insar_alos_displacement"}}, "description": "CEMP InSAR ALOS Displacement", "measurements": [{"name": "ew", "dtype": "float32", "units": "mm", "nodata": -9999, "aliases": ["eastwest"]}, {"name": "ud", "dtype": "float32", "units": "mm", "nodata": -9999, "aliases": ["updown"]}, {"name": "ewstd", "dtype": "float32", "units": "mm", "nodata": -9999, "aliases": ["eastweststandarddev"]}, {"name": "upstd", "dtype": "float32", "units": "mm", "nodata": -9999, "aliases": ["updownstandarddev"]}], "metadata_type": "eo3"}	2021-01-31 22:07:51.070766+00	africa	\N
21	cemp_insar_alos_velocity	{"product": {"name": "cemp_insar_alos_velocity"}}	1	{"name": "cemp_insar_alos_velocity", "metadata": {"product": {"name": "cemp_insar_alos_velocity"}}, "description": "CEMP InSAR ALOS Velocity", "measurements": [{"name": "ew", "dtype": "float32", "units": "mm/year", "nodata": -9999, "aliases": ["eastwest"]}, {"name": "ud", "dtype": "float32", "units": "mm/year", "nodata": -9999, "aliases": ["updown"]}, {"name": "ewstd", "dtype": "float32", "units": "mm/year", "nodata": -9999, "aliases": ["eastweststandarddev"]}, {"name": "upstd", "dtype": "float32", "units": "mm/year", "nodata": -9999, "aliases": ["updownstandarddev"]}], "metadata_type": "eo3"}	2021-01-31 22:07:52.925322+00	africa	\N
22	cemp_insar_envisat_displacement	{"product": {"name": "cemp_insar_envisat_displacement"}}	1	{"name": "cemp_insar_envisat_displacement", "metadata": {"product": {"name": "cemp_insar_envisat_displacement"}}, "description": "CEMP InSAR Envisat Displacement", "measurements": [{"name": "ew", "dtype": "float32", "units": "mm", "nodata": -9999, "aliases": ["eastwest"]}, {"name": "ud", "dtype": "float32", "units": "mm", "nodata": -9999, "aliases": ["updown"]}, {"name": "ewstd", "dtype": "float32", "units": "mm", "nodata": -9999, "aliases": ["eastweststandarddev"]}, {"name": "upstd", "dtype": "float32", "units": "mm", "nodata": -9999, "aliases": ["updownstandarddev"]}], "metadata_type": "eo3"}	2021-01-31 22:07:54.833533+00	africa	\N
23	cemp_insar_envisat_velocity	{"product": {"name": "cemp_insar_envisat_velocity"}}	1	{"name": "cemp_insar_envisat_velocity", "metadata": {"product": {"name": "cemp_insar_envisat_velocity"}}, "description": "CEMP InSAR Envisat Velocity", "measurements": [{"name": "ew", "dtype": "float32", "units": "mm", "nodata": -9999, "aliases": ["eastwest"]}, {"name": "ud", "dtype": "float32", "units": "mm", "nodata": -9999, "aliases": ["updown"]}, {"name": "ewstd", "dtype": "float32", "units": "mm", "nodata": -9999, "aliases": ["eastweststandarddev"]}, {"name": "upstd", "dtype": "float32", "units": "mm", "nodata": -9999, "aliases": ["updownstandarddev"]}], "metadata_type": "eo3"}	2021-01-31 22:07:56.752432+00	africa	\N
24	cemp_insar_radarsat2_displacement	{"product": {"name": "cemp_insar_radarsat2_displacement"}}	1	{"name": "cemp_insar_radarsat2_displacement", "metadata": {"product": {"name": "cemp_insar_radarsat2_displacement"}}, "description": "CEMP InSAR Radarsat-2 Displacement", "measurements": [{"name": "ew", "dtype": "float32", "units": "mm", "nodata": -9999, "aliases": ["eastwest"]}, {"name": "ud", "dtype": "float32", "units": "mm", "nodata": -9999, "aliases": ["updown"]}, {"name": "ewstd", "dtype": "float32", "units": "mm", "nodata": -9999, "aliases": ["eastweststandarddev"]}, {"name": "upstd", "dtype": "float32", "units": "mm", "nodata": -9999, "aliases": ["updownstandarddev"]}], "metadata_type": "eo3"}	2021-01-31 22:07:58.630844+00	africa	\N
25	cemp_insar_radarsat2_velocity	{"product": {"name": "cemp_insar_radarsat2_velocity"}}	1	{"name": "cemp_insar_radarsat2_velocity", "metadata": {"product": {"name": "cemp_insar_radarsat2_velocity"}}, "description": "CEMP InSAR Radarsat-2 Velocity", "measurements": [{"name": "ew", "dtype": "float32", "units": "mm/year", "nodata": -9999, "aliases": ["eastwest"]}, {"name": "ud", "dtype": "float32", "units": "mm/year", "nodata": -9999, "aliases": ["updown"]}, {"name": "ewstd", "dtype": "float32", "units": "mm/year", "nodata": -9999, "aliases": ["eastweststandarddev"]}, {"name": "upstd", "dtype": "float32", "units": "mm/year", "nodata": -9999, "aliases": ["updownstandarddev"]}], "metadata_type": "eo3"}	2021-01-31 22:08:00.566842+00	africa	\N
26	fc_percentile_albers_annual	{"format": {"name": "NetCDF"}, "platform": {"code": "LANDSAT_5,LANDSAT_7,LANDSAT_8"}, "instrument": {"name": "TM,ETM+,OLI"}, "statistics": {"period": "1y"}, "product_type": "fractional_cover_statistical_summary"}	2	{"name": "fc_percentile_albers_annual", "storage": {"crs": "EPSG:3577", "driver": "NetCDF CF", "tile_size": {"x": 100000.0, "y": 100000.0}, "resolution": {"x": 25, "y": -25}, "dimension_order": ["time", "y", "x"]}, "metadata": {"format": {"name": "NetCDF"}, "platform": {"code": "LANDSAT_5,LANDSAT_7,LANDSAT_8"}, "instrument": {"name": "TM,ETM+,OLI"}, "statistics": {"period": "1y"}, "product_type": "fractional_cover_statistical_summary"}, "description": "Landsat Fractional Cover percentile 25 metre, 100km tile, Australian Albers Equal Area projection (EPSG:3577)", "measurements": [{"name": "BS_PC_10", "dtype": "int8", "units": "percent", "nodata": -1}, {"name": "PV_PC_10", "dtype": "int8", "units": "percent", "nodata": -1}, {"name": "NPV_PC_10", "dtype": "int8", "units": "percent", "nodata": -1}, {"name": "BS_PC_50", "dtype": "int8", "units": "percent", "nodata": -1}, {"name": "PV_PC_50", "dtype": "int8", "units": "percent", "nodata": -1}, {"name": "NPV_PC_50", "dtype": "int8", "units": "percent", "nodata": -1}, {"name": "BS_PC_90", "dtype": "int8", "units": "percent", "nodata": -1}, {"name": "PV_PC_90", "dtype": "int8", "units": "percent", "nodata": -1}, {"name": "NPV_PC_90", "dtype": "int8", "units": "percent", "nodata": -1}], "metadata_type": "eo"}	2021-01-31 22:08:02.477889+00	africa	\N
27	fc_percentile_albers_seasonal	{"format": {"name": "GeoTIFF"}, "platform": {"code": "LANDSAT_5,LANDSAT_7,LANDSAT_8"}, "instrument": {"name": "TM,ETM+,OLI"}, "statistics": {"period": "3m"}, "product_type": "fractional_cover_seasonal_summary"}	2	{"name": "fc_percentile_albers_seasonal", "storage": {"crs": "EPSG:3577", "driver": "GeoTIFF", "tile_size": {"x": 100000.0, "y": 100000.0}, "resolution": {"x": 25, "y": -25}, "dimension_order": ["time", "y", "x"]}, "metadata": {"format": {"name": "GeoTIFF"}, "platform": {"code": "LANDSAT_5,LANDSAT_7,LANDSAT_8"}, "instrument": {"name": "TM,ETM+,OLI"}, "statistics": {"period": "3m"}, "product_type": "fractional_cover_seasonal_summary"}, "description": "Landsat Fractional Cover percentile 25 metre, 100km tile, Australian Albers Equal Area projection (EPSG:3577)", "measurements": [{"name": "BS_PC_10", "dtype": "int16", "units": "percent", "nodata": -1}, {"name": "PV_PC_10", "dtype": "int16", "units": "percent", "nodata": -1}, {"name": "NPV_PC_10", "dtype": "int16", "units": "percent", "nodata": -1}, {"name": "BS_PC_50", "dtype": "int16", "units": "percent", "nodata": -1}, {"name": "PV_PC_50", "dtype": "int16", "units": "percent", "nodata": -1}, {"name": "NPV_PC_50", "dtype": "int16", "units": "percent", "nodata": -1}, {"name": "BS_PC_90", "dtype": "int16", "units": "percent", "nodata": -1}, {"name": "PV_PC_90", "dtype": "int16", "units": "percent", "nodata": -1}, {"name": "NPV_PC_90", "dtype": "int16", "units": "percent", "nodata": -1}], "metadata_type": "eo"}	2021-01-31 22:08:04.374193+00	africa	\N
28	geodata_coast_100k	{"format": {"name": "GeoTIFF"}, "platform": {"code": "unknown"}, "instrument": {"name": "unknown"}, "product_type": "model"}	2	{"name": "geodata_coast_100k", "metadata": {"format": {"name": "GeoTIFF"}, "platform": {"code": "unknown"}, "instrument": {"name": "unknown"}, "product_type": "model"}, "description": "Coastline data for Australia", "measurements": [{"name": "land", "dtype": "uint8", "units": "1", "nodata": 0, "flags_definition": {"sea": {"bits": [0, 1], "values": {"0": true}, "description": "Sea"}, "land_type": {"bits": [0, 1], "values": {"0": "sea", "1": "island", "2": "mainland"}, "description": "Sea, Mainland or Island"}}}], "metadata_type": "eo"}	2021-01-31 22:08:11.788064+00	africa	\N
51	nidem	{"format": {"name": "GeoTIFF"}, "product_type": "nidem_v1.0.0"}	2	{"name": "nidem", "storage": {"crs": "EPSG:3577", "resolution": {"x": 25, "y": -25}}, "metadata": {"format": {"name": "GeoTIFF"}, "product_type": "nidem_v1.0.0"}, "description": "National Intertidal Digital Elevation Model 25m 1.0.0", "measurements": [{"name": "nidem", "dtype": "float32", "units": "metres", "nodata": -9999}], "metadata_type": "eo"}	2021-01-31 22:08:57.573608+00	africa	\N
29	high_tide_comp_20p	{"format": {"name": "GeoTIFF"}, "statistic": {"name": "precisegeomedian", "source": "nbar", "tidal_range": {"max": 100, "min": 80, "name": "high"}}, "product_type": "tidal_composite"}	2	{"name": "high_tide_comp_20p", "managed": true, "storage": {"crs": "EPSG:3577", "resolution": {"x": 25, "y": -25}}, "metadata": {"format": {"name": "GeoTIFF"}, "statistic": {"name": "precisegeomedian", "source": "nbar", "tidal_range": {"max": 100, "min": 80, "name": "high"}}, "product_type": "tidal_composite"}, "description": "High tide 20 percentage composites 25m v. 2.0.0", "measurements": [{"name": "blue", "dtype": "float32", "units": "metres", "nodata": -999}, {"name": "green", "dtype": "float32", "units": "metres", "nodata": -999}, {"name": "red", "dtype": "float32", "units": "metres", "nodata": -999}, {"name": "nir", "dtype": "float32", "units": "metres", "nodata": -999}, {"name": "swir1", "dtype": "float32", "units": "metres", "nodata": -999}, {"name": "swir2", "dtype": "float32", "units": "metres", "nodata": -999}], "metadata_type": "eo"}	2021-01-31 22:08:13.685784+00	africa	\N
30	low_tide_comp_20p	{"format": {"name": "GeoTIFF"}, "statistic": {"name": "precisegeomedian", "source": "nbar", "tidal_range": {"max": 20, "min": 0, "name": "low"}}, "product_type": "tidal_composite"}	2	{"name": "low_tide_comp_20p", "managed": true, "storage": {"crs": "EPSG:3577", "resolution": {"x": 25, "y": -25}}, "metadata": {"format": {"name": "GeoTIFF"}, "statistic": {"name": "precisegeomedian", "source": "nbar", "tidal_range": {"max": 20, "min": 0, "name": "low"}}, "product_type": "tidal_composite"}, "description": "Low tide 20 percentage composites 25m v. 2.0.0", "measurements": [{"name": "blue", "dtype": "float32", "units": "metres", "nodata": -999}, {"name": "green", "dtype": "float32", "units": "metres", "nodata": -999}, {"name": "red", "dtype": "float32", "units": "metres", "nodata": -999}, {"name": "nir", "dtype": "float32", "units": "metres", "nodata": -999}, {"name": "swir1", "dtype": "float32", "units": "metres", "nodata": -999}, {"name": "swir2", "dtype": "float32", "units": "metres", "nodata": -999}], "metadata_type": "eo"}	2021-01-31 22:08:13.731437+00	africa	\N
31	historical_airborne_photography	{"format": {"name": "GeoTIFF"}, "product_type": "airborne_photography"}	2	{"name": "historical_airborne_photography", "metadata": {"format": {"name": "GeoTIFF"}, "product_type": "airborne_photography"}, "description": "Historical Airborne Photography", "measurements": [{"name": "Band_1", "dtype": "uint8", "units": "1", "nodata": 0, "aliases": ["band_01", "B01", "Band1"]}], "metadata_type": "eo"}	2021-01-31 22:08:15.612352+00	africa	\N
32	item_v2	{"format": {"name": "NetCDF"}, "statistic": {"name": "decile"}, "product_type": "ITEM"}	2	{"name": "item_v2", "managed": true, "storage": {"crs": "EPSG:3577", "resolution": {"x": 25, "y": -25}}, "metadata": {"format": {"name": "NetCDF"}, "statistic": {"name": "decile"}, "product_type": "ITEM"}, "description": "Intertidal Extents Model", "measurements": [{"name": "relative", "dtype": "int16", "units": "0.1", "nodata": 0}], "metadata_type": "eo"}	2021-01-31 22:08:17.515248+00	africa	\N
33	item_v2_conf	{"format": {"name": "NetCDF"}, "statistic": {"name": "stddev", "source": "ndwi"}, "product_type": "ITEM"}	2	{"name": "item_v2_conf", "managed": true, "storage": {"crs": "EPSG:3577", "resolution": {"x": 25, "y": -25}}, "metadata": {"format": {"name": "NetCDF"}, "statistic": {"name": "stddev", "source": "ndwi"}, "product_type": "ITEM"}, "description": "Average ndwi Standard Deviation", "measurements": [{"name": "stddev", "dtype": "float32", "units": "1", "nodata": -6666}], "metadata_type": "eo"}	2021-01-31 22:08:17.560379+00	africa	\N
34	landsat_barest_earth	{"format": {"name": "GeoTIFF"}, "platform": {"code": "LANDSAT_5,LANDSAT_7,LANDSAT_8"}, "instrument": {"name": "TM,ETM+,OLI"}, "product_type": "landsat_barest_earth"}	2	{"name": "landsat_barest_earth", "storage": {"crs": "EPSG:3577", "driver": "GeoTIFF", "tile_size": {"x": 100000.0, "y": 100000.0}, "resolution": {"x": 25, "y": -25}, "dimension_order": ["time", "y", "x"]}, "metadata": {"format": {"name": "GeoTIFF"}, "platform": {"code": "LANDSAT_5,LANDSAT_7,LANDSAT_8"}, "instrument": {"name": "TM,ETM+,OLI"}, "product_type": "landsat_barest_earth"}, "description": "Landsat-5/Landsat-7/Landsat-8 combined Barest Earth pixel composite albers 25 metre, 100km tile, Australian Albers Equal Area projection (EPSG:3577)", "measurements": [{"name": "blue", "dtype": "int16", "units": "1", "nodata": -999}, {"name": "green", "dtype": "int16", "units": "1", "nodata": -999}, {"name": "red", "dtype": "int16", "units": "1", "nodata": -999}, {"name": "nir", "dtype": "int16", "units": "1", "nodata": -999}, {"name": "swir1", "dtype": "int16", "units": "1", "nodata": -999}, {"name": "swir2", "dtype": "int16", "units": "1", "nodata": -999}], "metadata_type": "eo"}	2021-01-31 22:08:21.036663+00	africa	\N
35	ls5_fc_albers	{"format": {"name": "GeoTIFF"}, "platform": {"code": "LANDSAT_5"}, "instrument": {"name": "TM"}, "product_type": "fractional_cover"}	2	{"name": "ls5_fc_albers", "storage": {"crs": "EPSG:3577", "resolution": {"x": 25, "y": -25}, "dimension_order": ["time", "y", "x"]}, "metadata": {"format": {"name": "GeoTIFF"}, "platform": {"code": "LANDSAT_5"}, "instrument": {"name": "TM"}, "product_type": "fractional_cover"}, "description": "Landsat 5 Fractional Cover 25 metre, 100km tile, Australian Albers Equal Area projection (EPSG:3577)", "measurements": [{"name": "BS", "dtype": "int16", "units": "percent", "nodata": -1, "aliases": ["bare"]}, {"name": "PV", "dtype": "int16", "units": "percent", "nodata": -1, "aliases": ["green_veg"]}, {"name": "NPV", "dtype": "int16", "units": "percent", "nodata": -1, "aliases": ["dead_veg"]}, {"name": "UE", "dtype": "int16", "units": "1", "nodata": -1, "aliases": ["err"]}], "metadata_type": "eo"}	2021-01-31 22:08:24.530448+00	africa	\N
52	sentinel2_wofs_nrt	{"format": {"name": "GeoTIFF"}, "instrument": {"name": "MSI"}, "product_type": "wofs"}	2	{"name": "sentinel2_wofs_nrt", "metadata": {"format": {"name": "GeoTIFF"}, "instrument": {"name": "MSI"}, "product_type": "wofs"}, "description": "Sentinel 2 NRT Water Observations from Space", "measurements": [{"name": "water", "dtype": "uint8", "units": "1", "nodata": 0}], "metadata_type": "eo"}	2021-01-31 22:09:04.932281+00	africa	\N
36	ls8_nbart_geomedian_annual	{"platform": {"code": "LANDSAT_8"}, "instrument": {"name": "OLI"}, "statistics": {"period": "1y"}, "product_type": "surface_reflectance_statistical_summary"}	2	{"name": "ls8_nbart_geomedian_annual", "storage": {"crs": "EPSG:3577", "driver": "GeoTIFF", "tile_size": {"x": 100000.0, "y": 100000.0}, "resolution": {"x": 25, "y": -25}, "dimension_order": ["time", "y", "x"]}, "metadata": {"platform": {"code": "LANDSAT_8"}, "instrument": {"name": "OLI"}, "statistics": {"period": "1y"}, "product_type": "surface_reflectance_statistical_summary"}, "description": "Surface Reflectance Geometric Median 25 metre, 100km tile, Australian Albers Equal Area projection (EPSG:3577)", "measurements": [{"name": "blue", "dtype": "int16", "units": "1", "nodata": -999}, {"name": "green", "dtype": "int16", "units": "1", "nodata": -999}, {"name": "red", "dtype": "int16", "units": "1", "nodata": -999}, {"name": "nir", "dtype": "int16", "units": "1", "nodata": -999}, {"name": "swir1", "dtype": "int16", "units": "1", "nodata": -999}, {"name": "swir2", "dtype": "int16", "units": "1", "nodata": -999}], "metadata_type": "eo"}	2021-01-31 22:08:28.1466+00	africa	\N
37	ls7_nbart_geomedian_annual	{"platform": {"code": "LANDSAT_7"}, "instrument": {"name": "ETM"}, "statistics": {"period": "1y"}, "product_type": "surface_reflectance_statistical_summary"}	2	{"name": "ls7_nbart_geomedian_annual", "storage": {"crs": "EPSG:3577", "driver": "GeoTIFF", "tile_size": {"x": 100000.0, "y": 100000.0}, "resolution": {"x": 25, "y": -25}, "dimension_order": ["time", "y", "x"]}, "metadata": {"platform": {"code": "LANDSAT_7"}, "instrument": {"name": "ETM"}, "statistics": {"period": "1y"}, "product_type": "surface_reflectance_statistical_summary"}, "description": "Surface Reflectance Geometric Median 25 metre, 100km tile, Australian Albers Equal Area projection (EPSG:3577)", "measurements": [{"name": "blue", "dtype": "int16", "units": "1", "nodata": -999}, {"name": "green", "dtype": "int16", "units": "1", "nodata": -999}, {"name": "red", "dtype": "int16", "units": "1", "nodata": -999}, {"name": "nir", "dtype": "int16", "units": "1", "nodata": -999}, {"name": "swir1", "dtype": "int16", "units": "1", "nodata": -999}, {"name": "swir2", "dtype": "int16", "units": "1", "nodata": -999}], "metadata_type": "eo"}	2021-01-31 22:08:28.188477+00	africa	\N
38	ls5_nbart_geomedian_annual	{"platform": {"code": "LANDSAT_5"}, "instrument": {"name": "TM"}, "statistics": {"period": "1y"}, "product_type": "surface_reflectance_statistical_summary"}	2	{"name": "ls5_nbart_geomedian_annual", "storage": {"crs": "EPSG:3577", "driver": "GeoTIFF", "tile_size": {"x": 100000.0, "y": 100000.0}, "resolution": {"x": 25, "y": -25}, "dimension_order": ["time", "y", "x"]}, "metadata": {"platform": {"code": "LANDSAT_5"}, "instrument": {"name": "TM"}, "statistics": {"period": "1y"}, "product_type": "surface_reflectance_statistical_summary"}, "description": "Surface Reflectance Geometric Median 25 metre, 100km tile, Australian Albers Equal Area projection (EPSG:3577)", "measurements": [{"name": "blue", "dtype": "int16", "units": "1", "nodata": -999}, {"name": "green", "dtype": "int16", "units": "1", "nodata": -999}, {"name": "red", "dtype": "int16", "units": "1", "nodata": -999}, {"name": "nir", "dtype": "int16", "units": "1", "nodata": -999}, {"name": "swir1", "dtype": "int16", "units": "1", "nodata": -999}, {"name": "swir2", "dtype": "int16", "units": "1", "nodata": -999}], "metadata_type": "eo"}	2021-01-31 22:08:28.226927+00	africa	\N
39	ls8_nbart_tmad_annual	{"platform": {"code": "LANDSAT_8"}, "instrument": {"name": "OLI"}, "statistics": {"period": "1y"}, "product_type": "surface_reflectance_triple_mad"}	2	{"name": "ls8_nbart_tmad_annual", "storage": {"crs": "EPSG:3577", "driver": "NetCDF CF", "tile_size": {"x": 100000.0, "y": 100000.0}, "resolution": {"x": 25, "y": -25}, "dimension_order": ["time", "y", "x"]}, "metadata": {"platform": {"code": "LANDSAT_8"}, "instrument": {"name": "OLI"}, "statistics": {"period": "1y"}, "product_type": "surface_reflectance_triple_mad"}, "description": "Surface Reflectance Triple Median Absolute Deviation 25 metre, 100km tile, Australian Albers Equal Area projection (EPSG:3577)", "measurements": [{"name": "sdev", "dtype": "float32", "units": "1", "nodata": "NaN"}, {"name": "edev", "dtype": "float32", "units": "1", "nodata": "NaN"}, {"name": "bcdev", "dtype": "float32", "units": "1", "nodata": "NaN"}], "metadata_type": "eo"}	2021-01-31 22:08:30.162985+00	africa	\N
40	ls7_nbart_tmad_annual	{"platform": {"code": "LANDSAT_7"}, "instrument": {"name": "ETM+"}, "statistics": {"period": "1y"}, "product_type": "surface_reflectance_triple_mad"}	2	{"name": "ls7_nbart_tmad_annual", "storage": {"crs": "EPSG:3577", "driver": "NetCDF CF", "tile_size": {"x": 100000.0, "y": 100000.0}, "resolution": {"x": 25, "y": -25}, "dimension_order": ["time", "y", "x"]}, "metadata": {"platform": {"code": "LANDSAT_7"}, "instrument": {"name": "ETM+"}, "statistics": {"period": "1y"}, "product_type": "surface_reflectance_triple_mad"}, "description": "Surface Reflectance Triple Median Absolute Deviation 25 metre, 100km tile, Australian Albers Equal Area projection (EPSG:3577)", "measurements": [{"name": "sdev", "dtype": "float32", "units": "1", "nodata": "NaN"}, {"name": "edev", "dtype": "float32", "units": "1", "nodata": "NaN"}, {"name": "bcdev", "dtype": "float32", "units": "1", "nodata": "NaN"}], "metadata_type": "eo"}	2021-01-31 22:08:30.203565+00	africa	\N
41	ls5_nbart_tmad_annual	{"platform": {"code": "LANDSAT_5"}, "instrument": {"name": "TM"}, "statistics": {"period": "1y"}, "product_type": "surface_reflectance_triple_mad"}	2	{"name": "ls5_nbart_tmad_annual", "storage": {"crs": "EPSG:3577", "driver": "NetCDF CF", "tile_size": {"x": 100000.0, "y": 100000.0}, "resolution": {"x": 25, "y": -25}, "dimension_order": ["time", "y", "x"]}, "metadata": {"platform": {"code": "LANDSAT_5"}, "instrument": {"name": "TM"}, "statistics": {"period": "1y"}, "product_type": "surface_reflectance_triple_mad"}, "description": "Surface Reflectance Triple Median Absolute Deviation 25 metre, 100km tile, Australian Albers Equal Area projection (EPSG:3577)", "measurements": [{"name": "sdev", "dtype": "float32", "units": "1", "nodata": "NaN"}, {"name": "edev", "dtype": "float32", "units": "1", "nodata": "NaN"}, {"name": "bcdev", "dtype": "float32", "units": "1", "nodata": "NaN"}], "metadata_type": "eo"}	2021-01-31 22:08:30.241274+00	africa	\N
43	ls7_fc_albers	{"format": {"name": "GeoTIFF"}, "platform": {"code": "LANDSAT_7"}, "instrument": {"name": "ETM"}, "product_type": "fractional_cover"}	2	{"name": "ls7_fc_albers", "storage": {"crs": "EPSG:3577", "resolution": {"x": 25, "y": -25}, "dimension_order": ["time", "y", "x"]}, "metadata": {"format": {"name": "GeoTIFF"}, "platform": {"code": "LANDSAT_7"}, "instrument": {"name": "ETM"}, "product_type": "fractional_cover"}, "description": "Landsat 7 Fractional Cover 25 metre, 100km tile, Australian Albers Equal Area projection (EPSG:3577)", "measurements": [{"name": "BS", "dtype": "int16", "units": "percent", "nodata": -1, "aliases": ["bare"]}, {"name": "PV", "dtype": "int16", "units": "percent", "nodata": -1, "aliases": ["green_veg"]}, {"name": "NPV", "dtype": "int16", "units": "percent", "nodata": -1, "aliases": ["dead_veg"]}, {"name": "UE", "dtype": "int16", "units": "1", "nodata": -1, "aliases": ["err"]}], "metadata_type": "eo"}	2021-01-31 22:08:34.293794+00	africa	\N
44	ls7_usgs_l2c1	{"format": {"name": "GeoTiff"}, "platform": {"code": "LANDSAT_7"}, "instrument": {"name": "ETM"}, "product_type": "LS_USGS_L2C1"}	2	{"name": "ls7_usgs_l2c1", "metadata": {"format": {"name": "GeoTiff"}, "platform": {"code": "LANDSAT_7"}, "instrument": {"name": "ETM"}, "product_type": "LS_USGS_L2C1"}, "description": "Landsat 7 Enhanced Thematic Mapper Plus (ETM+) USGS ARD 30 metre tile", "measurements": [{"name": "sr_cloud_qa", "dtype": "uint8", "units": "1", "nodata": 255, "aliases": ["cloud_qa"], "flags_definition": {"pixelqa": {"bits": [0, 1, 2, 3, 4, 5, 6, 7], "values": {"0": "dark dense vegetation", "1": "cloud", "2": "cloud shadow", "3": "adjacent to cloud", "4": "snow", "5": "land/water"}, "description": "cloud_qa"}}}, {"name": "sr_atmos_opacity", "dtype": "int16", "units": "1", "nodata": -9999, "aliases": ["opacity"]}, {"name": "blue", "dtype": "int16", "units": "1", "nodata": -9999, "aliases": ["band_1", "sr_band1"], "spectral_definition": {"response": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.016, 0.027, 0.048, 0.094, 0.167, 0.287, 0.459, 0.605, 0.728, 0.769, 0.792, 0.821, 0.857, 0.857, 0.862, 0.839, 0.845, 0.81, 0.802, 0.804, 0.779, 0.798, 0.816, 0.876, 0.888, 0.901, 0.918, 0.896, 0.903, 0.888, 0.89, 0.863, 0.86, 0.842, 0.866, 0.875, 0.881, 0.888, 0.898, 0.879, 0.884, 0.907, 0.928, 0.932, 0.955, 0.958, 0.948, 0.952, 0.956, 0.98, 0.98, 0.975, 0.973, 0.977, 0.958, 0.965, 0.957, 0.952, 0.973, 0.974, 0.995, 0.986, 0.986, 0.994, 1.0, 0.99, 0.99, 0.976, 0.983, 0.976, 0.983, 0.96, 0.973, 0.964, 0.975, 0.96, 0.932, 0.853, 0.684, 0.486, 0.293, 0.15, 0.073, 0.036, 0.019, 0.009, 0.0, 0.0, 0.0], "wavelength": [410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523]}}, {"name": "green", "dtype": "int16", "units": "1", "nodata": -9999, "aliases": ["band_2", "sr_band2"], "spectral_definition": {"response": [0.0006, 0.0009, 0.001, 0.002, 0.002, 0.003, 0.005, 0.009, 0.0145, 0.0236, 0.026, 0.041, 0.06, 0.088, 0.126, 0.174, 0.236, 0.308, 0.388, 0.472, 0.552, 0.621, 0.676, 0.716, 0.743, 0.759, 0.769, 0.779, 0.79, 0.805, 0.822, 0.842, 0.861, 0.878, 0.893, 0.905, 0.916, 0.924, 0.933, 0.942, 0.947, 0.951, 0.953, 0.952, 0.951, 0.952, 0.951, 0.951, 0.952, 0.952, 0.953, 0.951, 0.95, 0.95, 0.951, 0.954, 0.96, 0.966, 0.968, 0.965, 0.959, 0.951, 0.944, 0.937, 0.932, 0.933, 0.935, 0.937, 0.94, 0.945, 0.951, 0.955, 0.957, 0.956, 0.957, 0.955, 0.952, 0.954, 0.958, 0.963, 0.973, 0.981, 0.988, 0.995, 1.0, 1.0, 0.994, 0.983, 0.969, 0.954, 0.942, 0.936, 0.932, 0.928, 0.924, 0.912, 0.883, 0.834, 0.763, 0.674, 0.574, 0.473, 0.38, 0.3, 0.235, 0.185, 0.146, 0.117, 0.094, 0.077, 0.062, 0.052, 0.042, 0.033, 0.026, 0.021, 0.0158, 0.01235, 0.0094, 0.00717, 0.0048, 0.0037, 0.0026, 0.0017, 0.0014, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "wavelength": [500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 635, 640, 645, 650]}}, {"name": "red", "dtype": "int16", "units": "1", "nodata": -9999, "aliases": ["band_3", "sr_band3"], "spectral_definition": {"response": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0005, 0.0001, 0.0, 0.0005, 0.0006, 0.0014, 0.002, 0.003, 0.006, 0.013, 0.025, 0.047, 0.083, 0.137, 0.211, 0.306, 0.419, 0.545, 0.674, 0.788, 0.873, 0.921, 0.941, 0.943, 0.942, 0.939, 0.937, 0.935, 0.935, 0.938, 0.943, 0.949, 0.953, 0.961, 0.968, 0.971, 0.973, 0.974, 0.972, 0.969, 0.963, 0.958, 0.956, 0.955, 0.955, 0.956, 0.962, 0.969, 0.977, 0.983, 0.988, 0.993, 0.996, 0.997, 0.999, 1.0, 1.0, 0.998, 0.996, 0.995, 0.993, 0.992, 0.991, 0.989, 0.988, 0.984, 0.977, 0.97, 0.96, 0.949, 0.94, 0.932, 0.919, 0.898, 0.863, 0.809, 0.729, 0.625, 0.506, 0.382, 0.272, 0.183, 0.12, 0.079, 0.053, 0.036, 0.025, 0.0196, 0.0142, 0.0101, 0.0075, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "wavelength": [580, 590, 600, 605, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 683, 684, 685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704, 705, 710, 715, 720, 725, 730, 740]}}, {"name": "nir", "dtype": "int16", "units": "1", "nodata": -9999, "aliases": ["band_4", "sr_band4"], "spectral_definition": {"response": [0.0, 0.0, 0.0004, 0.0037, 0.001, 0.0144, 0.0182, 0.0216, 0.0269, 0.0315, 0.0377, 0.0474, 0.0562, 0.0688, 0.069, 0.083, 0.099, 0.121, 0.146, 0.175, 0.209, 0.248, 0.294, 0.346, 0.402, 0.463, 0.523, 0.588, 0.649, 0.705, 0.757, 0.797, 0.827, 0.853, 0.871, 0.884, 0.892, 0.899, 0.903, 0.908, 0.911, 0.916, 0.92, 0.925, 0.926, 0.927, 0.927, 0.929, 0.932, 0.93, 0.926, 0.926, 0.925, 0.928, 0.925, 0.926, 0.928, 0.928, 0.928, 0.923, 0.92, 0.919, 0.914, 0.91, 0.908, 0.905, 0.903, 0.904, 0.902, 0.909, 0.917, 0.92, 0.928, 0.938, 0.946, 0.953, 0.962, 0.969, 0.971, 0.971, 0.97, 0.969, 0.969, 0.97, 0.967, 0.969, 0.968, 0.963, 0.965, 0.967, 0.965, 0.963, 0.958, 0.95, 0.949, 0.943, 0.933, 0.929, 0.928, 0.925, 0.924, 0.927, 0.932, 0.934, 0.943, 0.952, 0.956, 0.966, 0.977, 0.985, 0.99, 0.992, 0.993, 0.994, 0.998, 0.996, 0.992, 0.991, 0.992, 0.994, 0.993, 0.997, 0.997, 0.996, 0.998, 0.999, 1.0, 0.999, 0.996, 0.991, 0.99, 0.991, 0.985, 0.978, 0.969, 0.955, 0.937, 0.916, 0.892, 0.868, 0.845, 0.824, 0.811, 0.807, 0.819, 0.841, 0.868, 0.892, 0.892, 0.854, 0.77, 0.644, 0.501, 0.365, 0.256, 0.177, 0.122, 0.085, 0.061, 0.044, 0.032, 0.025, 0.019, 0.014, 0.011, 0.0107, 0.008, 0.0061, 0.0052, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "wavelength": [730, 735, 740, 745, 750, 751, 752, 753, 754, 755, 756, 757, 758, 759, 760, 761, 762, 763, 764, 765, 766, 767, 768, 769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784, 785, 786, 787, 788, 789, 790, 791, 792, 793, 794, 795, 796, 797, 798, 799, 800, 801, 802, 803, 804, 805, 806, 807, 808, 809, 810, 811, 812, 813, 814, 815, 816, 817, 818, 819, 820, 821, 822, 823, 824, 825, 826, 827, 828, 829, 830, 831, 832, 833, 834, 835, 836, 837, 838, 839, 840, 841, 842, 843, 844, 845, 846, 847, 848, 849, 850, 851, 852, 853, 854, 855, 856, 857, 858, 859, 860, 861, 862, 863, 864, 865, 866, 867, 868, 869, 870, 871, 872, 873, 874, 875, 876, 877, 878, 879, 880, 881, 882, 883, 884, 885, 886, 887, 888, 889, 890, 891, 892, 893, 894, 895, 896, 897, 898, 899, 900, 901, 902, 903, 904, 905, 906, 907, 908, 909, 910, 911, 912, 913, 914, 915, 920, 925, 930, 935, 940, 945]}}, {"name": "swir1", "dtype": "int16", "units": "1", "nodata": -9999, "aliases": ["band_5", "sr_band5"], "spectral_definition": {"response": [0.006, 0.012, 0.003, 0.015, 0.012, 0.024, 0.04, 0.041, 0.057, 0.076, 0.097, 0.12, 0.176, 0.215, 0.274, 0.339, 0.393, 0.462, 0.499, 0.558, 0.598, 0.634, 0.667, 0.704, 0.724, 0.75, 0.778, 0.808, 0.825, 0.851, 0.867, 0.872, 0.884, 0.902, 0.901, 0.896, 0.897, 0.89, 0.899, 0.884, 0.876, 0.867, 0.873, 0.872, 0.879, 0.874, 0.861, 0.859, 0.877, 0.879, 0.899, 0.893, 0.9, 0.897, 0.917, 0.921, 0.926, 0.929, 0.945, 0.947, 0.948, 0.955, 0.952, 0.969, 0.96, 0.962, 0.959, 0.978, 0.96, 0.955, 0.952, 0.951, 0.952, 0.956, 0.944, 0.935, 0.933, 0.928, 0.942, 0.948, 0.942, 0.933, 0.944, 0.948, 0.945, 0.943, 0.951, 0.964, 0.967, 0.971, 0.974, 0.991, 0.995, 0.999, 0.996, 0.994, 1.0, 0.994, 0.983, 0.99, 0.987, 0.992, 0.986, 0.981, 0.983, 0.976, 0.978, 0.97, 0.968, 0.96, 0.944, 0.921, 0.883, 0.845, 0.791, 0.711, 0.638, 0.547, 0.462, 0.393, 0.325, 0.267, 0.212, 0.175, 0.142, 0.111, 0.084, 0.077, 0.058, 0.049, 0.042, 0.039, 0.034, 0.02, 0.021, 0.022, 0.011, 0.012, 0.004, 0.008, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "wavelength": [1514, 1515, 1517, 1519, 1521, 1523, 1525, 1526, 1528, 1530, 1532, 1534, 1536, 1538, 1540, 1542, 1543, 1545, 1547, 1549, 1551, 1553, 1555, 1557, 1559, 1561, 1563, 1565, 1567, 1569, 1571, 1572, 1574, 1576, 1578, 1580, 1582, 1584, 1586, 1588, 1590, 1592, 1594, 1596, 1598, 1600, 1602, 1604, 1606, 1608, 1610, 1613, 1615, 1617, 1619, 1621, 1623, 1625, 1627, 1629, 1631, 1633, 1635, 1637, 1639, 1641, 1643, 1645, 1647, 1649, 1651, 1653, 1656, 1658, 1660, 1662, 1664, 1666, 1668, 1670, 1672, 1674, 1676, 1678, 1680, 1682, 1684, 1687, 1689, 1691, 1693, 1695, 1697, 1699, 1701, 1703, 1705, 1707, 1709, 1711, 1714, 1716, 1718, 1720, 1722, 1724, 1725, 1726, 1728, 1730, 1732, 1734, 1736, 1738, 1740, 1742, 1744, 1747, 1749, 1751, 1753, 1755, 1757, 1759, 1761, 1763, 1765, 1767, 1769, 1771, 1773, 1775, 1777, 1779, 1781, 1783, 1785, 1787, 1789, 1791, 1793, 1795, 1797, 1799, 1801, 1803, 1805, 1807, 1809, 1811, 1813, 1815, 1820, 1825, 1830, 1840, 1850, 1860, 1870, 1880]}}, {"name": "swir2", "dtype": "int16", "units": "1", "nodata": -9999, "aliases": ["band_7", "sr_band7"], "spectral_definition": {"response": [0.0, 0.003, -0.002, 0.003, -0.001, 0.0, 0.004, -0.004, 0.002, 0.002, 0.002, 0.012, 0.009, 0.007, 0.011, 0.02, 0.017, 0.03, 0.035, 0.037, 0.044, 0.051, 0.065, 0.08, 0.088, 0.102, 0.133, 0.165, 0.188, 0.22, 0.264, 0.316, 0.367, 0.421, 0.484, 0.554, 0.59, 0.67, 0.683, 0.73, 0.756, 0.767, 0.794, 0.774, 0.776, 0.789, 0.775, 0.784, 0.778, 0.768, 0.762, 0.761, 0.775, 0.775, 0.764, 0.784, 0.792, 0.814, 0.794, 0.825, 0.817, 0.806, 0.819, 0.821, 0.852, 0.832, 0.836, 0.85, 0.855, 0.862, 0.853, 0.871, 0.848, 0.882, 0.875, 0.86, 0.856, 0.887, 0.85, 0.872, 0.879, 0.857, 0.865, 0.867, 0.871, 0.882, 0.87, 0.869, 0.873, 0.877, 0.868, 0.88, 0.877, 0.87, 0.878, 0.88, 0.868, 0.881, 0.87, 0.856, 0.863, 0.863, 0.857, 0.844, 0.859, 0.857, 0.852, 0.866, 0.868, 0.856, 0.856, 0.847, 0.861, 0.862, 0.84, 0.856, 0.838, 0.856, 0.837, 0.842, 0.826, 0.844, 0.827, 0.842, 0.822, 0.843, 0.823, 0.854, 0.839, 0.853, 0.854, 0.865, 0.873, 0.869, 0.865, 0.893, 0.89, 0.89, 0.906, 0.924, 0.92, 0.922, 0.939, 0.916, 0.94, 0.93, 0.942, 0.957, 0.954, 0.951, 0.954, 0.966, 0.975, 0.985, 0.971, 0.973, 0.97, 0.993, 0.996, 0.983, 0.972, 1.0, 0.998, 0.971, 0.968, 0.967, 0.962, 0.949, 0.923, 0.929, 0.917, 0.934, 0.903, 0.926, 0.916, 0.942, 0.924, 0.92, 0.863, 0.824, 0.775, 0.684, 0.583, 0.48, 0.378, 0.275, 0.233, 0.171, 0.131, 0.111, 0.081, 0.069, 0.046, 0.029, 0.038, -0.002, 0.029, 0.016, 0.009, 0.017, 0.003, 0.015, 0.0, -0.009, 0.007, 0.0, 0.0, 0.0], "wavelength": [2000, 2001, 2003, 2005, 2007, 2009, 2011, 2013, 2015, 2017, 2018, 2020, 2022, 2024, 2026, 2028, 2030, 2032, 2034, 2035, 2037, 2039, 2041, 2043, 2045, 2047, 2049, 2051, 2052, 2054, 2056, 2058, 2060, 2062, 2064, 2066, 2067, 2069, 2071, 2073, 2075, 2077, 2079, 2081, 2083, 2085, 2086, 2088, 2090, 2092, 2094, 2096, 2099, 2100, 2102, 2104, 2106, 2108, 2110, 2112, 2114, 2116, 2117, 2119, 2121, 2123, 2125, 2127, 2129, 2131, 2133, 2135, 2136, 2138, 2140, 2142, 2144, 2146, 2148, 2150, 2151, 2153, 2155, 2157, 2159, 2161, 2163, 2165, 2166, 2168, 2170, 2172, 2174, 2176, 2178, 2180, 2182, 2183, 2185, 2187, 2189, 2191, 2193, 2195, 2197, 2199, 2201, 2203, 2205, 2207, 2209, 2210, 2212, 2214, 2216, 2218, 2220, 2222, 2223, 2226, 2227, 2229, 2231, 2233, 2235, 2237, 2239, 2241, 2242, 2244, 2246, 2248, 2250, 2252, 2254, 2256, 2258, 2259, 2261, 2263, 2265, 2267, 2269, 2271, 2273, 2274, 2276, 2278, 2280, 2282, 2284, 2286, 2288, 2290, 2292, 2293, 2295, 2297, 2299, 2301, 2303, 2305, 2307, 2309, 2310, 2312, 2314, 2316, 2318, 2320, 2322, 2323, 2325, 2327, 2329, 2331, 2333, 2335, 2337, 2339, 2340, 2342, 2344, 2346, 2348, 2350, 2352, 2354, 2355, 2357, 2359, 2361, 2363, 2365, 2367, 2369, 2371, 2373, 2374, 2376, 2378, 2380, 2382, 2384, 2386, 2390, 2395, 2400]}}, {"name": "quality", "dtype": "uint8", "units": "1", "nodata": 255, "aliases": ["pixel_qa"], "flags_definition": {"pixelqa": {"bits": [0, 1, 2, 3, 4, 5, 6, 7], "values": {"0": "fill", "1": "clear", "2": "water", "3": "cloud shadow", "4": "snow", "5": "cloud", "6": "cloud confidence", "7": "cloud confidence", "8": "cirrus confidence", "9": "cirrus confidence", "10": "terrain occlusion", "11": "unused", "12": "unused", "13": "unused", "14": "unused", "15": "unused"}, "description": "PixelQA"}}}, {"name": "radsat_qa", "dtype": "uint8", "units": "1", "nodata": 255, "aliases": ["radasat"], "flags_definition": {"radsatqa": {"bits": [0, 1, 2, 3, 4, 5, 6, 7], "values": {"0": "Data Fill Flag (0 = valid data, 1 = invalid data)", "1": "Band 1 Data Saturation Flag (0 = valid data, 1 = saturated data)", "2": "Band 2 Data Saturation Flag (0 = valid data, 1 = saturated data)", "3": "Band 3 Data Saturation Flag (0 = valid data, 1 = saturated data)", "4": "Band 4 Data Saturation Flag (0 = valid data, 1 = saturated data)", "5": "Band 5 Data Saturation Flag (0 = valid data, 1 = saturated data)", "6": "Band 6 Data Saturation Flag (0 = valid data, 1 = saturated data)", "7": "Band 7 Data Saturation Flag (0 = valid data, 1 = saturated data)"}, "description": "saturation mask"}}}, {"name": "lwir1", "dtype": "int16", "units": "1", "nodata": -9999, "aliases": ["thermal60", "bt_band6"], "spectral_definition": {"response": [0, 0.0095, 0.019, 0.021, 0.007, 0.017, 0.027, 0.025, 0.027, 0.027, 0.03, 0.037, 0.044, 0.037, 0.065, 0.053, 0.052, 0.049, 0.068, 0.084, 0.109, 0.124, 0.134, 0.173, 0.175, 0.217, 0.256, 0.286, 0.344, 0.384, 0.443, 0.492, 0.518, 0.544, 0.614, 0.68, 0.725, 0.794, 0.823, 0.862, 0.89, 0.907, 0.93, 0.96, 0.965, 0.971, 0.969, 0.98, 0.979, 1, 0.981, 0.969, 0.988, 0.974, 0.952, 0.953, 0.954, 0.955, 0.956, 0.957, 0.957, 0.957, 0.957, 0.957, 0.957, 0.9555, 0.954, 0.9525, 0.951, 0.9495, 0.948, 0.948, 0.948, 0.948, 0.948, 0.948, 0.943, 0.938, 0.933, 0.928, 0.923, 0.9214, 0.9198, 0.9182, 0.9166, 0.915, 0.9106, 0.9062, 0.9018, 0.8974, 0.893, 0.8938, 0.8946, 0.8954, 0.8962, 0.897, 0.8948, 0.8926, 0.8904, 0.8882, 0.886, 0.8854, 0.8848, 0.8842, 0.8836, 0.883, 0.8828, 0.8826, 0.8824, 0.8822, 0.882, 0.8816, 0.8812, 0.8808, 0.8804, 0.88, 0.879, 0.878, 0.877, 0.876, 0.875, 0.8712, 0.8674, 0.8636, 0.8598, 0.856, 0.8562, 0.8565, 0.8568, 0.857, 0.8516, 0.8462, 0.8408, 0.8354, 0.83, 0.8306, 0.8312, 0.8318, 0.8324, 0.833, 0.8264, 0.8198, 0.8132, 0.8066, 0.8, 0.7994, 0.7988, 0.7982, 0.7976, 0.797, 0.7954, 0.7938, 0.7922, 0.7906, 0.789, 0.78, 0.771, 0.762, 0.753, 0.744, 0.7377, 0.7315, 0.7253, 0.719, 0.7174, 0.7158, 0.7142, 0.7126, 0.711, 0.7086, 0.7062, 0.7038, 0.7014, 0.699, 0.6924, 0.6858, 0.6792, 0.6726, 0.666, 0.666, 0.666, 0.666, 0.666, 0.6584, 0.6508, 0.6432, 0.6356, 0.628, 0.6276, 0.6272, 0.6268, 0.6264, 0.626, 0.6175, 0.609, 0.6005, 0.592, 0.5908, 0.5896, 0.5884, 0.5872, 0.586, 0.597, 0.613, 0.601, 0.544, 0.551, 0.578, 0.567, 0.546, 0.558, 0.544, 0.511, 0.565, 0.519, 0.546, 0.567, 0.545, 0.53, 0.53, 0.542, 0.532, 0.532, 0.533, 0.561, 0.518, 0.532, 0.533, 0.524, 0.55, 0.567, 0.531, 0.553, 0.527, 0.537, 0.53, 0.507, 0.488, 0.485, 0.447, 0.447, 0.425, 0.416, 0.405, 0.388, 0.358, 0.36, 0.275, 0.272, 0.29, 0.196, 0.205, 0.208, 0.172, 0.149, 0.126, 0.109, 0.105, 0.075, 0.069, 0.077, 0.099, 0.069, 0.073, 0.085, 0.069, 0.03, 0.045, 0.052, 0.013, 0.023, 0.009, 0.032, 0.017, 0, 0.011, 0.017, 0, 0.005, 0.011, 0.003, 0.011, 0, 0.013, 0.008, 0, 0.02, 0.015, 0, 0, 0, 0.001, 0], "wavelength": [10000, 10010, 10020, 10030, 10040, 10050, 10060, 10070, 10080, 10090, 10100, 10110, 10120, 10130, 10140, 10150, 10160, 10170, 10180, 10190, 10200, 10210, 10220, 10230, 10240, 10250, 10260, 10270, 10280, 10290, 10300, 10310, 10320, 10330, 10340, 10350, 10360, 10370, 10380, 10390, 10400, 10410, 10420, 10430, 10440, 10450, 10460, 10470, 10480, 10490, 10500, 10510, 10520, 10530, 10540, 10550, 10560, 10570, 10580, 10590, 10600, 10610, 10620, 10630, 10640, 10650, 10660, 10670, 10680, 10690, 10700, 10710, 10720, 10730, 10740, 10750, 10760, 10770, 10780, 10790, 10800, 10810, 10820, 10830, 10840, 10850, 10860, 10870, 10880, 10890, 10900, 10910, 10920, 10930, 10940, 10950, 10960, 10970, 10980, 10990, 11000, 11010, 11020, 11030, 11040, 11050, 11060, 11070, 11080, 11090, 11100, 11110, 11120, 11130, 11140, 11150, 11160, 11170, 11180, 11190, 11200, 11210, 11220, 11230, 11240, 11250, 11260, 11270, 11280, 11290, 11300, 11310, 11320, 11330, 11340, 11350, 11360, 11370, 11380, 11390, 11400, 11410, 11420, 11430, 11440, 11450, 11460, 11470, 11480, 11490, 11500, 11510, 11520, 11530, 11540, 11550, 11560, 11570, 11580, 11590, 11600, 11610, 11620, 11630, 11640, 11650, 11660, 11670, 11680, 11690, 11700, 11710, 11720, 11730, 11740, 11750, 11760, 11770, 11780, 11790, 11800, 11810, 11820, 11830, 11840, 11850, 11860, 11870, 11880, 11890, 11900, 11910, 11920, 11930, 11940, 11950, 11960, 11970, 11980, 11990, 12000, 12010, 12020, 12030, 12040, 12050, 12060, 12070, 12080, 12090, 12100, 12110, 12120, 12130, 12140, 12150, 12160, 12170, 12180, 12190, 12200, 12210, 12220, 12230, 12240, 12250, 12260, 12270, 12280, 12290, 12300, 12310, 12320, 12330, 12340, 12350, 12360, 12370, 12380, 12390, 12400, 12410, 12420, 12430, 12440, 12450, 12460, 12470, 12480, 12490, 12500, 12510, 12520, 12530, 12540, 12540, 12550, 12560, 12570, 12580, 12590, 12600, 12610, 12620, 12630, 12640, 12650, 12660, 12670, 12680, 12690, 12700, 12710, 12720, 12730, 12740, 12750, 12760, 12770, 12780, 12790, 12800, 12810, 12820, 12830, 12840, 12850, 12860, 12870, 12880, 12890, 12900, 12910]}}], "metadata_type": "eo"}	2021-01-31 22:08:40.976982+00	africa	\N
45	ls8_barest_earth_albers	{"format": {"name": "GeoTIFF"}, "platform": {"code": "LANDSAT_8"}, "instrument": {"name": "OLI"}, "product_type": "landsat8_barest_earth_mosaic"}	2	{"name": "ls8_barest_earth_albers", "storage": {"crs": "EPSG:3577", "driver": "GeoTIFF", "tile_size": {"x": 100000.0, "y": 100000.0}, "resolution": {"x": 25, "y": -25}, "dimension_order": ["time", "y", "x"]}, "metadata": {"format": {"name": "GeoTIFF"}, "platform": {"code": "LANDSAT_8"}, "instrument": {"name": "OLI"}, "product_type": "landsat8_barest_earth_mosaic"}, "description": "Landsat-8 Barest Earth pixel composite albers 25 metre, 100km tile, Australian Albers Equal Area projection (EPSG:3577)", "measurements": [{"name": "blue", "dtype": "int16", "units": "1", "nodata": -999}, {"name": "green", "dtype": "int16", "units": "1", "nodata": -999}, {"name": "red", "dtype": "int16", "units": "1", "nodata": -999}, {"name": "nir", "dtype": "int16", "units": "1", "nodata": -999}, {"name": "swir1", "dtype": "int16", "units": "1", "nodata": -999}, {"name": "swir2", "dtype": "int16", "units": "1", "nodata": -999}], "metadata_type": "eo"}	2021-01-31 22:08:42.87706+00	africa	\N
46	ls8_fc_albers	{"format": {"name": "GeoTIFF"}, "platform": {"code": "LANDSAT_8"}, "instrument": {"name": "OLI_TIRS"}, "product_type": "fractional_cover"}	2	{"name": "ls8_fc_albers", "storage": {"crs": "EPSG:3577", "resolution": {"x": 25, "y": -25}, "dimension_order": ["time", "y", "x"]}, "metadata": {"format": {"name": "GeoTIFF"}, "platform": {"code": "LANDSAT_8"}, "instrument": {"name": "OLI_TIRS"}, "product_type": "fractional_cover"}, "description": "Landsat 8 Fractional Cover 25 metre, 100km tile, Australian Albers Equal Area projection (EPSG:3577)", "measurements": [{"name": "BS", "dtype": "int16", "units": "percent", "nodata": -1, "aliases": ["bare"]}, {"name": "PV", "dtype": "int16", "units": "percent", "nodata": -1, "aliases": ["green_veg"]}, {"name": "NPV", "dtype": "int16", "units": "percent", "nodata": -1, "aliases": ["dead_veg"]}, {"name": "UE", "dtype": "int16", "units": "1", "nodata": -1, "aliases": ["err"]}], "metadata_type": "eo"}	2021-01-31 22:08:44.779749+00	africa	\N
47	ls8_level1_usgs	{"format": {"name": "GeoTiff"}, "product_type": "level1"}	2	{"name": "ls8_level1_usgs", "metadata": {"format": {"name": "GeoTiff"}, "product_type": "level1"}, "description": "Landsat 8 USGS Level 1 Collection-1 OLI-TIRS", "measurements": [{"name": "coastal_aerosol", "dtype": "int16", "units": "1", "nodata": -9999, "aliases": ["band_1", "coastal_aerosol"]}, {"name": "blue", "dtype": "int16", "units": "1", "nodata": -9999, "aliases": ["band_2", "blue"]}, {"name": "green", "dtype": "int16", "units": "1", "nodata": -9999, "aliases": ["band_3", "green"]}, {"name": "red", "dtype": "int16", "units": "1", "nodata": -9999, "aliases": ["band_4", "red"]}, {"name": "nir", "dtype": "int16", "units": "1", "nodata": -9999, "aliases": ["band_5", "nir"]}, {"name": "swir1", "dtype": "int16", "units": "1", "nodata": -9999, "aliases": ["band_6", "swir1"]}, {"name": "swir2", "dtype": "int16", "units": "1", "nodata": -9999, "aliases": ["band_7", "swir2"]}, {"name": "panchromatic", "dtype": "int16", "units": "1", "nodata": -9999, "aliases": ["band_8", "panchromatic"]}, {"name": "cirrus", "dtype": "int16", "units": "1", "nodata": -9999, "aliases": ["band_9", "cirrus"]}, {"name": "lwir1", "dtype": "int16", "units": "1", "nodata": -9999, "aliases": ["band_10", "lwir1"]}, {"name": "lwir2", "dtype": "int16", "units": "1", "nodata": -9999, "aliases": ["band_11", "lwir2"]}, {"name": "quality", "dtype": "int16", "units": "1", "nodata": 0, "aliases": ["QUALITY", "quality"], "flags_definition": {"cloud": {"bits": [4], "values": {"0": false, "1": true}, "description": "Cloud"}, "snow_ice_conf": {"bits": [9, 10], "values": {"0": "Not Determined", "1": "Low", "2": "Medium", "3": "High"}, "description": "Snow/Ice Confidence with low =(0-33)%, medium =(34-66)% and high =(67-100)%"}, "designated_fill": {"bits": [0], "values": {"0": false, "1": true}, "description": "Used to identify fill values"}, "cloud_confidence": {"bits": [5, 6], "values": {"0": "Not Determined", "1": "Low", "2": "Medium", "3": "High"}, "description": "Cloud Confidence with low =(0-33)%, medium =(34-66)% and high =(67-100)%"}, "cirrus_confidence": {"bits": [11, 12], "values": {"0": "Not Determined", "1": "Low", "2": "Medium", "3": "High"}, "description": "Cirrus Confidence with low =(0-33)%, medium =(34-66)% and high =(67-100)%"}, "cloud_shadow_conf": {"bits": [7, 8], "values": {"0": "Not Determined", "1": "Low", "2": "Medium", "3": "High"}, "description": "Cloud Shadow Confidence with low =(0-33)%, medium =(34-66)% and high =(67-100)%"}, "terrain_occlusion": {"bits": [1], "values": {"0": false, "1": true}, "description": "Terrain Occlusion"}, "radiometric_saturation": {"bits": [2, 3], "values": {"0": "none", "1": "1-2", "2": "3-4", "3": "<=5"}, "description": "Radiometric saturation bits, represents how many bands contains saturation"}}}], "metadata_type": "eo"}	2021-01-31 22:08:46.668505+00	africa	\N
48	ls8_usgs_l2c1	{"format": {"name": "GeoTiff"}, "platform": {"code": "LANDSAT_8"}, "instrument": {"name": "OLI_TIRS"}, "product_type": "LS_USGS_L2C1"}	2	{"name": "ls8_usgs_l2c1", "metadata": {"format": {"name": "GeoTiff"}, "platform": {"code": "LANDSAT_8"}, "instrument": {"name": "OLI_TIRS"}, "product_type": "LS_USGS_L2C1"}, "description": "Landsat 8 Operational Land Imager (OLI) and Thermal Infrared Sensor (TIRS) USGS Analysis Ready Data 30m scene", "measurements": [{"name": "sr_aerosol", "dtype": "int16", "units": "1", "nodata": -9999, "aliases": ["aerosol"]}, {"name": "coastal_aerosol", "dtype": "int16", "units": "1", "nodata": -9999, "aliases": ["band_1", "sr_band1"], "spectral_definition": {"response": [0.000073, 0.000609, 0.001628, 0.003421, 0.008019, 0.024767, 0.085688, 0.254149, 0.517821, 0.765117, 0.908749, 0.958204, 0.977393, 0.98379, 0.989052, 0.986713, 0.993683, 0.993137, 1.0, 0.996969, 0.98278, 0.972692, 0.905808, 0.745606, 0.471329, 0.226412, 0.09286, 0.036603, 0.014537, 0.005829, 0.002414, 0.000984, 0.000255], "wavelength": [427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459]}}, {"name": "blue", "dtype": "int16", "units": "1", "nodata": -9999, "aliases": ["band_2", "sr_band2"], "spectral_definition": {"response": [0.00001, 0.000061, 0.000117, 0.000241, 0.000349, 0.000455, 0.000756, 0.001197, 0.00207, 0.003712, 0.006869, 0.013212, 0.02717, 0.058606, 0.130876, 0.27137, 0.493542, 0.723971, 0.85751, 0.894222, 0.903034, 0.910928, 0.90988, 0.899475, 0.897977, 0.889667, 0.883542, 0.877453, 0.881011, 0.874721, 0.879688, 0.886569, 0.891913, 0.88768, 0.861157, 0.848533, 0.840828, 0.828339, 0.844202, 0.865864, 0.868497, 0.890253, 0.912538, 0.910385, 0.918822, 0.931726, 0.931813, 0.954248, 0.955545, 0.96242, 0.956424, 0.953352, 0.978564, 0.989104, 0.985615, 0.989469, 0.982262, 0.968801, 0.967332, 0.976836, 0.988729, 0.980826, 0.967361, 0.954754, 0.964132, 0.966125, 0.966772, 0.981834, 0.98232, 0.965685, 0.963135, 0.972261, 0.996498, 1.0, 0.9556, 0.844893, 0.534592, 0.190738, 0.048329, 0.013894, 0.005328, 0.002611, 0.001557, 0.0011, 0.000785, 0.000516, 0.000321, 0.000162, 0.000072, 0.000057, 0.000023, 0.000032, -0.000016], "wavelength": [436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528]}}, {"name": "green", "dtype": "int16", "units": "1", "nodata": -9999, "aliases": ["band_3", "sr_band3"], "spectral_definition": {"response": [-0.000046, 0.000016, 0.00011, 0.000247, 0.000362, 0.000648, 0.000935, 0.001332, 0.001816, 0.002515, 0.003446, 0.00488, 0.007024, 0.010441, 0.016247, 0.025513, 0.041451, 0.070551, 0.123444, 0.21168, 0.353885, 0.545856, 0.741205, 0.865225, 0.927396, 0.954627, 0.954163, 0.959215, 0.961328, 0.964902, 0.969873, 0.952489, 0.961397, 0.97827, 0.977533, 0.977001, 0.980884, 0.990784, 1.0, 0.992264, 0.982642, 0.983832, 0.977765, 0.965081, 0.957314, 0.946245, 0.947871, 0.959038, 0.966534, 0.977656, 0.966447, 0.953399, 0.958314, 0.970039, 0.978607, 0.983397, 0.98096, 0.974522, 0.967229, 0.979406, 0.978208, 0.975818, 0.974392, 0.979973, 0.968827, 0.969181, 0.967838, 0.982956, 0.979598, 0.963811, 0.968886, 0.983655, 0.986657, 0.974207, 0.946407, 0.904478, 0.809275, 0.684974, 0.525304, 0.345364, 0.190467, 0.087833, 0.035393, 0.014077, 0.005944, 0.002574, 0.001046, 0.000394, 0.000085, -0.000084, -0.000194, -0.000234, -0.000292, -0.000307, -0.000343, -0.000348, -0.000329, -0.000351, -0.000317], "wavelength": [512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610]}}, {"name": "red", "dtype": "int16", "units": "1", "nodata": -9999, "aliases": ["band_4", "sr_band4"], "spectral_definition": {"response": [-0.000342, 0.00027, 0.000895, 0.00185, 0.003648, 0.007197, 0.014515, 0.030432, 0.066861, 0.148518, 0.299778, 0.526812, 0.764443, 0.905473, 0.947949, 0.950823, 0.947418, 0.951831, 0.962705, 0.975075, 0.984173, 0.983613, 0.983434, 0.982911, 0.973636, 0.959441, 0.955641, 0.955548, 0.953337, 0.956628, 0.981688, 1.0, 0.992388, 0.984615, 0.981568, 0.97696, 0.97298, 0.98108, 0.996804, 0.992142, 0.980678, 0.964002, 0.962154, 0.970778, 0.96718, 0.966928, 0.949928, 0.848855, 0.609359, 0.31635, 0.123946, 0.046033, 0.017702, 0.007333, 0.003205, 0.001402, 0.000554, 0.000117, -0.000122, -0.000289, -0.000376, -0.000396, -0.000458, -0.000488, -0.000457, -0.000429, -0.000417], "wavelength": [625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 683, 684, 685, 686, 687, 688, 689, 690, 691]}}, {"name": "nir", "dtype": "int16", "units": "1", "nodata": -9999, "aliases": ["band_5", "sr_band5"], "spectral_definition": {"response": [-0.000034, 0.000011, 0.00005, 0.0001, 0.000239, 0.000314, 0.000495, 0.000719, 0.000986, 0.001445, 0.002107, 0.00316, 0.004744, 0.007059, 0.0109, 0.017346, 0.028332, 0.048191, 0.084363, 0.145365, 0.249733, 0.403526, 0.582623, 0.745037, 0.890315, 0.960215, 0.986833, 0.973133, 0.980606, 0.99612, 1.0, 0.989777, 0.980733, 0.975935, 0.972043, 0.957357, 0.951209, 0.947044, 0.953162, 0.951499, 0.94845, 0.940094, 0.950632, 0.956079, 0.96646, 0.969821, 0.93661, 0.891066, 0.788733, 0.63532, 0.448364, 0.288847, 0.174619, 0.100343, 0.058265, 0.034532, 0.02072, 0.01244, 0.007601, 0.004702, 0.002944, 0.00187, 0.001192, 0.000743, 0.000423, 0.000241, 0.000116, 0.000044, -0.000013, -0.00005, -0.000084, -0.0001], "wavelength": [829, 830, 831, 832, 833, 834, 835, 836, 837, 838, 839, 840, 841, 842, 843, 844, 845, 846, 847, 848, 849, 850, 851, 852, 853, 854, 855, 856, 857, 858, 859, 860, 861, 862, 863, 864, 865, 866, 867, 868, 869, 870, 871, 872, 873, 874, 875, 876, 877, 878, 879, 880, 881, 882, 883, 884, 885, 886, 887, 888, 889, 890, 891, 892, 893, 894, 895, 896, 897, 898, 899, 900]}}, {"name": "swir1", "dtype": "int16", "units": "1", "nodata": -9999, "aliases": ["band_6", "sr_band6"], "spectral_definition": {"response": [-0.000016, 0.000067, 0.000151, 0.000249, 0.000348, 0.000466, 0.000585, 0.000758, 0.000932, 0.00115, 0.001369, 0.001613, 0.001859, 0.002172, 0.002488, 0.002881, 0.003277, 0.003772, 0.004271, 0.004898, 0.005528, 0.006421, 0.007319, 0.008459, 0.009606, 0.010989, 0.012372, 0.014303, 0.016248, 0.019029, 0.021831, 0.02589, 0.029952, 0.035171, 0.040434, 0.047864, 0.055352, 0.065732, 0.076166, 0.089024, 0.101893, 0.12015, 0.138642, 0.163127, 0.187803, 0.220261, 0.252894, 0.291359, 0.329939, 0.375648, 0.42147, 0.47356, 0.525681, 0.578787, 0.631645, 0.676683, 0.721282, 0.75477, 0.788248, 0.821155, 0.854065, 0.87337, 0.89183, 0.899817, 0.907252, 0.913009, 0.918685, 0.922953, 0.927163, 0.92686, 0.926413, 0.925059, 0.923683, 0.923953, 0.924259, 0.922828, 0.921383, 0.922061, 0.922756, 0.924648, 0.926605, 0.934552, 0.942525, 0.944351, 0.945872, 0.946175, 0.946432, 0.947006, 0.947589, 0.950194, 0.952859, 0.951303, 0.94967, 0.953047, 0.956494, 0.959047, 0.961545, 0.960048, 0.958335, 0.959835, 0.96147, 0.960857, 0.960175, 0.960813, 0.961486, 0.964703, 0.967943, 0.969314, 0.970589, 0.973713, 0.976906, 0.9791, 0.981258, 0.981285, 0.981372, 0.988609, 0.995869, 0.998021, 1.0, 0.999848, 0.999642, 0.99659, 0.993439, 0.986217, 0.978989, 0.967125, 0.95512, 0.936199, 0.917239, 0.879424, 0.840967, 0.796545, 0.751893, 0.694313, 0.636542, 0.573232, 0.509946, 0.451966, 0.39403, 0.34275, 0.291752, 0.251309, 0.211153, 0.180823, 0.15054, 0.128463, 0.106664, 0.090735, 0.074941, 0.06379, 0.052752, 0.045028, 0.03731, 0.031821, 0.02635, 0.022504, 0.018724, 0.016045, 0.013394, 0.011483, 0.009587, 0.008227, 0.006882, 0.00591, 0.00494, 0.004257, 0.003576, 0.003055, 0.002541, 0.00216, 0.001781, 0.001512, 0.001244, 0.00104, 0.000837, 0.000677, 0.000517, 0.000409, 0.000301, 0.000206, 0.000112, 0.00004, -0.000031], "wavelength": [1515, 1516, 1517, 1518, 1519, 1520, 1521, 1522, 1523, 1524, 1525, 1526, 1527, 1528, 1529, 1530, 1531, 1532, 1533, 1534, 1535, 1536, 1537, 1538, 1539, 1540, 1541, 1542, 1543, 1544, 1545, 1546, 1547, 1548, 1549, 1550, 1551, 1552, 1553, 1554, 1555, 1556, 1557, 1558, 1559, 1560, 1561, 1562, 1563, 1564, 1565, 1566, 1567, 1568, 1569, 1570, 1571, 1572, 1573, 1574, 1575, 1576, 1577, 1578, 1579, 1580, 1581, 1582, 1583, 1584, 1585, 1586, 1587, 1588, 1589, 1590, 1591, 1592, 1593, 1594, 1595, 1596, 1597, 1598, 1599, 1600, 1601, 1602, 1603, 1604, 1605, 1606, 1607, 1608, 1609, 1610, 1611, 1612, 1613, 1614, 1615, 1616, 1617, 1618, 1619, 1620, 1621, 1622, 1623, 1624, 1625, 1626, 1627, 1628, 1629, 1630, 1631, 1632, 1633, 1634, 1635, 1636, 1637, 1638, 1639, 1640, 1641, 1642, 1643, 1644, 1645, 1646, 1647, 1648, 1649, 1650, 1651, 1652, 1653, 1654, 1655, 1656, 1657, 1658, 1659, 1660, 1661, 1662, 1663, 1664, 1665, 1666, 1667, 1668, 1669, 1670, 1671, 1672, 1673, 1674, 1675, 1676, 1677, 1678, 1679, 1680, 1681, 1682, 1683, 1684, 1685, 1686, 1687, 1688, 1689, 1690, 1691, 1692, 1693, 1694, 1695, 1696, 1697]}}, {"name": "swir2", "dtype": "int16", "units": "1", "nodata": -9999, "aliases": ["band_7", "sr_band7"], "spectral_definition": {"response": [-0.00001, 0.000037, 0.000083, 0.000131, 0.000179, 0.00024, 0.000305, 0.000368, 0.00043, 0.000512, 0.000599, 0.000704, 0.000814, 0.000947, 0.001085, 0.001222, 0.00136, 0.001546, 0.001745, 0.001964, 0.002187, 0.002439, 0.002696, 0.00301, 0.003339, 0.003733, 0.004141, 0.004627, 0.005137, 0.005728, 0.006337, 0.007139, 0.007996, 0.008903, 0.009824, 0.011005, 0.012261, 0.01361, 0.014987, 0.016872, 0.018899, 0.021, 0.023121, 0.025897, 0.028847, 0.032071, 0.035363, 0.040206, 0.045432, 0.050903, 0.056429, 0.06327, 0.070409, 0.079382, 0.088907, 0.10064, 0.11283, 0.128292, 0.144668, 0.162055, 0.179714, 0.20278, 0.227234, 0.253732, 0.280925, 0.311347, 0.342526, 0.377044, 0.412621, 0.45047, 0.488816, 0.522458, 0.554715, 0.593227, 0.633521, 0.663067, 0.689664, 0.722284, 0.756529, 0.776463, 0.792667, 0.813716, 0.836001, 0.846344, 0.853714, 0.867845, 0.883615, 0.886411, 0.886127, 0.895232, 0.906527, 0.909739, 0.911091, 0.917985, 0.926131, 0.929693, 0.932227, 0.936544, 0.941406, 0.942571, 0.942952, 0.943112, 0.943194, 0.945168, 0.947537, 0.948776, 0.949694, 0.949643, 0.9494, 0.952551, 0.956635, 0.953083, 0.947423, 0.949094, 0.952773, 0.950874, 0.947477, 0.947014, 0.947085, 0.951812, 0.957717, 0.953332, 0.946412, 0.947778, 0.951119, 0.951641, 0.951518, 0.948644, 0.944956, 0.942515, 0.940311, 0.9434, 0.947923, 0.94501, 0.940213, 0.938737, 0.93806, 0.941859, 0.947019, 0.946554, 0.944482, 0.947414, 0.951661, 0.949283, 0.945318, 0.939939, 0.934142, 0.935493, 0.93882, 0.939253, 0.938955, 0.934675, 0.929162, 0.927085, 0.925692, 0.930508, 0.936899, 0.933908, 0.927984, 0.930981, 0.936472, 0.935776, 0.933523, 0.935132, 0.937592, 0.946217, 0.956567, 0.955661, 0.951991, 0.956666, 0.963135, 0.964442, 0.964365, 0.963523, 0.962434, 0.962905, 0.963685, 0.962473, 0.960741, 0.959239, 0.957814, 0.957781, 0.958041, 0.953274, 0.94716, 0.951706, 0.958833, 0.960212, 0.960339, 0.954785, 0.947696, 0.951965, 0.95906, 0.960554, 0.960764, 0.95575, 0.949261, 0.953245, 0.95997, 0.963736, 0.966786, 0.964315, 0.960173, 0.965473, 0.973416, 0.977637, 0.980904, 0.98276, 0.984155, 0.984693, 0.985056, 0.991486, 0.9996, 0.997654, 0.993153, 0.992469, 0.992675, 0.995894, 1.0, 0.999279, 0.997261, 0.994356, 0.991127, 0.987747, 0.984349, 0.986037, 0.989132, 0.984536, 0.978024, 0.975019, 0.972794, 0.974168, 0.97654, 0.976199, 0.975206, 0.974409, 0.973662, 0.967502, 0.959895, 0.956943, 0.955095, 0.955085, 0.955588, 0.947195, 0.93665, 0.922405, 0.907109, 0.89494, 0.883588, 0.855489, 0.823876, 0.78488, 0.744025, 0.69852, 0.651673, 0.602539, 0.552647, 0.502693, 0.452698, 0.403993, 0.355569, 0.315712, 0.27826, 0.244645, 0.212213, 0.186151, 0.161749, 0.141435, 0.122015, 0.106531, 0.092029, 0.080268, 0.069276, 0.060703, 0.052702, 0.046332, 0.040405, 0.035634, 0.031213, 0.027516, 0.024, 0.021262, 0.018688, 0.016562, 0.014545, 0.01293, 0.011426, 0.010155, 0.008959, 0.007992, 0.007088, 0.006348, 0.005643, 0.005019, 0.004415, 0.003903, 0.003421, 0.003025, 0.002651, 0.00234, 0.002047, 0.001795, 0.001554, 0.001345, 0.001145, 0.000974, 0.000811, 0.00068, 0.00056, 0.00044, 0.00032, 0.000217, 0.000119, 0.000028, -0.000062, -0.000134, -0.000202, -0.000263, -0.000322], "wavelength": [2037, 2038, 2039, 2040, 2041, 2042, 2043, 2044, 2045, 2046, 2047, 2048, 2049, 2050, 2051, 2052, 2053, 2054, 2055, 2056, 2057, 2058, 2059, 2060, 2061, 2062, 2063, 2064, 2065, 2066, 2067, 2068, 2069, 2070, 2071, 2072, 2073, 2074, 2075, 2076, 2077, 2078, 2079, 2080, 2081, 2082, 2083, 2084, 2085, 2086, 2087, 2088, 2089, 2090, 2091, 2092, 2093, 2094, 2095, 2096, 2097, 2098, 2099, 2100, 2101, 2102, 2103, 2104, 2105, 2106, 2107, 2108, 2109, 2110, 2111, 2112, 2113, 2114, 2115, 2116, 2117, 2118, 2119, 2120, 2121, 2122, 2123, 2124, 2125, 2126, 2127, 2128, 2129, 2130, 2131, 2132, 2133, 2134, 2135, 2136, 2137, 2138, 2139, 2140, 2141, 2142, 2143, 2144, 2145, 2146, 2147, 2148, 2149, 2150, 2151, 2152, 2153, 2154, 2155, 2156, 2157, 2158, 2159, 2160, 2161, 2162, 2163, 2164, 2165, 2166, 2167, 2168, 2169, 2170, 2171, 2172, 2173, 2174, 2175, 2176, 2177, 2178, 2179, 2180, 2181, 2182, 2183, 2184, 2185, 2186, 2187, 2188, 2189, 2190, 2191, 2192, 2193, 2194, 2195, 2196, 2197, 2198, 2199, 2200, 2201, 2202, 2203, 2204, 2205, 2206, 2207, 2208, 2209, 2210, 2211, 2212, 2213, 2214, 2215, 2216, 2217, 2218, 2219, 2220, 2221, 2222, 2223, 2224, 2225, 2226, 2227, 2228, 2229, 2230, 2231, 2232, 2233, 2234, 2235, 2236, 2237, 2238, 2239, 2240, 2241, 2242, 2243, 2244, 2245, 2246, 2247, 2248, 2249, 2250, 2251, 2252, 2253, 2254, 2255, 2256, 2257, 2258, 2259, 2260, 2261, 2262, 2263, 2264, 2265, 2266, 2267, 2268, 2269, 2270, 2271, 2272, 2273, 2274, 2275, 2276, 2277, 2278, 2279, 2280, 2281, 2282, 2283, 2284, 2285, 2286, 2287, 2288, 2289, 2290, 2291, 2292, 2293, 2294, 2295, 2296, 2297, 2298, 2299, 2300, 2301, 2302, 2303, 2304, 2305, 2306, 2307, 2308, 2309, 2310, 2311, 2312, 2313, 2314, 2315, 2316, 2317, 2318, 2319, 2320, 2321, 2322, 2323, 2324, 2325, 2326, 2327, 2328, 2329, 2330, 2331, 2332, 2333, 2334, 2335, 2336, 2337, 2338, 2339, 2340, 2341, 2342, 2343, 2344, 2345, 2346, 2347, 2348, 2349, 2350, 2351, 2352, 2353, 2354, 2355]}}, {"name": "quality", "dtype": "uint8", "units": "1", "nodata": 255, "aliases": ["pixel_qa"], "flags_definition": {"pixelqa": {"bits": [0, 1, 2, 3, 4, 5, 6, 7], "values": {"0": "fill", "1": "clear", "2": "water", "3": "cloud shadow", "4": "snow", "5": "cloud", "6": "cloud confidence", "7": "cloud confidence", "8": "cirrus confidence", "9": "cirrus confidence", "10": "terrain occlusion", "11": "unused", "12": "unused", "13": "unused", "14": "unused", "15": "unused"}, "description": "PixelQA"}}}, {"name": "radsat_qa", "dtype": "uint8", "units": "1", "nodata": 255, "aliases": ["radasat"], "flags_definition": {"radsatqa": {"bits": [0, 1, 2, 3, 4, 5, 6, 7], "values": {"0": "Data Fill Flag (0 = valid data, 1 = invalid data)", "1": "Band 1 Data Saturation Flag (0 = valid data, 1 = saturated data)", "2": "Band 2 Data Saturation Flag (0 = valid data, 1 = saturated data)", "3": "Band 3 Data Saturation Flag (0 = valid data, 1 = saturated data)", "4": "Band 4 Data Saturation Flag (0 = valid data, 1 = saturated data)", "5": "Band 5 Data Saturation Flag (0 = valid data, 1 = saturated data)", "6": "Band 6 Data Saturation Flag (0 = valid data, 1 = saturated data)", "7": "Band 7 Data Saturation Flag (0 = valid data, 1 = saturated data)"}, "description": "saturation mask"}}}, {"name": "lwir1", "dtype": "int16", "units": "1", "nodata": -9999, "aliases": ["bt_band10"], "spectral_definition": {"response": [0.00076333, 0.00076341, 0.00076348, 0.00076356, 0.00076363, 0.00076371, 0.00075856, 0.00075341, 0.00074827, 0.00074312, 0.00073797, 0.00075017, 0.00076237, 0.00077456, 0.00078676, 0.00079895, 0.00081567, 0.00083239, 0.00084911, 0.00086583, 0.00088255, 0.00085741, 0.00083227, 0.00080713, 0.00078199, 0.00075685, 0.00074273, 0.00072862, 0.00071451, 0.0007004, 0.00068629, 0.00069495, 0.00070362, 0.00071229, 0.00072096, 0.00072963, 0.000737, 0.00074437, 0.00075174, 0.00075911, 0.00076648, 0.00077394, 0.00078141, 0.00078887, 0.00079633, 0.0008038, 0.00079284, 0.00078188, 0.00077092, 0.00075997, 0.00074901, 0.00076924, 0.00078947, 0.00080971, 0.00082994, 0.00085017, 0.00080123, 0.00075228, 0.00070334, 0.00065439, 0.00060545, 0.00063631, 0.00066718, 0.00069804, 0.00072891, 0.00075977, 0.0007515, 0.00074323, 0.00073496, 0.00072668, 0.00071841, 0.00067944, 0.00064046, 0.00060148, 0.00056251, 0.00052353, 0.00057207, 0.00062062, 0.00066916, 0.0007177, 0.00076625, 0.0007198, 0.00067336, 0.00062691, 0.00058046, 0.00053402, 0.00061341, 0.0006928, 0.00077218, 0.00085157, 0.00093096, 0.00087899, 0.00082702, 0.00077505, 0.00072308, 0.0006711, 0.00066875, 0.0006664, 0.00066405, 0.00066169, 0.00065934, 0.0006856, 0.00071187, 0.00073813, 0.0007644, 0.00079066, 0.00078055, 0.00077043, 0.00076031, 0.00075019, 0.00074008, 0.00071988, 0.00069967, 0.00067947, 0.00065927, 0.00063907, 0.00091845, 0.00119783, 0.00147721, 0.00175659, 0.00203597, 0.00242901, 0.00282206, 0.0032151, 0.00360814, 0.00400118, 0.0047606, 0.00552003, 0.00627945, 0.00703887, 0.00779829, 0.0094834, 0.01116851, 0.01285362, 0.01453873, 0.01622384, 0.0193706, 0.02251737, 0.02566413, 0.0288109, 0.03195766, 0.03878213, 0.04560659, 0.05243106, 0.05925552, 0.06607999, 0.08054304, 0.09500609, 0.10946914, 0.1239322, 0.13839525, 0.16639759, 0.19439994, 0.22240229, 0.25040464, 0.27840698, 0.32385807, 0.36930915, 0.41476023, 0.46021132, 0.5056624, 0.54970276, 0.59374312, 0.63778348, 0.68182384, 0.7258642, 0.74239389, 0.75892357, 0.77545326, 0.79198295, 0.80851264, 0.81502619, 0.82153975, 0.8280533, 0.83456686, 0.84108041, 0.84153405, 0.84198768, 0.84244132, 0.84289496, 0.84334859, 0.84936559, 0.85538259, 0.86139959, 0.86741659, 0.87343359, 0.88183542, 0.89023726, 0.8986391, 0.90704094, 0.91544277, 0.92796, 0.94047723, 0.95299445, 0.96551168, 0.97802891, 0.98242313, 0.98681734, 0.99121156, 0.99560578, 1.0, 0.99817758, 0.99635516, 0.99453274, 0.99271032, 0.9908879, 0.96701999, 0.94315209, 0.91928418, 0.89541628, 0.87154837, 0.82791686, 0.78428534, 0.74065383, 0.69702231, 0.6533908, 0.60464088, 0.55589096, 0.50714104, 0.45839113, 0.40964121, 0.37597665, 0.34231209, 0.30864753, 0.27498297, 0.24131841, 0.22023909, 0.19915977, 0.17808044, 0.15700112, 0.1359218, 0.1229886, 0.11005539, 0.09712219, 0.08418899, 0.07125578, 0.06361179, 0.0559678, 0.04832381, 0.04067981, 0.03303582, 0.02909353, 0.02515123, 0.02120894, 0.01726665, 0.01332436, 0.0116181, 0.00991184, 0.00820559, 0.00649933, 0.00479307, 0.00428195, 0.00377082, 0.0032597, 0.00274857, 0.00223745, 0.00203186, 0.00182628, 0.0016207, 0.00141512, 0.00120954, 0.0011241, 0.00103867, 0.00095323, 0.0008678, 0.00078237, 0.00084064, 0.00089891, 0.00095718, 0.00101545, 0.00107372, 0.00109337, 0.00111302, 0.00113267, 0.00115231, 0.00117196, 0.00116136, 0.00115076, 0.00114016, 0.00112956, 0.00111896, 0.0010925, 0.00106605, 0.00103959, 0.00101313, 0.00098667, 0.0009396, 0.00089253, 0.00084547, 0.0007984, 0.00075133, 0.00060106, 0.0004508, 0.00030053, 0.00015027, 0.0, 0.00024108, 0.00048216, 0.00072324, 0.00096432, 0.0012054, 0.00119834, 0.00119128, 0.00118422, 0.00117716, 0.0011701, 0.00109879, 0.00102749, 0.00095618, 0.00088487, 0.00081357, 0.0007715, 0.00072944, 0.00068737, 0.0006453, 0.00060324, 0.00068642, 0.00076961, 0.0008528, 0.00093598, 0.00101917, 0.00097432, 0.00092947, 0.00088462, 0.00083977, 0.00079492, 0.00076786, 0.00074079, 0.00071372, 0.00068666, 0.00065959, 0.00059126, 0.00052294, 0.00045461, 0.00038629, 0.00031796, 0.00050929, 0.00070062, 0.00089195, 0.00108328, 0.00127461, 0.00121607, 0.00115754, 0.001099, 0.00104047, 0.00098193, 0.00099448, 0.00100703, 0.00101959, 0.00103214, 0.00104469, 0.00097149, 0.0008983, 0.0008251, 0.00075191, 0.00067871, 0.00070985, 0.00074099, 0.00077213, 0.00080326, 0.0008344, 0.00069102, 0.00054763, 0.00040425, 0.00026086, 0.00011748, 0.00016083, 0.00020418, 0.00024753, 0.00029088, 0.00033423, 0.00037672, 0.00041922, 0.00046172, 0.00050421, 0.00054671, 0.00056416, 0.00058162, 0.00059907, 0.00061652, 0.00063398, 0.0006166, 0.00059922, 0.00058184, 0.00056446, 0.00054708, 0.00057041, 0.00059375, 0.00061708, 0.00064041, 0.00066374, 0.00066251, 0.00066128, 0.00066005, 0.00065883, 0.0006576, 0.00070262, 0.00074764, 0.00079266, 0.00083768, 0.00088271, 0.00084151, 0.0008003, 0.0007591, 0.0007179, 0.0006767, 0.0007344, 0.0007921, 0.0008498, 0.0009075, 0.0009652, 0.0009463, 0.0009274, 0.0009085, 0.0008896, 0.00087071, 0.00086477, 0.00085884, 0.00085291, 0.00084697, 0.00084104, 0.00085026, 0.00085948, 0.00086869, 0.00087791, 0.00088713, 0.00089629, 0.00090545, 0.00091461, 0.00092377, 0.00093293, 0.00093607, 0.0009392, 0.00094234, 0.00094548, 0.00094862, 0.00094262, 0.00093663, 0.00093063, 0.00092463, 0.00091864, 0.00088311, 0.00084758, 0.00081205, 0.00077651, 0.00074098, 0.00074078, 0.00074058, 0.00074037, 0.00074017, 0.00073997, 0.00075149, 0.00076301, 0.00077454, 0.00078606, 0.00079759, 0.00079531, 0.00079303, 0.00079076, 0.00078848, 0.00078621, 0.00078908, 0.00079195, 0.00079482, 0.00079769, 0.00080056, 0.00080445, 0.00080834, 0.00081223, 0.00081613, 0.00082002, 0.00081863, 0.00081725, 0.00081587, 0.00081449, 0.0008131, 0.00080953, 0.00080596, 0.00080239, 0.00079882, 0.00079525, 0.00079941, 0.00080358, 0.00080774, 0.00081191, 0.00081607, 0.00080946, 0.00080285, 0.00079624, 0.00078963, 0.00078302, 0.00078596, 0.00078889, 0.00079182, 0.00079476, 0.00079769, 0.00079524, 0.00079279, 0.00079035, 0.0007879, 0.00078545], "wavelength": [9000, 9010, 9020, 9030, 9040, 9050, 9060, 9070, 9080, 9090, 9100, 9110, 9120, 9130, 9140, 9150, 9160, 9170, 9180, 9190, 9200, 9210, 9220, 9230, 9240, 9250, 9260, 9270, 9280, 9290, 9300, 9310, 9320, 9330, 9340, 9350, 9360, 9370, 9380, 9390, 9400, 9410, 9420, 9430, 9440, 9450, 9460, 9470, 9480, 9490, 9500, 9510, 9520, 9530, 9540, 9550, 9560, 9570, 9580, 9590, 9600, 9610, 9620, 9630, 9640, 9650, 9660, 9670, 9680, 9690, 9700, 9710, 9720, 9730, 9740, 9750, 9760, 9770, 9780, 9790, 9800, 9810, 9820, 9830, 9840, 9850, 9860, 9870, 9880, 9890, 9900, 9910, 9920, 9930, 9940, 9950, 9960, 9970, 9980, 9990, 10000, 10010, 10020, 10030, 10040, 10050, 10060, 10070, 10080, 10090, 10100, 10110, 10120, 10130, 10140, 10150, 10160, 10170, 10180, 10190, 10200, 10210, 10220, 10230, 10240, 10250, 10260, 10270, 10280, 10290, 10300, 10310, 10320, 10330, 10340, 10350, 10360, 10370, 10380, 10390, 10400, 10410, 10420, 10430, 10440, 10450, 10460, 10470, 10480, 10490, 10500, 10510, 10520, 10530, 10540, 10550, 10560, 10570, 10580, 10590, 10600, 10610, 10620, 10630, 10640, 10650, 10660, 10670, 10680, 10690, 10700, 10710, 10720, 10730, 10740, 10750, 10760, 10770, 10780, 10790, 10800, 10810, 10820, 10830, 10840, 10850, 10860, 10870, 10880, 10890, 10900, 10910, 10920, 10930, 10940, 10950, 10960, 10970, 10980, 10990, 11000, 11010, 11020, 11030, 11040, 11050, 11060, 11070, 11080, 11090, 11100, 11110, 11120, 11130, 11140, 11150, 11160, 11170, 11180, 11190, 11200, 11210, 11220, 11230, 11240, 11250, 11260, 11270, 11280, 11290, 11300, 11310, 11320, 11330, 11340, 11350, 11360, 11370, 11380, 11390, 11400, 11410, 11420, 11430, 11440, 11450, 11460, 11470, 11480, 11490, 11500, 11510, 11520, 11530, 11540, 11550, 11560, 11570, 11580, 11590, 11600, 11610, 11620, 11630, 11640, 11650, 11660, 11670, 11680, 11690, 11700, 11710, 11720, 11730, 11740, 11750, 11760, 11770, 11780, 11790, 11800, 11810, 11820, 11830, 11840, 11850, 11860, 11870, 11880, 11890, 11900, 11910, 11920, 11930, 11940, 11950, 11960, 11970, 11980, 11990, 12000, 12010, 12020, 12030, 12040, 12050, 12060, 12070, 12080, 12090, 12100, 12110, 12120, 12130, 12140, 12150, 12160, 12170, 12180, 12190, 12200, 12210, 12220, 12230, 12240, 12250, 12260, 12270, 12280, 12290, 12300, 12310, 12320, 12330, 12340, 12350, 12360, 12370, 12380, 12390, 12400, 12410, 12420, 12430, 12440, 12450, 12460, 12470, 12480, 12490, 12500, 12510, 12520, 12530, 12540, 12550, 12560, 12570, 12580, 12590, 12600, 12610, 12620, 12630, 12640, 12650, 12660, 12670, 12680, 12690, 12700, 12710, 12720, 12730, 12740, 12750, 12760, 12770, 12780, 12790, 12800, 12810, 12820, 12830, 12840, 12850, 12860, 12870, 12880, 12890, 12900, 12910, 12920, 12930, 12940, 12950, 12960, 12970, 12980, 12990, 13000, 13010, 13020, 13030, 13040, 13050, 13060, 13070, 13080, 13090, 13100, 13110, 13120, 13130, 13140, 13150, 13160, 13170, 13180, 13190, 13200, 13210, 13220, 13230, 13240, 13250, 13260, 13270, 13280, 13290, 13300, 13310, 13320, 13330, 13340, 13350, 13360, 13370, 13380, 13390, 13400, 13410, 13420, 13430, 13440, 13450, 13460, 13470, 13480, 13490, 13500, 13510, 13520, 13530, 13540, 13550, 13560, 13570, 13580, 13590, 13600, 13610, 13620, 13630, 13640, 13650, 13660, 13670, 13680, 13690, 13700, 13710, 13720, 13730, 13740, 13750, 13760, 13770, 13780, 13790, 13800, 13810, 13820, 13830, 13840, 13850, 13860, 13870, 13880, 13890, 13900, 13910, 13920, 13930, 13940, 13950, 13960, 13970, 13980, 13990, 14000]}}, {"name": "lwir2", "dtype": "int16", "units": "1", "nodata": -9999, "aliases": ["bt_band11"], "spectral_definition": {"response": [0.00147111, 0.00147208, 0.00147305, 0.00147402, 0.00147499, 0.00147596, 0.00153114, 0.00158632, 0.00164151, 0.00169669, 0.00175187, 0.00175554, 0.0017592, 0.00176287, 0.00176653, 0.0017702, 0.00178418, 0.00179817, 0.00181216, 0.00182615, 0.00184014, 0.00182643, 0.00181273, 0.00179902, 0.00178532, 0.00177161, 0.00180017, 0.00182873, 0.00185728, 0.00188584, 0.00191439, 0.00195655, 0.00199871, 0.00204088, 0.00208304, 0.0021252, 0.00203775, 0.0019503, 0.00186285, 0.0017754, 0.00168795, 0.00171634, 0.00174472, 0.00177311, 0.00180149, 0.00182988, 0.00188768, 0.00194548, 0.00200328, 0.00206109, 0.00211889, 0.00219018, 0.00226147, 0.00233276, 0.00240405, 0.00247534, 0.00244098, 0.00240663, 0.00237228, 0.00233793, 0.00230358, 0.00224542, 0.00218726, 0.00212911, 0.00207095, 0.0020128, 0.00200625, 0.00199971, 0.00199316, 0.00198662, 0.00198007, 0.00201261, 0.00204514, 0.00207768, 0.00211021, 0.00214275, 0.0020989, 0.00205506, 0.00201122, 0.00196737, 0.00192353, 0.00202407, 0.00212461, 0.00222515, 0.0023257, 0.00242624, 0.0023444, 0.00226256, 0.00218072, 0.00209888, 0.00201705, 0.00202602, 0.00203499, 0.00204396, 0.00205293, 0.0020619, 0.00194168, 0.00182147, 0.00170125, 0.00158103, 0.00146082, 0.00136256, 0.00126429, 0.00116603, 0.00106777, 0.00096951, 0.00102244, 0.00107538, 0.00112831, 0.00118124, 0.00123417, 0.00167353, 0.0021129, 0.00255226, 0.00299162, 0.00343098, 0.00318402, 0.00293706, 0.00269009, 0.00244313, 0.00219617, 0.00213715, 0.00207812, 0.00201909, 0.00196007, 0.00190104, 0.00194096, 0.00198087, 0.00202078, 0.0020607, 0.00210061, 0.00195124, 0.00180187, 0.0016525, 0.00150313, 0.00135376, 0.00127555, 0.00119733, 0.00111912, 0.0010409, 0.00096269, 0.00127228, 0.00158188, 0.00189148, 0.00220108, 0.00251068, 0.00211746, 0.00172425, 0.00133103, 0.00093782, 0.0005446, 0.00088503, 0.00122545, 0.00156588, 0.00190631, 0.00224674, 0.00215703, 0.00206733, 0.00197763, 0.00188792, 0.00179822, 0.0017655, 0.00173277, 0.00170004, 0.00166732, 0.00163459, 0.00133583, 0.00103706, 0.00073829, 0.00043952, 0.00014076, 0.00035816, 0.00057557, 0.00079298, 0.00101038, 0.00122779, 0.00121215, 0.00119651, 0.00118086, 0.00116522, 0.00114958, 0.00091966, 0.00068975, 0.00045983, 0.00022992, 0.0, 0.00026495, 0.0005299, 0.00079485, 0.0010598, 0.00132476, 0.00133077, 0.00133678, 0.00134279, 0.00134881, 0.00135482, 0.00135319, 0.00135155, 0.00134992, 0.00134829, 0.00134666, 0.00127296, 0.00119926, 0.00112556, 0.00105186, 0.00097816, 0.00125556, 0.00153296, 0.00181036, 0.00208776, 0.00236515, 0.00287448, 0.00338381, 0.00389313, 0.00440246, 0.00491178, 0.00675325, 0.00859472, 0.01043619, 0.01227766, 0.01411913, 0.01592666, 0.01773419, 0.01954172, 0.02134925, 0.02315678, 0.02763034, 0.0321039, 0.03657746, 0.04105102, 0.04552458, 0.05545584, 0.06538709, 0.07531835, 0.0852496, 0.09518086, 0.11155975, 0.12793863, 0.14431752, 0.16069641, 0.1770753, 0.20282723, 0.22857916, 0.25433109, 0.28008303, 0.30583496, 0.34030416, 0.37477335, 0.40924255, 0.44371175, 0.47818094, 0.51813865, 0.55809635, 0.59805405, 0.63801175, 0.67796945, 0.7136761, 0.74938275, 0.7850894, 0.82079605, 0.8565027, 0.87855963, 0.90061656, 0.92267349, 0.94473042, 0.96678735, 0.96896581, 0.97114427, 0.97332274, 0.9755012, 0.97767966, 0.96340716, 0.94913466, 0.93486216, 0.92058966, 0.90631716, 0.89752734, 0.88873751, 0.87994769, 0.87115786, 0.86236804, 0.85570159, 0.84903513, 0.84236868, 0.83570223, 0.82903577, 0.83514332, 0.84125087, 0.84735843, 0.85346598, 0.85957353, 0.86691465, 0.87425577, 0.88159689, 0.88893801, 0.89627913, 0.91143564, 0.92659215, 0.94174866, 0.95690517, 0.97206168, 0.97715497, 0.98224826, 0.98734154, 0.99243483, 0.99752812, 0.99553008, 0.99353204, 0.991534, 0.98953596, 0.98753792, 0.98755665, 0.98757537, 0.9875941, 0.98761282, 0.98763155, 0.98092716, 0.97422276, 0.96751837, 0.96081398, 0.95410959, 0.94800519, 0.94190079, 0.93579638, 0.92969198, 0.92358758, 0.93112225, 0.93865692, 0.9461916, 0.95372627, 0.96126094, 0.96900875, 0.97675657, 0.98450438, 0.99225219, 1.0, 0.99544487, 0.99088974, 0.98633461, 0.98177948, 0.97722436, 0.94198275, 0.90674115, 0.87149955, 0.83625794, 0.80101634, 0.74571382, 0.6904113, 0.63510877, 0.57980625, 0.52450373, 0.47802637, 0.431549, 0.38507164, 0.33859428, 0.29211691, 0.2641406, 0.23616428, 0.20818797, 0.18021165, 0.15223534, 0.13659485, 0.12095435, 0.10531386, 0.08967337, 0.07403288, 0.06607557, 0.05811827, 0.05016097, 0.04220367, 0.03424637, 0.03008912, 0.02593188, 0.02177463, 0.01761738, 0.01346014, 0.01212884, 0.01079754, 0.00946624, 0.00813495, 0.00680365, 0.00612254, 0.00544143, 0.00476031, 0.0040792, 0.00339809, 0.00338149, 0.00336489, 0.00334829, 0.00333169, 0.00331509, 0.00330477, 0.00329445, 0.00328413, 0.00327381, 0.00326349, 0.00326578, 0.00326807, 0.00327036, 0.00327265, 0.00327494, 0.00301937, 0.0027638, 0.00250823, 0.00225266, 0.00199709, 0.00201271, 0.00202833, 0.00204394, 0.00205956, 0.00207518, 0.00203035, 0.00198551, 0.00194068, 0.00189585, 0.00185101, 0.00194522, 0.00203943, 0.00213363, 0.00222784, 0.00232204, 0.0022252, 0.00212837, 0.00203153, 0.0019347, 0.00183786, 0.00193395, 0.00203004, 0.00212612, 0.00222221, 0.0023183, 0.00233962, 0.00236094, 0.00238226, 0.00240358, 0.0024249, 0.00241182, 0.00239874, 0.00238566, 0.00237258, 0.0023595, 0.00230593, 0.00225236, 0.0021988, 0.00214523, 0.00209166, 0.00202647, 0.00196128, 0.00189609, 0.0018309, 0.00176571, 0.00177363, 0.00178156, 0.00178948, 0.00179741, 0.00180533, 0.00178942, 0.00177351, 0.00175761, 0.0017417, 0.00172579, 0.00175414, 0.00178248, 0.00181082, 0.00183916, 0.00186751, 0.00185015, 0.00183279, 0.00181544, 0.00179808, 0.00178073, 0.00179472, 0.00180872, 0.00182272, 0.00183671, 0.00185071, 0.00183326, 0.00181582, 0.00179838, 0.00178093, 0.00176349, 0.0017762, 0.00178891, 0.00180162, 0.00181434, 0.00182705, 0.00184991, 0.00187277, 0.00189563, 0.00191849, 0.00194134, 0.00191998, 0.00189862, 0.00187726, 0.0018559, 0.00183454, 0.00182028, 0.00180602, 0.00179175, 0.00177749, 0.00176323], "wavelength": [9000, 9010, 9020, 9030, 9040, 9050, 9060, 9070, 9080, 9090, 9100, 9110, 9120, 9130, 9140, 9150, 9160, 9170, 9180, 9190, 9200, 9210, 9220, 9230, 9240, 9250, 9260, 9270, 9280, 9290, 9300, 9310, 9320, 9330, 9340, 9350, 9360, 9370, 9380, 9390, 9400, 9410, 9420, 9430, 9440, 9450, 9460, 9470, 9480, 9490, 9500, 9510, 9520, 9530, 9540, 9550, 9560, 9570, 9580, 9590, 9600, 9610, 9620, 9630, 9640, 9650, 9660, 9670, 9680, 9690, 9700, 9710, 9720, 9730, 9740, 9750, 9760, 9770, 9780, 9790, 9800, 9810, 9820, 9830, 9840, 9850, 9860, 9870, 9880, 9890, 9900, 9910, 9920, 9930, 9940, 9950, 9960, 9970, 9980, 9990, 10000, 10010, 10020, 10030, 10040, 10050, 10060, 10070, 10080, 10090, 10100, 10110, 10120, 10130, 10140, 10150, 10160, 10170, 10180, 10190, 10200, 10210, 10220, 10230, 10240, 10250, 10260, 10270, 10280, 10290, 10300, 10310, 10320, 10330, 10340, 10350, 10360, 10370, 10380, 10390, 10400, 10410, 10420, 10430, 10440, 10450, 10460, 10470, 10480, 10490, 10500, 10510, 10520, 10530, 10540, 10550, 10560, 10570, 10580, 10590, 10600, 10610, 10620, 10630, 10640, 10650, 10660, 10670, 10680, 10690, 10700, 10710, 10720, 10730, 10740, 10750, 10760, 10770, 10780, 10790, 10800, 10810, 10820, 10830, 10840, 10850, 10860, 10870, 10880, 10890, 10900, 10910, 10920, 10930, 10940, 10950, 10960, 10970, 10980, 10990, 11000, 11010, 11020, 11030, 11040, 11050, 11060, 11070, 11080, 11090, 11100, 11110, 11120, 11130, 11140, 11150, 11160, 11170, 11180, 11190, 11200, 11210, 11220, 11230, 11240, 11250, 11260, 11270, 11280, 11290, 11300, 11310, 11320, 11330, 11340, 11350, 11360, 11370, 11380, 11390, 11400, 11410, 11420, 11430, 11440, 11450, 11460, 11470, 11480, 11490, 11500, 11510, 11520, 11530, 11540, 11550, 11560, 11570, 11580, 11590, 11600, 11610, 11620, 11630, 11640, 11650, 11660, 11670, 11680, 11690, 11700, 11710, 11720, 11730, 11740, 11750, 11760, 11770, 11780, 11790, 11800, 11810, 11820, 11830, 11840, 11850, 11860, 11870, 11880, 11890, 11900, 11910, 11920, 11930, 11940, 11950, 11960, 11970, 11980, 11990, 12000, 12010, 12020, 12030, 12040, 12050, 12060, 12070, 12080, 12090, 12100, 12110, 12120, 12130, 12140, 12150, 12160, 12170, 12180, 12190, 12200, 12210, 12220, 12230, 12240, 12250, 12260, 12270, 12280, 12290, 12300, 12310, 12320, 12330, 12340, 12350, 12360, 12370, 12380, 12390, 12400, 12410, 12420, 12430, 12440, 12450, 12460, 12470, 12480, 12490, 12500, 12510, 12520, 12530, 12540, 12550, 12560, 12570, 12580, 12590, 12600, 12610, 12620, 12630, 12640, 12650, 12660, 12670, 12680, 12690, 12700, 12710, 12720, 12730, 12740, 12750, 12760, 12770, 12780, 12790, 12800, 12810, 12820, 12830, 12840, 12850, 12860, 12870, 12880, 12890, 12900, 12910, 12920, 12930, 12940, 12950, 12960, 12970, 12980, 12990, 13000, 13010, 13020, 13030, 13040, 13050, 13060, 13070, 13080, 13090, 13100, 13110, 13120, 13130, 13140, 13150, 13160, 13170, 13180, 13190, 13200, 13210, 13220, 13230, 13240, 13250, 13260, 13270, 13280, 13290, 13300, 13310, 13320, 13330, 13340, 13350, 13360, 13370, 13380, 13390, 13400, 13410, 13420, 13430, 13440, 13450, 13460, 13470, 13480, 13490, 13500, 13510, 13520, 13530, 13540, 13550, 13560, 13570, 13580, 13590, 13600, 13610, 13620, 13630, 13640, 13650, 13660, 13670, 13680, 13690, 13700, 13710, 13720, 13730, 13740, 13750, 13760, 13770, 13780, 13790, 13800, 13810, 13820, 13830, 13840, 13850, 13860, 13870, 13880, 13890, 13900, 13910, 13920, 13930, 13940, 13950, 13960, 13970, 13980, 13990, 14000]}}], "metadata_type": "eo"}	2021-01-31 22:08:51.848762+00	africa	\N
49	mangrove_cover	{"format": {"name": "GeoTIFF"}, "platform": {"code": "LANDSAT_5,LANDSAT_7,LANDSAT_8"}, "instrument": {"name": "TM,ETM+,OLI"}, "product_type": "mangrove_extent_cover"}	2	{"name": "mangrove_cover", "storage": {"crs": "EPSG:3577", "tile_size": {"x": 100000.0, "y": 100000.0}, "resolution": {"x": 25, "y": -25}, "dimension_order": ["time", "y", "x"]}, "metadata": {"format": {"name": "GeoTIFF"}, "platform": {"code": "LANDSAT_5,LANDSAT_7,LANDSAT_8"}, "instrument": {"name": "TM,ETM+,OLI"}, "product_type": "mangrove_extent_cover"}, "description": "Mangrove Cover, Australian Albers Equal Area projection (EPSG:3577)", "measurements": [{"name": "canopy_cover_class", "dtype": "int16", "units": "1", "nodata": -1, "aliases": ["cover"], "flags_definition": {"woodland": {"bits": [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0], "values": {"1": true}, "description": "Woodland"}, "open_forest": {"bits": [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0], "values": {"2": true}, "description": "Open Forest"}, "closed_forest": {"bits": [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0], "values": {"3": true}, "description": "Closed Forest"}}}, {"name": "extent", "dtype": "int16", "units": "1", "nodata": -1, "aliases": ["extent"]}], "metadata_type": "eo"}	2021-01-31 22:08:53.739983+00	africa	\N
50	multi_scale_topographic_position	{"format": {"name": "GeoTIFF"}, "product_type": "topographic_model"}	2	{"name": "multi_scale_topographic_position", "managed": true, "storage": {"crs": "EPSG:4326", "tile_size": {"latitude": 1.0, "longitude": 1.0}, "resolution": {"latitude": -0.000833333333347, "longitude": 0.000833333333347}}, "metadata": {"format": {"name": "GeoTIFF"}, "product_type": "topographic_model"}, "description": "Multi-scale Topographic Position Image", "measurements": [{"name": "regional", "dtype": "int16", "units": "0.0039", "nodata": 0}, {"name": "intermediate", "dtype": "int16", "units": "0.0039", "nodata": 0}, {"name": "local", "dtype": "int16", "units": "0.0039", "nodata": 0}], "metadata_type": "eo"}	2021-01-31 22:08:55.678911+00	africa	\N
53	water_bodies	{"format": {"name": "GeoTIFF"}, "product_type": "water_body_identifier"}	2	{"name": "water_bodies", "storage": {"crs": "EPSG:3577", "resolution": {"x": 25, "y": -25}}, "metadata": {"format": {"name": "GeoTIFF"}, "product_type": "water_body_identifier"}, "description": "Water Body ID Map", "measurements": [{"name": "dam_id", "dtype": "uint32", "units": "id", "nodata": 8388607}], "metadata_type": "eo"}	2021-01-31 22:09:06.820294+00	africa	\N
54	weathering_intensity	{"format": {"name": "GeoTIFF"}, "platform": {"code": "unknown"}, "instrument": {"name": "STRM"}, "product_type": "model"}	2	{"name": "weathering_intensity", "storage": {"crs": "EPSG:4326", "tile_size": {"latitude": 1200.0, "longitude": 1200.0}, "resolution": {"latitude": -0.000833333333347, "longitude": 0.000833333333347}}, "metadata": {"format": {"name": "GeoTIFF"}, "platform": {"code": "unknown"}, "instrument": {"name": "STRM"}, "product_type": "model"}, "description": "Weathering Intensity Model", "measurements": [{"name": "intensity", "dtype": "float32", "units": "0.16666666666666666", "nodata": -1}], "metadata_type": "eo"}	2021-01-31 22:09:08.721622+00	africa	\N
55	wofs_albers	{"format": {"name": "NetCDF"}, "product_type": "wofs"}	2	{"name": "wofs_albers", "managed": true, "storage": {"crs": "EPSG:3577", "driver": "NetCDF CF", "chunking": {"x": 200, "y": 200, "time": 5}, "tile_size": {"x": 100000.0, "y": 100000.0}, "resolution": {"x": 25, "y": -25}, "dimension_order": ["time", "y", "x"]}, "metadata": {"format": {"name": "NetCDF"}, "product_type": "wofs"}, "description": "Historic Flood Mapping Water Observations from Space", "measurements": [{"name": "water", "dtype": "int16", "units": "1", "nodata": 1, "flags_definition": {"dry": {"bits": [7, 6, 5, 4, 3, 1, 0], "values": {"0": true}, "description": "Clear and dry"}, "sea": {"bits": 2, "values": {"0": false, "1": true}, "description": "Sea"}, "wet": {"bits": [7, 6, 5, 4, 3, 1, 0], "values": {"128": true}, "description": "Clear and Wet"}, "cloud": {"bits": 6, "values": {"0": false, "1": true}, "description": "Cloudy"}, "nodata": {"bits": 0, "values": {"1": true}, "description": "No data"}, "high_slope": {"bits": 4, "values": {"0": false, "1": true}, "description": "High slope"}, "cloud_shadow": {"bits": 5, "values": {"0": false, "1": true}, "description": "Cloud shadow"}, "noncontiguous": {"bits": 1, "values": {"0": false, "1": true}, "description": "At least one EO band is missing over over/undersaturated"}, "water_observed": {"bits": 7, "values": {"0": false, "1": true}, "description": "Classified as water by the decision tree"}, "terrain_or_low_angle": {"bits": 3, "values": {"0": false, "1": true}, "description": "Terrain shadow or low solar angle"}}}], "metadata_type": "eo"}	2021-01-31 22:09:10.621394+00	africa	\N
56	wofs_annual_summary	{"format": {"name": "NetCDF"}, "platform": {"code": "LANDSAT_5,LANDSAT_7,LANDSAT_8"}, "instrument": {"name": "TM,ETM,OLI"}, "product_type": "wofs_annual_summary"}	2	{"name": "wofs_annual_summary", "storage": {"crs": "EPSG:3577", "tile_size": {"x": 100000.0, "y": 100000.0}, "resolution": {"x": 25, "y": -25}, "dimension_order": ["time", "y", "x"]}, "metadata": {"format": {"name": "NetCDF"}, "platform": {"code": "LANDSAT_5,LANDSAT_7,LANDSAT_8"}, "instrument": {"name": "TM,ETM,OLI"}, "product_type": "wofs_annual_summary"}, "description": "Water Observations from Space Annual Statistics", "measurements": [{"name": "count_wet", "dtype": "int16", "units": "1", "nodata": -1}, {"name": "count_clear", "dtype": "int16", "units": "1", "nodata": -1}, {"name": "frequency", "dtype": "float32", "units": "1", "nodata": -1}], "metadata_type": "eo"}	2021-01-31 22:09:12.51767+00	africa	\N
57	wofs_apr_oct_summary	{"format": {"name": "NetCDF"}, "platform": {"code": "LANDSAT_5,LANDSAT_7,LANDSAT_8"}, "instrument": {"name": "TM,ETM,OLI"}, "product_type": "wofs_apr_oct_summary"}	2	{"name": "wofs_apr_oct_summary", "storage": {"crs": "EPSG:3577", "tile_size": {"x": 100000.0, "y": 100000.0}, "resolution": {"x": 25, "y": -25}, "dimension_order": ["time", "y", "x"]}, "metadata": {"format": {"name": "NetCDF"}, "platform": {"code": "LANDSAT_5,LANDSAT_7,LANDSAT_8"}, "instrument": {"name": "TM,ETM,OLI"}, "product_type": "wofs_apr_oct_summary"}, "description": "Water Observations from Space April to October Statistics", "measurements": [{"name": "count_wet", "dtype": "int16", "units": "1", "nodata": -1}, {"name": "count_clear", "dtype": "int16", "units": "1", "nodata": -1}, {"name": "frequency", "dtype": "float32", "units": "1", "nodata": -1}], "metadata_type": "eo"}	2021-01-31 22:09:14.445497+00	africa	\N
58	wofs_filtered_summary	{"format": {"name": "NetCDF"}, "platform": {"code": "LANDSAT_5,LANDSAT_7,LANDSAT_8"}, "instrument": {"name": "TM,ETM+,OLI"}, "product_type": "wofs_filtered_summary"}	2	{"name": "wofs_filtered_summary", "storage": {"crs": "EPSG:3577", "tile_size": {"x": 100000.0, "y": 100000.0}, "resolution": {"x": 25, "y": -25}, "dimension_order": ["time", "y", "x"]}, "metadata": {"format": {"name": "NetCDF"}, "platform": {"code": "LANDSAT_5,LANDSAT_7,LANDSAT_8"}, "instrument": {"name": "TM,ETM+,OLI"}, "product_type": "wofs_filtered_summary"}, "description": "Water Observations from Space Statistics confidence filtered", "measurements": [{"name": "confidence", "dtype": "float32", "units": "1", "nodata": -1}, {"name": "wofs_filtered_summary", "dtype": "float32", "units": "1", "nodata": -1}], "metadata_type": "eo"}	2021-01-31 22:09:16.325436+00	africa	\N
59	wofs_nov_mar_summary	{"format": {"name": "NetCDF"}, "platform": {"code": "LANDSAT_5,LANDSAT_7,LANDSAT_8"}, "instrument": {"name": "TM,ETM,OLI"}, "product_type": "wofs_nov_mar_summary"}	2	{"name": "wofs_nov_mar_summary", "storage": {"crs": "EPSG:3577", "tile_size": {"x": 100000.0, "y": 100000.0}, "resolution": {"x": 25, "y": -25}, "dimension_order": ["time", "y", "x"]}, "metadata": {"format": {"name": "NetCDF"}, "platform": {"code": "LANDSAT_5,LANDSAT_7,LANDSAT_8"}, "instrument": {"name": "TM,ETM,OLI"}, "product_type": "wofs_nov_mar_summary"}, "description": "Water Observations from Space November to March Statistics", "measurements": [{"name": "count_wet", "dtype": "int16", "units": "1", "nodata": -1}, {"name": "count_clear", "dtype": "int16", "units": "1", "nodata": -1}, {"name": "frequency", "dtype": "float32", "units": "1", "nodata": -1}], "metadata_type": "eo"}	2021-01-31 22:09:18.208899+00	africa	\N
60	wofs_summary	{"format": {"name": "NetCDF"}, "platform": {"code": "LANDSAT_5,LANDSAT_7,LANDSAT_8"}, "instrument": {"name": "TM,ETM+,OLI"}, "product_type": "wofs_statistical_summary"}	2	{"name": "wofs_summary", "storage": {"crs": "EPSG:3577", "tile_size": {"x": 100000.0, "y": 100000.0}, "resolution": {"x": 25, "y": -25}, "dimension_order": ["time", "y", "x"]}, "metadata": {"format": {"name": "NetCDF"}, "platform": {"code": "LANDSAT_5,LANDSAT_7,LANDSAT_8"}, "instrument": {"name": "TM,ETM+,OLI"}, "product_type": "wofs_statistical_summary"}, "description": "Water Observations from Space Statistics", "measurements": [{"name": "count_wet", "dtype": "int16", "units": "1", "nodata": -1}, {"name": "count_clear", "dtype": "int16", "units": "1", "nodata": -1}, {"name": "frequency", "dtype": "float32", "units": "1", "nodata": -1}], "metadata_type": "eo"}	2021-01-31 22:09:20.099229+00	africa	\N
61	ga_ls8c_ard_3	{"product": {"name": "ga_ls8c_ard_3"}}	5	{"name": "ga_ls8c_ard_3", "metadata": {"product": {"name": "ga_ls8c_ard_3"}}, "description": "Landsat 8 OLI-TIRS ARD, GA Collection 3", "measurements": [{"name": "nbar_coastal_aerosol", "dtype": "int16", "units": "1", "nodata": -999, "aliases": ["nbar_band01"]}, {"name": "nbar_blue", "dtype": "int16", "units": "1", "nodata": -999, "aliases": ["nbar_band02"]}, {"name": "nbar_green", "dtype": "int16", "units": "1", "nodata": -999, "aliases": ["nbar_band03"]}, {"name": "nbar_red", "dtype": "int16", "units": "1", "nodata": -999, "aliases": ["nbar_band04"]}, {"name": "nbar_nir", "dtype": "int16", "units": "1", "nodata": -999, "aliases": ["nbar_band05"]}, {"name": "nbar_swir_1", "dtype": "int16", "units": "1", "nodata": -999, "aliases": ["nbar_band06"]}, {"name": "nbar_swir_2", "dtype": "int16", "units": "1", "nodata": -999, "aliases": ["nbar_band07"]}, {"name": "nbar_panchromatic", "dtype": "int16", "units": "1", "nodata": -999, "aliases": ["nbar_band08"]}, {"name": "nbart_coastal_aerosol", "dtype": "int16", "units": "1", "nodata": -999, "aliases": ["nbart_band01", "coastal_aerosol"]}, {"name": "nbart_blue", "dtype": "int16", "units": "1", "nodata": -999, "aliases": ["nbart_band02", "blue"]}, {"name": "nbart_green", "dtype": "int16", "units": "1", "nodata": -999, "aliases": ["nbart_band03", "green"]}, {"name": "nbart_red", "dtype": "int16", "units": "1", "nodata": -999, "aliases": ["nbart_band04", "red"]}, {"name": "nbart_nir", "dtype": "int16", "units": "1", "nodata": -999, "aliases": ["nbart_band05", "nir"]}, {"name": "nbart_swir_1", "dtype": "int16", "units": "1", "nodata": -999, "aliases": ["nbart_band06", "swir_1", "swir1"]}, {"name": "nbart_swir_2", "dtype": "int16", "units": "1", "nodata": -999, "aliases": ["nbart_band07", "swir_2", "swir2"]}, {"name": "nbart_panchromatic", "dtype": "int16", "units": "1", "nodata": -999, "aliases": ["nbart_band08", "panchromatic"]}, {"name": "oa_fmask", "dtype": "uint8", "units": "1", "nodata": 0, "aliases": ["fmask"], "flags_definition": {"fmask": {"bits": [0, 1, 2, 3, 4, 5, 6, 7], "values": {"0": "nodata", "1": "valid", "2": "cloud", "3": "shadow", "4": "snow", "5": "water"}, "description": "Fmask"}}}, {"name": "oa_nbar_contiguity", "dtype": "uint8", "units": "1", "nodata": 255, "aliases": ["nbar_contiguity"], "flags_definition": {"contiguous": {"bits": [0], "values": {"0": false, "1": true}}}}, {"name": "oa_nbart_contiguity", "dtype": "uint8", "units": "1", "nodata": 255, "aliases": ["nbart_contiguity"], "flags_definition": {"contiguous": {"bits": [0], "values": {"0": false, "1": true}}}}, {"name": "oa_azimuthal_exiting", "dtype": "float32", "units": "1", "nodata": "NaN", "aliases": ["azimuthal_exiting"]}, {"name": "oa_azimuthal_incident", "dtype": "float32", "units": "1", "nodata": "NaN", "aliases": ["azimuthal_incident"]}, {"name": "oa_combined_terrain_shadow", "dtype": "uint8", "units": "1", "nodata": 255, "aliases": ["combined_terrain_shadow"]}, {"name": "oa_exiting_angle", "dtype": "float32", "units": "1", "nodata": "NaN", "aliases": ["exiting_angle"]}, {"name": "oa_incident_angle", "dtype": "float32", "units": "1", "nodata": "NaN", "aliases": ["incident_angle"]}, {"name": "oa_relative_azimuth", "dtype": "float32", "units": "1", "nodata": "NaN", "aliases": ["relative_azimuth"]}, {"name": "oa_relative_slope", "dtype": "float32", "units": "1", "nodata": "NaN", "aliases": ["relative_slope"]}, {"name": "oa_satellite_azimuth", "dtype": "float32", "units": "1", "nodata": "NaN", "aliases": ["satellite_azimuth"]}, {"name": "oa_satellite_view", "dtype": "float32", "units": "1", "nodata": "NaN", "aliases": ["satellite_view"]}, {"name": "oa_solar_azimuth", "dtype": "float32", "units": "1", "nodata": "NaN", "aliases": ["solar_azimuth"]}, {"name": "oa_solar_zenith", "dtype": "float32", "units": "1", "nodata": "NaN", "aliases": ["solar_zenith"]}, {"name": "oa_time_delta", "dtype": "float32", "units": "1", "nodata": "NaN", "aliases": ["time_delta"]}], "metadata_type": "eo3_landsat_ard"}	2021-01-31 22:18:43.689267+00	africa	\N
62	ga_s2a_ard_nbar_granule	{"format": {"name": "GeoTIFF"}, "platform": {"code": "SENTINEL_2A"}, "instrument": {"name": "MSI"}, "product_type": "S2MSIARD_NBAR", "processing_level": "Level-2"}	7	{"name": "ga_s2a_ard_nbar_granule", "metadata": {"format": {"name": "GeoTIFF"}, "platform": {"code": "SENTINEL_2A"}, "instrument": {"name": "MSI"}, "product_type": "S2MSIARD_NBAR", "processing_level": "Level-2"}, "description": "Sentinel-2A MSI Definitive ARD - NBAR and Pixel Quality", "measurements": [{"name": "azimuthal_exiting", "dtype": "float32", "units": "1", "nodata": -999, "aliases": ["azimuthal_exiting"]}, {"name": "azimuthal_incident", "dtype": "float32", "units": "1", "nodata": -999, "aliases": ["azimuthal_incident"]}, {"name": "exiting", "dtype": "float32", "units": "1", "nodata": -999, "aliases": ["exiting"]}, {"name": "incident", "dtype": "float32", "units": "1", "nodata": -999, "aliases": ["incident"]}, {"name": "relative_azimuth", "dtype": "float32", "units": "1", "nodata": -999, "aliases": ["relative_azimuth"]}, {"name": "relative_slope", "dtype": "float32", "units": "1", "nodata": -999, "aliases": ["relative_slope"]}, {"name": "satellite_azimuth", "dtype": "float32", "units": "1", "nodata": -999, "aliases": ["satellite_azimuth"]}, {"name": "satellite_view", "dtype": "float32", "units": "1", "nodata": -999, "aliases": ["satellite_view"]}, {"name": "solar_azimuth", "dtype": "float32", "units": "1", "nodata": -999, "aliases": ["solar_azimuth"]}, {"name": "solar_zenith", "dtype": "float32", "units": "1", "nodata": -999, "aliases": ["solar_zenith"]}, {"name": "terrain_shadow", "dtype": "uint8", "units": "1", "nodata": 0, "aliases": ["terrain_shadow"]}, {"name": "fmask", "dtype": "uint8", "units": "1", "nodata": 0, "aliases": ["mask", "Fmask"], "flags_definition": {"fmask": {"bits": [0, 1, 2, 3, 4, 5, 6, 7], "values": {"0": "nodata", "1": "valid", "2": "cloud", "3": "shadow", "4": "snow", "5": "water"}, "description": "Fmask"}}}, {"name": "nbar_contiguity", "dtype": "uint8", "units": "1", "nodata": 255, "flags_definition": {"contiguity": {"bits": [0, 1, 2, 3, 4, 5, 6, 7], "values": {"0": "not_contiguous", "1": "contiguous"}, "description": "Pixel contiguity in band stack"}}}, {"name": "nbar_coastal_aerosol", "dtype": "int16", "units": "1", "nodata": -999, "aliases": ["nbar_band_01", "nbar_B01", "nbar_Band1"], "spectral_definition": {"response": [0.015297, 0.067133, 0.19593, 0.357242, 0.460571, 0.511598, 0.551051, 0.587385, 0.613478, 0.650014, 0.699199, 0.74543, 0.792047, 0.862824, 0.947307, 0.993878, 1.0, 0.990178, 0.972897, 0.957042, 0.956726, 0.922389, 0.723933, 0.388302, 0.14596, 0.051814, 0.017459, 0.000303], "wavelength": [430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457]}}, {"name": "nbar_blue", "dtype": "int16", "units": "1", "nodata": -999, "aliases": ["nbar_band_02", "nbar_B02", "nbar_Band2"], "spectral_definition": {"response": [0.001206, 0.00204, 0.002623, 0.002738, 0.002746, 0.002076, 0.003246, 0.002224, 0.002789, 0.003127, 0.002377, 0.003776, 0.002856, 0.003063, 0.00607, 0.009028, 0.019547, 0.038955, 0.084088, 0.176255, 0.292197, 0.364612, 0.382418, 0.385789, 0.393447, 0.400158, 0.410291, 0.424686, 0.449286, 0.481594, 0.505323, 0.523406, 0.529543, 0.534688, 0.533786, 0.534656, 0.5381, 0.543691, 0.557717, 0.578585, 0.601967, 0.616037, 0.621092, 0.613597, 0.596062, 0.575863, 0.558063, 0.546131, 0.542099, 0.553602, 0.571684, 0.598269, 0.633236, 0.67337, 0.711752, 0.738396, 0.758249, 0.768325, 0.773367, 0.780468, 0.788363, 0.795449, 0.809151, 0.824011, 0.837709, 0.844983, 0.847328, 0.840111, 0.825797, 0.804778, 0.78694, 0.771578, 0.761923, 0.765487, 0.781682, 0.810031, 0.850586, 0.901671, 0.95467, 0.987257, 1.0, 0.986389, 0.908308, 0.724, 0.478913, 0.286992, 0.169976, 0.102833, 0.065163, 0.04116, 0.02508, 0.013112, 0.002585, 0.001095, 0.000308, 0.000441, 0.0, 0.0, 0.000443], "wavelength": [440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538]}}, {"name": "nbar_green", "dtype": "int16", "units": "1", "nodata": -999, "aliases": ["nbar_band_03", "nbar_B03", "nbar_Band3"], "spectral_definition": {"response": [0.00084, 0.016372, 0.037688, 0.080665, 0.169509, 0.341374, 0.573031, 0.746711, 0.828036, 0.868228, 0.888565, 0.891572, 0.87815, 0.860271, 0.843698, 0.834035, 0.832617, 0.844968, 0.867734, 0.897361, 0.933938, 0.966923, 0.990762, 1.0, 0.997812, 0.981107, 0.947088, 0.907183, 0.868656, 0.837622, 0.81291, 0.792434, 0.7851, 0.789606, 0.807011, 0.830458, 0.846433, 0.858402, 0.85799, 0.799824, 0.62498, 0.386994, 0.200179, 0.098293, 0.042844, 0.016512], "wavelength": [537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582]}}, {"name": "nbar_red", "dtype": "int16", "units": "1", "nodata": -999, "aliases": ["nbar_band_04", "nbar_B04", "nbar_Band4"], "spectral_definition": {"response": [0.002584, 0.034529, 0.14997, 0.464826, 0.817746, 0.965324, 0.983869, 0.9969, 1.0, 0.995449, 0.991334, 0.977215, 0.936802, 0.873776, 0.814166, 0.776669, 0.764864, 0.775091, 0.801359, 0.830828, 0.857112, 0.883581, 0.90895, 0.934759, 0.955931, 0.96811, 0.973219, 0.971572, 0.969003, 0.965712, 0.960481, 0.944811, 0.884152, 0.706167, 0.422967, 0.189853, 0.063172, 0.020615, 0.002034], "wavelength": [646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 683, 684]}}, {"name": "nbar_red_edge_1", "dtype": "int16", "units": "1", "nodata": -999, "aliases": ["nbar_band_05", "nbar_B05", "nbar_Band5"], "spectral_definition": {"response": [0.001187, 0.04126, 0.167712, 0.478496, 0.833878, 0.985479, 1.0, 0.999265, 0.993239, 0.982416, 0.965583, 0.945953, 0.924699, 0.902399, 0.885582, 0.861231, 0.757197, 0.521268, 0.196706, 0.036825], "wavelength": [694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713]}}, {"name": "nbar_red_edge_2", "dtype": "int16", "units": "1", "nodata": -999, "aliases": ["nbar_band_06", "nbar_B06", "nbar_Band6"], "spectral_definition": {"response": [0.005331, 0.085006, 0.345714, 0.750598, 0.920265, 0.917917, 0.934211, 0.957861, 0.975829, 0.981932, 0.981518, 0.993406, 1.0, 0.982579, 0.962584, 0.854908, 0.506722, 0.135357, 0.013438], "wavelength": [731, 732, 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748, 749]}}, {"name": "nbar_red_edge_3", "dtype": "int16", "units": "1", "nodata": -999, "aliases": ["nbar_band_07", "nbar_B07", "nbar_Band7"], "spectral_definition": {"response": [0.001595, 0.014731, 0.067032, 0.199495, 0.422803, 0.694015, 0.898494, 0.983173, 0.994759, 1.0, 0.994913, 0.964657, 0.908117, 0.846898, 0.802091, 0.778839, 0.777241, 0.789523, 0.800984, 0.802916, 0.791711, 0.757695, 0.677951, 0.536855, 0.364033, 0.193498, 0.077219, 0.019707, 0.003152], "wavelength": [769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784, 785, 786, 787, 788, 789, 790, 791, 792, 793, 794, 795, 796, 797]}}, {"name": "nbar_nir_1", "dtype": "int16", "units": "1", "nodata": -999, "aliases": ["nbar_band_08", "nbar_B08", "nbar_Band8"], "spectral_definition": {"response": [0.000451, 0.007614, 0.019072, 0.033498, 0.056536, 0.087148, 0.13246, 0.203436, 0.314068, 0.450085, 0.587433, 0.714518, 0.81829, 0.902932, 0.960732, 0.993723, 1.0, 0.985213, 0.958376, 0.93655, 0.925816, 0.930376, 0.941281, 0.953344, 0.962183, 0.965631, 0.963105, 0.959009, 0.951205, 0.945147, 0.943136, 0.945814, 0.945357, 0.943762, 0.937084, 0.92789, 0.915897, 0.900979, 0.881577, 0.86216, 0.8432, 0.822684, 0.801819, 0.776911, 0.755632, 0.737893, 0.722217, 0.708669, 0.698416, 0.690211, 0.682257, 0.681494, 0.682649, 0.678491, 0.67595, 0.671304, 0.665538, 0.660812, 0.658739, 0.65831, 0.66407, 0.672731, 0.685501, 0.701159, 0.720686, 0.742292, 0.75953, 0.776608, 0.784061, 0.78772, 0.787693, 0.783525, 0.776161, 0.768339, 0.759264, 0.745943, 0.733022, 0.720589, 0.706663, 0.69087, 0.675896, 0.661558, 0.649339, 0.638008, 0.627424, 0.618963, 0.610945, 0.604322, 0.597408, 0.591724, 0.586961, 0.582746, 0.581202, 0.57948, 0.580197, 0.582505, 0.585308, 0.589481, 0.592827, 0.596749, 0.601372, 0.603234, 0.605476, 0.608972, 0.613463, 0.618715, 0.626841, 0.637436, 0.648791, 0.659233, 0.66734, 0.668624, 0.659924, 0.641666, 0.615841, 0.583567, 0.552076, 0.526407, 0.507116, 0.49653, 0.499119, 0.512088, 0.529093, 0.542739, 0.537964, 0.495953, 0.419305, 0.326791, 0.231085, 0.14854, 0.089683, 0.054977, 0.033246, 0.019774, 0.007848, 0.001286], "wavelength": [773, 774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784, 785, 786, 787, 788, 789, 790, 791, 792, 793, 794, 795, 796, 797, 798, 799, 800, 801, 802, 803, 804, 805, 806, 807, 808, 809, 810, 811, 812, 813, 814, 815, 816, 817, 818, 819, 820, 821, 822, 823, 824, 825, 826, 827, 828, 829, 830, 831, 832, 833, 834, 835, 836, 837, 838, 839, 840, 841, 842, 843, 844, 845, 846, 847, 848, 849, 850, 851, 852, 853, 854, 855, 856, 857, 858, 859, 860, 861, 862, 863, 864, 865, 866, 867, 868, 869, 870, 871, 872, 873, 874, 875, 876, 877, 878, 879, 880, 881, 882, 883, 884, 885, 886, 887, 888, 889, 890, 891, 892, 893, 894, 895, 896, 897, 898, 899, 900, 901, 902, 903, 904, 905, 906, 907, 908]}}, {"name": "nbar_nir_2", "dtype": "int16", "units": "1", "nodata": -999, "aliases": ["nbar_band_8A", "nbar_B8A", "nbar_Band8A"], "spectral_definition": {"response": [0.001651, 0.013242, 0.02471, 0.051379, 0.104944, 0.216577, 0.384865, 0.585731, 0.774481, 0.87843, 0.914944, 0.922574, 0.926043, 0.929676, 0.935962, 0.946583, 0.955792, 0.965458, 0.974461, 0.97988, 0.983325, 0.982881, 0.988474, 1.0, 0.999626, 0.921005, 0.728632, 0.472189, 0.238082, 0.106955, 0.046096, 0.022226, 0.008819, 0.000455], "wavelength": [848, 849, 850, 851, 852, 853, 854, 855, 856, 857, 858, 859, 860, 861, 862, 863, 864, 865, 866, 867, 868, 869, 870, 871, 872, 873, 874, 875, 876, 877, 878, 879, 880, 881]}}, {"name": "nbar_swir_2", "dtype": "int16", "units": "1", "nodata": -999, "aliases": ["nbar_band_11", "nbar_B11", "nbar_Band11"], "spectral_definition": {"response": [0.000007, 0.000007, 0.000008, 0.000028, 0.000038, 0.000091, 0.000147, 0.000251, 0.00048, 0.00057, 0.000662, 0.000911, 0.001166, 0.001684, 0.002458, 0.003567, 0.005345, 0.008318, 0.012628, 0.018996, 0.027781, 0.039584, 0.054865, 0.07493, 0.10107, 0.135476, 0.182597, 0.247276, 0.330736, 0.429691, 0.537634, 0.647173, 0.743528, 0.815215, 0.859202, 0.879669, 0.88703, 0.889098, 0.891417, 0.897586, 0.906631, 0.916528, 0.926579, 0.935322, 0.942394, 0.947507, 0.951416, 0.954254, 0.956429, 0.958205, 0.960688, 0.96348, 0.965797, 0.96818, 0.971012, 0.97338, 0.975915, 0.978581, 0.979878, 0.980589, 0.980912, 0.981412, 0.981244, 0.980705, 0.980377, 0.981066, 0.982736, 0.985122, 0.987807, 0.990376, 0.992016, 0.993288, 0.992536, 0.990405, 0.987128, 0.983502, 0.980023, 0.976174, 0.972568, 0.969828, 0.967709, 0.966371, 0.965849, 0.96605, 0.967427, 0.96987, 0.973463, 0.978683, 0.983472, 0.987635, 0.991875, 0.995476, 0.997586, 0.998568, 0.999328, 0.999234, 0.998804, 0.999111, 0.99973, 0.999745, 1.0, 0.999814, 0.996693, 0.99162, 0.985702, 0.978569, 0.969903, 0.960896, 0.953287, 0.946546, 0.941712, 0.938586, 0.935489, 0.928114, 0.912102, 0.880598, 0.82498, 0.743118, 0.641891, 0.534002, 0.426963, 0.32371, 0.234284, 0.163972, 0.110211, 0.072478, 0.046194, 0.029401, 0.019359, 0.013308, 0.009317, 0.006523, 0.004864, 0.003409, 0.002491, 0.001958, 0.001423, 0.001055, 0.000498, 0.000228, 0.000159, 0.000034, 0.000045, 0.000013], "wavelength": [1539, 1540, 1541, 1542, 1543, 1544, 1545, 1546, 1547, 1548, 1549, 1550, 1551, 1552, 1553, 1554, 1555, 1556, 1557, 1558, 1559, 1560, 1561, 1562, 1563, 1564, 1565, 1566, 1567, 1568, 1569, 1570, 1571, 1572, 1573, 1574, 1575, 1576, 1577, 1578, 1579, 1580, 1581, 1582, 1583, 1584, 1585, 1586, 1587, 1588, 1589, 1590, 1591, 1592, 1593, 1594, 1595, 1596, 1597, 1598, 1599, 1600, 1601, 1602, 1603, 1604, 1605, 1606, 1607, 1608, 1609, 1610, 1611, 1612, 1613, 1614, 1615, 1616, 1617, 1618, 1619, 1620, 1621, 1622, 1623, 1624, 1625, 1626, 1627, 1628, 1629, 1630, 1631, 1632, 1633, 1634, 1635, 1636, 1637, 1638, 1639, 1640, 1641, 1642, 1643, 1644, 1645, 1646, 1647, 1648, 1649, 1650, 1651, 1652, 1653, 1654, 1655, 1656, 1657, 1658, 1659, 1660, 1661, 1662, 1663, 1664, 1665, 1666, 1667, 1668, 1669, 1670, 1671, 1672, 1673, 1674, 1675, 1676, 1677, 1678, 1679, 1680, 1681, 1682]}}, {"name": "nbar_swir_3", "dtype": "int16", "units": "1", "nodata": -999, "aliases": ["nbar_band_12", "nbar_B12", "nbar_Band12"], "spectral_definition": {"response": [0.000639, 0.001023, 0.002885, 0.003997, 0.006597, 0.00766, 0.008004, 0.00854, 0.0093, 0.010002, 0.010972, 0.012089, 0.013364, 0.015017, 0.017126, 0.01978, 0.023336, 0.027668, 0.033216, 0.040217, 0.048883, 0.059642, 0.073175, 0.090535, 0.11147, 0.136903, 0.167811, 0.203461, 0.242871, 0.284898, 0.327178, 0.368404, 0.408003, 0.444778, 0.476537, 0.503107, 0.525318, 0.543352, 0.557253, 0.568634, 0.57903, 0.588684, 0.598891, 0.609981, 0.621362, 0.634283, 0.648546, 0.663707, 0.680046, 0.696165, 0.711964, 0.727011, 0.741301, 0.757405, 0.772071, 0.785581, 0.798238, 0.809677, 0.819702, 0.828599, 0.836722, 0.844443, 0.851107, 0.853252, 0.854746, 0.856174, 0.857821, 0.859532, 0.86146, 0.863257, 0.865139, 0.867319, 0.869696, 0.874302, 0.878588, 0.882439, 0.885929, 0.889473, 0.893226, 0.896696, 0.899897, 0.902596, 0.904831, 0.905525, 0.905665, 0.905503, 0.905158, 0.904783, 0.904082, 0.903347, 0.902761, 0.902377, 0.901983, 0.903424, 0.904313, 0.905315, 0.906446, 0.908092, 0.910123, 0.91295, 0.915585, 0.918444, 0.921302, 0.924337, 0.927219, 0.92974, 0.931922, 0.934142, 0.935906, 0.937086, 0.937641, 0.938301, 0.937652, 0.940441, 0.942518, 0.943259, 0.943031, 0.942117, 0.940632, 0.938428, 0.93666, 0.935256, 0.933022, 0.92688, 0.921057, 0.915483, 0.91102, 0.908293, 0.907283, 0.908191, 0.911169, 0.916189, 0.922855, 0.920605, 0.919482, 0.919489, 0.921276, 0.924526, 0.927733, 0.931974, 0.93677, 0.941483, 0.946802, 0.951203, 0.954437, 0.957047, 0.959729, 0.962539, 0.964858, 0.966042, 0.966647, 0.96631, 0.96546, 0.964841, 0.963656, 0.961698, 0.959454, 0.957327, 0.95514, 0.953558, 0.952732, 0.952181, 0.951731, 0.952146, 0.952641, 0.954057, 0.957078, 0.960639, 0.964222, 0.968307, 0.972691, 0.977423, 0.982898, 0.987144, 0.990734, 0.993983, 0.996787, 0.998753, 1.0, 0.999927, 0.999152, 0.997129, 0.993884, 0.989686, 0.983735, 0.976213, 0.967813, 0.958343, 0.94844, 0.938203, 0.927725, 0.917039, 0.905999, 0.893868, 0.881683, 0.868647, 0.854635, 0.84062, 0.826016, 0.809516, 0.791867, 0.772443, 0.749107, 0.720346, 0.688185, 0.651283, 0.61005, 0.566031, 0.52097, 0.474659, 0.429259, 0.385857, 0.342092, 0.30068, 0.263176, 0.227704, 0.195721, 0.16809, 0.14468, 0.124831, 0.108237, 0.094401, 0.082363, 0.0715, 0.062691, 0.054985, 0.048195, 0.042864, 0.038598, 0.034947, 0.031999, 0.029588, 0.027418, 0.025577, 0.023959, 0.021672, 0.019148, 0.016331, 0.010989, 0.007379, 0.006511, 0.00471, 0.002065], "wavelength": [2078, 2079, 2080, 2081, 2082, 2083, 2084, 2085, 2086, 2087, 2088, 2089, 2090, 2091, 2092, 2093, 2094, 2095, 2096, 2097, 2098, 2099, 2100, 2101, 2102, 2103, 2104, 2105, 2106, 2107, 2108, 2109, 2110, 2111, 2112, 2113, 2114, 2115, 2116, 2117, 2118, 2119, 2120, 2121, 2122, 2123, 2124, 2125, 2126, 2127, 2128, 2129, 2130, 2131, 2132, 2133, 2134, 2135, 2136, 2137, 2138, 2139, 2140, 2141, 2142, 2143, 2144, 2145, 2146, 2147, 2148, 2149, 2150, 2151, 2152, 2153, 2154, 2155, 2156, 2157, 2158, 2159, 2160, 2161, 2162, 2163, 2164, 2165, 2166, 2167, 2168, 2169, 2170, 2171, 2172, 2173, 2174, 2175, 2176, 2177, 2178, 2179, 2180, 2181, 2182, 2183, 2184, 2185, 2186, 2187, 2188, 2189, 2190, 2191, 2192, 2193, 2194, 2195, 2196, 2197, 2198, 2199, 2200, 2201, 2202, 2203, 2204, 2205, 2206, 2207, 2208, 2209, 2210, 2211, 2212, 2213, 2214, 2215, 2216, 2217, 2218, 2219, 2220, 2221, 2222, 2223, 2224, 2225, 2226, 2227, 2228, 2229, 2230, 2231, 2232, 2233, 2234, 2235, 2236, 2237, 2238, 2239, 2240, 2241, 2242, 2243, 2244, 2245, 2246, 2247, 2248, 2249, 2250, 2251, 2252, 2253, 2254, 2255, 2256, 2257, 2258, 2259, 2260, 2261, 2262, 2263, 2264, 2265, 2266, 2267, 2268, 2269, 2270, 2271, 2272, 2273, 2274, 2275, 2276, 2277, 2278, 2279, 2280, 2281, 2282, 2283, 2284, 2285, 2286, 2287, 2288, 2289, 2290, 2291, 2292, 2293, 2294, 2295, 2296, 2297, 2298, 2299, 2300, 2301, 2302, 2303, 2304, 2305, 2306, 2307, 2308, 2309, 2310, 2311, 2312, 2313, 2314, 2315, 2316, 2317, 2318, 2319, 2320]}}], "metadata_type": "eo_plus"}	2021-01-31 22:18:45.610775+00	africa	\N
63	ga_s2b_ard_nbar_granule	{"format": {"name": "GeoTIFF"}, "platform": {"code": "SENTINEL_2B"}, "instrument": {"name": "MSI"}, "product_type": "S2MSIARD_NBAR", "processing_level": "Level-2"}	7	{"name": "ga_s2b_ard_nbar_granule", "metadata": {"format": {"name": "GeoTIFF"}, "platform": {"code": "SENTINEL_2B"}, "instrument": {"name": "MSI"}, "product_type": "S2MSIARD_NBAR", "processing_level": "Level-2"}, "description": "Sentinel-2B MSI Definitive ARD - NBAR and Pixel Quality", "measurements": [{"name": "azimuthal_exiting", "dtype": "float32", "units": "1", "nodata": -999, "aliases": ["azimuthal_exiting"]}, {"name": "azimuthal_incident", "dtype": "float32", "units": "1", "nodata": -999, "aliases": ["azimuthal_incident"]}, {"name": "exiting", "dtype": "float32", "units": "1", "nodata": -999, "aliases": ["exiting"]}, {"name": "incident", "dtype": "float32", "units": "1", "nodata": -999, "aliases": ["incident"]}, {"name": "relative_azimuth", "dtype": "float32", "units": "1", "nodata": -999, "aliases": ["relative_azimuth"]}, {"name": "relative_slope", "dtype": "float32", "units": "1", "nodata": -999, "aliases": ["relative_slope"]}, {"name": "satellite_azimuth", "dtype": "float32", "units": "1", "nodata": -999, "aliases": ["satellite_azimuth"]}, {"name": "satellite_view", "dtype": "float32", "units": "1", "nodata": -999, "aliases": ["satellite_view"]}, {"name": "solar_azimuth", "dtype": "float32", "units": "1", "nodata": -999, "aliases": ["solar_azimuth"]}, {"name": "solar_zenith", "dtype": "float32", "units": "1", "nodata": -999, "aliases": ["solar_zenith"]}, {"name": "terrain_shadow", "dtype": "uint8", "units": "1", "nodata": 0, "aliases": ["terrain_shadow"]}, {"name": "fmask", "dtype": "uint8", "units": "1", "nodata": 0, "aliases": ["mask", "Fmask"], "flags_definition": {"fmask": {"bits": [0, 1, 2, 3, 4, 5, 6, 7], "values": {"0": "nodata", "1": "valid", "2": "cloud", "3": "shadow", "4": "snow", "5": "water"}, "description": "Fmask"}}}, {"name": "nbar_contiguity", "dtype": "uint8", "units": "1", "nodata": 255, "flags_definition": {"contiguity": {"bits": [0, 1, 2, 3, 4, 5, 6, 7], "values": {"0": "not_contiguous", "1": "contiguous"}, "description": "Pixel contiguity in band stack"}}}, {"name": "nbar_coastal_aerosol", "dtype": "int16", "units": "1", "nodata": -999, "aliases": ["nbar_band_01", "nbar_B01", "nbar_Band1"], "spectral_definition": {"response": [0.006797798, 0.01099643, 0.004208363, 0.006568034, 0.005883123, 0.00713011, 0.004333651, 0.006263537, 0.004393687, 0.00253157, 0.000621707, 0.002117729, 0.003175796, 0.005213085, 0.003387375, 0.00258671, 0.002384167, 0.004595227, 0.012990945, 0.050622293, 0.18872241, 0.459106539, 0.730160597, 0.847259495, 0.871235903, 0.881448354, 0.899392736, 0.918669431, 0.933420754, 0.94596319, 0.95041031, 0.953972339, 0.96903168, 0.999546173, 1, 0.976368067, 0.96404957, 0.95417544, 0.923744832, 0.88548879, 0.809016274, 0.601561144, 0.306766029, 0.108527711, 0.030542088, 0.008935131], "wavelength": [411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456]}}, {"name": "nbar_blue", "dtype": "int16", "units": "1", "nodata": -999, "aliases": ["nbar_band_02", "nbar_B02", "nbar_Band2"], "spectral_definition": {"response": [0.001893306, 0.019440751, 0.020059028, 0.014109631, 0.015612858, 0.015448868, 0.017034152, 0.013311359, 0.014462036, 0.009592091, 0.014500694, 0.011159264, 0.013332524, 0.01355731, 0.01426, 0.014717634, 0.015989541, 0.030654247, 0.055432753, 0.120228972, 0.252260953, 0.462862499, 0.65241169, 0.77750832, 0.824333103, 0.832077099, 0.835037767, 0.838761115, 0.864126031, 0.883293587, 0.90569382, 0.921186621, 0.936616967, 0.931024626, 0.927547539, 0.916622744, 0.9060165, 0.897870416, 0.903146598, 0.908994286, 0.920859439, 0.924523699, 0.918843658, 0.907981319, 0.898032665, 0.88735796, 0.873065866, 0.857761622, 0.846132814, 0.843382711, 0.857924772, 0.879320632, 0.903975503, 0.919580552, 0.946712663, 0.969406608, 0.993636046, 0.999320649, 1, 0.995107621, 0.984163047, 0.979509527, 0.978185449, 0.972278886, 0.96293492, 0.95355824, 0.938134944, 0.924777929, 0.909590075, 0.902313691, 0.892251397, 0.890060534, 0.891851681, 0.899164865, 0.910901434, 0.924636296, 0.938626228, 0.953526854, 0.971831245, 0.987690608, 0.996791216, 0.993851876, 0.9816383, 0.958970396, 0.893259218, 0.736063596, 0.52101528, 0.332578748, 0.195080476, 0.117429222, 0.075138809, 0.050991983, 0.032154822, 0.015134166, 0.004477169], "wavelength": [438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532]}}, {"name": "nbar_green", "dtype": "int16", "units": "1", "nodata": -999, "aliases": ["nbar_band_03", "nbar_B03", "nbar_Band3"], "spectral_definition": {"response": [0.005090312, 0.026897029, 0.12087986, 0.33742273, 0.603624689, 0.810967523, 0.91573833, 0.92605288, 0.92083242, 0.911237119, 0.902005739, 0.897081513, 0.899066029, 0.900672338, 0.902488081, 0.906886173, 0.915610562, 0.927756371, 0.941055569, 0.954196504, 0.966908428, 0.981390028, 0.991619278, 1, 0.999754078, 0.994046577, 0.981792818, 0.968692612, 0.957607907, 0.945644641, 0.92580977, 0.897152993, 0.838534201, 0.698446797, 0.493502787, 0.276900547, 0.107781358, 0.029913795, 0.007336673, 0.000838123], "wavelength": [536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582]}}, {"name": "nbar_red", "dtype": "int16", "units": "1", "nodata": -999, "aliases": ["nbar_band_04", "nbar_B04", "nbar_Band4"], "spectral_definition": {"response": [0.002584, 0.034529, 0.14997, 0.464826, 0.817746, 0.965324, 0.983869, 0.9969, 1.0, 0.995449, 0.991334, 0.977215, 0.936802, 0.873776, 0.814166, 0.776669, 0.764864, 0.775091, 0.801359, 0.830828, 0.857112, 0.883581, 0.90895, 0.934759, 0.955931, 0.96811, 0.973219, 0.971572, 0.969003, 0.965712, 0.960481, 0.944811, 0.884152, 0.706167, 0.422967, 0.189853, 0.063172, 0.020615, 0.002034], "wavelength": [646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 683, 684, 685]}}, {"name": "nbar_red_edge_1", "dtype": "int16", "units": "1", "nodata": -999, "aliases": ["nbar_band_05", "nbar_B05", "nbar_Band5"], "spectral_definition": {"response": [0.010471827, 0.057252544, 0.214724996, 0.547189415, 0.871043978, 0.968446586, 0.99124182, 1, 0.99509331, 0.987602081, 0.979408704, 0.970910946, 0.959528083, 0.94236861, 0.926720132, 0.894557475, 0.767248071, 0.504134435, 0.180610636, 0.034019737, 0.002436944], "wavelength": [694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714]}}, {"name": "nbar_red_edge_2", "dtype": "int16", "units": "1", "nodata": -999, "aliases": ["nbar_band_06", "nbar_B06", "nbar_Band6"], "spectral_definition": {"response": [0.017433807, 0.105812957, 0.386050533, 0.782313159, 0.905953099, 0.916416606, 0.92333441, 0.932013378, 0.947550036, 0.965839591, 0.978552758, 0.991319723, 1, 0.999955845, 0.971267313, 0.81917496, 0.467395748, 0.094120897, 0.009834009], "wavelength": [730, 731, 732, 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748]}}, {"name": "nbar_red_edge_3", "dtype": "int16", "units": "1", "nodata": -999, "aliases": ["nbar_band_07", "nbar_B07", "nbar_Band7"], "spectral_definition": {"response": [0.010282026, 0.037427714, 0.112026989, 0.257953812, 0.478980823, 0.730216783, 0.912510408, 0.971721033, 0.964616097, 0.955734525, 0.964925586, 0.986223289, 1, 0.998046627, 0.98393444, 0.96569621, 0.947277433, 0.927083998, 0.90976539, 0.886948914, 0.859517187, 0.827959173, 0.776383783, 0.671173028, 0.481809979, 0.236251944, 0.069538392, 0.013431956, 0.001257675], "wavelength": [766, 767, 768, 769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784, 785, 786, 787, 788, 789, 790, 791, 792, 793, 794]}}, {"name": "nbar_nir_1", "dtype": "int16", "units": "1", "nodata": -999, "aliases": ["nbar_band_08", "nbar_B08", "nbar_Band8"], "spectral_definition": {"response": [0.000386696, 0.003018401, 0.01669158, 0.028340486, 0.0502885, 0.08626388, 0.149596686, 0.258428566, 0.425108406, 0.631697563, 0.803109115, 0.904984654, 0.939674653, 0.944958731, 0.948238826, 0.963880684, 0.979861632, 0.991635585, 0.996362309, 1, 0.998257939, 0.998488834, 0.989253171, 0.98294089, 0.968189827, 0.958222106, 0.951650369, 0.947054991, 0.944166995, 0.948383123, 0.946461415, 0.942132884, 0.929937199, 0.914683918, 0.893248878, 0.873037871, 0.852648452, 0.836447483, 0.824300756, 0.814333379, 0.810955964, 0.803715941, 0.791980175, 0.783270185, 0.767838865, 0.754167357, 0.742309406, 0.727235815, 0.719323269, 0.713866399, 0.718941021, 0.726527917, 0.738324031, 0.750210769, 0.761800392, 0.769900245, 0.781725199, 0.78381047, 0.783069959, 0.782718588, 0.781644143, 0.780380397, 0.781443024, 0.781701218, 0.78177353, 0.780064535, 0.777591823, 0.770831803, 0.764574958, 0.753876586, 0.743324604, 0.733775698, 0.722497914, 0.712900724, 0.699439134, 0.688575227, 0.674039061, 0.657552716, 0.643729834, 0.62865391, 0.614005803, 0.603233252, 0.594982815, 0.588091928, 0.585186507, 0.582889219, 0.581493721, 0.580137218, 0.574804624, 0.576654614, 0.572399696, 0.570992768, 0.569291451, 0.571025201, 0.570861066, 0.572213154, 0.575418141, 0.577804028, 0.579603586, 0.579294979, 0.578302049, 0.57565598, 0.569721665, 0.561891364, 0.556830745, 0.549385012, 0.545858439, 0.542536249, 0.541895109, 0.539852497, 0.537997281, 0.53195493, 0.522275927, 0.505572421, 0.48804203, 0.469610434, 0.456107021, 0.445848869, 0.443119818, 0.445581498, 0.447532506, 0.440183411, 0.418240241, 0.369455837, 0.301788007, 0.235014942, 0.174244972, 0.122382945, 0.083462794, 0.056162189, 0.038006008, 0.024240249, 0.014845963, 0.006132899], "wavelength": [774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784, 785, 786, 787, 788, 789, 790, 791, 792, 793, 794, 795, 796, 797, 798, 799, 800, 801, 802, 803, 804, 805, 806, 807, 808, 809, 810, 811, 812, 813, 814, 815, 816, 817, 818, 819, 820, 821, 822, 823, 824, 825, 826, 827, 828, 829, 830, 831, 832, 833, 834, 835, 836, 837, 838, 839, 840, 841, 842, 843, 844, 845, 846, 847, 848, 849, 850, 851, 852, 853, 854, 855, 856, 857, 858, 859, 860, 861, 862, 863, 864, 865, 866, 867, 868, 869, 870, 871, 872, 873, 874, 875, 876, 877, 878, 879, 880, 881, 882, 883, 884, 885, 886, 887, 888, 889, 890, 891, 892, 893, 894, 895, 896, 897, 898, 899, 900, 901, 902, 903, 904, 905, 906, 907]}}, {"name": "nbar_nir_2", "dtype": "int16", "units": "1", "nodata": -999, "aliases": ["nbar_band_8A", "nbar_B8A", "nbar_Band8A"], "spectral_definition": {"response": [0.001661751, 0.01602581, 0.032253895, 0.073411273, 0.168937582, 0.345506138, 0.569417239, 0.79634996, 0.937581155, 0.980942645, 0.987241334, 0.994409463, 0.998963959, 0.999788107, 1, 0.994482469, 0.987807181, 0.983157165, 0.979826684, 0.975089851, 0.972818786, 0.966320275, 0.958195153, 0.941870745, 0.894185366, 0.778588669, 0.597362542, 0.377361257, 0.184667876, 0.079045495, 0.033393337, 0.015808546, 0.00162404], "wavelength": [848, 849, 850, 851, 852, 853, 854, 855, 856, 857, 858, 859, 860, 861, 862, 863, 864, 865, 866, 867, 868, 869, 870, 871, 872, 873, 874, 875, 876, 877, 878, 879, 880]}}, {"name": "nbar_swir_2", "dtype": "int16", "units": "1", "nodata": -999, "aliases": ["nbar_band_11", "nbar_B11", "nbar_Band11"], "spectral_definition": {"response": [0.0000115, 0.000026996, 0.000081157, 0.000169507, 0.000273428, 0.000343776, 0.000459515, 0.000651677, 0.0008223, 0.001076746, 0.001428776, 0.001958681, 0.002660821, 0.003682001, 0.005217308, 0.007572684, 0.011246256, 0.01713141, 0.026703068, 0.041388968, 0.062904714, 0.094492263, 0.139743066, 0.200760503, 0.281513117, 0.380879812, 0.490209915, 0.606204368, 0.714558374, 0.80351452, 0.86986655, 0.916284448, 0.946609049, 0.963892644, 0.973065345, 0.977057349, 0.977796293, 0.976890332, 0.975338048, 0.973392995, 0.971480798, 0.969740168, 0.969095034, 0.96969742, 0.970522078, 0.972736269, 0.976138953, 0.978944681, 0.981010782, 0.983513536, 0.984837133, 0.984404132, 0.983920166, 0.983372624, 0.981458796, 0.979391949, 0.978058392, 0.976263051, 0.975392679, 0.9757089, 0.976805245, 0.978986183, 0.981998545, 0.98520893, 0.988659162, 0.992331977, 0.994804634, 0.99589809, 0.995903119, 0.994773417, 0.992101664, 0.988591774, 0.984908418, 0.981101728, 0.976805235, 0.97354566, 0.971948013, 0.97053597, 0.970436371, 0.972382602, 0.975244492, 0.978552743, 0.982971465, 0.98808508, 0.992662671, 0.996435703, 0.99906056, 1, 0.999036445, 0.996642174, 0.993293536, 0.989674029, 0.98579838, 0.982153372, 0.979817194, 0.979473331, 0.980262857, 0.982464858, 0.986000509, 0.989562258, 0.991723341, 0.992201372, 0.98939229, 0.982102331, 0.970157085, 0.953186779, 0.932369062, 0.908001591, 0.884086561, 0.864271526, 0.850889881, 0.844206087, 0.843448232, 0.847024828, 0.848701823, 0.840540222, 0.81352592, 0.756843245, 0.670393147, 0.565754809, 0.457566037, 0.353763564, 0.256912748, 0.176281, 0.115842988, 0.073512768, 0.046527708, 0.02905985, 0.018579999, 0.012463091, 0.00878944, 0.006316358, 0.004582867, 0.003359394, 0.002462997, 0.001990739, 0.001501488, 0.001123371, 0.00078272, 0.000541322, 0.000281204, 0.00013347], "wavelength": [1538, 1539, 1540, 1541, 1542, 1543, 1544, 1545, 1546, 1547, 1548, 1549, 1550, 1551, 1552, 1553, 1554, 1555, 1556, 1557, 1558, 1559, 1560, 1561, 1562, 1563, 1564, 1565, 1566, 1567, 1568, 1569, 1570, 1571, 1572, 1573, 1574, 1575, 1576, 1577, 1578, 1579, 1580, 1581, 1582, 1583, 1584, 1585, 1586, 1587, 1588, 1589, 1590, 1591, 1592, 1593, 1594, 1595, 1596, 1597, 1598, 1599, 1600, 1601, 1602, 1603, 1604, 1605, 1606, 1607, 1608, 1609, 1610, 1611, 1612, 1613, 1614, 1615, 1616, 1617, 1618, 1619, 1620, 1621, 1622, 1623, 1624, 1625, 1626, 1627, 1628, 1629, 1630, 1631, 1632, 1633, 1634, 1635, 1636, 1637, 1638, 1639, 1640, 1641, 1642, 1643, 1644, 1645, 1646, 1647, 1648, 1649, 1650, 1651, 1652, 1653, 1654, 1655, 1656, 1657, 1658, 1659, 1660, 1661, 1662, 1663, 1664, 1665, 1666, 1667, 1668, 1669, 1670, 1671, 1672, 1673, 1674, 1675, 1676, 1677, 1678, 1679]}}, {"name": "nbar_swir_3", "dtype": "int16", "units": "1", "nodata": -999, "aliases": ["nbar_band_12", "nbar_B12", "nbar_Band12"], "spectral_definition": {"response": [0.000227567, 0.000739283, 0.001656775, 0.003019587, 0.004589377, 0.005924935, 0.007534774, 0.008748008, 0.010265481, 0.012236179, 0.014593479, 0.017458937, 0.021063245, 0.025428056, 0.03060944, 0.037234457, 0.045771325, 0.056362502, 0.070016996, 0.088004988, 0.110694417, 0.138884174, 0.173287791, 0.214374591, 0.261990789, 0.317227795, 0.380865706, 0.449470316, 0.522785467, 0.598898522, 0.672128213, 0.737899139, 0.792930708, 0.835658783, 0.866335142, 0.886329697, 0.897588245, 0.901517855, 0.900790721, 0.897113531, 0.892352598, 0.88796428, 0.884432193, 0.882095059, 0.881695748, 0.88269782, 0.887154405, 0.892732955, 0.898903582, 0.905619271, 0.912841006, 0.920179789, 0.926912882, 0.933094888, 0.938438355, 0.943377038, 0.945579227, 0.947407512, 0.948568289, 0.94882972, 0.948111791, 0.947115734, 0.946126982, 0.944870644, 0.943485039, 0.941894052, 0.942445527, 0.943274219, 0.944243794, 0.94528606, 0.946212496, 0.947084905, 0.947941677, 0.948940117, 0.949880321, 0.950676414, 0.951054332, 0.951531833, 0.952326952, 0.952721089, 0.952552047, 0.952417855, 0.952654092, 0.95296197, 0.95331832, 0.953779111, 0.954291677, 0.954837035, 0.955539257, 0.956750259, 0.957986198, 0.959237259, 0.960451396, 0.96141302, 0.96264388, 0.964122014, 0.963609737, 0.963104517, 0.962753979, 0.961850624, 0.960730243, 0.959560745, 0.958377188, 0.956972347, 0.955119849, 0.953076144, 0.95406055, 0.955176712, 0.955719159, 0.955674616, 0.955356546, 0.954611539, 0.953453566, 0.952124922, 0.950597985, 0.948594073, 0.948562399, 0.948548442, 0.94829598, 0.947706109, 0.946620434, 0.94521576, 0.943480979, 0.942137936, 0.940654943, 0.938918576, 0.941493007, 0.943778866, 0.945751584, 0.947277308, 0.948481875, 0.949621704, 0.950767479, 0.951991493, 0.953624457, 0.955262594, 0.952413026, 0.950488752, 0.949721652, 0.949105026, 0.949712169, 0.95167296, 0.955012323, 0.959777857, 0.966208245, 0.973886163, 0.970920044, 0.969139883, 0.968329935, 0.967635904, 0.967555279, 0.968040602, 0.968508397, 0.968956722, 0.969510275, 0.969967732, 0.969097684, 0.968258197, 0.967549788, 0.96650394, 0.965459532, 0.964366923, 0.962929804, 0.961665594, 0.96063821, 0.959368085, 0.959707097, 0.960359643, 0.9616448, 0.962729828, 0.96370081, 0.964773629, 0.965512685, 0.96634935, 0.96753842, 0.96886815, 0.970549249, 0.972426171, 0.974301395, 0.976012041, 0.977203216, 0.978986062, 0.980446263, 0.981524356, 0.982531672, 0.983336508, 0.98463147, 0.986737985, 0.989144288, 0.991223348, 0.99318448, 0.995273324, 0.996704667, 0.998282418, 0.999605161, 1, 0.998654554, 0.995753158, 0.990605371, 0.981520886, 0.968715091, 0.951679125, 0.929343556, 0.902305299, 0.87044084, 0.831947776, 0.786119345, 0.736343248, 0.681862245, 0.623137717, 0.564024643, 0.506650261, 0.451376118, 0.400487569, 0.354176773, 0.309839746, 0.269312679, 0.234102225, 0.20225298, 0.173669677, 0.149356419, 0.128957364, 0.111530972, 0.09689948, 0.084874763, 0.074063524, 0.064469344, 0.056321561, 0.049381236, 0.043196026, 0.037986086, 0.033468826, 0.028983375, 0.025085752, 0.020007676, 0.013837921, 0.008464001, 0.004443102, 0.000848571], "wavelength": [2065, 2066, 2067, 2068, 2069, 2070, 2071, 2072, 2073, 2074, 2075, 2076, 2077, 2078, 2079, 2080, 2081, 2082, 2083, 2084, 2085, 2086, 2087, 2088, 2089, 2090, 2091, 2092, 2093, 2094, 2095, 2096, 2097, 2098, 2099, 2100, 2101, 2102, 2103, 2104, 2105, 2106, 2107, 2108, 2109, 2110, 2111, 2112, 2113, 2114, 2115, 2116, 2117, 2118, 2119, 2120, 2121, 2122, 2123, 2124, 2125, 2126, 2127, 2128, 2129, 2130, 2131, 2132, 2133, 2134, 2135, 2136, 2137, 2138, 2139, 2140, 2141, 2142, 2143, 2144, 2145, 2146, 2147, 2148, 2149, 2150, 2151, 2152, 2153, 2154, 2155, 2156, 2157, 2158, 2159, 2160, 2161, 2162, 2163, 2164, 2165, 2166, 2167, 2168, 2169, 2170, 2171, 2172, 2173, 2174, 2175, 2176, 2177, 2178, 2179, 2180, 2181, 2182, 2183, 2184, 2185, 2186, 2187, 2188, 2189, 2190, 2191, 2192, 2193, 2194, 2195, 2196, 2197, 2198, 2199, 2200, 2201, 2202, 2203, 2204, 2205, 2206, 2207, 2208, 2209, 2210, 2211, 2212, 2213, 2214, 2215, 2216, 2217, 2218, 2219, 2220, 2221, 2222, 2223, 2224, 2225, 2226, 2227, 2228, 2229, 2230, 2231, 2232, 2233, 2234, 2235, 2236, 2237, 2238, 2239, 2240, 2241, 2242, 2243, 2244, 2245, 2246, 2247, 2248, 2249, 2250, 2251, 2252, 2253, 2254, 2255, 2256, 2257, 2258, 2259, 2260, 2261, 2262, 2263, 2264, 2265, 2266, 2267, 2268, 2269, 2270, 2271, 2272, 2273, 2274, 2275, 2276, 2277, 2278, 2279, 2280, 2281, 2282, 2283, 2284, 2285, 2286, 2287, 2288, 2289, 2290, 2291, 2292, 2293, 2294, 2295, 2296, 2297, 2298, 2299, 2300, 2301, 2302, 2303]}}], "metadata_type": "eo_plus"}	2021-01-31 22:18:45.700709+00	africa	\N
64	s2a_nrt_granule	{"format": {"name": "GeoTiff"}, "platform": {"code": "SENTINEL_2A"}, "instrument": {"name": "MSI"}, "product_type": "ard", "processing_level": "Level-2"}	4	{"name": "s2a_nrt_granule", "metadata": {"format": {"name": "GeoTiff"}, "platform": {"code": "SENTINEL_2A"}, "instrument": {"name": "MSI"}, "product_type": "ard", "processing_level": "Level-2"}, "description": "Sentinel-2A MSI ARD NRT - NBAR NBART and Pixel Quality", "measurements": [{"name": "azimuthal_exiting", "dtype": "float32", "units": "1", "nodata": -999, "aliases": ["azimuthal_exiting"]}, {"name": "azimuthal_incident", "dtype": "float32", "units": "1", "nodata": -999, "aliases": ["azimuthal_incident"]}, {"name": "exiting", "dtype": "float32", "units": "1", "nodata": -999, "aliases": ["exiting"]}, {"name": "incident", "dtype": "float32", "units": "1", "nodata": -999, "aliases": ["incident"]}, {"name": "relative_azimuth", "dtype": "float32", "units": "1", "nodata": -999, "aliases": ["relative_azimuth"]}, {"name": "relative_slope", "dtype": "float32", "units": "1", "nodata": -999, "aliases": ["relative_slope"]}, {"name": "satellite_azimuth", "dtype": "float32", "units": "1", "nodata": -999, "aliases": ["satellite_azimuth"]}, {"name": "satellite_view", "dtype": "float32", "units": "1", "nodata": -999, "aliases": ["satellite_view"]}, {"name": "solar_azimuth", "dtype": "float32", "units": "1", "nodata": -999, "aliases": ["solar_azimuth"]}, {"name": "solar_zenith", "dtype": "float32", "units": "1", "nodata": -999, "aliases": ["solar_zenith"]}, {"name": "terrain_shadow", "dtype": "uint8", "units": "1", "nodata": 0, "aliases": ["terrain_shadow"]}, {"name": "fmask", "dtype": "uint8", "units": "1", "nodata": 0, "aliases": ["mask", "Fmask"], "flags_definition": {"fmask": {"bits": [0, 1, 2, 3, 4, 5, 6, 7], "values": {"0": "nodata", "1": "valid", "2": "cloud", "3": "shadow", "4": "snow", "5": "water"}, "description": "Fmask"}}}, {"name": "nbar_contiguity", "dtype": "uint8", "units": "1", "nodata": 255, "flags_definition": {"contiguity": {"bits": [0, 1, 2, 3, 4, 5, 6, 7], "values": {"0": "not_contiguous", "1": "contiguous"}, "description": "Pixel contiguity in band stack"}}}, {"name": "nbar_coastal_aerosol", "dtype": "int16", "units": "1", "nodata": -999, "aliases": ["nbar_band_01", "nbar_B01", "nbar_Band1"], "spectral_definition": {"response": [0.015297, 0.067133, 0.19593, 0.357242, 0.460571, 0.511598, 0.551051, 0.587385, 0.613478, 0.650014, 0.699199, 0.74543, 0.792047, 0.862824, 0.947307, 0.993878, 1.0, 0.990178, 0.972897, 0.957042, 0.956726, 0.922389, 0.723933, 0.388302, 0.14596, 0.051814, 0.017459, 0.000303], "wavelength": [430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457]}}, {"name": "nbar_blue", "dtype": "int16", "units": "1", "nodata": -999, "aliases": ["nbar_band_02", "nbar_B02", "nbar_Band2"], "spectral_definition": {"response": [0.001206, 0.00204, 0.002623, 0.002738, 0.002746, 0.002076, 0.003246, 0.002224, 0.002789, 0.003127, 0.002377, 0.003776, 0.002856, 0.003063, 0.00607, 0.009028, 0.019547, 0.038955, 0.084088, 0.176255, 0.292197, 0.364612, 0.382418, 0.385789, 0.393447, 0.400158, 0.410291, 0.424686, 0.449286, 0.481594, 0.505323, 0.523406, 0.529543, 0.534688, 0.533786, 0.534656, 0.5381, 0.543691, 0.557717, 0.578585, 0.601967, 0.616037, 0.621092, 0.613597, 0.596062, 0.575863, 0.558063, 0.546131, 0.542099, 0.553602, 0.571684, 0.598269, 0.633236, 0.67337, 0.711752, 0.738396, 0.758249, 0.768325, 0.773367, 0.780468, 0.788363, 0.795449, 0.809151, 0.824011, 0.837709, 0.844983, 0.847328, 0.840111, 0.825797, 0.804778, 0.78694, 0.771578, 0.761923, 0.765487, 0.781682, 0.810031, 0.850586, 0.901671, 0.95467, 0.987257, 1.0, 0.986389, 0.908308, 0.724, 0.478913, 0.286992, 0.169976, 0.102833, 0.065163, 0.04116, 0.02508, 0.013112, 0.002585, 0.001095, 0.000308, 0.000441, 0.0, 0.0, 0.000443], "wavelength": [440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538]}}, {"name": "nbar_green", "dtype": "int16", "units": "1", "nodata": -999, "aliases": ["nbar_band_03", "nbar_B03", "nbar_Band3"], "spectral_definition": {"response": [0.00084, 0.016372, 0.037688, 0.080665, 0.169509, 0.341374, 0.573031, 0.746711, 0.828036, 0.868228, 0.888565, 0.891572, 0.87815, 0.860271, 0.843698, 0.834035, 0.832617, 0.844968, 0.867734, 0.897361, 0.933938, 0.966923, 0.990762, 1.0, 0.997812, 0.981107, 0.947088, 0.907183, 0.868656, 0.837622, 0.81291, 0.792434, 0.7851, 0.789606, 0.807011, 0.830458, 0.846433, 0.858402, 0.85799, 0.799824, 0.62498, 0.386994, 0.200179, 0.098293, 0.042844, 0.016512], "wavelength": [537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582]}}, {"name": "nbar_red", "dtype": "int16", "units": "1", "nodata": -999, "aliases": ["nbar_band_04", "nbar_B04", "nbar_Band4"], "spectral_definition": {"response": [0.002584, 0.034529, 0.14997, 0.464826, 0.817746, 0.965324, 0.983869, 0.9969, 1.0, 0.995449, 0.991334, 0.977215, 0.936802, 0.873776, 0.814166, 0.776669, 0.764864, 0.775091, 0.801359, 0.830828, 0.857112, 0.883581, 0.90895, 0.934759, 0.955931, 0.96811, 0.973219, 0.971572, 0.969003, 0.965712, 0.960481, 0.944811, 0.884152, 0.706167, 0.422967, 0.189853, 0.063172, 0.020615, 0.002034], "wavelength": [646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 683, 684]}}, {"name": "nbar_red_edge_1", "dtype": "int16", "units": "1", "nodata": -999, "aliases": ["nbar_band_05", "nbar_B05", "nbar_Band5"], "spectral_definition": {"response": [0.001187, 0.04126, 0.167712, 0.478496, 0.833878, 0.985479, 1.0, 0.999265, 0.993239, 0.982416, 0.965583, 0.945953, 0.924699, 0.902399, 0.885582, 0.861231, 0.757197, 0.521268, 0.196706, 0.036825], "wavelength": [694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713]}}, {"name": "nbar_red_edge_2", "dtype": "int16", "units": "1", "nodata": -999, "aliases": ["nbar_band_06", "nbar_B06", "nbar_Band6"], "spectral_definition": {"response": [0.005331, 0.085006, 0.345714, 0.750598, 0.920265, 0.917917, 0.934211, 0.957861, 0.975829, 0.981932, 0.981518, 0.993406, 1.0, 0.982579, 0.962584, 0.854908, 0.506722, 0.135357, 0.013438], "wavelength": [731, 732, 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748, 749]}}, {"name": "nbar_red_edge_3", "dtype": "int16", "units": "1", "nodata": -999, "aliases": ["nbar_band_07", "nbar_B07", "nbar_Band7"], "spectral_definition": {"response": [0.001595, 0.014731, 0.067032, 0.199495, 0.422803, 0.694015, 0.898494, 0.983173, 0.994759, 1.0, 0.994913, 0.964657, 0.908117, 0.846898, 0.802091, 0.778839, 0.777241, 0.789523, 0.800984, 0.802916, 0.791711, 0.757695, 0.677951, 0.536855, 0.364033, 0.193498, 0.077219, 0.019707, 0.003152], "wavelength": [769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784, 785, 786, 787, 788, 789, 790, 791, 792, 793, 794, 795, 796, 797]}}, {"name": "nbar_nir_1", "dtype": "int16", "units": "1", "nodata": -999, "aliases": ["nbar_band_08", "nbar_B08", "nbar_Band8"], "spectral_definition": {"response": [0.000451, 0.007614, 0.019072, 0.033498, 0.056536, 0.087148, 0.13246, 0.203436, 0.314068, 0.450085, 0.587433, 0.714518, 0.81829, 0.902932, 0.960732, 0.993723, 1.0, 0.985213, 0.958376, 0.93655, 0.925816, 0.930376, 0.941281, 0.953344, 0.962183, 0.965631, 0.963105, 0.959009, 0.951205, 0.945147, 0.943136, 0.945814, 0.945357, 0.943762, 0.937084, 0.92789, 0.915897, 0.900979, 0.881577, 0.86216, 0.8432, 0.822684, 0.801819, 0.776911, 0.755632, 0.737893, 0.722217, 0.708669, 0.698416, 0.690211, 0.682257, 0.681494, 0.682649, 0.678491, 0.67595, 0.671304, 0.665538, 0.660812, 0.658739, 0.65831, 0.66407, 0.672731, 0.685501, 0.701159, 0.720686, 0.742292, 0.75953, 0.776608, 0.784061, 0.78772, 0.787693, 0.783525, 0.776161, 0.768339, 0.759264, 0.745943, 0.733022, 0.720589, 0.706663, 0.69087, 0.675896, 0.661558, 0.649339, 0.638008, 0.627424, 0.618963, 0.610945, 0.604322, 0.597408, 0.591724, 0.586961, 0.582746, 0.581202, 0.57948, 0.580197, 0.582505, 0.585308, 0.589481, 0.592827, 0.596749, 0.601372, 0.603234, 0.605476, 0.608972, 0.613463, 0.618715, 0.626841, 0.637436, 0.648791, 0.659233, 0.66734, 0.668624, 0.659924, 0.641666, 0.615841, 0.583567, 0.552076, 0.526407, 0.507116, 0.49653, 0.499119, 0.512088, 0.529093, 0.542739, 0.537964, 0.495953, 0.419305, 0.326791, 0.231085, 0.14854, 0.089683, 0.054977, 0.033246, 0.019774, 0.007848, 0.001286], "wavelength": [773, 774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784, 785, 786, 787, 788, 789, 790, 791, 792, 793, 794, 795, 796, 797, 798, 799, 800, 801, 802, 803, 804, 805, 806, 807, 808, 809, 810, 811, 812, 813, 814, 815, 816, 817, 818, 819, 820, 821, 822, 823, 824, 825, 826, 827, 828, 829, 830, 831, 832, 833, 834, 835, 836, 837, 838, 839, 840, 841, 842, 843, 844, 845, 846, 847, 848, 849, 850, 851, 852, 853, 854, 855, 856, 857, 858, 859, 860, 861, 862, 863, 864, 865, 866, 867, 868, 869, 870, 871, 872, 873, 874, 875, 876, 877, 878, 879, 880, 881, 882, 883, 884, 885, 886, 887, 888, 889, 890, 891, 892, 893, 894, 895, 896, 897, 898, 899, 900, 901, 902, 903, 904, 905, 906, 907, 908]}}, {"name": "nbar_nir_2", "dtype": "int16", "units": "1", "nodata": -999, "aliases": ["nbar_band_8A", "nbar_B8A", "nbar_Band8A"], "spectral_definition": {"response": [0.001651, 0.013242, 0.02471, 0.051379, 0.104944, 0.216577, 0.384865, 0.585731, 0.774481, 0.87843, 0.914944, 0.922574, 0.926043, 0.929676, 0.935962, 0.946583, 0.955792, 0.965458, 0.974461, 0.97988, 0.983325, 0.982881, 0.988474, 1.0, 0.999626, 0.921005, 0.728632, 0.472189, 0.238082, 0.106955, 0.046096, 0.022226, 0.008819, 0.000455], "wavelength": [848, 849, 850, 851, 852, 853, 854, 855, 856, 857, 858, 859, 860, 861, 862, 863, 864, 865, 866, 867, 868, 869, 870, 871, 872, 873, 874, 875, 876, 877, 878, 879, 880, 881]}}, {"name": "nbar_swir_2", "dtype": "int16", "units": "1", "nodata": -999, "aliases": ["nbar_band_11", "nbar_B11", "nbar_Band11"], "spectral_definition": {"response": [0.000007, 0.000007, 0.000008, 0.000028, 0.000038, 0.000091, 0.000147, 0.000251, 0.00048, 0.00057, 0.000662, 0.000911, 0.001166, 0.001684, 0.002458, 0.003567, 0.005345, 0.008318, 0.012628, 0.018996, 0.027781, 0.039584, 0.054865, 0.07493, 0.10107, 0.135476, 0.182597, 0.247276, 0.330736, 0.429691, 0.537634, 0.647173, 0.743528, 0.815215, 0.859202, 0.879669, 0.88703, 0.889098, 0.891417, 0.897586, 0.906631, 0.916528, 0.926579, 0.935322, 0.942394, 0.947507, 0.951416, 0.954254, 0.956429, 0.958205, 0.960688, 0.96348, 0.965797, 0.96818, 0.971012, 0.97338, 0.975915, 0.978581, 0.979878, 0.980589, 0.980912, 0.981412, 0.981244, 0.980705, 0.980377, 0.981066, 0.982736, 0.985122, 0.987807, 0.990376, 0.992016, 0.993288, 0.992536, 0.990405, 0.987128, 0.983502, 0.980023, 0.976174, 0.972568, 0.969828, 0.967709, 0.966371, 0.965849, 0.96605, 0.967427, 0.96987, 0.973463, 0.978683, 0.983472, 0.987635, 0.991875, 0.995476, 0.997586, 0.998568, 0.999328, 0.999234, 0.998804, 0.999111, 0.99973, 0.999745, 1.0, 0.999814, 0.996693, 0.99162, 0.985702, 0.978569, 0.969903, 0.960896, 0.953287, 0.946546, 0.941712, 0.938586, 0.935489, 0.928114, 0.912102, 0.880598, 0.82498, 0.743118, 0.641891, 0.534002, 0.426963, 0.32371, 0.234284, 0.163972, 0.110211, 0.072478, 0.046194, 0.029401, 0.019359, 0.013308, 0.009317, 0.006523, 0.004864, 0.003409, 0.002491, 0.001958, 0.001423, 0.001055, 0.000498, 0.000228, 0.000159, 0.000034, 0.000045, 0.000013], "wavelength": [1539, 1540, 1541, 1542, 1543, 1544, 1545, 1546, 1547, 1548, 1549, 1550, 1551, 1552, 1553, 1554, 1555, 1556, 1557, 1558, 1559, 1560, 1561, 1562, 1563, 1564, 1565, 1566, 1567, 1568, 1569, 1570, 1571, 1572, 1573, 1574, 1575, 1576, 1577, 1578, 1579, 1580, 1581, 1582, 1583, 1584, 1585, 1586, 1587, 1588, 1589, 1590, 1591, 1592, 1593, 1594, 1595, 1596, 1597, 1598, 1599, 1600, 1601, 1602, 1603, 1604, 1605, 1606, 1607, 1608, 1609, 1610, 1611, 1612, 1613, 1614, 1615, 1616, 1617, 1618, 1619, 1620, 1621, 1622, 1623, 1624, 1625, 1626, 1627, 1628, 1629, 1630, 1631, 1632, 1633, 1634, 1635, 1636, 1637, 1638, 1639, 1640, 1641, 1642, 1643, 1644, 1645, 1646, 1647, 1648, 1649, 1650, 1651, 1652, 1653, 1654, 1655, 1656, 1657, 1658, 1659, 1660, 1661, 1662, 1663, 1664, 1665, 1666, 1667, 1668, 1669, 1670, 1671, 1672, 1673, 1674, 1675, 1676, 1677, 1678, 1679, 1680, 1681, 1682]}}, {"name": "nbar_swir_3", "dtype": "int16", "units": "1", "nodata": -999, "aliases": ["nbar_band_12", "nbar_B12", "nbar_Band12"], "spectral_definition": {"response": [0.000639, 0.001023, 0.002885, 0.003997, 0.006597, 0.00766, 0.008004, 0.00854, 0.0093, 0.010002, 0.010972, 0.012089, 0.013364, 0.015017, 0.017126, 0.01978, 0.023336, 0.027668, 0.033216, 0.040217, 0.048883, 0.059642, 0.073175, 0.090535, 0.11147, 0.136903, 0.167811, 0.203461, 0.242871, 0.284898, 0.327178, 0.368404, 0.408003, 0.444778, 0.476537, 0.503107, 0.525318, 0.543352, 0.557253, 0.568634, 0.57903, 0.588684, 0.598891, 0.609981, 0.621362, 0.634283, 0.648546, 0.663707, 0.680046, 0.696165, 0.711964, 0.727011, 0.741301, 0.757405, 0.772071, 0.785581, 0.798238, 0.809677, 0.819702, 0.828599, 0.836722, 0.844443, 0.851107, 0.853252, 0.854746, 0.856174, 0.857821, 0.859532, 0.86146, 0.863257, 0.865139, 0.867319, 0.869696, 0.874302, 0.878588, 0.882439, 0.885929, 0.889473, 0.893226, 0.896696, 0.899897, 0.902596, 0.904831, 0.905525, 0.905665, 0.905503, 0.905158, 0.904783, 0.904082, 0.903347, 0.902761, 0.902377, 0.901983, 0.903424, 0.904313, 0.905315, 0.906446, 0.908092, 0.910123, 0.91295, 0.915585, 0.918444, 0.921302, 0.924337, 0.927219, 0.92974, 0.931922, 0.934142, 0.935906, 0.937086, 0.937641, 0.938301, 0.937652, 0.940441, 0.942518, 0.943259, 0.943031, 0.942117, 0.940632, 0.938428, 0.93666, 0.935256, 0.933022, 0.92688, 0.921057, 0.915483, 0.91102, 0.908293, 0.907283, 0.908191, 0.911169, 0.916189, 0.922855, 0.920605, 0.919482, 0.919489, 0.921276, 0.924526, 0.927733, 0.931974, 0.93677, 0.941483, 0.946802, 0.951203, 0.954437, 0.957047, 0.959729, 0.962539, 0.964858, 0.966042, 0.966647, 0.96631, 0.96546, 0.964841, 0.963656, 0.961698, 0.959454, 0.957327, 0.95514, 0.953558, 0.952732, 0.952181, 0.951731, 0.952146, 0.952641, 0.954057, 0.957078, 0.960639, 0.964222, 0.968307, 0.972691, 0.977423, 0.982898, 0.987144, 0.990734, 0.993983, 0.996787, 0.998753, 1.0, 0.999927, 0.999152, 0.997129, 0.993884, 0.989686, 0.983735, 0.976213, 0.967813, 0.958343, 0.94844, 0.938203, 0.927725, 0.917039, 0.905999, 0.893868, 0.881683, 0.868647, 0.854635, 0.84062, 0.826016, 0.809516, 0.791867, 0.772443, 0.749107, 0.720346, 0.688185, 0.651283, 0.61005, 0.566031, 0.52097, 0.474659, 0.429259, 0.385857, 0.342092, 0.30068, 0.263176, 0.227704, 0.195721, 0.16809, 0.14468, 0.124831, 0.108237, 0.094401, 0.082363, 0.0715, 0.062691, 0.054985, 0.048195, 0.042864, 0.038598, 0.034947, 0.031999, 0.029588, 0.027418, 0.025577, 0.023959, 0.021672, 0.019148, 0.016331, 0.010989, 0.007379, 0.006511, 0.00471, 0.002065], "wavelength": [2078, 2079, 2080, 2081, 2082, 2083, 2084, 2085, 2086, 2087, 2088, 2089, 2090, 2091, 2092, 2093, 2094, 2095, 2096, 2097, 2098, 2099, 2100, 2101, 2102, 2103, 2104, 2105, 2106, 2107, 2108, 2109, 2110, 2111, 2112, 2113, 2114, 2115, 2116, 2117, 2118, 2119, 2120, 2121, 2122, 2123, 2124, 2125, 2126, 2127, 2128, 2129, 2130, 2131, 2132, 2133, 2134, 2135, 2136, 2137, 2138, 2139, 2140, 2141, 2142, 2143, 2144, 2145, 2146, 2147, 2148, 2149, 2150, 2151, 2152, 2153, 2154, 2155, 2156, 2157, 2158, 2159, 2160, 2161, 2162, 2163, 2164, 2165, 2166, 2167, 2168, 2169, 2170, 2171, 2172, 2173, 2174, 2175, 2176, 2177, 2178, 2179, 2180, 2181, 2182, 2183, 2184, 2185, 2186, 2187, 2188, 2189, 2190, 2191, 2192, 2193, 2194, 2195, 2196, 2197, 2198, 2199, 2200, 2201, 2202, 2203, 2204, 2205, 2206, 2207, 2208, 2209, 2210, 2211, 2212, 2213, 2214, 2215, 2216, 2217, 2218, 2219, 2220, 2221, 2222, 2223, 2224, 2225, 2226, 2227, 2228, 2229, 2230, 2231, 2232, 2233, 2234, 2235, 2236, 2237, 2238, 2239, 2240, 2241, 2242, 2243, 2244, 2245, 2246, 2247, 2248, 2249, 2250, 2251, 2252, 2253, 2254, 2255, 2256, 2257, 2258, 2259, 2260, 2261, 2262, 2263, 2264, 2265, 2266, 2267, 2268, 2269, 2270, 2271, 2272, 2273, 2274, 2275, 2276, 2277, 2278, 2279, 2280, 2281, 2282, 2283, 2284, 2285, 2286, 2287, 2288, 2289, 2290, 2291, 2292, 2293, 2294, 2295, 2296, 2297, 2298, 2299, 2300, 2301, 2302, 2303, 2304, 2305, 2306, 2307, 2308, 2309, 2310, 2311, 2312, 2313, 2314, 2315, 2316, 2317, 2318, 2319, 2320]}}, {"name": "nbart_contiguity", "dtype": "uint8", "units": "1", "nodata": 255, "flags_definition": {"contiguity": {"bits": [0, 1, 2, 3, 4, 5, 6, 7], "values": {"0": "not_contiguous", "1": "contiguous"}, "description": "Pixel contiguity in band stack"}}}, {"name": "nbart_coastal_aerosol", "dtype": "int16", "units": "1", "nodata": -999, "aliases": ["nbart_band_01", "nbart_B01", "nbart_Band1"], "spectral_definition": {"response": [0.015297, 0.067133, 0.19593, 0.357242, 0.460571, 0.511598, 0.551051, 0.587385, 0.613478, 0.650014, 0.699199, 0.74543, 0.792047, 0.862824, 0.947307, 0.993878, 1.0, 0.990178, 0.972897, 0.957042, 0.956726, 0.922389, 0.723933, 0.388302, 0.14596, 0.051814, 0.017459, 0.000303], "wavelength": [430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457]}}, {"name": "nbart_blue", "dtype": "int16", "units": "1", "nodata": -999, "aliases": ["nbart_band_02", "nbart_B02", "nbart_Band2"], "spectral_definition": {"response": [0.001206, 0.00204, 0.002623, 0.002738, 0.002746, 0.002076, 0.003246, 0.002224, 0.002789, 0.003127, 0.002377, 0.003776, 0.002856, 0.003063, 0.00607, 0.009028, 0.019547, 0.038955, 0.084088, 0.176255, 0.292197, 0.364612, 0.382418, 0.385789, 0.393447, 0.400158, 0.410291, 0.424686, 0.449286, 0.481594, 0.505323, 0.523406, 0.529543, 0.534688, 0.533786, 0.534656, 0.5381, 0.543691, 0.557717, 0.578585, 0.601967, 0.616037, 0.621092, 0.613597, 0.596062, 0.575863, 0.558063, 0.546131, 0.542099, 0.553602, 0.571684, 0.598269, 0.633236, 0.67337, 0.711752, 0.738396, 0.758249, 0.768325, 0.773367, 0.780468, 0.788363, 0.795449, 0.809151, 0.824011, 0.837709, 0.844983, 0.847328, 0.840111, 0.825797, 0.804778, 0.78694, 0.771578, 0.761923, 0.765487, 0.781682, 0.810031, 0.850586, 0.901671, 0.95467, 0.987257, 1.0, 0.986389, 0.908308, 0.724, 0.478913, 0.286992, 0.169976, 0.102833, 0.065163, 0.04116, 0.02508, 0.013112, 0.002585, 0.001095, 0.000308, 0.000441, 0.0, 0.0, 0.000443], "wavelength": [440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538]}}, {"name": "nbart_green", "dtype": "int16", "units": "1", "nodata": -999, "aliases": ["nbart_band_03", "nbart_B03", "nbart_Band3"], "spectral_definition": {"response": [0.00084, 0.016372, 0.037688, 0.080665, 0.169509, 0.341374, 0.573031, 0.746711, 0.828036, 0.868228, 0.888565, 0.891572, 0.87815, 0.860271, 0.843698, 0.834035, 0.832617, 0.844968, 0.867734, 0.897361, 0.933938, 0.966923, 0.990762, 1.0, 0.997812, 0.981107, 0.947088, 0.907183, 0.868656, 0.837622, 0.81291, 0.792434, 0.7851, 0.789606, 0.807011, 0.830458, 0.846433, 0.858402, 0.85799, 0.799824, 0.62498, 0.386994, 0.200179, 0.098293, 0.042844, 0.016512], "wavelength": [537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582]}}, {"name": "nbart_red", "dtype": "int16", "units": "1", "nodata": -999, "aliases": ["nbart_band_04", "nbart_B04", "nbart_Band4"], "spectral_definition": {"response": [0.002584, 0.034529, 0.14997, 0.464826, 0.817746, 0.965324, 0.983869, 0.9969, 1.0, 0.995449, 0.991334, 0.977215, 0.936802, 0.873776, 0.814166, 0.776669, 0.764864, 0.775091, 0.801359, 0.830828, 0.857112, 0.883581, 0.90895, 0.934759, 0.955931, 0.96811, 0.973219, 0.971572, 0.969003, 0.965712, 0.960481, 0.944811, 0.884152, 0.706167, 0.422967, 0.189853, 0.063172, 0.020615, 0.002034], "wavelength": [646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 683, 684]}}, {"name": "nbart_red_edge_1", "dtype": "int16", "units": "1", "nodata": -999, "aliases": ["nbart_band_05", "nbart_B05", "nbart_Band5"], "spectral_definition": {"response": [0.001187, 0.04126, 0.167712, 0.478496, 0.833878, 0.985479, 1.0, 0.999265, 0.993239, 0.982416, 0.965583, 0.945953, 0.924699, 0.902399, 0.885582, 0.861231, 0.757197, 0.521268, 0.196706, 0.036825], "wavelength": [694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713]}}, {"name": "nbart_red_edge_2", "dtype": "int16", "units": "1", "nodata": -999, "aliases": ["nbart_band_06", "nbart_B06", "nbart_Band6"], "spectral_definition": {"response": [0.005331, 0.085006, 0.345714, 0.750598, 0.920265, 0.917917, 0.934211, 0.957861, 0.975829, 0.981932, 0.981518, 0.993406, 1.0, 0.982579, 0.962584, 0.854908, 0.506722, 0.135357, 0.013438], "wavelength": [731, 732, 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748, 749]}}, {"name": "nbart_red_edge_3", "dtype": "int16", "units": "1", "nodata": -999, "aliases": ["nbart_band_07", "nbart_B07", "nbart_Band7"], "spectral_definition": {"response": [0.001595, 0.014731, 0.067032, 0.199495, 0.422803, 0.694015, 0.898494, 0.983173, 0.994759, 1.0, 0.994913, 0.964657, 0.908117, 0.846898, 0.802091, 0.778839, 0.777241, 0.789523, 0.800984, 0.802916, 0.791711, 0.757695, 0.677951, 0.536855, 0.364033, 0.193498, 0.077219, 0.019707, 0.003152], "wavelength": [769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784, 785, 786, 787, 788, 789, 790, 791, 792, 793, 794, 795, 796, 797]}}, {"name": "nbart_nir_1", "dtype": "int16", "units": "1", "nodata": -999, "aliases": ["nbart_band_08", "nbart_B08", "nbart_Band8"], "spectral_definition": {"response": [0.000451, 0.007614, 0.019072, 0.033498, 0.056536, 0.087148, 0.13246, 0.203436, 0.314068, 0.450085, 0.587433, 0.714518, 0.81829, 0.902932, 0.960732, 0.993723, 1.0, 0.985213, 0.958376, 0.93655, 0.925816, 0.930376, 0.941281, 0.953344, 0.962183, 0.965631, 0.963105, 0.959009, 0.951205, 0.945147, 0.943136, 0.945814, 0.945357, 0.943762, 0.937084, 0.92789, 0.915897, 0.900979, 0.881577, 0.86216, 0.8432, 0.822684, 0.801819, 0.776911, 0.755632, 0.737893, 0.722217, 0.708669, 0.698416, 0.690211, 0.682257, 0.681494, 0.682649, 0.678491, 0.67595, 0.671304, 0.665538, 0.660812, 0.658739, 0.65831, 0.66407, 0.672731, 0.685501, 0.701159, 0.720686, 0.742292, 0.75953, 0.776608, 0.784061, 0.78772, 0.787693, 0.783525, 0.776161, 0.768339, 0.759264, 0.745943, 0.733022, 0.720589, 0.706663, 0.69087, 0.675896, 0.661558, 0.649339, 0.638008, 0.627424, 0.618963, 0.610945, 0.604322, 0.597408, 0.591724, 0.586961, 0.582746, 0.581202, 0.57948, 0.580197, 0.582505, 0.585308, 0.589481, 0.592827, 0.596749, 0.601372, 0.603234, 0.605476, 0.608972, 0.613463, 0.618715, 0.626841, 0.637436, 0.648791, 0.659233, 0.66734, 0.668624, 0.659924, 0.641666, 0.615841, 0.583567, 0.552076, 0.526407, 0.507116, 0.49653, 0.499119, 0.512088, 0.529093, 0.542739, 0.537964, 0.495953, 0.419305, 0.326791, 0.231085, 0.14854, 0.089683, 0.054977, 0.033246, 0.019774, 0.007848, 0.001286], "wavelength": [773, 774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784, 785, 786, 787, 788, 789, 790, 791, 792, 793, 794, 795, 796, 797, 798, 799, 800, 801, 802, 803, 804, 805, 806, 807, 808, 809, 810, 811, 812, 813, 814, 815, 816, 817, 818, 819, 820, 821, 822, 823, 824, 825, 826, 827, 828, 829, 830, 831, 832, 833, 834, 835, 836, 837, 838, 839, 840, 841, 842, 843, 844, 845, 846, 847, 848, 849, 850, 851, 852, 853, 854, 855, 856, 857, 858, 859, 860, 861, 862, 863, 864, 865, 866, 867, 868, 869, 870, 871, 872, 873, 874, 875, 876, 877, 878, 879, 880, 881, 882, 883, 884, 885, 886, 887, 888, 889, 890, 891, 892, 893, 894, 895, 896, 897, 898, 899, 900, 901, 902, 903, 904, 905, 906, 907, 908]}}, {"name": "nbart_nir_2", "dtype": "int16", "units": "1", "nodata": -999, "aliases": ["nbart_band_8A", "nbart_B8A", "nbart_Band8A"], "spectral_definition": {"response": [0.001651, 0.013242, 0.02471, 0.051379, 0.104944, 0.216577, 0.384865, 0.585731, 0.774481, 0.87843, 0.914944, 0.922574, 0.926043, 0.929676, 0.935962, 0.946583, 0.955792, 0.965458, 0.974461, 0.97988, 0.983325, 0.982881, 0.988474, 1.0, 0.999626, 0.921005, 0.728632, 0.472189, 0.238082, 0.106955, 0.046096, 0.022226, 0.008819, 0.000455], "wavelength": [848, 849, 850, 851, 852, 853, 854, 855, 856, 857, 858, 859, 860, 861, 862, 863, 864, 865, 866, 867, 868, 869, 870, 871, 872, 873, 874, 875, 876, 877, 878, 879, 880, 881]}}, {"name": "nbart_swir_2", "dtype": "int16", "units": "1", "nodata": -999, "aliases": ["nbart_band_11", "nbart_B11", "nbart_Band11"], "spectral_definition": {"response": [0.000007, 0.000007, 0.000008, 0.000028, 0.000038, 0.000091, 0.000147, 0.000251, 0.00048, 0.00057, 0.000662, 0.000911, 0.001166, 0.001684, 0.002458, 0.003567, 0.005345, 0.008318, 0.012628, 0.018996, 0.027781, 0.039584, 0.054865, 0.07493, 0.10107, 0.135476, 0.182597, 0.247276, 0.330736, 0.429691, 0.537634, 0.647173, 0.743528, 0.815215, 0.859202, 0.879669, 0.88703, 0.889098, 0.891417, 0.897586, 0.906631, 0.916528, 0.926579, 0.935322, 0.942394, 0.947507, 0.951416, 0.954254, 0.956429, 0.958205, 0.960688, 0.96348, 0.965797, 0.96818, 0.971012, 0.97338, 0.975915, 0.978581, 0.979878, 0.980589, 0.980912, 0.981412, 0.981244, 0.980705, 0.980377, 0.981066, 0.982736, 0.985122, 0.987807, 0.990376, 0.992016, 0.993288, 0.992536, 0.990405, 0.987128, 0.983502, 0.980023, 0.976174, 0.972568, 0.969828, 0.967709, 0.966371, 0.965849, 0.96605, 0.967427, 0.96987, 0.973463, 0.978683, 0.983472, 0.987635, 0.991875, 0.995476, 0.997586, 0.998568, 0.999328, 0.999234, 0.998804, 0.999111, 0.99973, 0.999745, 1.0, 0.999814, 0.996693, 0.99162, 0.985702, 0.978569, 0.969903, 0.960896, 0.953287, 0.946546, 0.941712, 0.938586, 0.935489, 0.928114, 0.912102, 0.880598, 0.82498, 0.743118, 0.641891, 0.534002, 0.426963, 0.32371, 0.234284, 0.163972, 0.110211, 0.072478, 0.046194, 0.029401, 0.019359, 0.013308, 0.009317, 0.006523, 0.004864, 0.003409, 0.002491, 0.001958, 0.001423, 0.001055, 0.000498, 0.000228, 0.000159, 0.000034, 0.000045, 0.000013], "wavelength": [1539, 1540, 1541, 1542, 1543, 1544, 1545, 1546, 1547, 1548, 1549, 1550, 1551, 1552, 1553, 1554, 1555, 1556, 1557, 1558, 1559, 1560, 1561, 1562, 1563, 1564, 1565, 1566, 1567, 1568, 1569, 1570, 1571, 1572, 1573, 1574, 1575, 1576, 1577, 1578, 1579, 1580, 1581, 1582, 1583, 1584, 1585, 1586, 1587, 1588, 1589, 1590, 1591, 1592, 1593, 1594, 1595, 1596, 1597, 1598, 1599, 1600, 1601, 1602, 1603, 1604, 1605, 1606, 1607, 1608, 1609, 1610, 1611, 1612, 1613, 1614, 1615, 1616, 1617, 1618, 1619, 1620, 1621, 1622, 1623, 1624, 1625, 1626, 1627, 1628, 1629, 1630, 1631, 1632, 1633, 1634, 1635, 1636, 1637, 1638, 1639, 1640, 1641, 1642, 1643, 1644, 1645, 1646, 1647, 1648, 1649, 1650, 1651, 1652, 1653, 1654, 1655, 1656, 1657, 1658, 1659, 1660, 1661, 1662, 1663, 1664, 1665, 1666, 1667, 1668, 1669, 1670, 1671, 1672, 1673, 1674, 1675, 1676, 1677, 1678, 1679, 1680, 1681, 1682]}}, {"name": "nbart_swir_3", "dtype": "int16", "units": "1", "nodata": -999, "aliases": ["nbart_band_12", "nbart_B12", "nbart_Band12"], "spectral_definition": {"response": [0.000639, 0.001023, 0.002885, 0.003997, 0.006597, 0.00766, 0.008004, 0.00854, 0.0093, 0.010002, 0.010972, 0.012089, 0.013364, 0.015017, 0.017126, 0.01978, 0.023336, 0.027668, 0.033216, 0.040217, 0.048883, 0.059642, 0.073175, 0.090535, 0.11147, 0.136903, 0.167811, 0.203461, 0.242871, 0.284898, 0.327178, 0.368404, 0.408003, 0.444778, 0.476537, 0.503107, 0.525318, 0.543352, 0.557253, 0.568634, 0.57903, 0.588684, 0.598891, 0.609981, 0.621362, 0.634283, 0.648546, 0.663707, 0.680046, 0.696165, 0.711964, 0.727011, 0.741301, 0.757405, 0.772071, 0.785581, 0.798238, 0.809677, 0.819702, 0.828599, 0.836722, 0.844443, 0.851107, 0.853252, 0.854746, 0.856174, 0.857821, 0.859532, 0.86146, 0.863257, 0.865139, 0.867319, 0.869696, 0.874302, 0.878588, 0.882439, 0.885929, 0.889473, 0.893226, 0.896696, 0.899897, 0.902596, 0.904831, 0.905525, 0.905665, 0.905503, 0.905158, 0.904783, 0.904082, 0.903347, 0.902761, 0.902377, 0.901983, 0.903424, 0.904313, 0.905315, 0.906446, 0.908092, 0.910123, 0.91295, 0.915585, 0.918444, 0.921302, 0.924337, 0.927219, 0.92974, 0.931922, 0.934142, 0.935906, 0.937086, 0.937641, 0.938301, 0.937652, 0.940441, 0.942518, 0.943259, 0.943031, 0.942117, 0.940632, 0.938428, 0.93666, 0.935256, 0.933022, 0.92688, 0.921057, 0.915483, 0.91102, 0.908293, 0.907283, 0.908191, 0.911169, 0.916189, 0.922855, 0.920605, 0.919482, 0.919489, 0.921276, 0.924526, 0.927733, 0.931974, 0.93677, 0.941483, 0.946802, 0.951203, 0.954437, 0.957047, 0.959729, 0.962539, 0.964858, 0.966042, 0.966647, 0.96631, 0.96546, 0.964841, 0.963656, 0.961698, 0.959454, 0.957327, 0.95514, 0.953558, 0.952732, 0.952181, 0.951731, 0.952146, 0.952641, 0.954057, 0.957078, 0.960639, 0.964222, 0.968307, 0.972691, 0.977423, 0.982898, 0.987144, 0.990734, 0.993983, 0.996787, 0.998753, 1.0, 0.999927, 0.999152, 0.997129, 0.993884, 0.989686, 0.983735, 0.976213, 0.967813, 0.958343, 0.94844, 0.938203, 0.927725, 0.917039, 0.905999, 0.893868, 0.881683, 0.868647, 0.854635, 0.84062, 0.826016, 0.809516, 0.791867, 0.772443, 0.749107, 0.720346, 0.688185, 0.651283, 0.61005, 0.566031, 0.52097, 0.474659, 0.429259, 0.385857, 0.342092, 0.30068, 0.263176, 0.227704, 0.195721, 0.16809, 0.14468, 0.124831, 0.108237, 0.094401, 0.082363, 0.0715, 0.062691, 0.054985, 0.048195, 0.042864, 0.038598, 0.034947, 0.031999, 0.029588, 0.027418, 0.025577, 0.023959, 0.021672, 0.019148, 0.016331, 0.010989, 0.007379, 0.006511, 0.00471, 0.002065], "wavelength": [2078, 2079, 2080, 2081, 2082, 2083, 2084, 2085, 2086, 2087, 2088, 2089, 2090, 2091, 2092, 2093, 2094, 2095, 2096, 2097, 2098, 2099, 2100, 2101, 2102, 2103, 2104, 2105, 2106, 2107, 2108, 2109, 2110, 2111, 2112, 2113, 2114, 2115, 2116, 2117, 2118, 2119, 2120, 2121, 2122, 2123, 2124, 2125, 2126, 2127, 2128, 2129, 2130, 2131, 2132, 2133, 2134, 2135, 2136, 2137, 2138, 2139, 2140, 2141, 2142, 2143, 2144, 2145, 2146, 2147, 2148, 2149, 2150, 2151, 2152, 2153, 2154, 2155, 2156, 2157, 2158, 2159, 2160, 2161, 2162, 2163, 2164, 2165, 2166, 2167, 2168, 2169, 2170, 2171, 2172, 2173, 2174, 2175, 2176, 2177, 2178, 2179, 2180, 2181, 2182, 2183, 2184, 2185, 2186, 2187, 2188, 2189, 2190, 2191, 2192, 2193, 2194, 2195, 2196, 2197, 2198, 2199, 2200, 2201, 2202, 2203, 2204, 2205, 2206, 2207, 2208, 2209, 2210, 2211, 2212, 2213, 2214, 2215, 2216, 2217, 2218, 2219, 2220, 2221, 2222, 2223, 2224, 2225, 2226, 2227, 2228, 2229, 2230, 2231, 2232, 2233, 2234, 2235, 2236, 2237, 2238, 2239, 2240, 2241, 2242, 2243, 2244, 2245, 2246, 2247, 2248, 2249, 2250, 2251, 2252, 2253, 2254, 2255, 2256, 2257, 2258, 2259, 2260, 2261, 2262, 2263, 2264, 2265, 2266, 2267, 2268, 2269, 2270, 2271, 2272, 2273, 2274, 2275, 2276, 2277, 2278, 2279, 2280, 2281, 2282, 2283, 2284, 2285, 2286, 2287, 2288, 2289, 2290, 2291, 2292, 2293, 2294, 2295, 2296, 2297, 2298, 2299, 2300, 2301, 2302, 2303, 2304, 2305, 2306, 2307, 2308, 2309, 2310, 2311, 2312, 2313, 2314, 2315, 2316, 2317, 2318, 2319, 2320]}}], "metadata_type": "eo_s2_nrt"}	2021-01-31 22:19:36.131641+00	africa	\N
65	s2b_nrt_granule	{"format": {"name": "GeoTiff"}, "platform": {"code": "SENTINEL_2B"}, "instrument": {"name": "MSI"}, "product_type": "ard", "processing_level": "Level-2"}	4	{"name": "s2b_nrt_granule", "metadata": {"format": {"name": "GeoTiff"}, "platform": {"code": "SENTINEL_2B"}, "instrument": {"name": "MSI"}, "product_type": "ard", "processing_level": "Level-2"}, "description": "Sentinel-2B MSI ARD NRT - NBAR NBART and Pixel Quality", "measurements": [{"name": "azimuthal_exiting", "dtype": "float32", "units": "1", "nodata": -999, "aliases": ["azimuthal_exiting"]}, {"name": "azimuthal_incident", "dtype": "float32", "units": "1", "nodata": -999, "aliases": ["azimuthal_incident"]}, {"name": "exiting", "dtype": "float32", "units": "1", "nodata": -999, "aliases": ["exiting"]}, {"name": "incident", "dtype": "float32", "units": "1", "nodata": -999, "aliases": ["incident"]}, {"name": "relative_azimuth", "dtype": "float32", "units": "1", "nodata": -999, "aliases": ["relative_azimuth"]}, {"name": "relative_slope", "dtype": "float32", "units": "1", "nodata": -999, "aliases": ["relative_slope"]}, {"name": "satellite_azimuth", "dtype": "float32", "units": "1", "nodata": -999, "aliases": ["satellite_azimuth"]}, {"name": "satellite_view", "dtype": "float32", "units": "1", "nodata": -999, "aliases": ["satellite_view"]}, {"name": "solar_azimuth", "dtype": "float32", "units": "1", "nodata": -999, "aliases": ["solar_azimuth"]}, {"name": "solar_zenith", "dtype": "float32", "units": "1", "nodata": -999, "aliases": ["solar_zenith"]}, {"name": "terrain_shadow", "dtype": "uint8", "units": "1", "nodata": 0, "aliases": ["terrain_shadow"]}, {"name": "fmask", "dtype": "uint8", "units": "1", "nodata": 0, "aliases": ["mask", "Fmask"], "flags_definition": {"fmask": {"bits": [0, 1, 2, 3, 4, 5, 6, 7], "values": {"0": "nodata", "1": "valid", "2": "cloud", "3": "shadow", "4": "snow", "5": "water"}, "description": "Fmask"}}}, {"name": "nbar_contiguity", "dtype": "uint8", "units": "1", "nodata": 255, "flags_definition": {"contiguity": {"bits": [0, 1, 2, 3, 4, 5, 6, 7], "values": {"0": "not_contiguous", "1": "contiguous"}, "description": "Pixel contiguity in band stack"}}}, {"name": "nbar_coastal_aerosol", "dtype": "int16", "units": "1", "nodata": -999, "aliases": ["nbar_band_01", "nbar_B01", "nbar_Band1"], "spectral_definition": {"response": [0.006797798, 0.01099643, 0.004208363, 0.006568034, 0.005883123, 0.00713011, 0.004333651, 0.006263537, 0.004393687, 0.00253157, 0.000621707, 0.002117729, 0.003175796, 0.005213085, 0.003387375, 0.00258671, 0.002384167, 0.004595227, 0.012990945, 0.050622293, 0.18872241, 0.459106539, 0.730160597, 0.847259495, 0.871235903, 0.881448354, 0.899392736, 0.918669431, 0.933420754, 0.94596319, 0.95041031, 0.953972339, 0.96903168, 0.999546173, 1, 0.976368067, 0.96404957, 0.95417544, 0.923744832, 0.88548879, 0.809016274, 0.601561144, 0.306766029, 0.108527711, 0.030542088, 0.008935131], "wavelength": [411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456]}}, {"name": "nbar_blue", "dtype": "int16", "units": "1", "nodata": -999, "aliases": ["nbar_band_02", "nbar_B02", "nbar_Band2"], "spectral_definition": {"response": [0.001893306, 0.019440751, 0.020059028, 0.014109631, 0.015612858, 0.015448868, 0.017034152, 0.013311359, 0.014462036, 0.009592091, 0.014500694, 0.011159264, 0.013332524, 0.01355731, 0.01426, 0.014717634, 0.015989541, 0.030654247, 0.055432753, 0.120228972, 0.252260953, 0.462862499, 0.65241169, 0.77750832, 0.824333103, 0.832077099, 0.835037767, 0.838761115, 0.864126031, 0.883293587, 0.90569382, 0.921186621, 0.936616967, 0.931024626, 0.927547539, 0.916622744, 0.9060165, 0.897870416, 0.903146598, 0.908994286, 0.920859439, 0.924523699, 0.918843658, 0.907981319, 0.898032665, 0.88735796, 0.873065866, 0.857761622, 0.846132814, 0.843382711, 0.857924772, 0.879320632, 0.903975503, 0.919580552, 0.946712663, 0.969406608, 0.993636046, 0.999320649, 1, 0.995107621, 0.984163047, 0.979509527, 0.978185449, 0.972278886, 0.96293492, 0.95355824, 0.938134944, 0.924777929, 0.909590075, 0.902313691, 0.892251397, 0.890060534, 0.891851681, 0.899164865, 0.910901434, 0.924636296, 0.938626228, 0.953526854, 0.971831245, 0.987690608, 0.996791216, 0.993851876, 0.9816383, 0.958970396, 0.893259218, 0.736063596, 0.52101528, 0.332578748, 0.195080476, 0.117429222, 0.075138809, 0.050991983, 0.032154822, 0.015134166, 0.004477169], "wavelength": [438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532]}}, {"name": "nbar_green", "dtype": "int16", "units": "1", "nodata": -999, "aliases": ["nbar_band_03", "nbar_B03", "nbar_Band3"], "spectral_definition": {"response": [0.005090312, 0.026897029, 0.12087986, 0.33742273, 0.603624689, 0.810967523, 0.91573833, 0.92605288, 0.92083242, 0.911237119, 0.902005739, 0.897081513, 0.899066029, 0.900672338, 0.902488081, 0.906886173, 0.915610562, 0.927756371, 0.941055569, 0.954196504, 0.966908428, 0.981390028, 0.991619278, 1, 0.999754078, 0.994046577, 0.981792818, 0.968692612, 0.957607907, 0.945644641, 0.92580977, 0.897152993, 0.838534201, 0.698446797, 0.493502787, 0.276900547, 0.107781358, 0.029913795, 0.007336673, 0.000838123], "wavelength": [536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582]}}, {"name": "nbar_red", "dtype": "int16", "units": "1", "nodata": -999, "aliases": ["nbar_band_04", "nbar_B04", "nbar_Band4"], "spectral_definition": {"response": [0.002584, 0.034529, 0.14997, 0.464826, 0.817746, 0.965324, 0.983869, 0.9969, 1.0, 0.995449, 0.991334, 0.977215, 0.936802, 0.873776, 0.814166, 0.776669, 0.764864, 0.775091, 0.801359, 0.830828, 0.857112, 0.883581, 0.90895, 0.934759, 0.955931, 0.96811, 0.973219, 0.971572, 0.969003, 0.965712, 0.960481, 0.944811, 0.884152, 0.706167, 0.422967, 0.189853, 0.063172, 0.020615, 0.002034], "wavelength": [646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 683, 684, 685]}}, {"name": "nbar_red_edge_1", "dtype": "int16", "units": "1", "nodata": -999, "aliases": ["nbar_band_05", "nbar_B05", "nbar_Band5"], "spectral_definition": {"response": [0.010471827, 0.057252544, 0.214724996, 0.547189415, 0.871043978, 0.968446586, 0.99124182, 1, 0.99509331, 0.987602081, 0.979408704, 0.970910946, 0.959528083, 0.94236861, 0.926720132, 0.894557475, 0.767248071, 0.504134435, 0.180610636, 0.034019737, 0.002436944], "wavelength": [694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714]}}, {"name": "nbar_red_edge_2", "dtype": "int16", "units": "1", "nodata": -999, "aliases": ["nbar_band_06", "nbar_B06", "nbar_Band6"], "spectral_definition": {"response": [0.017433807, 0.105812957, 0.386050533, 0.782313159, 0.905953099, 0.916416606, 0.92333441, 0.932013378, 0.947550036, 0.965839591, 0.978552758, 0.991319723, 1, 0.999955845, 0.971267313, 0.81917496, 0.467395748, 0.094120897, 0.009834009], "wavelength": [730, 731, 732, 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748]}}, {"name": "nbar_red_edge_3", "dtype": "int16", "units": "1", "nodata": -999, "aliases": ["nbar_band_07", "nbar_B07", "nbar_Band7"], "spectral_definition": {"response": [0.010282026, 0.037427714, 0.112026989, 0.257953812, 0.478980823, 0.730216783, 0.912510408, 0.971721033, 0.964616097, 0.955734525, 0.964925586, 0.986223289, 1, 0.998046627, 0.98393444, 0.96569621, 0.947277433, 0.927083998, 0.90976539, 0.886948914, 0.859517187, 0.827959173, 0.776383783, 0.671173028, 0.481809979, 0.236251944, 0.069538392, 0.013431956, 0.001257675], "wavelength": [766, 767, 768, 769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784, 785, 786, 787, 788, 789, 790, 791, 792, 793, 794]}}, {"name": "nbar_nir_1", "dtype": "int16", "units": "1", "nodata": -999, "aliases": ["nbar_band_08", "nbar_B08", "nbar_Band8"], "spectral_definition": {"response": [0.000386696, 0.003018401, 0.01669158, 0.028340486, 0.0502885, 0.08626388, 0.149596686, 0.258428566, 0.425108406, 0.631697563, 0.803109115, 0.904984654, 0.939674653, 0.944958731, 0.948238826, 0.963880684, 0.979861632, 0.991635585, 0.996362309, 1, 0.998257939, 0.998488834, 0.989253171, 0.98294089, 0.968189827, 0.958222106, 0.951650369, 0.947054991, 0.944166995, 0.948383123, 0.946461415, 0.942132884, 0.929937199, 0.914683918, 0.893248878, 0.873037871, 0.852648452, 0.836447483, 0.824300756, 0.814333379, 0.810955964, 0.803715941, 0.791980175, 0.783270185, 0.767838865, 0.754167357, 0.742309406, 0.727235815, 0.719323269, 0.713866399, 0.718941021, 0.726527917, 0.738324031, 0.750210769, 0.761800392, 0.769900245, 0.781725199, 0.78381047, 0.783069959, 0.782718588, 0.781644143, 0.780380397, 0.781443024, 0.781701218, 0.78177353, 0.780064535, 0.777591823, 0.770831803, 0.764574958, 0.753876586, 0.743324604, 0.733775698, 0.722497914, 0.712900724, 0.699439134, 0.688575227, 0.674039061, 0.657552716, 0.643729834, 0.62865391, 0.614005803, 0.603233252, 0.594982815, 0.588091928, 0.585186507, 0.582889219, 0.581493721, 0.580137218, 0.574804624, 0.576654614, 0.572399696, 0.570992768, 0.569291451, 0.571025201, 0.570861066, 0.572213154, 0.575418141, 0.577804028, 0.579603586, 0.579294979, 0.578302049, 0.57565598, 0.569721665, 0.561891364, 0.556830745, 0.549385012, 0.545858439, 0.542536249, 0.541895109, 0.539852497, 0.537997281, 0.53195493, 0.522275927, 0.505572421, 0.48804203, 0.469610434, 0.456107021, 0.445848869, 0.443119818, 0.445581498, 0.447532506, 0.440183411, 0.418240241, 0.369455837, 0.301788007, 0.235014942, 0.174244972, 0.122382945, 0.083462794, 0.056162189, 0.038006008, 0.024240249, 0.014845963, 0.006132899], "wavelength": [774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784, 785, 786, 787, 788, 789, 790, 791, 792, 793, 794, 795, 796, 797, 798, 799, 800, 801, 802, 803, 804, 805, 806, 807, 808, 809, 810, 811, 812, 813, 814, 815, 816, 817, 818, 819, 820, 821, 822, 823, 824, 825, 826, 827, 828, 829, 830, 831, 832, 833, 834, 835, 836, 837, 838, 839, 840, 841, 842, 843, 844, 845, 846, 847, 848, 849, 850, 851, 852, 853, 854, 855, 856, 857, 858, 859, 860, 861, 862, 863, 864, 865, 866, 867, 868, 869, 870, 871, 872, 873, 874, 875, 876, 877, 878, 879, 880, 881, 882, 883, 884, 885, 886, 887, 888, 889, 890, 891, 892, 893, 894, 895, 896, 897, 898, 899, 900, 901, 902, 903, 904, 905, 906, 907]}}, {"name": "nbar_nir_2", "dtype": "int16", "units": "1", "nodata": -999, "aliases": ["nbar_band_8A", "nbar_B8A", "nbar_Band8A"], "spectral_definition": {"response": [0.001661751, 0.01602581, 0.032253895, 0.073411273, 0.168937582, 0.345506138, 0.569417239, 0.79634996, 0.937581155, 0.980942645, 0.987241334, 0.994409463, 0.998963959, 0.999788107, 1, 0.994482469, 0.987807181, 0.983157165, 0.979826684, 0.975089851, 0.972818786, 0.966320275, 0.958195153, 0.941870745, 0.894185366, 0.778588669, 0.597362542, 0.377361257, 0.184667876, 0.079045495, 0.033393337, 0.015808546, 0.00162404], "wavelength": [848, 849, 850, 851, 852, 853, 854, 855, 856, 857, 858, 859, 860, 861, 862, 863, 864, 865, 866, 867, 868, 869, 870, 871, 872, 873, 874, 875, 876, 877, 878, 879, 880]}}, {"name": "nbar_swir_2", "dtype": "int16", "units": "1", "nodata": -999, "aliases": ["nbar_band_11", "nbar_B11", "nbar_Band11"], "spectral_definition": {"response": [0.0000115, 0.000026996, 0.000081157, 0.000169507, 0.000273428, 0.000343776, 0.000459515, 0.000651677, 0.0008223, 0.001076746, 0.001428776, 0.001958681, 0.002660821, 0.003682001, 0.005217308, 0.007572684, 0.011246256, 0.01713141, 0.026703068, 0.041388968, 0.062904714, 0.094492263, 0.139743066, 0.200760503, 0.281513117, 0.380879812, 0.490209915, 0.606204368, 0.714558374, 0.80351452, 0.86986655, 0.916284448, 0.946609049, 0.963892644, 0.973065345, 0.977057349, 0.977796293, 0.976890332, 0.975338048, 0.973392995, 0.971480798, 0.969740168, 0.969095034, 0.96969742, 0.970522078, 0.972736269, 0.976138953, 0.978944681, 0.981010782, 0.983513536, 0.984837133, 0.984404132, 0.983920166, 0.983372624, 0.981458796, 0.979391949, 0.978058392, 0.976263051, 0.975392679, 0.9757089, 0.976805245, 0.978986183, 0.981998545, 0.98520893, 0.988659162, 0.992331977, 0.994804634, 0.99589809, 0.995903119, 0.994773417, 0.992101664, 0.988591774, 0.984908418, 0.981101728, 0.976805235, 0.97354566, 0.971948013, 0.97053597, 0.970436371, 0.972382602, 0.975244492, 0.978552743, 0.982971465, 0.98808508, 0.992662671, 0.996435703, 0.99906056, 1, 0.999036445, 0.996642174, 0.993293536, 0.989674029, 0.98579838, 0.982153372, 0.979817194, 0.979473331, 0.980262857, 0.982464858, 0.986000509, 0.989562258, 0.991723341, 0.992201372, 0.98939229, 0.982102331, 0.970157085, 0.953186779, 0.932369062, 0.908001591, 0.884086561, 0.864271526, 0.850889881, 0.844206087, 0.843448232, 0.847024828, 0.848701823, 0.840540222, 0.81352592, 0.756843245, 0.670393147, 0.565754809, 0.457566037, 0.353763564, 0.256912748, 0.176281, 0.115842988, 0.073512768, 0.046527708, 0.02905985, 0.018579999, 0.012463091, 0.00878944, 0.006316358, 0.004582867, 0.003359394, 0.002462997, 0.001990739, 0.001501488, 0.001123371, 0.00078272, 0.000541322, 0.000281204, 0.00013347], "wavelength": [1538, 1539, 1540, 1541, 1542, 1543, 1544, 1545, 1546, 1547, 1548, 1549, 1550, 1551, 1552, 1553, 1554, 1555, 1556, 1557, 1558, 1559, 1560, 1561, 1562, 1563, 1564, 1565, 1566, 1567, 1568, 1569, 1570, 1571, 1572, 1573, 1574, 1575, 1576, 1577, 1578, 1579, 1580, 1581, 1582, 1583, 1584, 1585, 1586, 1587, 1588, 1589, 1590, 1591, 1592, 1593, 1594, 1595, 1596, 1597, 1598, 1599, 1600, 1601, 1602, 1603, 1604, 1605, 1606, 1607, 1608, 1609, 1610, 1611, 1612, 1613, 1614, 1615, 1616, 1617, 1618, 1619, 1620, 1621, 1622, 1623, 1624, 1625, 1626, 1627, 1628, 1629, 1630, 1631, 1632, 1633, 1634, 1635, 1636, 1637, 1638, 1639, 1640, 1641, 1642, 1643, 1644, 1645, 1646, 1647, 1648, 1649, 1650, 1651, 1652, 1653, 1654, 1655, 1656, 1657, 1658, 1659, 1660, 1661, 1662, 1663, 1664, 1665, 1666, 1667, 1668, 1669, 1670, 1671, 1672, 1673, 1674, 1675, 1676, 1677, 1678, 1679]}}, {"name": "nbar_swir_3", "dtype": "int16", "units": "1", "nodata": -999, "aliases": ["nbar_band_12", "nbar_B12", "nbar_Band12"], "spectral_definition": {"response": [0.000227567, 0.000739283, 0.001656775, 0.003019587, 0.004589377, 0.005924935, 0.007534774, 0.008748008, 0.010265481, 0.012236179, 0.014593479, 0.017458937, 0.021063245, 0.025428056, 0.03060944, 0.037234457, 0.045771325, 0.056362502, 0.070016996, 0.088004988, 0.110694417, 0.138884174, 0.173287791, 0.214374591, 0.261990789, 0.317227795, 0.380865706, 0.449470316, 0.522785467, 0.598898522, 0.672128213, 0.737899139, 0.792930708, 0.835658783, 0.866335142, 0.886329697, 0.897588245, 0.901517855, 0.900790721, 0.897113531, 0.892352598, 0.88796428, 0.884432193, 0.882095059, 0.881695748, 0.88269782, 0.887154405, 0.892732955, 0.898903582, 0.905619271, 0.912841006, 0.920179789, 0.926912882, 0.933094888, 0.938438355, 0.943377038, 0.945579227, 0.947407512, 0.948568289, 0.94882972, 0.948111791, 0.947115734, 0.946126982, 0.944870644, 0.943485039, 0.941894052, 0.942445527, 0.943274219, 0.944243794, 0.94528606, 0.946212496, 0.947084905, 0.947941677, 0.948940117, 0.949880321, 0.950676414, 0.951054332, 0.951531833, 0.952326952, 0.952721089, 0.952552047, 0.952417855, 0.952654092, 0.95296197, 0.95331832, 0.953779111, 0.954291677, 0.954837035, 0.955539257, 0.956750259, 0.957986198, 0.959237259, 0.960451396, 0.96141302, 0.96264388, 0.964122014, 0.963609737, 0.963104517, 0.962753979, 0.961850624, 0.960730243, 0.959560745, 0.958377188, 0.956972347, 0.955119849, 0.953076144, 0.95406055, 0.955176712, 0.955719159, 0.955674616, 0.955356546, 0.954611539, 0.953453566, 0.952124922, 0.950597985, 0.948594073, 0.948562399, 0.948548442, 0.94829598, 0.947706109, 0.946620434, 0.94521576, 0.943480979, 0.942137936, 0.940654943, 0.938918576, 0.941493007, 0.943778866, 0.945751584, 0.947277308, 0.948481875, 0.949621704, 0.950767479, 0.951991493, 0.953624457, 0.955262594, 0.952413026, 0.950488752, 0.949721652, 0.949105026, 0.949712169, 0.95167296, 0.955012323, 0.959777857, 0.966208245, 0.973886163, 0.970920044, 0.969139883, 0.968329935, 0.967635904, 0.967555279, 0.968040602, 0.968508397, 0.968956722, 0.969510275, 0.969967732, 0.969097684, 0.968258197, 0.967549788, 0.96650394, 0.965459532, 0.964366923, 0.962929804, 0.961665594, 0.96063821, 0.959368085, 0.959707097, 0.960359643, 0.9616448, 0.962729828, 0.96370081, 0.964773629, 0.965512685, 0.96634935, 0.96753842, 0.96886815, 0.970549249, 0.972426171, 0.974301395, 0.976012041, 0.977203216, 0.978986062, 0.980446263, 0.981524356, 0.982531672, 0.983336508, 0.98463147, 0.986737985, 0.989144288, 0.991223348, 0.99318448, 0.995273324, 0.996704667, 0.998282418, 0.999605161, 1, 0.998654554, 0.995753158, 0.990605371, 0.981520886, 0.968715091, 0.951679125, 0.929343556, 0.902305299, 0.87044084, 0.831947776, 0.786119345, 0.736343248, 0.681862245, 0.623137717, 0.564024643, 0.506650261, 0.451376118, 0.400487569, 0.354176773, 0.309839746, 0.269312679, 0.234102225, 0.20225298, 0.173669677, 0.149356419, 0.128957364, 0.111530972, 0.09689948, 0.084874763, 0.074063524, 0.064469344, 0.056321561, 0.049381236, 0.043196026, 0.037986086, 0.033468826, 0.028983375, 0.025085752, 0.020007676, 0.013837921, 0.008464001, 0.004443102, 0.000848571], "wavelength": [2065, 2066, 2067, 2068, 2069, 2070, 2071, 2072, 2073, 2074, 2075, 2076, 2077, 2078, 2079, 2080, 2081, 2082, 2083, 2084, 2085, 2086, 2087, 2088, 2089, 2090, 2091, 2092, 2093, 2094, 2095, 2096, 2097, 2098, 2099, 2100, 2101, 2102, 2103, 2104, 2105, 2106, 2107, 2108, 2109, 2110, 2111, 2112, 2113, 2114, 2115, 2116, 2117, 2118, 2119, 2120, 2121, 2122, 2123, 2124, 2125, 2126, 2127, 2128, 2129, 2130, 2131, 2132, 2133, 2134, 2135, 2136, 2137, 2138, 2139, 2140, 2141, 2142, 2143, 2144, 2145, 2146, 2147, 2148, 2149, 2150, 2151, 2152, 2153, 2154, 2155, 2156, 2157, 2158, 2159, 2160, 2161, 2162, 2163, 2164, 2165, 2166, 2167, 2168, 2169, 2170, 2171, 2172, 2173, 2174, 2175, 2176, 2177, 2178, 2179, 2180, 2181, 2182, 2183, 2184, 2185, 2186, 2187, 2188, 2189, 2190, 2191, 2192, 2193, 2194, 2195, 2196, 2197, 2198, 2199, 2200, 2201, 2202, 2203, 2204, 2205, 2206, 2207, 2208, 2209, 2210, 2211, 2212, 2213, 2214, 2215, 2216, 2217, 2218, 2219, 2220, 2221, 2222, 2223, 2224, 2225, 2226, 2227, 2228, 2229, 2230, 2231, 2232, 2233, 2234, 2235, 2236, 2237, 2238, 2239, 2240, 2241, 2242, 2243, 2244, 2245, 2246, 2247, 2248, 2249, 2250, 2251, 2252, 2253, 2254, 2255, 2256, 2257, 2258, 2259, 2260, 2261, 2262, 2263, 2264, 2265, 2266, 2267, 2268, 2269, 2270, 2271, 2272, 2273, 2274, 2275, 2276, 2277, 2278, 2279, 2280, 2281, 2282, 2283, 2284, 2285, 2286, 2287, 2288, 2289, 2290, 2291, 2292, 2293, 2294, 2295, 2296, 2297, 2298, 2299, 2300, 2301, 2302, 2303]}}, {"name": "nbart_contiguity", "dtype": "uint8", "units": "1", "nodata": 255, "flags_definition": {"contiguity": {"bits": [0, 1, 2, 3, 4, 5, 6, 7], "values": {"0": "not_contiguous", "1": "contiguous"}, "description": "Pixel contiguity in band stack"}}}, {"name": "nbart_coastal_aerosol", "dtype": "int16", "units": "1", "nodata": -999, "aliases": ["nbart_band_01", "nbart_B01", "nbart_Band1"], "spectral_definition": {"response": [0.006797798, 0.01099643, 0.004208363, 0.006568034, 0.005883123, 0.00713011, 0.004333651, 0.006263537, 0.004393687, 0.00253157, 0.000621707, 0.002117729, 0.003175796, 0.005213085, 0.003387375, 0.00258671, 0.002384167, 0.004595227, 0.012990945, 0.050622293, 0.18872241, 0.459106539, 0.730160597, 0.847259495, 0.871235903, 0.881448354, 0.899392736, 0.918669431, 0.933420754, 0.94596319, 0.95041031, 0.953972339, 0.96903168, 0.999546173, 1, 0.976368067, 0.96404957, 0.95417544, 0.923744832, 0.88548879, 0.809016274, 0.601561144, 0.306766029, 0.108527711, 0.030542088, 0.008935131], "wavelength": [411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456]}}, {"name": "nbart_blue", "dtype": "int16", "units": "1", "nodata": -999, "aliases": ["nbart_band_02", "nbart_B02", "nbart_Band2"], "spectral_definition": {"response": [0.001893306, 0.019440751, 0.020059028, 0.014109631, 0.015612858, 0.015448868, 0.017034152, 0.013311359, 0.014462036, 0.009592091, 0.014500694, 0.011159264, 0.013332524, 0.01355731, 0.01426, 0.014717634, 0.015989541, 0.030654247, 0.055432753, 0.120228972, 0.252260953, 0.462862499, 0.65241169, 0.77750832, 0.824333103, 0.832077099, 0.835037767, 0.838761115, 0.864126031, 0.883293587, 0.90569382, 0.921186621, 0.936616967, 0.931024626, 0.927547539, 0.916622744, 0.9060165, 0.897870416, 0.903146598, 0.908994286, 0.920859439, 0.924523699, 0.918843658, 0.907981319, 0.898032665, 0.88735796, 0.873065866, 0.857761622, 0.846132814, 0.843382711, 0.857924772, 0.879320632, 0.903975503, 0.919580552, 0.946712663, 0.969406608, 0.993636046, 0.999320649, 1, 0.995107621, 0.984163047, 0.979509527, 0.978185449, 0.972278886, 0.96293492, 0.95355824, 0.938134944, 0.924777929, 0.909590075, 0.902313691, 0.892251397, 0.890060534, 0.891851681, 0.899164865, 0.910901434, 0.924636296, 0.938626228, 0.953526854, 0.971831245, 0.987690608, 0.996791216, 0.993851876, 0.9816383, 0.958970396, 0.893259218, 0.736063596, 0.52101528, 0.332578748, 0.195080476, 0.117429222, 0.075138809, 0.050991983, 0.032154822, 0.015134166, 0.004477169], "wavelength": [438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532]}}, {"name": "nbart_green", "dtype": "int16", "units": "1", "nodata": -999, "aliases": ["nbart_band_03", "nbart_B03", "nbart_Band3"], "spectral_definition": {"response": [0.005090312, 0.026897029, 0.12087986, 0.33742273, 0.603624689, 0.810967523, 0.91573833, 0.92605288, 0.92083242, 0.911237119, 0.902005739, 0.897081513, 0.899066029, 0.900672338, 0.902488081, 0.906886173, 0.915610562, 0.927756371, 0.941055569, 0.954196504, 0.966908428, 0.981390028, 0.991619278, 1, 0.999754078, 0.994046577, 0.981792818, 0.968692612, 0.957607907, 0.945644641, 0.92580977, 0.897152993, 0.838534201, 0.698446797, 0.493502787, 0.276900547, 0.107781358, 0.029913795, 0.007336673, 0.000838123], "wavelength": [536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582]}}, {"name": "nbart_red", "dtype": "int16", "units": "1", "nodata": -999, "aliases": ["nbart_band_04", "nbart_B04", "nbart_Band4"], "spectral_definition": {"response": [0.002584, 0.034529, 0.14997, 0.464826, 0.817746, 0.965324, 0.983869, 0.9969, 1.0, 0.995449, 0.991334, 0.977215, 0.936802, 0.873776, 0.814166, 0.776669, 0.764864, 0.775091, 0.801359, 0.830828, 0.857112, 0.883581, 0.90895, 0.934759, 0.955931, 0.96811, 0.973219, 0.971572, 0.969003, 0.965712, 0.960481, 0.944811, 0.884152, 0.706167, 0.422967, 0.189853, 0.063172, 0.020615, 0.002034], "wavelength": [646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 683, 684, 685]}}, {"name": "nbart_red_edge_1", "dtype": "int16", "units": "1", "nodata": -999, "aliases": ["nbart_band_05", "nbart_B05", "nbart_Band5"], "spectral_definition": {"response": [0.010471827, 0.057252544, 0.214724996, 0.547189415, 0.871043978, 0.968446586, 0.99124182, 1, 0.99509331, 0.987602081, 0.979408704, 0.970910946, 0.959528083, 0.94236861, 0.926720132, 0.894557475, 0.767248071, 0.504134435, 0.180610636, 0.034019737, 0.002436944], "wavelength": [694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714]}}, {"name": "nbart_red_edge_2", "dtype": "int16", "units": "1", "nodata": -999, "aliases": ["nbart_band_06", "nbart_B06", "nbart_Band6"], "spectral_definition": {"response": [0.017433807, 0.105812957, 0.386050533, 0.782313159, 0.905953099, 0.916416606, 0.92333441, 0.932013378, 0.947550036, 0.965839591, 0.978552758, 0.991319723, 1, 0.999955845, 0.971267313, 0.81917496, 0.467395748, 0.094120897, 0.009834009], "wavelength": [730, 731, 732, 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748]}}, {"name": "nbart_red_edge_3", "dtype": "int16", "units": "1", "nodata": -999, "aliases": ["nbart_band_07", "nbart_B07", "nbart_Band7"], "spectral_definition": {"response": [0.010282026, 0.037427714, 0.112026989, 0.257953812, 0.478980823, 0.730216783, 0.912510408, 0.971721033, 0.964616097, 0.955734525, 0.964925586, 0.986223289, 1, 0.998046627, 0.98393444, 0.96569621, 0.947277433, 0.927083998, 0.90976539, 0.886948914, 0.859517187, 0.827959173, 0.776383783, 0.671173028, 0.481809979, 0.236251944, 0.069538392, 0.013431956, 0.001257675], "wavelength": [766, 767, 768, 769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784, 785, 786, 787, 788, 789, 790, 791, 792, 793, 794]}}, {"name": "nbart_nir_1", "dtype": "int16", "units": "1", "nodata": -999, "aliases": ["nbart_band_08", "nbart_B08", "nbart_Band8"], "spectral_definition": {"response": [0.000386696, 0.003018401, 0.01669158, 0.028340486, 0.0502885, 0.08626388, 0.149596686, 0.258428566, 0.425108406, 0.631697563, 0.803109115, 0.904984654, 0.939674653, 0.944958731, 0.948238826, 0.963880684, 0.979861632, 0.991635585, 0.996362309, 1, 0.998257939, 0.998488834, 0.989253171, 0.98294089, 0.968189827, 0.958222106, 0.951650369, 0.947054991, 0.944166995, 0.948383123, 0.946461415, 0.942132884, 0.929937199, 0.914683918, 0.893248878, 0.873037871, 0.852648452, 0.836447483, 0.824300756, 0.814333379, 0.810955964, 0.803715941, 0.791980175, 0.783270185, 0.767838865, 0.754167357, 0.742309406, 0.727235815, 0.719323269, 0.713866399, 0.718941021, 0.726527917, 0.738324031, 0.750210769, 0.761800392, 0.769900245, 0.781725199, 0.78381047, 0.783069959, 0.782718588, 0.781644143, 0.780380397, 0.781443024, 0.781701218, 0.78177353, 0.780064535, 0.777591823, 0.770831803, 0.764574958, 0.753876586, 0.743324604, 0.733775698, 0.722497914, 0.712900724, 0.699439134, 0.688575227, 0.674039061, 0.657552716, 0.643729834, 0.62865391, 0.614005803, 0.603233252, 0.594982815, 0.588091928, 0.585186507, 0.582889219, 0.581493721, 0.580137218, 0.574804624, 0.576654614, 0.572399696, 0.570992768, 0.569291451, 0.571025201, 0.570861066, 0.572213154, 0.575418141, 0.577804028, 0.579603586, 0.579294979, 0.578302049, 0.57565598, 0.569721665, 0.561891364, 0.556830745, 0.549385012, 0.545858439, 0.542536249, 0.541895109, 0.539852497, 0.537997281, 0.53195493, 0.522275927, 0.505572421, 0.48804203, 0.469610434, 0.456107021, 0.445848869, 0.443119818, 0.445581498, 0.447532506, 0.440183411, 0.418240241, 0.369455837, 0.301788007, 0.235014942, 0.174244972, 0.122382945, 0.083462794, 0.056162189, 0.038006008, 0.024240249, 0.014845963, 0.006132899], "wavelength": [774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784, 785, 786, 787, 788, 789, 790, 791, 792, 793, 794, 795, 796, 797, 798, 799, 800, 801, 802, 803, 804, 805, 806, 807, 808, 809, 810, 811, 812, 813, 814, 815, 816, 817, 818, 819, 820, 821, 822, 823, 824, 825, 826, 827, 828, 829, 830, 831, 832, 833, 834, 835, 836, 837, 838, 839, 840, 841, 842, 843, 844, 845, 846, 847, 848, 849, 850, 851, 852, 853, 854, 855, 856, 857, 858, 859, 860, 861, 862, 863, 864, 865, 866, 867, 868, 869, 870, 871, 872, 873, 874, 875, 876, 877, 878, 879, 880, 881, 882, 883, 884, 885, 886, 887, 888, 889, 890, 891, 892, 893, 894, 895, 896, 897, 898, 899, 900, 901, 902, 903, 904, 905, 906, 907]}}, {"name": "nbart_nir_2", "dtype": "int16", "units": "1", "nodata": -999, "aliases": ["nbart_band_8A", "nbart_B8A", "nbart_Band8A"], "spectral_definition": {"response": [0.001661751, 0.01602581, 0.032253895, 0.073411273, 0.168937582, 0.345506138, 0.569417239, 0.79634996, 0.937581155, 0.980942645, 0.987241334, 0.994409463, 0.998963959, 0.999788107, 1, 0.994482469, 0.987807181, 0.983157165, 0.979826684, 0.975089851, 0.972818786, 0.966320275, 0.958195153, 0.941870745, 0.894185366, 0.778588669, 0.597362542, 0.377361257, 0.184667876, 0.079045495, 0.033393337, 0.015808546, 0.00162404], "wavelength": [848, 849, 850, 851, 852, 853, 854, 855, 856, 857, 858, 859, 860, 861, 862, 863, 864, 865, 866, 867, 868, 869, 870, 871, 872, 873, 874, 875, 876, 877, 878, 879, 880]}}, {"name": "nbart_swir_2", "dtype": "int16", "units": "1", "nodata": -999, "aliases": ["nbart_band_11", "nbart_B11", "nbart_Band11"], "spectral_definition": {"response": [0.0000115, 0.000026996, 0.000081157, 0.000169507, 0.000273428, 0.000343776, 0.000459515, 0.000651677, 0.0008223, 0.001076746, 0.001428776, 0.001958681, 0.002660821, 0.003682001, 0.005217308, 0.007572684, 0.011246256, 0.01713141, 0.026703068, 0.041388968, 0.062904714, 0.094492263, 0.139743066, 0.200760503, 0.281513117, 0.380879812, 0.490209915, 0.606204368, 0.714558374, 0.80351452, 0.86986655, 0.916284448, 0.946609049, 0.963892644, 0.973065345, 0.977057349, 0.977796293, 0.976890332, 0.975338048, 0.973392995, 0.971480798, 0.969740168, 0.969095034, 0.96969742, 0.970522078, 0.972736269, 0.976138953, 0.978944681, 0.981010782, 0.983513536, 0.984837133, 0.984404132, 0.983920166, 0.983372624, 0.981458796, 0.979391949, 0.978058392, 0.976263051, 0.975392679, 0.9757089, 0.976805245, 0.978986183, 0.981998545, 0.98520893, 0.988659162, 0.992331977, 0.994804634, 0.99589809, 0.995903119, 0.994773417, 0.992101664, 0.988591774, 0.984908418, 0.981101728, 0.976805235, 0.97354566, 0.971948013, 0.97053597, 0.970436371, 0.972382602, 0.975244492, 0.978552743, 0.982971465, 0.98808508, 0.992662671, 0.996435703, 0.99906056, 1, 0.999036445, 0.996642174, 0.993293536, 0.989674029, 0.98579838, 0.982153372, 0.979817194, 0.979473331, 0.980262857, 0.982464858, 0.986000509, 0.989562258, 0.991723341, 0.992201372, 0.98939229, 0.982102331, 0.970157085, 0.953186779, 0.932369062, 0.908001591, 0.884086561, 0.864271526, 0.850889881, 0.844206087, 0.843448232, 0.847024828, 0.848701823, 0.840540222, 0.81352592, 0.756843245, 0.670393147, 0.565754809, 0.457566037, 0.353763564, 0.256912748, 0.176281, 0.115842988, 0.073512768, 0.046527708, 0.02905985, 0.018579999, 0.012463091, 0.00878944, 0.006316358, 0.004582867, 0.003359394, 0.002462997, 0.001990739, 0.001501488, 0.001123371, 0.00078272, 0.000541322, 0.000281204, 0.00013347], "wavelength": [1538, 1539, 1540, 1541, 1542, 1543, 1544, 1545, 1546, 1547, 1548, 1549, 1550, 1551, 1552, 1553, 1554, 1555, 1556, 1557, 1558, 1559, 1560, 1561, 1562, 1563, 1564, 1565, 1566, 1567, 1568, 1569, 1570, 1571, 1572, 1573, 1574, 1575, 1576, 1577, 1578, 1579, 1580, 1581, 1582, 1583, 1584, 1585, 1586, 1587, 1588, 1589, 1590, 1591, 1592, 1593, 1594, 1595, 1596, 1597, 1598, 1599, 1600, 1601, 1602, 1603, 1604, 1605, 1606, 1607, 1608, 1609, 1610, 1611, 1612, 1613, 1614, 1615, 1616, 1617, 1618, 1619, 1620, 1621, 1622, 1623, 1624, 1625, 1626, 1627, 1628, 1629, 1630, 1631, 1632, 1633, 1634, 1635, 1636, 1637, 1638, 1639, 1640, 1641, 1642, 1643, 1644, 1645, 1646, 1647, 1648, 1649, 1650, 1651, 1652, 1653, 1654, 1655, 1656, 1657, 1658, 1659, 1660, 1661, 1662, 1663, 1664, 1665, 1666, 1667, 1668, 1669, 1670, 1671, 1672, 1673, 1674, 1675, 1676, 1677, 1678, 1679]}}, {"name": "nbart_swir_3", "dtype": "int16", "units": "1", "nodata": -999, "aliases": ["nbart_band_12", "nbart_B12", "nbart_Band12"], "spectral_definition": {"response": [0.000227567, 0.000739283, 0.001656775, 0.003019587, 0.004589377, 0.005924935, 0.007534774, 0.008748008, 0.010265481, 0.012236179, 0.014593479, 0.017458937, 0.021063245, 0.025428056, 0.03060944, 0.037234457, 0.045771325, 0.056362502, 0.070016996, 0.088004988, 0.110694417, 0.138884174, 0.173287791, 0.214374591, 0.261990789, 0.317227795, 0.380865706, 0.449470316, 0.522785467, 0.598898522, 0.672128213, 0.737899139, 0.792930708, 0.835658783, 0.866335142, 0.886329697, 0.897588245, 0.901517855, 0.900790721, 0.897113531, 0.892352598, 0.88796428, 0.884432193, 0.882095059, 0.881695748, 0.88269782, 0.887154405, 0.892732955, 0.898903582, 0.905619271, 0.912841006, 0.920179789, 0.926912882, 0.933094888, 0.938438355, 0.943377038, 0.945579227, 0.947407512, 0.948568289, 0.94882972, 0.948111791, 0.947115734, 0.946126982, 0.944870644, 0.943485039, 0.941894052, 0.942445527, 0.943274219, 0.944243794, 0.94528606, 0.946212496, 0.947084905, 0.947941677, 0.948940117, 0.949880321, 0.950676414, 0.951054332, 0.951531833, 0.952326952, 0.952721089, 0.952552047, 0.952417855, 0.952654092, 0.95296197, 0.95331832, 0.953779111, 0.954291677, 0.954837035, 0.955539257, 0.956750259, 0.957986198, 0.959237259, 0.960451396, 0.96141302, 0.96264388, 0.964122014, 0.963609737, 0.963104517, 0.962753979, 0.961850624, 0.960730243, 0.959560745, 0.958377188, 0.956972347, 0.955119849, 0.953076144, 0.95406055, 0.955176712, 0.955719159, 0.955674616, 0.955356546, 0.954611539, 0.953453566, 0.952124922, 0.950597985, 0.948594073, 0.948562399, 0.948548442, 0.94829598, 0.947706109, 0.946620434, 0.94521576, 0.943480979, 0.942137936, 0.940654943, 0.938918576, 0.941493007, 0.943778866, 0.945751584, 0.947277308, 0.948481875, 0.949621704, 0.950767479, 0.951991493, 0.953624457, 0.955262594, 0.952413026, 0.950488752, 0.949721652, 0.949105026, 0.949712169, 0.95167296, 0.955012323, 0.959777857, 0.966208245, 0.973886163, 0.970920044, 0.969139883, 0.968329935, 0.967635904, 0.967555279, 0.968040602, 0.968508397, 0.968956722, 0.969510275, 0.969967732, 0.969097684, 0.968258197, 0.967549788, 0.96650394, 0.965459532, 0.964366923, 0.962929804, 0.961665594, 0.96063821, 0.959368085, 0.959707097, 0.960359643, 0.9616448, 0.962729828, 0.96370081, 0.964773629, 0.965512685, 0.96634935, 0.96753842, 0.96886815, 0.970549249, 0.972426171, 0.974301395, 0.976012041, 0.977203216, 0.978986062, 0.980446263, 0.981524356, 0.982531672, 0.983336508, 0.98463147, 0.986737985, 0.989144288, 0.991223348, 0.99318448, 0.995273324, 0.996704667, 0.998282418, 0.999605161, 1, 0.998654554, 0.995753158, 0.990605371, 0.981520886, 0.968715091, 0.951679125, 0.929343556, 0.902305299, 0.87044084, 0.831947776, 0.786119345, 0.736343248, 0.681862245, 0.623137717, 0.564024643, 0.506650261, 0.451376118, 0.400487569, 0.354176773, 0.309839746, 0.269312679, 0.234102225, 0.20225298, 0.173669677, 0.149356419, 0.128957364, 0.111530972, 0.09689948, 0.084874763, 0.074063524, 0.064469344, 0.056321561, 0.049381236, 0.043196026, 0.037986086, 0.033468826, 0.028983375, 0.025085752, 0.020007676, 0.013837921, 0.008464001, 0.004443102, 0.000848571], "wavelength": [2065, 2066, 2067, 2068, 2069, 2070, 2071, 2072, 2073, 2074, 2075, 2076, 2077, 2078, 2079, 2080, 2081, 2082, 2083, 2084, 2085, 2086, 2087, 2088, 2089, 2090, 2091, 2092, 2093, 2094, 2095, 2096, 2097, 2098, 2099, 2100, 2101, 2102, 2103, 2104, 2105, 2106, 2107, 2108, 2109, 2110, 2111, 2112, 2113, 2114, 2115, 2116, 2117, 2118, 2119, 2120, 2121, 2122, 2123, 2124, 2125, 2126, 2127, 2128, 2129, 2130, 2131, 2132, 2133, 2134, 2135, 2136, 2137, 2138, 2139, 2140, 2141, 2142, 2143, 2144, 2145, 2146, 2147, 2148, 2149, 2150, 2151, 2152, 2153, 2154, 2155, 2156, 2157, 2158, 2159, 2160, 2161, 2162, 2163, 2164, 2165, 2166, 2167, 2168, 2169, 2170, 2171, 2172, 2173, 2174, 2175, 2176, 2177, 2178, 2179, 2180, 2181, 2182, 2183, 2184, 2185, 2186, 2187, 2188, 2189, 2190, 2191, 2192, 2193, 2194, 2195, 2196, 2197, 2198, 2199, 2200, 2201, 2202, 2203, 2204, 2205, 2206, 2207, 2208, 2209, 2210, 2211, 2212, 2213, 2214, 2215, 2216, 2217, 2218, 2219, 2220, 2221, 2222, 2223, 2224, 2225, 2226, 2227, 2228, 2229, 2230, 2231, 2232, 2233, 2234, 2235, 2236, 2237, 2238, 2239, 2240, 2241, 2242, 2243, 2244, 2245, 2246, 2247, 2248, 2249, 2250, 2251, 2252, 2253, 2254, 2255, 2256, 2257, 2258, 2259, 2260, 2261, 2262, 2263, 2264, 2265, 2266, 2267, 2268, 2269, 2270, 2271, 2272, 2273, 2274, 2275, 2276, 2277, 2278, 2279, 2280, 2281, 2282, 2283, 2284, 2285, 2286, 2287, 2288, 2289, 2290, 2291, 2292, 2293, 2294, 2295, 2296, 2297, 2298, 2299, 2300, 2301, 2302, 2303]}}], "metadata_type": "eo_s2_nrt"}	2021-01-31 22:19:36.289193+00	africa	\N
66	s2_tsmask	{"format": {"name": "GeoTIFF"}, "platform": {"code": "SENTINEL_2A,SENTINEL_2B"}, "instrument": {"name": "MSI"}, "product_type": "S2_MSI_TSmask"}	7	{"name": "s2_tsmask", "metadata": {"format": {"name": "GeoTIFF"}, "platform": {"code": "SENTINEL_2A,SENTINEL_2B"}, "instrument": {"name": "MSI"}, "product_type": "S2_MSI_TSmask"}, "description": "Time series cloud and cloud shadow detection for Sentinel-2A and Sentinel-2B surface reflectance data.\\n\\nTSmask classifies a pixel as one of the following four categories: no observation, clear, cloud, and cloud shadow.\\n", "measurements": [{"name": "classification", "dtype": "uint8", "units": "1", "nodata": 0, "flags_definition": {"classification": {"bits": [0, 1, 2, 3, 4, 5, 6, 7], "values": {"0": "nodata", "1": "valid", "2": "cloud", "3": "shadow"}, "description": "TSmask classification"}}}], "metadata_type": "eo_plus"}	2021-01-31 22:19:39.909408+00	africa	\N
\.


--
-- Data for Name: metadata_type; Type: TABLE DATA; Schema: agdc; Owner: agdc_admin
--

COPY agdc.metadata_type (id, name, definition, added, added_by, updated) FROM stdin;
1	eo3	{"name": "eo3", "dataset": {"id": ["id"], "label": ["label"], "format": ["properties", "odc:file_format"], "sources": ["lineage", "source_datasets"], "creation_dt": ["properties", "odc:processing_datetime"], "grid_spatial": ["grid_spatial", "projection"], "measurements": ["measurements"], "search_fields": {"lat": {"type": "double-range", "max_offset": [["extent", "lat", "end"]], "min_offset": [["extent", "lat", "begin"]], "description": "Latitude range"}, "lon": {"type": "double-range", "max_offset": [["extent", "lon", "end"]], "min_offset": [["extent", "lon", "begin"]], "description": "Longitude range"}, "time": {"type": "datetime-range", "max_offset": [["properties", "dtr:end_datetime"], ["properties", "datetime"]], "min_offset": [["properties", "dtr:start_datetime"], ["properties", "datetime"]], "description": "Acquisition time range"}, "platform": {"offset": ["properties", "eo:platform"], "indexed": false, "description": "Platform code"}, "instrument": {"offset": ["properties", "eo:instrument"], "indexed": false, "description": "Instrument name"}, "region_code": {"offset": ["properties", "odc:region_code"], "description": "Spatial reference code from the provider. For Landsat region_code is a scene path row:\\n        '{:03d}{:03d}.format(path,row)'.\\nFor Sentinel it is MGRS code. In general it is a unique string identifier that datasets covering roughly the same spatial region share.\\n"}, "product_family": {"offset": ["properties", "odc:product_family"], "indexed": false, "description": "Product family code"}, "dataset_maturity": {"offset": ["properties", "dea:dataset_maturity"], "indexed": false, "description": "One of - final|interim|nrt  (near real time)"}}}, "description": "Default EO3 with no custom fields"}	2021-01-31 21:49:04.461095+00	africa	\N
2	eo	{"name": "eo", "dataset": {"id": ["id"], "label": ["ga_label"], "format": ["format", "name"], "sources": ["lineage", "source_datasets"], "creation_dt": ["creation_dt"], "grid_spatial": ["grid_spatial", "projection"], "measurements": ["image", "bands"], "search_fields": {"lat": {"type": "double-range", "max_offset": [["extent", "coord", "ur", "lat"], ["extent", "coord", "lr", "lat"], ["extent", "coord", "ul", "lat"], ["extent", "coord", "ll", "lat"]], "min_offset": [["extent", "coord", "ur", "lat"], ["extent", "coord", "lr", "lat"], ["extent", "coord", "ul", "lat"], ["extent", "coord", "ll", "lat"]], "description": "Latitude range"}, "lon": {"type": "double-range", "max_offset": [["extent", "coord", "ul", "lon"], ["extent", "coord", "ur", "lon"], ["extent", "coord", "ll", "lon"], ["extent", "coord", "lr", "lon"]], "min_offset": [["extent", "coord", "ul", "lon"], ["extent", "coord", "ur", "lon"], ["extent", "coord", "ll", "lon"], ["extent", "coord", "lr", "lon"]], "description": "Longitude range"}, "time": {"type": "datetime-range", "max_offset": [["extent", "to_dt"], ["extent", "center_dt"]], "min_offset": [["extent", "from_dt"], ["extent", "center_dt"]], "description": "Acquisition time"}, "platform": {"offset": ["platform", "code"], "description": "Platform code"}, "instrument": {"offset": ["instrument", "name"], "description": "Instrument name"}, "product_type": {"offset": ["product_type"], "description": "Product code"}}}, "description": "Earth Observation datasets.\\n\\nExpected metadata structure produced by the eodatasets library, as used internally at GA.\\n\\nhttps://github.com/GeoscienceAustralia/eo-datasets\\n"}	2021-01-31 21:49:04.485902+00	africa	\N
3	telemetry	{"name": "telemetry", "dataset": {"id": ["id"], "label": ["ga_label"], "sources": ["lineage", "source_datasets"], "creation_dt": ["creation_dt"], "search_fields": {"gsi": {"offset": ["acquisition", "groundstation", "code"], "indexed": false, "description": "Ground Station Identifier (eg. ASA)"}, "time": {"type": "datetime-range", "max_offset": [["acquisition", "los"]], "min_offset": [["acquisition", "aos"]], "description": "Acquisition time"}, "orbit": {"type": "integer", "offset": ["acquisition", "platform_orbit"], "description": "Orbit number"}, "sat_row": {"type": "integer-range", "max_offset": [["image", "satellite_ref_point_end", "y"], ["image", "satellite_ref_point_start", "y"]], "min_offset": [["image", "satellite_ref_point_start", "y"]], "description": "Landsat row"}, "platform": {"offset": ["platform", "code"], "description": "Platform code"}, "sat_path": {"type": "integer-range", "max_offset": [["image", "satellite_ref_point_end", "x"], ["image", "satellite_ref_point_start", "x"]], "min_offset": [["image", "satellite_ref_point_start", "x"]], "description": "Landsat path"}, "instrument": {"offset": ["instrument", "name"], "description": "Instrument name"}, "product_type": {"offset": ["product_type"], "description": "Product code"}}}, "description": "Satellite telemetry datasets.\\n\\nExpected metadata structure produced by telemetry datasets from the eodatasets library, as used internally at GA.\\n\\nhttps://github.com/GeoscienceAustralia/eo-datasets\\n"}	2021-01-31 21:49:04.511552+00	africa	\N
4	eo_s2_nrt	{"name": "eo_s2_nrt", "dataset": {"id": ["id"], "label": ["tile_id"], "format": ["format", "name"], "sources": ["lineage", "source_datasets"], "creation_dt": ["system_information", "time_processed"], "grid_spatial": ["grid_spatial", "projection"], "measurements": ["image", "bands"], "search_fields": {"lat": {"type": "double-range", "max_offset": [["extent", "coord", "ur", "lat"], ["extent", "coord", "lr", "lat"], ["extent", "coord", "ul", "lat"], ["extent", "coord", "ll", "lat"]], "min_offset": [["extent", "coord", "ur", "lat"], ["extent", "coord", "lr", "lat"], ["extent", "coord", "ul", "lat"], ["extent", "coord", "ll", "lat"]], "description": "Latitude range"}, "lon": {"type": "double-range", "max_offset": [["extent", "coord", "ul", "lon"], ["extent", "coord", "ur", "lon"], ["extent", "coord", "ll", "lon"], ["extent", "coord", "lr", "lon"]], "min_offset": [["extent", "coord", "ul", "lon"], ["extent", "coord", "ur", "lon"], ["extent", "coord", "ll", "lon"], ["extent", "coord", "lr", "lon"]], "description": "Longitude range"}, "time": {"type": "datetime-range", "max_offset": [["extent", "center_dt"]], "min_offset": [["extent", "center_dt"]], "description": "Acquisition time"}, "format": {"offset": ["format", "name"], "indexed": false, "description": "File format (GeoTIFF, NetCDF)"}, "platform": {"offset": ["platform", "code"], "description": "Platform code"}, "instrument": {"offset": ["instrument", "name"], "description": "Instrument name"}, "product_type": {"offset": ["product_type"], "description": "Product code"}}}, "description": "Legacy S2 NRT document structure"}	2021-01-31 22:15:37.078889+00	africa	\N
5	eo3_landsat_ard	{"name": "eo3_landsat_ard", "dataset": {"id": ["id"], "label": ["label"], "format": ["properties", "odc:file_format"], "sources": ["lineage", "source_datasets"], "creation_dt": ["properties", "odc:processing_datetime"], "grid_spatial": ["grid_spatial", "projection"], "measurements": ["measurements"], "search_fields": {"gqa": {"type": "double", "offset": ["properties", "gqa:cep90"], "description": "GQA Circular error probable (90%)"}, "lat": {"type": "double-range", "max_offset": [["extent", "lat", "end"]], "min_offset": [["extent", "lat", "begin"]], "description": "Latitude range"}, "lon": {"type": "double-range", "max_offset": [["extent", "lon", "end"]], "min_offset": [["extent", "lon", "begin"]], "description": "Longitude range"}, "time": {"type": "datetime-range", "max_offset": [["properties", "dtr:end_datetime"], ["properties", "datetime"]], "min_offset": [["properties", "dtr:start_datetime"], ["properties", "datetime"]], "description": "Acquisition time range"}, "eo_gsd": {"type": "double", "offset": ["properties", "eo:gsd"], "indexed": false, "description": "Ground sample distance, meters"}, "platform": {"offset": ["properties", "eo:platform"], "indexed": false, "description": "Platform code"}, "gqa_abs_x": {"type": "double", "offset": ["properties", "gqa:abs_x"], "indexed": false, "description": "TODO: <gqa:abs_x>"}, "gqa_abs_y": {"type": "double", "offset": ["properties", "gqa:abs_y"], "indexed": false, "description": "TODO: <gqa:abs_y>"}, "gqa_cep90": {"type": "double", "offset": ["properties", "gqa:cep90"], "indexed": false, "description": "TODO: <gqa:cep90>"}, "fmask_snow": {"type": "double", "offset": ["properties", "fmask:snow"], "indexed": false, "description": "TODO: <fmask:snow>"}, "gqa_abs_xy": {"type": "double", "offset": ["properties", "gqa:abs_xy"], "indexed": false, "description": "TODO: <gqa:abs_xy>"}, "gqa_mean_x": {"type": "double", "offset": ["properties", "gqa:mean_x"], "indexed": false, "description": "TODO: <gqa:mean_x>"}, "gqa_mean_y": {"type": "double", "offset": ["properties", "gqa:mean_y"], "indexed": false, "description": "TODO: <gqa:mean_y>"}, "instrument": {"offset": ["properties", "eo:instrument"], "indexed": false, "description": "Instrument name"}, "cloud_cover": {"type": "double", "offset": ["properties", "eo:cloud_cover"], "description": "Cloud cover percentage [0, 100]"}, "fmask_clear": {"type": "double", "offset": ["properties", "fmask:clear"], "indexed": false, "description": "TODO: <fmask:clear>"}, "fmask_water": {"type": "double", "offset": ["properties", "fmask:water"], "indexed": false, "description": "TODO: <fmask:water>"}, "gqa_mean_xy": {"type": "double", "offset": ["properties", "gqa:mean_xy"], "indexed": false, "description": "TODO: <gqa:mean_xy>"}, "region_code": {"offset": ["properties", "odc:region_code"], "description": "Spatial reference code from the provider. For Landsat region_code is a scene path row:\\n        '{:03d}{:03d}.format(path,row)'\\nFor Sentinel it is MGRS code. In general it is a unique string identifier that datasets covering roughly the same spatial region share.\\n"}, "gqa_stddev_x": {"type": "double", "offset": ["properties", "gqa:stddev_x"], "indexed": false, "description": "TODO: <gqa:stddev_x>"}, "gqa_stddev_y": {"type": "double", "offset": ["properties", "gqa:stddev_y"], "indexed": false, "description": "TODO: <gqa:stddev_y>"}, "gqa_stddev_xy": {"type": "double", "offset": ["properties", "gqa:stddev_xy"], "indexed": false, "description": "TODO: <gqa:stddev_xy>"}, "eo_sun_azimuth": {"type": "double", "offset": ["properties", "eo:sun_azimuth"], "indexed": false, "description": "TODO: <eo:sun_azimuth>"}, "product_family": {"offset": ["properties", "odc:product_family"], "indexed": false, "description": "Product family code"}, "dataset_maturity": {"offset": ["properties", "dea:dataset_maturity"], "description": "One of - final|interim|nrt  (near real time)"}, "eo_sun_elevation": {"type": "double", "offset": ["properties", "eo:sun_elevation"], "indexed": false, "description": "TODO: <eo:sun_elevation>"}, "fmask_cloud_shadow": {"type": "double", "offset": ["properties", "fmask:cloud_shadow"], "indexed": false, "description": "TODO: <fmask:cloud_shadow>"}, "gqa_iterative_mean_x": {"type": "double", "offset": ["properties", "gqa:iterative_mean_x"], "indexed": false, "description": "TODO: <gqa:iterative_mean_x>"}, "gqa_iterative_mean_y": {"type": "double", "offset": ["properties", "gqa:iterative_mean_y"], "indexed": false, "description": "TODO: <gqa:iterative_mean_y>"}, "gqa_iterative_mean_xy": {"type": "double", "offset": ["properties", "gqa:iterative_mean_xy"], "indexed": false, "description": "TODO: <gqa:iterative_mean_xy>"}, "gqa_iterative_stddev_x": {"type": "double", "offset": ["properties", "gqa:iterative_stddev_x"], "indexed": false, "description": "TODO: <gqa:iterative_stddev_x>"}, "gqa_iterative_stddev_y": {"type": "double", "offset": ["properties", "gqa:iterative_stddev_y"], "indexed": false, "description": "TODO: <gqa:iterative_stddev_y>"}, "gqa_iterative_stddev_xy": {"type": "double", "offset": ["properties", "gqa:iterative_stddev_xy"], "indexed": false, "description": "TODO: <gqa:iterative_stddev_xy>"}, "gqa_abs_iterative_mean_x": {"type": "double", "offset": ["properties", "gqa:abs_iterative_mean_x"], "indexed": false, "description": "TODO: <gqa:abs_iterative_mean_x>"}, "gqa_abs_iterative_mean_y": {"type": "double", "offset": ["properties", "gqa:abs_iterative_mean_y"], "indexed": false, "description": "TODO: <gqa:abs_iterative_mean_y>"}, "gqa_abs_iterative_mean_xy": {"type": "double", "offset": ["properties", "gqa:abs_iterative_mean_xy"], "indexed": false, "description": "TODO: <gqa:abs_iterative_mean_xy>"}}}, "description": "EO3 for ARD Landsat Collection 3"}	2021-01-31 22:17:47.699677+00	africa	\N
6	eo3_landsat_l1	{"name": "eo3_landsat_l1", "dataset": {"id": ["id"], "label": ["label"], "format": ["properties", "odc:file_format"], "sources": ["lineage", "source_datasets"], "creation_dt": ["properties", "odc:processing_datetime"], "grid_spatial": ["grid_spatial", "projection"], "measurements": ["measurements"], "search_fields": {"lat": {"type": "double-range", "max_offset": [["extent", "lat", "end"]], "min_offset": [["extent", "lat", "begin"]], "description": "Latitude range"}, "lon": {"type": "double-range", "max_offset": [["extent", "lon", "end"]], "min_offset": [["extent", "lon", "begin"]], "description": "Longitude range"}, "time": {"type": "datetime-range", "max_offset": [["properties", "dtr:end_datetime"], ["properties", "datetime"]], "min_offset": [["properties", "dtr:start_datetime"], ["properties", "datetime"]], "description": "Acquisition time range"}, "eo_gsd": {"type": "double", "offset": ["properties", "eo:gsd"], "indexed": false, "description": "Ground Sample distance, meters"}, "platform": {"offset": ["properties", "eo:platform"], "indexed": false, "description": "Platform code"}, "instrument": {"offset": ["properties", "eo:instrument"], "indexed": false, "description": "Instrument name"}, "cloud_cover": {"type": "double", "offset": ["properties", "eo:cloud_cover"], "description": "Cloud cover percentage [0, 100]"}, "region_code": {"offset": ["properties", "odc:region_code"], "description": "Spatial reference code from the provider. For Landsat region_code is a scene path row:\\n        '{:03d}{:03d}.format(path,row)'.\\nFor Sentinel it is MGRS code. In general it is a unique string identifier that datasets covering roughly the same spatial region share.\\n"}, "eo_sun_azimuth": {"type": "double", "offset": ["properties", "eo:sun_azimuth"], "indexed": false, "description": "Sun azimuth angle"}, "product_family": {"offset": ["properties", "odc:product_family"], "indexed": false, "description": "Product family code"}, "dataset_maturity": {"offset": ["properties", "dea:dataset_maturity"], "indexed": false, "description": "One of - final|interim|nrt  (near real time)"}, "eo_sun_elevation": {"type": "double", "offset": ["properties", "eo:sun_elevation"], "indexed": false, "description": "Sun elevation angle"}, "landsat_scene_id": {"offset": ["properties", "landsat:landsat_scene_id"], "indexed": false, "description": "Landsat Scene ID"}, "landsat_product_id": {"offset": ["properties", "landsat:landsat_product_id"], "indexed": false, "description": "Landsat Product ID"}}}, "description": "EO3 for Level 1 Landsat, GA Collection 3"}	2021-01-31 22:17:47.750328+00	africa	\N
7	eo_plus	{"name": "eo_plus", "dataset": {"id": ["id"], "label": ["ga_label"], "format": ["format", "name"], "sources": ["lineage", "source_datasets"], "creation_dt": ["system_information", "time_processed"], "grid_spatial": ["grid_spatial", "projection"], "measurements": ["image", "bands"], "search_fields": {"gqa": {"type": "double", "offset": ["gqa", "cep90"], "indexed": false, "description": "GQA circular error probable (90%)"}, "lat": {"type": "double-range", "max_offset": [["extent", "coord", "ur", "lat"], ["extent", "coord", "lr", "lat"], ["extent", "coord", "ul", "lat"], ["extent", "coord", "ll", "lat"]], "min_offset": [["extent", "coord", "ur", "lat"], ["extent", "coord", "lr", "lat"], ["extent", "coord", "ul", "lat"], ["extent", "coord", "ll", "lat"]], "description": "Latitude range"}, "lon": {"type": "double-range", "max_offset": [["extent", "coord", "ul", "lon"], ["extent", "coord", "ur", "lon"], ["extent", "coord", "ll", "lon"], ["extent", "coord", "lr", "lon"]], "min_offset": [["extent", "coord", "ul", "lon"], ["extent", "coord", "ur", "lon"], ["extent", "coord", "ll", "lon"], ["extent", "coord", "lr", "lon"]], "description": "Longitude range"}, "time": {"type": "datetime-range", "max_offset": [["extent", "to_dt"]], "min_offset": [["extent", "from_dt"]], "description": "Acquisition time"}, "format": {"offset": ["format", "name"], "indexed": false, "description": "File format (GeoTIFF, NetCDF)"}, "platform": {"offset": ["platform", "code"], "description": "Platform code"}, "gqa_cep90": {"type": "double", "offset": ["gqa", "residual", "cep90"], "indexed": false, "description": "Circular error probable (90%) of the values of the GCP residuals"}, "gqa_abs_xy": {"type": "double", "offset": ["gqa", "residual", "abs", "xy"], "indexed": false, "description": "Absolute value of the total GCP residual"}, "instrument": {"offset": ["instrument", "name"], "description": "Instrument name"}, "gqa_mean_xy": {"type": "double", "offset": ["gqa", "residual", "mean", "xy"], "indexed": false, "description": "Mean of the values of the GCP residuals"}, "region_code": {"offset": ["provider", "reference_code"], "description": "Spatial reference code from the provider"}, "product_type": {"offset": ["product_type"], "description": "Product code"}, "gqa_stddev_xy": {"type": "double", "offset": ["gqa", "residual", "stddev", "xy"], "indexed": false, "description": "Standard Deviation of the values of the GCP residuals"}, "gqa_ref_source": {"offset": ["gqa", "ref_source"], "indexed": false, "description": "GQA reference imagery collection name"}, "gqa_error_message": {"offset": ["gqa", "error_message"], "indexed": false, "description": "GQA error message"}, "gqa_final_qa_count": {"type": "integer", "offset": ["gqa", "final_qa_count"], "indexed": false, "description": "GQA QA point count"}, "gqa_iterative_mean_xy": {"type": "double", "offset": ["gqa", "residual", "iterative_mean", "xy"], "indexed": false, "description": "Mean of the values of the GCP residuals after removal of outliers"}, "gqa_iterative_stddev_xy": {"type": "double", "offset": ["gqa", "residual", "iterative_stddev", "xy"], "indexed": false, "description": "Standard Deviation of the values of the GCP residuals after removal of outliers"}, "gqa_abs_iterative_mean_xy": {"type": "double", "offset": ["gqa", "residual", "abs_iterative_mean", "xy"], "indexed": false, "description": "Mean of the absolute values of the GCP residuals after removal of outliers"}}}, "description": "EO metadata for DEA products with GQA."}	2021-01-31 22:17:47.780693+00	africa	\N
8	gqa_eo	{"name": "gqa_eo", "dataset": {"id": ["id"], "label": ["ga_label"], "format": ["format", "name"], "sources": ["lineage", "source_datasets"], "creation_dt": ["system_information", "time_processed"], "grid_spatial": ["grid_spatial", "projection"], "measurements": ["image", "bands"], "search_fields": {"gqa": {"type": "double", "offset": ["gqa", "cep90"], "indexed": false, "description": "GQA Circular error probable (90%)"}, "lat": {"type": "double-range", "max_offset": [["extent", "coord", "ur", "lat"], ["extent", "coord", "lr", "lat"], ["extent", "coord", "ul", "lat"], ["extent", "coord", "ll", "lat"]], "min_offset": [["extent", "coord", "ur", "lat"], ["extent", "coord", "lr", "lat"], ["extent", "coord", "ul", "lat"], ["extent", "coord", "ll", "lat"]], "description": "Latitude range"}, "lon": {"type": "double-range", "max_offset": [["extent", "coord", "ul", "lon"], ["extent", "coord", "ur", "lon"], ["extent", "coord", "ll", "lon"], ["extent", "coord", "lr", "lon"]], "min_offset": [["extent", "coord", "ul", "lon"], ["extent", "coord", "ur", "lon"], ["extent", "coord", "ll", "lon"], ["extent", "coord", "lr", "lon"]], "description": "Longitude range"}, "time": {"type": "datetime-range", "max_offset": [["extent", "to_dt"]], "min_offset": [["extent", "from_dt"]], "description": "Acquisition time"}, "format": {"offset": ["format", "name"], "indexed": false, "description": "File format (GeoTIFF, NetCDF)"}, "platform": {"offset": ["platform", "code"], "description": "Platform code"}, "gqa_cep90": {"type": "double", "offset": ["gqa", "residual", "cep90"], "indexed": false, "description": "Circular error probable (90%) of the values of the GCP residuals"}, "gqa_abs_xy": {"type": "double", "offset": ["gqa", "residual", "abs", "xy"], "indexed": false, "description": "Absolute value of the total GCP residual"}, "instrument": {"offset": ["instrument", "name"], "description": "Instrument name"}, "gqa_mean_xy": {"type": "double", "offset": ["gqa", "residual", "mean", "xy"], "indexed": false, "description": "Mean of the values of the GCP residuals"}, "region_code": {"offset": ["provider", "reference_code"], "description": "Spatial reference code from the provider"}, "product_type": {"offset": ["product_type"], "description": "Product code"}, "gqa_stddev_xy": {"type": "double", "offset": ["gqa", "residual", "stddev", "xy"], "indexed": false, "description": "Standard Deviation of the values of the GCP residuals"}, "gqa_ref_source": {"offset": ["gqa", "ref_source"], "indexed": false, "description": "GQA reference imagery collection name"}, "gqa_error_message": {"offset": ["gqa", "error_message"], "indexed": false, "description": "GQA Error Message"}, "gqa_final_gcp_count": {"type": "integer", "offset": ["gqa", "final_gcp_count"], "indexed": false, "description": "GQA GCP Count"}, "gqa_iterative_mean_xy": {"type": "double", "offset": ["gqa", "residual", "iterative_mean", "xy"], "indexed": false, "description": "Mean of the values of the GCP residuals after removal of outliers"}, "gqa_iterative_stddev_xy": {"type": "double", "offset": ["gqa", "residual", "iterative_stddev", "xy"], "indexed": false, "description": "Standard Deviation of the values of the GCP residuals after removal of outliers"}, "gqa_abs_iterative_mean_xy": {"type": "double", "offset": ["gqa", "residual", "abs_iterative_mean", "xy"], "indexed": false, "description": "Mean of the absolute values of the GCP residuals after removal of outliers"}}}, "description": "Minimal eo metadata for products with GQA."}	2021-01-31 22:17:47.818578+00	africa	\N
\.


--
-- Name: dataset_location_id_seq; Type: SEQUENCE SET; Schema: agdc; Owner: agdc_admin
--

SELECT pg_catalog.setval('agdc.dataset_location_id_seq', 1, false);


--
-- Name: dataset_type_id_seq; Type: SEQUENCE SET; Schema: agdc; Owner: agdc_admin
--

SELECT pg_catalog.setval('agdc.dataset_type_id_seq', 66, true);


--
-- Name: metadata_type_id_seq; Type: SEQUENCE SET; Schema: agdc; Owner: agdc_admin
--

SELECT pg_catalog.setval('agdc.metadata_type_id_seq', 8, true);


--
-- Name: dataset pk_dataset; Type: CONSTRAINT; Schema: agdc; Owner: agdc_admin
--

ALTER TABLE ONLY agdc.dataset
    ADD CONSTRAINT pk_dataset PRIMARY KEY (id);


--
-- Name: dataset_location pk_dataset_location; Type: CONSTRAINT; Schema: agdc; Owner: agdc_admin
--

ALTER TABLE ONLY agdc.dataset_location
    ADD CONSTRAINT pk_dataset_location PRIMARY KEY (id);


--
-- Name: dataset_source pk_dataset_source; Type: CONSTRAINT; Schema: agdc; Owner: agdc_admin
--

ALTER TABLE ONLY agdc.dataset_source
    ADD CONSTRAINT pk_dataset_source PRIMARY KEY (dataset_ref, classifier);


--
-- Name: dataset_type pk_dataset_type; Type: CONSTRAINT; Schema: agdc; Owner: agdc_admin
--

ALTER TABLE ONLY agdc.dataset_type
    ADD CONSTRAINT pk_dataset_type PRIMARY KEY (id);


--
-- Name: metadata_type pk_metadata_type; Type: CONSTRAINT; Schema: agdc; Owner: agdc_admin
--

ALTER TABLE ONLY agdc.metadata_type
    ADD CONSTRAINT pk_metadata_type PRIMARY KEY (id);


--
-- Name: dataset_location uq_dataset_location_uri_scheme; Type: CONSTRAINT; Schema: agdc; Owner: agdc_admin
--

ALTER TABLE ONLY agdc.dataset_location
    ADD CONSTRAINT uq_dataset_location_uri_scheme UNIQUE (uri_scheme, uri_body, dataset_ref);


--
-- Name: dataset_source uq_dataset_source_source_dataset_ref; Type: CONSTRAINT; Schema: agdc; Owner: agdc_admin
--

ALTER TABLE ONLY agdc.dataset_source
    ADD CONSTRAINT uq_dataset_source_source_dataset_ref UNIQUE (source_dataset_ref, dataset_ref);


--
-- Name: dataset_type uq_dataset_type_name; Type: CONSTRAINT; Schema: agdc; Owner: agdc_admin
--

ALTER TABLE ONLY agdc.dataset_type
    ADD CONSTRAINT uq_dataset_type_name UNIQUE (name);


--
-- Name: metadata_type uq_metadata_type_name; Type: CONSTRAINT; Schema: agdc; Owner: agdc_admin
--

ALTER TABLE ONLY agdc.metadata_type
    ADD CONSTRAINT uq_metadata_type_name UNIQUE (name);


--
-- Name: dix_aster_aloh_group_composition_instrument; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_aster_aloh_group_composition_instrument ON agdc.dataset USING btree (((metadata #>> '{instrument,name}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 3));


--
-- Name: dix_aster_aloh_group_composition_lat_lon_time; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_aster_aloh_group_composition_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 3));


--
-- Name: dix_aster_aloh_group_composition_platform; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_aster_aloh_group_composition_platform ON agdc.dataset USING btree (((metadata #>> '{platform,code}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 3));


--
-- Name: dix_aster_aloh_group_composition_time_lat_lon; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_aster_aloh_group_composition_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 3));


--
-- Name: dix_aster_aloh_group_content_instrument; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_aster_aloh_group_content_instrument ON agdc.dataset USING btree (((metadata #>> '{instrument,name}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 4));


--
-- Name: dix_aster_aloh_group_content_lat_lon_time; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_aster_aloh_group_content_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 4));


--
-- Name: dix_aster_aloh_group_content_platform; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_aster_aloh_group_content_platform ON agdc.dataset USING btree (((metadata #>> '{platform,code}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 4));


--
-- Name: dix_aster_aloh_group_content_time_lat_lon; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_aster_aloh_group_content_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 4));


--
-- Name: dix_aster_false_colour_instrument; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_aster_false_colour_instrument ON agdc.dataset USING btree (((metadata #>> '{instrument,name}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 5));


--
-- Name: dix_aster_false_colour_lat_lon_time; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_aster_false_colour_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 5));


--
-- Name: dix_aster_false_colour_platform; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_aster_false_colour_platform ON agdc.dataset USING btree (((metadata #>> '{platform,code}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 5));


--
-- Name: dix_aster_false_colour_time_lat_lon; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_aster_false_colour_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 5));


--
-- Name: dix_aster_feoh_group_content_instrument; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_aster_feoh_group_content_instrument ON agdc.dataset USING btree (((metadata #>> '{instrument,name}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 6));


--
-- Name: dix_aster_feoh_group_content_lat_lon_time; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_aster_feoh_group_content_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 6));


--
-- Name: dix_aster_feoh_group_content_platform; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_aster_feoh_group_content_platform ON agdc.dataset USING btree (((metadata #>> '{platform,code}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 6));


--
-- Name: dix_aster_feoh_group_content_time_lat_lon; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_aster_feoh_group_content_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 6));


--
-- Name: dix_aster_ferric_oxide_composition_instrument; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_aster_ferric_oxide_composition_instrument ON agdc.dataset USING btree (((metadata #>> '{instrument,name}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 7));


--
-- Name: dix_aster_ferric_oxide_composition_lat_lon_time; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_aster_ferric_oxide_composition_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 7));


--
-- Name: dix_aster_ferric_oxide_composition_platform; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_aster_ferric_oxide_composition_platform ON agdc.dataset USING btree (((metadata #>> '{platform,code}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 7));


--
-- Name: dix_aster_ferric_oxide_composition_time_lat_lon; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_aster_ferric_oxide_composition_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 7));


--
-- Name: dix_aster_ferric_oxide_content_instrument; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_aster_ferric_oxide_content_instrument ON agdc.dataset USING btree (((metadata #>> '{instrument,name}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 8));


--
-- Name: dix_aster_ferric_oxide_content_lat_lon_time; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_aster_ferric_oxide_content_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 8));


--
-- Name: dix_aster_ferric_oxide_content_platform; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_aster_ferric_oxide_content_platform ON agdc.dataset USING btree (((metadata #>> '{platform,code}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 8));


--
-- Name: dix_aster_ferric_oxide_content_time_lat_lon; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_aster_ferric_oxide_content_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 8));


--
-- Name: dix_aster_ferrous_iron_content_in_mgoh_instrument; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_aster_ferrous_iron_content_in_mgoh_instrument ON agdc.dataset USING btree (((metadata #>> '{instrument,name}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 9));


--
-- Name: dix_aster_ferrous_iron_content_in_mgoh_lat_lon_time; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_aster_ferrous_iron_content_in_mgoh_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 9));


--
-- Name: dix_aster_ferrous_iron_content_in_mgoh_platform; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_aster_ferrous_iron_content_in_mgoh_platform ON agdc.dataset USING btree (((metadata #>> '{platform,code}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 9));


--
-- Name: dix_aster_ferrous_iron_content_in_mgoh_time_lat_lon; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_aster_ferrous_iron_content_in_mgoh_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 9));


--
-- Name: dix_aster_ferrous_iron_index_instrument; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_aster_ferrous_iron_index_instrument ON agdc.dataset USING btree (((metadata #>> '{instrument,name}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 10));


--
-- Name: dix_aster_ferrous_iron_index_lat_lon_time; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_aster_ferrous_iron_index_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 10));


--
-- Name: dix_aster_ferrous_iron_index_platform; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_aster_ferrous_iron_index_platform ON agdc.dataset USING btree (((metadata #>> '{platform,code}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 10));


--
-- Name: dix_aster_ferrous_iron_index_time_lat_lon; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_aster_ferrous_iron_index_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 10));


--
-- Name: dix_aster_green_vegetation_instrument; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_aster_green_vegetation_instrument ON agdc.dataset USING btree (((metadata #>> '{instrument,name}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 11));


--
-- Name: dix_aster_green_vegetation_lat_lon_time; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_aster_green_vegetation_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 11));


--
-- Name: dix_aster_green_vegetation_platform; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_aster_green_vegetation_platform ON agdc.dataset USING btree (((metadata #>> '{platform,code}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 11));


--
-- Name: dix_aster_green_vegetation_time_lat_lon; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_aster_green_vegetation_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 11));


--
-- Name: dix_aster_gypsum_index_instrument; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_aster_gypsum_index_instrument ON agdc.dataset USING btree (((metadata #>> '{instrument,name}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 12));


--
-- Name: dix_aster_gypsum_index_lat_lon_time; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_aster_gypsum_index_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 12));


--
-- Name: dix_aster_gypsum_index_platform; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_aster_gypsum_index_platform ON agdc.dataset USING btree (((metadata #>> '{platform,code}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 12));


--
-- Name: dix_aster_gypsum_index_time_lat_lon; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_aster_gypsum_index_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 12));


--
-- Name: dix_aster_kaolin_group_index_instrument; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_aster_kaolin_group_index_instrument ON agdc.dataset USING btree (((metadata #>> '{instrument,name}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 13));


--
-- Name: dix_aster_kaolin_group_index_lat_lon_time; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_aster_kaolin_group_index_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 13));


--
-- Name: dix_aster_kaolin_group_index_platform; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_aster_kaolin_group_index_platform ON agdc.dataset USING btree (((metadata #>> '{platform,code}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 13));


--
-- Name: dix_aster_kaolin_group_index_time_lat_lon; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_aster_kaolin_group_index_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 13));


--
-- Name: dix_aster_mgoh_group_composition_instrument; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_aster_mgoh_group_composition_instrument ON agdc.dataset USING btree (((metadata #>> '{instrument,name}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 14));


--
-- Name: dix_aster_mgoh_group_composition_lat_lon_time; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_aster_mgoh_group_composition_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 14));


--
-- Name: dix_aster_mgoh_group_composition_platform; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_aster_mgoh_group_composition_platform ON agdc.dataset USING btree (((metadata #>> '{platform,code}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 14));


--
-- Name: dix_aster_mgoh_group_composition_time_lat_lon; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_aster_mgoh_group_composition_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 14));


--
-- Name: dix_aster_mgoh_group_content_instrument; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_aster_mgoh_group_content_instrument ON agdc.dataset USING btree (((metadata #>> '{instrument,name}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 15));


--
-- Name: dix_aster_mgoh_group_content_lat_lon_time; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_aster_mgoh_group_content_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 15));


--
-- Name: dix_aster_mgoh_group_content_platform; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_aster_mgoh_group_content_platform ON agdc.dataset USING btree (((metadata #>> '{platform,code}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 15));


--
-- Name: dix_aster_mgoh_group_content_time_lat_lon; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_aster_mgoh_group_content_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 15));


--
-- Name: dix_aster_opaque_index_instrument; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_aster_opaque_index_instrument ON agdc.dataset USING btree (((metadata #>> '{instrument,name}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 16));


--
-- Name: dix_aster_opaque_index_lat_lon_time; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_aster_opaque_index_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 16));


--
-- Name: dix_aster_opaque_index_platform; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_aster_opaque_index_platform ON agdc.dataset USING btree (((metadata #>> '{platform,code}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 16));


--
-- Name: dix_aster_opaque_index_time_lat_lon; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_aster_opaque_index_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 16));


--
-- Name: dix_aster_quartz_index_instrument; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_aster_quartz_index_instrument ON agdc.dataset USING btree (((metadata #>> '{instrument,name}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 17));


--
-- Name: dix_aster_quartz_index_lat_lon_time; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_aster_quartz_index_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 17));


--
-- Name: dix_aster_quartz_index_platform; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_aster_quartz_index_platform ON agdc.dataset USING btree (((metadata #>> '{platform,code}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 17));


--
-- Name: dix_aster_quartz_index_time_lat_lon; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_aster_quartz_index_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 17));


--
-- Name: dix_aster_regolith_ratios_instrument; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_aster_regolith_ratios_instrument ON agdc.dataset USING btree (((metadata #>> '{instrument,name}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 18));


--
-- Name: dix_aster_regolith_ratios_lat_lon_time; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_aster_regolith_ratios_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 18));


--
-- Name: dix_aster_regolith_ratios_platform; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_aster_regolith_ratios_platform ON agdc.dataset USING btree (((metadata #>> '{platform,code}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 18));


--
-- Name: dix_aster_regolith_ratios_time_lat_lon; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_aster_regolith_ratios_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 18));


--
-- Name: dix_aster_silica_index_instrument; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_aster_silica_index_instrument ON agdc.dataset USING btree (((metadata #>> '{instrument,name}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 19));


--
-- Name: dix_aster_silica_index_lat_lon_time; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_aster_silica_index_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 19));


--
-- Name: dix_aster_silica_index_platform; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_aster_silica_index_platform ON agdc.dataset USING btree (((metadata #>> '{platform,code}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 19));


--
-- Name: dix_aster_silica_index_time_lat_lon; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_aster_silica_index_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 19));


--
-- Name: dix_cemp_insar_alos_displacement_lat_lon_time; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_cemp_insar_alos_displacement_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(((metadata #>> '{extent,lat,begin}'::text[]))::double precision, ((metadata #>> '{extent,lat,end}'::text[]))::double precision, '[]'::text), agdc.float8range(((metadata #>> '{extent,lon,begin}'::text[]))::double precision, ((metadata #>> '{extent,lon,end}'::text[]))::double precision, '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{properties,dtr:start_datetime}'::text[])), agdc.common_timestamp((metadata #>> '{properties,datetime}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{properties,dtr:end_datetime}'::text[])), agdc.common_timestamp((metadata #>> '{properties,datetime}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 20));


--
-- Name: dix_cemp_insar_alos_displacement_region_code; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_cemp_insar_alos_displacement_region_code ON agdc.dataset USING btree (((metadata #>> '{properties,odc:region_code}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 20));


--
-- Name: dix_cemp_insar_alos_displacement_time_lat_lon; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_cemp_insar_alos_displacement_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{properties,dtr:start_datetime}'::text[])), agdc.common_timestamp((metadata #>> '{properties,datetime}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{properties,dtr:end_datetime}'::text[])), agdc.common_timestamp((metadata #>> '{properties,datetime}'::text[]))), '[]'::text), agdc.float8range(((metadata #>> '{extent,lat,begin}'::text[]))::double precision, ((metadata #>> '{extent,lat,end}'::text[]))::double precision, '[]'::text), agdc.float8range(((metadata #>> '{extent,lon,begin}'::text[]))::double precision, ((metadata #>> '{extent,lon,end}'::text[]))::double precision, '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 20));


--
-- Name: dix_cemp_insar_alos_velocity_lat_lon_time; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_cemp_insar_alos_velocity_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(((metadata #>> '{extent,lat,begin}'::text[]))::double precision, ((metadata #>> '{extent,lat,end}'::text[]))::double precision, '[]'::text), agdc.float8range(((metadata #>> '{extent,lon,begin}'::text[]))::double precision, ((metadata #>> '{extent,lon,end}'::text[]))::double precision, '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{properties,dtr:start_datetime}'::text[])), agdc.common_timestamp((metadata #>> '{properties,datetime}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{properties,dtr:end_datetime}'::text[])), agdc.common_timestamp((metadata #>> '{properties,datetime}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 21));


--
-- Name: dix_cemp_insar_alos_velocity_region_code; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_cemp_insar_alos_velocity_region_code ON agdc.dataset USING btree (((metadata #>> '{properties,odc:region_code}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 21));


--
-- Name: dix_cemp_insar_alos_velocity_time_lat_lon; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_cemp_insar_alos_velocity_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{properties,dtr:start_datetime}'::text[])), agdc.common_timestamp((metadata #>> '{properties,datetime}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{properties,dtr:end_datetime}'::text[])), agdc.common_timestamp((metadata #>> '{properties,datetime}'::text[]))), '[]'::text), agdc.float8range(((metadata #>> '{extent,lat,begin}'::text[]))::double precision, ((metadata #>> '{extent,lat,end}'::text[]))::double precision, '[]'::text), agdc.float8range(((metadata #>> '{extent,lon,begin}'::text[]))::double precision, ((metadata #>> '{extent,lon,end}'::text[]))::double precision, '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 21));


--
-- Name: dix_cemp_insar_envisat_displacement_lat_lon_time; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_cemp_insar_envisat_displacement_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(((metadata #>> '{extent,lat,begin}'::text[]))::double precision, ((metadata #>> '{extent,lat,end}'::text[]))::double precision, '[]'::text), agdc.float8range(((metadata #>> '{extent,lon,begin}'::text[]))::double precision, ((metadata #>> '{extent,lon,end}'::text[]))::double precision, '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{properties,dtr:start_datetime}'::text[])), agdc.common_timestamp((metadata #>> '{properties,datetime}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{properties,dtr:end_datetime}'::text[])), agdc.common_timestamp((metadata #>> '{properties,datetime}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 22));


--
-- Name: dix_cemp_insar_envisat_displacement_region_code; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_cemp_insar_envisat_displacement_region_code ON agdc.dataset USING btree (((metadata #>> '{properties,odc:region_code}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 22));


--
-- Name: dix_cemp_insar_envisat_displacement_time_lat_lon; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_cemp_insar_envisat_displacement_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{properties,dtr:start_datetime}'::text[])), agdc.common_timestamp((metadata #>> '{properties,datetime}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{properties,dtr:end_datetime}'::text[])), agdc.common_timestamp((metadata #>> '{properties,datetime}'::text[]))), '[]'::text), agdc.float8range(((metadata #>> '{extent,lat,begin}'::text[]))::double precision, ((metadata #>> '{extent,lat,end}'::text[]))::double precision, '[]'::text), agdc.float8range(((metadata #>> '{extent,lon,begin}'::text[]))::double precision, ((metadata #>> '{extent,lon,end}'::text[]))::double precision, '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 22));


--
-- Name: dix_cemp_insar_envisat_velocity_lat_lon_time; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_cemp_insar_envisat_velocity_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(((metadata #>> '{extent,lat,begin}'::text[]))::double precision, ((metadata #>> '{extent,lat,end}'::text[]))::double precision, '[]'::text), agdc.float8range(((metadata #>> '{extent,lon,begin}'::text[]))::double precision, ((metadata #>> '{extent,lon,end}'::text[]))::double precision, '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{properties,dtr:start_datetime}'::text[])), agdc.common_timestamp((metadata #>> '{properties,datetime}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{properties,dtr:end_datetime}'::text[])), agdc.common_timestamp((metadata #>> '{properties,datetime}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 23));


--
-- Name: dix_cemp_insar_envisat_velocity_region_code; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_cemp_insar_envisat_velocity_region_code ON agdc.dataset USING btree (((metadata #>> '{properties,odc:region_code}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 23));


--
-- Name: dix_cemp_insar_envisat_velocity_time_lat_lon; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_cemp_insar_envisat_velocity_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{properties,dtr:start_datetime}'::text[])), agdc.common_timestamp((metadata #>> '{properties,datetime}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{properties,dtr:end_datetime}'::text[])), agdc.common_timestamp((metadata #>> '{properties,datetime}'::text[]))), '[]'::text), agdc.float8range(((metadata #>> '{extent,lat,begin}'::text[]))::double precision, ((metadata #>> '{extent,lat,end}'::text[]))::double precision, '[]'::text), agdc.float8range(((metadata #>> '{extent,lon,begin}'::text[]))::double precision, ((metadata #>> '{extent,lon,end}'::text[]))::double precision, '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 23));


--
-- Name: dix_cemp_insar_radarsat2_displacement_lat_lon_time; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_cemp_insar_radarsat2_displacement_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(((metadata #>> '{extent,lat,begin}'::text[]))::double precision, ((metadata #>> '{extent,lat,end}'::text[]))::double precision, '[]'::text), agdc.float8range(((metadata #>> '{extent,lon,begin}'::text[]))::double precision, ((metadata #>> '{extent,lon,end}'::text[]))::double precision, '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{properties,dtr:start_datetime}'::text[])), agdc.common_timestamp((metadata #>> '{properties,datetime}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{properties,dtr:end_datetime}'::text[])), agdc.common_timestamp((metadata #>> '{properties,datetime}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 24));


--
-- Name: dix_cemp_insar_radarsat2_displacement_region_code; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_cemp_insar_radarsat2_displacement_region_code ON agdc.dataset USING btree (((metadata #>> '{properties,odc:region_code}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 24));


--
-- Name: dix_cemp_insar_radarsat2_displacement_time_lat_lon; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_cemp_insar_radarsat2_displacement_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{properties,dtr:start_datetime}'::text[])), agdc.common_timestamp((metadata #>> '{properties,datetime}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{properties,dtr:end_datetime}'::text[])), agdc.common_timestamp((metadata #>> '{properties,datetime}'::text[]))), '[]'::text), agdc.float8range(((metadata #>> '{extent,lat,begin}'::text[]))::double precision, ((metadata #>> '{extent,lat,end}'::text[]))::double precision, '[]'::text), agdc.float8range(((metadata #>> '{extent,lon,begin}'::text[]))::double precision, ((metadata #>> '{extent,lon,end}'::text[]))::double precision, '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 24));


--
-- Name: dix_cemp_insar_radarsat2_velocity_lat_lon_time; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_cemp_insar_radarsat2_velocity_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(((metadata #>> '{extent,lat,begin}'::text[]))::double precision, ((metadata #>> '{extent,lat,end}'::text[]))::double precision, '[]'::text), agdc.float8range(((metadata #>> '{extent,lon,begin}'::text[]))::double precision, ((metadata #>> '{extent,lon,end}'::text[]))::double precision, '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{properties,dtr:start_datetime}'::text[])), agdc.common_timestamp((metadata #>> '{properties,datetime}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{properties,dtr:end_datetime}'::text[])), agdc.common_timestamp((metadata #>> '{properties,datetime}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 25));


--
-- Name: dix_cemp_insar_radarsat2_velocity_region_code; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_cemp_insar_radarsat2_velocity_region_code ON agdc.dataset USING btree (((metadata #>> '{properties,odc:region_code}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 25));


--
-- Name: dix_cemp_insar_radarsat2_velocity_time_lat_lon; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_cemp_insar_radarsat2_velocity_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{properties,dtr:start_datetime}'::text[])), agdc.common_timestamp((metadata #>> '{properties,datetime}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{properties,dtr:end_datetime}'::text[])), agdc.common_timestamp((metadata #>> '{properties,datetime}'::text[]))), '[]'::text), agdc.float8range(((metadata #>> '{extent,lat,begin}'::text[]))::double precision, ((metadata #>> '{extent,lat,end}'::text[]))::double precision, '[]'::text), agdc.float8range(((metadata #>> '{extent,lon,begin}'::text[]))::double precision, ((metadata #>> '{extent,lon,end}'::text[]))::double precision, '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 25));


--
-- Name: dix_fc_percentile_albers_annual_lat_lon_time; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_fc_percentile_albers_annual_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 26));


--
-- Name: dix_fc_percentile_albers_annual_time_lat_lon; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_fc_percentile_albers_annual_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 26));


--
-- Name: dix_fc_percentile_albers_seasonal_lat_lon_time; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_fc_percentile_albers_seasonal_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 27));


--
-- Name: dix_fc_percentile_albers_seasonal_time_lat_lon; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_fc_percentile_albers_seasonal_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 27));


--
-- Name: dix_ga_ls8c_ard_3_cloud_cover; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_ga_ls8c_ard_3_cloud_cover ON agdc.dataset USING btree ((((metadata #>> '{properties,eo:cloud_cover}'::text[]))::double precision)) WHERE ((archived IS NULL) AND (dataset_type_ref = 61));


--
-- Name: dix_ga_ls8c_ard_3_dataset_maturity; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_ga_ls8c_ard_3_dataset_maturity ON agdc.dataset USING btree (((metadata #>> '{properties,dea:dataset_maturity}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 61));


--
-- Name: dix_ga_ls8c_ard_3_gqa; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_ga_ls8c_ard_3_gqa ON agdc.dataset USING btree ((((metadata #>> '{properties,gqa:cep90}'::text[]))::double precision)) WHERE ((archived IS NULL) AND (dataset_type_ref = 61));


--
-- Name: dix_ga_ls8c_ard_3_lat_lon_time; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_ga_ls8c_ard_3_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(((metadata #>> '{extent,lat,begin}'::text[]))::double precision, ((metadata #>> '{extent,lat,end}'::text[]))::double precision, '[]'::text), agdc.float8range(((metadata #>> '{extent,lon,begin}'::text[]))::double precision, ((metadata #>> '{extent,lon,end}'::text[]))::double precision, '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{properties,dtr:start_datetime}'::text[])), agdc.common_timestamp((metadata #>> '{properties,datetime}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{properties,dtr:end_datetime}'::text[])), agdc.common_timestamp((metadata #>> '{properties,datetime}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 61));


--
-- Name: dix_ga_ls8c_ard_3_region_code; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_ga_ls8c_ard_3_region_code ON agdc.dataset USING btree (((metadata #>> '{properties,odc:region_code}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 61));


--
-- Name: dix_ga_ls8c_ard_3_time_lat_lon; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_ga_ls8c_ard_3_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{properties,dtr:start_datetime}'::text[])), agdc.common_timestamp((metadata #>> '{properties,datetime}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{properties,dtr:end_datetime}'::text[])), agdc.common_timestamp((metadata #>> '{properties,datetime}'::text[]))), '[]'::text), agdc.float8range(((metadata #>> '{extent,lat,begin}'::text[]))::double precision, ((metadata #>> '{extent,lat,end}'::text[]))::double precision, '[]'::text), agdc.float8range(((metadata #>> '{extent,lon,begin}'::text[]))::double precision, ((metadata #>> '{extent,lon,end}'::text[]))::double precision, '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 61));


--
-- Name: dix_ga_s2a_ard_nbar_granule_lat_lon_time; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_ga_s2a_ard_nbar_granule_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 62));


--
-- Name: dix_ga_s2a_ard_nbar_granule_region_code; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_ga_s2a_ard_nbar_granule_region_code ON agdc.dataset USING btree (((metadata #>> '{provider,reference_code}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 62));


--
-- Name: dix_ga_s2a_ard_nbar_granule_time_lat_lon; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_ga_s2a_ard_nbar_granule_time_lat_lon ON agdc.dataset USING gist (tstzrange(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 62));


--
-- Name: dix_ga_s2b_ard_nbar_granule_lat_lon_time; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_ga_s2b_ard_nbar_granule_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 63));


--
-- Name: dix_ga_s2b_ard_nbar_granule_region_code; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_ga_s2b_ard_nbar_granule_region_code ON agdc.dataset USING btree (((metadata #>> '{provider,reference_code}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 63));


--
-- Name: dix_ga_s2b_ard_nbar_granule_time_lat_lon; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_ga_s2b_ard_nbar_granule_time_lat_lon ON agdc.dataset USING gist (tstzrange(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 63));


--
-- Name: dix_geodata_coast_100k_lat_lon_time; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_geodata_coast_100k_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 28));


--
-- Name: dix_geodata_coast_100k_time_lat_lon; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_geodata_coast_100k_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 28));


--
-- Name: dix_high_tide_comp_20p_instrument; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_high_tide_comp_20p_instrument ON agdc.dataset USING btree (((metadata #>> '{instrument,name}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 29));


--
-- Name: dix_high_tide_comp_20p_lat_lon_time; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_high_tide_comp_20p_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 29));


--
-- Name: dix_high_tide_comp_20p_platform; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_high_tide_comp_20p_platform ON agdc.dataset USING btree (((metadata #>> '{platform,code}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 29));


--
-- Name: dix_high_tide_comp_20p_time_lat_lon; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_high_tide_comp_20p_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 29));


--
-- Name: dix_historical_airborne_photography_instrument; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_historical_airborne_photography_instrument ON agdc.dataset USING btree (((metadata #>> '{instrument,name}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 31));


--
-- Name: dix_historical_airborne_photography_lat_lon_time; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_historical_airborne_photography_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 31));


--
-- Name: dix_historical_airborne_photography_platform; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_historical_airborne_photography_platform ON agdc.dataset USING btree (((metadata #>> '{platform,code}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 31));


--
-- Name: dix_historical_airborne_photography_time_lat_lon; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_historical_airborne_photography_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 31));


--
-- Name: dix_item_v2_conf_instrument; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_item_v2_conf_instrument ON agdc.dataset USING btree (((metadata #>> '{instrument,name}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 33));


--
-- Name: dix_item_v2_conf_lat_lon_time; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_item_v2_conf_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 33));


--
-- Name: dix_item_v2_conf_platform; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_item_v2_conf_platform ON agdc.dataset USING btree (((metadata #>> '{platform,code}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 33));


--
-- Name: dix_item_v2_conf_time_lat_lon; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_item_v2_conf_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 33));


--
-- Name: dix_item_v2_instrument; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_item_v2_instrument ON agdc.dataset USING btree (((metadata #>> '{instrument,name}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 32));


--
-- Name: dix_item_v2_lat_lon_time; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_item_v2_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 32));


--
-- Name: dix_item_v2_platform; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_item_v2_platform ON agdc.dataset USING btree (((metadata #>> '{platform,code}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 32));


--
-- Name: dix_item_v2_time_lat_lon; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_item_v2_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 32));


--
-- Name: dix_landsat_barest_earth_lat_lon_time; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_landsat_barest_earth_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 34));


--
-- Name: dix_landsat_barest_earth_time_lat_lon; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_landsat_barest_earth_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 34));


--
-- Name: dix_low_tide_comp_20p_instrument; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_low_tide_comp_20p_instrument ON agdc.dataset USING btree (((metadata #>> '{instrument,name}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 30));


--
-- Name: dix_low_tide_comp_20p_lat_lon_time; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_low_tide_comp_20p_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 30));


--
-- Name: dix_low_tide_comp_20p_platform; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_low_tide_comp_20p_platform ON agdc.dataset USING btree (((metadata #>> '{platform,code}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 30));


--
-- Name: dix_low_tide_comp_20p_time_lat_lon; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_low_tide_comp_20p_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 30));


--
-- Name: dix_ls5_fc_albers_lat_lon_time; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_ls5_fc_albers_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 35));


--
-- Name: dix_ls5_fc_albers_time_lat_lon; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_ls5_fc_albers_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 35));


--
-- Name: dix_ls5_level1_usgs_lat_lon_time; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_ls5_level1_usgs_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 1));


--
-- Name: dix_ls5_level1_usgs_time_lat_lon; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_ls5_level1_usgs_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 1));


--
-- Name: dix_ls5_nbart_geomedian_annual_lat_lon_time; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_ls5_nbart_geomedian_annual_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 38));


--
-- Name: dix_ls5_nbart_geomedian_annual_time_lat_lon; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_ls5_nbart_geomedian_annual_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 38));


--
-- Name: dix_ls5_nbart_tmad_annual_lat_lon_time; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_ls5_nbart_tmad_annual_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 41));


--
-- Name: dix_ls5_nbart_tmad_annual_time_lat_lon; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_ls5_nbart_tmad_annual_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 41));


--
-- Name: dix_ls5_usgs_l2c1_lat_lon_time; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_ls5_usgs_l2c1_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 42));


--
-- Name: dix_ls5_usgs_l2c1_time_lat_lon; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_ls5_usgs_l2c1_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 42));


--
-- Name: dix_ls7_fc_albers_lat_lon_time; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_ls7_fc_albers_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 43));


--
-- Name: dix_ls7_fc_albers_time_lat_lon; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_ls7_fc_albers_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 43));


--
-- Name: dix_ls7_level1_usgs_lat_lon_time; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_ls7_level1_usgs_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 2));


--
-- Name: dix_ls7_level1_usgs_time_lat_lon; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_ls7_level1_usgs_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 2));


--
-- Name: dix_ls7_nbart_geomedian_annual_lat_lon_time; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_ls7_nbart_geomedian_annual_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 37));


--
-- Name: dix_ls7_nbart_geomedian_annual_time_lat_lon; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_ls7_nbart_geomedian_annual_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 37));


--
-- Name: dix_ls7_nbart_tmad_annual_lat_lon_time; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_ls7_nbart_tmad_annual_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 40));


--
-- Name: dix_ls7_nbart_tmad_annual_time_lat_lon; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_ls7_nbart_tmad_annual_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 40));


--
-- Name: dix_ls7_usgs_l2c1_lat_lon_time; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_ls7_usgs_l2c1_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 44));


--
-- Name: dix_ls7_usgs_l2c1_time_lat_lon; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_ls7_usgs_l2c1_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 44));


--
-- Name: dix_ls8_barest_earth_albers_lat_lon_time; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_ls8_barest_earth_albers_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 45));


--
-- Name: dix_ls8_barest_earth_albers_time_lat_lon; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_ls8_barest_earth_albers_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 45));


--
-- Name: dix_ls8_fc_albers_lat_lon_time; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_ls8_fc_albers_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 46));


--
-- Name: dix_ls8_fc_albers_time_lat_lon; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_ls8_fc_albers_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 46));


--
-- Name: dix_ls8_level1_usgs_instrument; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_ls8_level1_usgs_instrument ON agdc.dataset USING btree (((metadata #>> '{instrument,name}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 47));


--
-- Name: dix_ls8_level1_usgs_lat_lon_time; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_ls8_level1_usgs_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 47));


--
-- Name: dix_ls8_level1_usgs_platform; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_ls8_level1_usgs_platform ON agdc.dataset USING btree (((metadata #>> '{platform,code}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 47));


--
-- Name: dix_ls8_level1_usgs_time_lat_lon; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_ls8_level1_usgs_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 47));


--
-- Name: dix_ls8_nbart_geomedian_annual_lat_lon_time; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_ls8_nbart_geomedian_annual_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 36));


--
-- Name: dix_ls8_nbart_geomedian_annual_time_lat_lon; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_ls8_nbart_geomedian_annual_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 36));


--
-- Name: dix_ls8_nbart_tmad_annual_lat_lon_time; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_ls8_nbart_tmad_annual_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 39));


--
-- Name: dix_ls8_nbart_tmad_annual_time_lat_lon; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_ls8_nbart_tmad_annual_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 39));


--
-- Name: dix_ls8_usgs_l2c1_lat_lon_time; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_ls8_usgs_l2c1_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 48));


--
-- Name: dix_ls8_usgs_l2c1_time_lat_lon; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_ls8_usgs_l2c1_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 48));


--
-- Name: dix_mangrove_cover_lat_lon_time; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_mangrove_cover_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 49));


--
-- Name: dix_mangrove_cover_time_lat_lon; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_mangrove_cover_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 49));


--
-- Name: dix_multi_scale_topographic_position_instrument; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_multi_scale_topographic_position_instrument ON agdc.dataset USING btree (((metadata #>> '{instrument,name}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 50));


--
-- Name: dix_multi_scale_topographic_position_lat_lon_time; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_multi_scale_topographic_position_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 50));


--
-- Name: dix_multi_scale_topographic_position_platform; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_multi_scale_topographic_position_platform ON agdc.dataset USING btree (((metadata #>> '{platform,code}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 50));


--
-- Name: dix_multi_scale_topographic_position_time_lat_lon; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_multi_scale_topographic_position_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 50));


--
-- Name: dix_nidem_instrument; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_nidem_instrument ON agdc.dataset USING btree (((metadata #>> '{instrument,name}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 51));


--
-- Name: dix_nidem_lat_lon_time; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_nidem_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 51));


--
-- Name: dix_nidem_platform; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_nidem_platform ON agdc.dataset USING btree (((metadata #>> '{platform,code}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 51));


--
-- Name: dix_nidem_time_lat_lon; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_nidem_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 51));


--
-- Name: dix_s2_tsmask_lat_lon_time; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_s2_tsmask_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 66));


--
-- Name: dix_s2_tsmask_region_code; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_s2_tsmask_region_code ON agdc.dataset USING btree (((metadata #>> '{provider,reference_code}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 66));


--
-- Name: dix_s2_tsmask_time_lat_lon; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_s2_tsmask_time_lat_lon ON agdc.dataset USING gist (tstzrange(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 66));


--
-- Name: dix_s2a_nrt_granule_lat_lon_time; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_s2a_nrt_granule_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[])), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 64));


--
-- Name: dix_s2a_nrt_granule_time_lat_lon; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_s2a_nrt_granule_time_lat_lon ON agdc.dataset USING gist (tstzrange(agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[])), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 64));


--
-- Name: dix_s2b_nrt_granule_lat_lon_time; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_s2b_nrt_granule_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[])), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 65));


--
-- Name: dix_s2b_nrt_granule_time_lat_lon; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_s2b_nrt_granule_time_lat_lon ON agdc.dataset USING gist (tstzrange(agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[])), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 65));


--
-- Name: dix_sentinel2_wofs_nrt_lat_lon_time; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_sentinel2_wofs_nrt_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 52));


--
-- Name: dix_sentinel2_wofs_nrt_platform; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_sentinel2_wofs_nrt_platform ON agdc.dataset USING btree (((metadata #>> '{platform,code}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 52));


--
-- Name: dix_sentinel2_wofs_nrt_time_lat_lon; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_sentinel2_wofs_nrt_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 52));


--
-- Name: dix_water_bodies_instrument; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_water_bodies_instrument ON agdc.dataset USING btree (((metadata #>> '{instrument,name}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 53));


--
-- Name: dix_water_bodies_lat_lon_time; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_water_bodies_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 53));


--
-- Name: dix_water_bodies_platform; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_water_bodies_platform ON agdc.dataset USING btree (((metadata #>> '{platform,code}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 53));


--
-- Name: dix_water_bodies_time_lat_lon; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_water_bodies_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 53));


--
-- Name: dix_weathering_intensity_lat_lon_time; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_weathering_intensity_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 54));


--
-- Name: dix_weathering_intensity_time_lat_lon; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_weathering_intensity_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 54));


--
-- Name: dix_wofs_albers_instrument; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_wofs_albers_instrument ON agdc.dataset USING btree (((metadata #>> '{instrument,name}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 55));


--
-- Name: dix_wofs_albers_lat_lon_time; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_wofs_albers_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 55));


--
-- Name: dix_wofs_albers_platform; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_wofs_albers_platform ON agdc.dataset USING btree (((metadata #>> '{platform,code}'::text[]))) WHERE ((archived IS NULL) AND (dataset_type_ref = 55));


--
-- Name: dix_wofs_albers_time_lat_lon; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_wofs_albers_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 55));


--
-- Name: dix_wofs_annual_summary_lat_lon_time; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_wofs_annual_summary_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 56));


--
-- Name: dix_wofs_annual_summary_time_lat_lon; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_wofs_annual_summary_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 56));


--
-- Name: dix_wofs_apr_oct_summary_lat_lon_time; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_wofs_apr_oct_summary_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 57));


--
-- Name: dix_wofs_apr_oct_summary_time_lat_lon; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_wofs_apr_oct_summary_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 57));


--
-- Name: dix_wofs_filtered_summary_lat_lon_time; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_wofs_filtered_summary_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 58));


--
-- Name: dix_wofs_filtered_summary_time_lat_lon; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_wofs_filtered_summary_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 58));


--
-- Name: dix_wofs_nov_mar_summary_lat_lon_time; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_wofs_nov_mar_summary_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 59));


--
-- Name: dix_wofs_nov_mar_summary_time_lat_lon; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_wofs_nov_mar_summary_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 59));


--
-- Name: dix_wofs_summary_lat_lon_time; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_wofs_summary_lat_lon_time ON agdc.dataset USING gist (agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text), tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 60));


--
-- Name: dix_wofs_summary_time_lat_lon; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX dix_wofs_summary_time_lat_lon ON agdc.dataset USING gist (tstzrange(LEAST(agdc.common_timestamp((metadata #>> '{extent,from_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), GREATEST(agdc.common_timestamp((metadata #>> '{extent,to_dt}'::text[])), agdc.common_timestamp((metadata #>> '{extent,center_dt}'::text[]))), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ur,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ul,lat}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lat}'::text[]))::double precision), '[]'::text), agdc.float8range(LEAST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), GREATEST(((metadata #>> '{extent,coord,ul,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ur,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,ll,lon}'::text[]))::double precision, ((metadata #>> '{extent,coord,lr,lon}'::text[]))::double precision), '[]'::text)) WHERE ((archived IS NULL) AND (dataset_type_ref = 60));


--
-- Name: ix_agdc_dataset_dataset_type_ref; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX ix_agdc_dataset_dataset_type_ref ON agdc.dataset USING btree (dataset_type_ref);


--
-- Name: ix_agdc_dataset_location_dataset_ref; Type: INDEX; Schema: agdc; Owner: agdc_admin
--

CREATE INDEX ix_agdc_dataset_location_dataset_ref ON agdc.dataset_location USING btree (dataset_ref);


--
-- Name: dataset row_update_time_dataset; Type: TRIGGER; Schema: agdc; Owner: agdc_admin
--

CREATE TRIGGER row_update_time_dataset BEFORE UPDATE ON agdc.dataset FOR EACH ROW EXECUTE PROCEDURE agdc.set_row_update_time();


--
-- Name: dataset_type row_update_time_dataset_type; Type: TRIGGER; Schema: agdc; Owner: agdc_admin
--

CREATE TRIGGER row_update_time_dataset_type BEFORE UPDATE ON agdc.dataset_type FOR EACH ROW EXECUTE PROCEDURE agdc.set_row_update_time();


--
-- Name: metadata_type row_update_time_metadata_type; Type: TRIGGER; Schema: agdc; Owner: agdc_admin
--

CREATE TRIGGER row_update_time_metadata_type BEFORE UPDATE ON agdc.metadata_type FOR EACH ROW EXECUTE PROCEDURE agdc.set_row_update_time();


--
-- Name: dataset fk_dataset_dataset_type_ref_dataset_type; Type: FK CONSTRAINT; Schema: agdc; Owner: agdc_admin
--

ALTER TABLE ONLY agdc.dataset
    ADD CONSTRAINT fk_dataset_dataset_type_ref_dataset_type FOREIGN KEY (dataset_type_ref) REFERENCES agdc.dataset_type(id);


--
-- Name: dataset_location fk_dataset_location_dataset_ref_dataset; Type: FK CONSTRAINT; Schema: agdc; Owner: agdc_admin
--

ALTER TABLE ONLY agdc.dataset_location
    ADD CONSTRAINT fk_dataset_location_dataset_ref_dataset FOREIGN KEY (dataset_ref) REFERENCES agdc.dataset(id);


--
-- Name: dataset fk_dataset_metadata_type_ref_metadata_type; Type: FK CONSTRAINT; Schema: agdc; Owner: agdc_admin
--

ALTER TABLE ONLY agdc.dataset
    ADD CONSTRAINT fk_dataset_metadata_type_ref_metadata_type FOREIGN KEY (metadata_type_ref) REFERENCES agdc.metadata_type(id);


--
-- Name: dataset_source fk_dataset_source_dataset_ref_dataset; Type: FK CONSTRAINT; Schema: agdc; Owner: agdc_admin
--

ALTER TABLE ONLY agdc.dataset_source
    ADD CONSTRAINT fk_dataset_source_dataset_ref_dataset FOREIGN KEY (dataset_ref) REFERENCES agdc.dataset(id);


--
-- Name: dataset_source fk_dataset_source_source_dataset_ref_dataset; Type: FK CONSTRAINT; Schema: agdc; Owner: agdc_admin
--

ALTER TABLE ONLY agdc.dataset_source
    ADD CONSTRAINT fk_dataset_source_source_dataset_ref_dataset FOREIGN KEY (source_dataset_ref) REFERENCES agdc.dataset(id);


--
-- Name: dataset_type fk_dataset_type_metadata_type_ref_metadata_type; Type: FK CONSTRAINT; Schema: agdc; Owner: agdc_admin
--

ALTER TABLE ONLY agdc.dataset_type
    ADD CONSTRAINT fk_dataset_type_metadata_type_ref_metadata_type FOREIGN KEY (metadata_type_ref) REFERENCES agdc.metadata_type(id);


--
-- Name: SCHEMA agdc; Type: ACL; Schema: -; Owner: agdc_admin
--

GRANT USAGE ON SCHEMA agdc TO agdc_user;
GRANT CREATE ON SCHEMA agdc TO agdc_manage;


--
-- Name: FUNCTION common_timestamp(text); Type: ACL; Schema: agdc; Owner: agdc_admin
--

GRANT ALL ON FUNCTION agdc.common_timestamp(text) TO agdc_user;


--
-- Name: TABLE dataset; Type: ACL; Schema: agdc; Owner: agdc_admin
--

GRANT SELECT ON TABLE agdc.dataset TO agdc_user;
GRANT INSERT ON TABLE agdc.dataset TO agdc_ingest;


--
-- Name: TABLE dataset_location; Type: ACL; Schema: agdc; Owner: agdc_admin
--

GRANT SELECT ON TABLE agdc.dataset_location TO agdc_user;
GRANT INSERT ON TABLE agdc.dataset_location TO agdc_ingest;


--
-- Name: SEQUENCE dataset_location_id_seq; Type: ACL; Schema: agdc; Owner: agdc_admin
--

GRANT SELECT,USAGE ON SEQUENCE agdc.dataset_location_id_seq TO agdc_ingest;


--
-- Name: TABLE dataset_source; Type: ACL; Schema: agdc; Owner: agdc_admin
--

GRANT SELECT ON TABLE agdc.dataset_source TO agdc_user;
GRANT INSERT ON TABLE agdc.dataset_source TO agdc_ingest;


--
-- Name: TABLE dataset_type; Type: ACL; Schema: agdc; Owner: agdc_admin
--

GRANT SELECT ON TABLE agdc.dataset_type TO agdc_user;
GRANT INSERT,DELETE ON TABLE agdc.dataset_type TO agdc_manage;


--
-- Name: SEQUENCE dataset_type_id_seq; Type: ACL; Schema: agdc; Owner: agdc_admin
--

GRANT SELECT,USAGE ON SEQUENCE agdc.dataset_type_id_seq TO agdc_ingest;


--
-- Name: TABLE metadata_type; Type: ACL; Schema: agdc; Owner: agdc_admin
--

GRANT SELECT ON TABLE agdc.metadata_type TO agdc_user;
GRANT INSERT,DELETE ON TABLE agdc.metadata_type TO agdc_manage;


--
-- Name: SEQUENCE metadata_type_id_seq; Type: ACL; Schema: agdc; Owner: agdc_admin
--

GRANT SELECT,USAGE ON SEQUENCE agdc.metadata_type_id_seq TO agdc_ingest;


--
-- PostgreSQL database dump complete
--

