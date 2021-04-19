--
-- PostgreSQL database dump
--

-- Dumped from database version 11.7 (Debian 11.7-2.pgdg100+1)
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
-- Name: pg_cron; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS pg_cron WITH SCHEMA public;


--
-- Name: EXTENSION pg_cron; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION pg_cron IS 'Job scheduler for PostgreSQL';


--
-- Name: topology; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA topology;


ALTER SCHEMA topology OWNER TO postgres;

--
-- Name: SCHEMA topology; Type: COMMENT; Schema: -; Owner: postgres
--

COMMENT ON SCHEMA topology IS 'PostGIS Topology schema';


--
-- Name: hstore; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS hstore WITH SCHEMA public;


--
-- Name: EXTENSION hstore; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION hstore IS 'data type for storing sets of (key, value) pairs';


--
-- Name: postgis; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS postgis WITH SCHEMA public;


--
-- Name: EXTENSION postgis; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION postgis IS 'PostGIS geometry, geography, and raster spatial types and functions';


--
-- Name: postgis_topology; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS postgis_topology WITH SCHEMA topology;


--
-- Name: EXTENSION postgis_topology; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION postgis_topology IS 'PostGIS topology spatial types and functions';


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

--
-- Name: asbinary(public.geometry); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION public.asbinary(public.geometry) RETURNS bytea
    LANGUAGE c IMMUTABLE STRICT
    AS '$libdir/postgis-2.5', 'LWGEOM_asBinary';


ALTER FUNCTION public.asbinary(public.geometry) OWNER TO postgres;

--
-- Name: asbinary(public.geometry, text); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION public.asbinary(public.geometry, text) RETURNS bytea
    LANGUAGE c IMMUTABLE STRICT
    AS '$libdir/postgis-2.5', 'LWGEOM_asBinary';


ALTER FUNCTION public.asbinary(public.geometry, text) OWNER TO postgres;

--
-- Name: astext(public.geometry); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION public.astext(public.geometry) RETURNS text
    LANGUAGE c IMMUTABLE STRICT
    AS '$libdir/postgis-2.5', 'LWGEOM_asText';


ALTER FUNCTION public.astext(public.geometry) OWNER TO postgres;

--
-- Name: estimated_extent(text, text); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION public.estimated_extent(text, text) RETURNS public.box2d
    LANGUAGE c IMMUTABLE STRICT SECURITY DEFINER
    AS '$libdir/postgis-2.5', 'geometry_estimated_extent';


ALTER FUNCTION public.estimated_extent(text, text) OWNER TO postgres;

--
-- Name: estimated_extent(text, text, text); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION public.estimated_extent(text, text, text) RETURNS public.box2d
    LANGUAGE c IMMUTABLE STRICT SECURITY DEFINER
    AS '$libdir/postgis-2.5', 'geometry_estimated_extent';


ALTER FUNCTION public.estimated_extent(text, text, text) OWNER TO postgres;

--
-- Name: geomfromtext(text); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION public.geomfromtext(text) RETURNS public.geometry
    LANGUAGE sql IMMUTABLE STRICT
    AS $_$SELECT ST_GeomFromText($1)$_$;


ALTER FUNCTION public.geomfromtext(text) OWNER TO postgres;

--
-- Name: geomfromtext(text, integer); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION public.geomfromtext(text, integer) RETURNS public.geometry
    LANGUAGE sql IMMUTABLE STRICT
    AS $_$SELECT ST_GeomFromText($1, $2)$_$;


ALTER FUNCTION public.geomfromtext(text, integer) OWNER TO postgres;

--
-- Name: ndims(public.geometry); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION public.ndims(public.geometry) RETURNS smallint
    LANGUAGE c IMMUTABLE STRICT
    AS '$libdir/postgis-2.5', 'LWGEOM_ndims';


ALTER FUNCTION public.ndims(public.geometry) OWNER TO postgres;

--
-- Name: setsrid(public.geometry, integer); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION public.setsrid(public.geometry, integer) RETURNS public.geometry
    LANGUAGE c IMMUTABLE STRICT
    AS '$libdir/postgis-2.5', 'LWGEOM_set_srid';


ALTER FUNCTION public.setsrid(public.geometry, integer) OWNER TO postgres;

--
-- Name: srid(public.geometry); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION public.srid(public.geometry) RETURNS integer
    LANGUAGE c IMMUTABLE STRICT
    AS '$libdir/postgis-2.5', 'LWGEOM_get_srid';


ALTER FUNCTION public.srid(public.geometry) OWNER TO postgres;

--
-- Name: st_asbinary(text); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION public.st_asbinary(text) RETURNS bytea
    LANGUAGE sql IMMUTABLE STRICT
    AS $_$ SELECT ST_AsBinary($1::geometry);$_$;


ALTER FUNCTION public.st_asbinary(text) OWNER TO postgres;

--
-- Name: st_astext(bytea); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION public.st_astext(bytea) RETURNS text
    LANGUAGE sql IMMUTABLE STRICT
    AS $_$ SELECT ST_AsText($1::geometry);$_$;


ALTER FUNCTION public.st_astext(bytea) OWNER TO postgres;

--
-- Name: gist_geometry_ops; Type: OPERATOR FAMILY; Schema: public; Owner: postgres
--

CREATE OPERATOR FAMILY public.gist_geometry_ops USING gist;


ALTER OPERATOR FAMILY public.gist_geometry_ops USING gist OWNER TO postgres;

--
-- Name: gist_geometry_ops; Type: OPERATOR CLASS; Schema: public; Owner: postgres
--

CREATE OPERATOR CLASS public.gist_geometry_ops
    FOR TYPE public.geometry USING gist FAMILY public.gist_geometry_ops AS
    STORAGE public.box2df ,
    OPERATOR 1 public.<<(public.geometry,public.geometry) ,
    OPERATOR 2 public.&<(public.geometry,public.geometry) ,
    OPERATOR 3 public.&&(public.geometry,public.geometry) ,
    OPERATOR 4 public.&>(public.geometry,public.geometry) ,
    OPERATOR 5 public.>>(public.geometry,public.geometry) ,
    OPERATOR 6 public.~=(public.geometry,public.geometry) ,
    OPERATOR 7 public.~(public.geometry,public.geometry) ,
    OPERATOR 8 public.@(public.geometry,public.geometry) ,
    OPERATOR 9 public.&<|(public.geometry,public.geometry) ,
    OPERATOR 10 public.<<|(public.geometry,public.geometry) ,
    OPERATOR 11 public.|>>(public.geometry,public.geometry) ,
    OPERATOR 12 public.|&>(public.geometry,public.geometry) ,
    OPERATOR 13 public.<->(public.geometry,public.geometry) FOR ORDER BY pg_catalog.float_ops ,
    OPERATOR 14 public.<#>(public.geometry,public.geometry) FOR ORDER BY pg_catalog.float_ops ,
    FUNCTION 1 (public.geometry, public.geometry) public.geometry_gist_consistent_2d(internal,public.geometry,integer) ,
    FUNCTION 2 (public.geometry, public.geometry) public.geometry_gist_union_2d(bytea,internal) ,
    FUNCTION 3 (public.geometry, public.geometry) public.geometry_gist_compress_2d(internal) ,
    FUNCTION 4 (public.geometry, public.geometry) public.geometry_gist_decompress_2d(internal) ,
    FUNCTION 5 (public.geometry, public.geometry) public.geometry_gist_penalty_2d(internal,internal,internal) ,
    FUNCTION 6 (public.geometry, public.geometry) public.geometry_gist_picksplit_2d(internal,internal) ,
    FUNCTION 7 (public.geometry, public.geometry) public.geometry_gist_same_2d(public.geometry,public.geometry,internal) ,
    FUNCTION 8 (public.geometry, public.geometry) public.geometry_gist_distance_2d(internal,public.geometry,integer);


ALTER OPERATOR CLASS public.gist_geometry_ops USING gist OWNER TO postgres;

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
-- Name: dv_eo3_dataset; Type: VIEW; Schema: agdc; Owner: opendatacube
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


ALTER TABLE agdc.dv_eo3_dataset OWNER TO opendatacube;

--
-- Name: dv_eo_dataset; Type: VIEW; Schema: agdc; Owner: opendatacube
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


ALTER TABLE agdc.dv_eo_dataset OWNER TO opendatacube;

--
-- Name: dv_telemetry_dataset; Type: VIEW; Schema: agdc; Owner: opendatacube
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


ALTER TABLE agdc.dv_telemetry_dataset OWNER TO opendatacube;

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
\.


--
-- Data for Name: metadata_type; Type: TABLE DATA; Schema: agdc; Owner: agdc_admin
--

COPY agdc.metadata_type (id, name, definition, added, added_by, updated) FROM stdin;
1	eo3	{"name": "eo3", "dataset": {"id": ["id"], "label": ["label"], "format": ["properties", "odc:file_format"], "sources": ["lineage", "source_datasets"], "creation_dt": ["properties", "odc:processing_datetime"], "grid_spatial": ["grid_spatial", "projection"], "measurements": ["measurements"], "search_fields": {"lat": {"type": "double-range", "max_offset": [["extent", "lat", "end"]], "min_offset": [["extent", "lat", "begin"]], "description": "Latitude range"}, "lon": {"type": "double-range", "max_offset": [["extent", "lon", "end"]], "min_offset": [["extent", "lon", "begin"]], "description": "Longitude range"}, "time": {"type": "datetime-range", "max_offset": [["properties", "dtr:end_datetime"], ["properties", "datetime"]], "min_offset": [["properties", "dtr:start_datetime"], ["properties", "datetime"]], "description": "Acquisition time range"}, "platform": {"offset": ["properties", "eo:platform"], "indexed": false, "description": "Platform code"}, "instrument": {"offset": ["properties", "eo:instrument"], "indexed": false, "description": "Instrument name"}, "region_code": {"offset": ["properties", "odc:region_code"], "description": "Spatial reference code from the provider. For Landsat region_code is a scene path row:\\n        '{:03d}{:03d}.format(path,row)'.\\nFor Sentinel it is MGRS code. In general it is a unique string identifier that datasets covering roughly the same spatial region share.\\n"}, "product_family": {"offset": ["properties", "odc:product_family"], "indexed": false, "description": "Product family code"}, "dataset_maturity": {"offset": ["properties", "dea:dataset_maturity"], "indexed": false, "description": "One of - final|interim|nrt  (near real time)"}}}, "description": "Default EO3 with no custom fields"}	2021-02-16 22:33:54.856082+00	opendatacube	\N
2	eo	{"name": "eo", "dataset": {"id": ["id"], "label": ["ga_label"], "format": ["format", "name"], "sources": ["lineage", "source_datasets"], "creation_dt": ["creation_dt"], "grid_spatial": ["grid_spatial", "projection"], "measurements": ["image", "bands"], "search_fields": {"lat": {"type": "double-range", "max_offset": [["extent", "coord", "ur", "lat"], ["extent", "coord", "lr", "lat"], ["extent", "coord", "ul", "lat"], ["extent", "coord", "ll", "lat"]], "min_offset": [["extent", "coord", "ur", "lat"], ["extent", "coord", "lr", "lat"], ["extent", "coord", "ul", "lat"], ["extent", "coord", "ll", "lat"]], "description": "Latitude range"}, "lon": {"type": "double-range", "max_offset": [["extent", "coord", "ul", "lon"], ["extent", "coord", "ur", "lon"], ["extent", "coord", "ll", "lon"], ["extent", "coord", "lr", "lon"]], "min_offset": [["extent", "coord", "ul", "lon"], ["extent", "coord", "ur", "lon"], ["extent", "coord", "ll", "lon"], ["extent", "coord", "lr", "lon"]], "description": "Longitude range"}, "time": {"type": "datetime-range", "max_offset": [["extent", "to_dt"], ["extent", "center_dt"]], "min_offset": [["extent", "from_dt"], ["extent", "center_dt"]], "description": "Acquisition time"}, "platform": {"offset": ["platform", "code"], "description": "Platform code"}, "instrument": {"offset": ["instrument", "name"], "description": "Instrument name"}, "product_type": {"offset": ["product_type"], "description": "Product code"}}}, "description": "Earth Observation datasets.\\n\\nExpected metadata structure produced by the eodatasets library, as used internally at GA.\\n\\nhttps://github.com/GeoscienceAustralia/eo-datasets\\n"}	2021-02-16 22:33:54.881149+00	opendatacube	\N
3	telemetry	{"name": "telemetry", "dataset": {"id": ["id"], "label": ["ga_label"], "sources": ["lineage", "source_datasets"], "creation_dt": ["creation_dt"], "search_fields": {"gsi": {"offset": ["acquisition", "groundstation", "code"], "indexed": false, "description": "Ground Station Identifier (eg. ASA)"}, "time": {"type": "datetime-range", "max_offset": [["acquisition", "los"]], "min_offset": [["acquisition", "aos"]], "description": "Acquisition time"}, "orbit": {"type": "integer", "offset": ["acquisition", "platform_orbit"], "description": "Orbit number"}, "sat_row": {"type": "integer-range", "max_offset": [["image", "satellite_ref_point_end", "y"], ["image", "satellite_ref_point_start", "y"]], "min_offset": [["image", "satellite_ref_point_start", "y"]], "description": "Landsat row"}, "platform": {"offset": ["platform", "code"], "description": "Platform code"}, "sat_path": {"type": "integer-range", "max_offset": [["image", "satellite_ref_point_end", "x"], ["image", "satellite_ref_point_start", "x"]], "min_offset": [["image", "satellite_ref_point_start", "x"]], "description": "Landsat path"}, "instrument": {"offset": ["instrument", "name"], "description": "Instrument name"}, "product_type": {"offset": ["product_type"], "description": "Product code"}}}, "description": "Satellite telemetry datasets.\\n\\nExpected metadata structure produced by telemetry datasets from the eodatasets library, as used internally at GA.\\n\\nhttps://github.com/GeoscienceAustralia/eo-datasets\\n"}	2021-02-16 22:33:54.904797+00	opendatacube	\N
\.


--
-- Data for Name: job; Type: TABLE DATA; Schema: cron; Owner: postgres
--

COPY cron.job (jobid, schedule, command, nodename, nodeport, database, username, active) FROM stdin;
\.


--
-- Data for Name: spatial_ref_sys; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.spatial_ref_sys (srid, auth_name, auth_srid, srtext, proj4text) FROM stdin;
\.


--
-- Data for Name: topology; Type: TABLE DATA; Schema: topology; Owner: postgres
--

COPY topology.topology (id, name, srid, "precision", hasz) FROM stdin;
\.


--
-- Data for Name: layer; Type: TABLE DATA; Schema: topology; Owner: postgres
--

COPY topology.layer (topology_id, layer_id, schema_name, table_name, feature_column, feature_type, level, child_id) FROM stdin;
\.


--
-- Name: dataset_location_id_seq; Type: SEQUENCE SET; Schema: agdc; Owner: agdc_admin
--

SELECT pg_catalog.setval('agdc.dataset_location_id_seq', 1, false);


--
-- Name: dataset_type_id_seq; Type: SEQUENCE SET; Schema: agdc; Owner: agdc_admin
--

SELECT pg_catalog.setval('agdc.dataset_type_id_seq', 1, false);


--
-- Name: metadata_type_id_seq; Type: SEQUENCE SET; Schema: agdc; Owner: agdc_admin
--

SELECT pg_catalog.setval('agdc.metadata_type_id_seq', 33, true);


--
-- Name: jobid_seq; Type: SEQUENCE SET; Schema: cron; Owner: postgres
--

SELECT pg_catalog.setval('cron.jobid_seq', 1, false);


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
-- Name: job cron_job_policy; Type: POLICY; Schema: cron; Owner: postgres
--

CREATE POLICY cron_job_policy ON cron.job USING ((username = (CURRENT_USER)::text));


--
-- Name: job; Type: ROW SECURITY; Schema: cron; Owner: postgres
--

ALTER TABLE cron.job ENABLE ROW LEVEL SECURITY;

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
-- Name: DEFAULT PRIVILEGES FOR TABLES; Type: DEFAULT ACL; Schema: public; Owner: opendatacube
--

ALTER DEFAULT PRIVILEGES FOR ROLE opendatacube IN SCHEMA public REVOKE ALL ON TABLES  FROM opendatacube;
ALTER DEFAULT PRIVILEGES FOR ROLE opendatacube IN SCHEMA public GRANT SELECT ON TABLES  TO replicator;


--
-- PostgreSQL database dump complete
--

