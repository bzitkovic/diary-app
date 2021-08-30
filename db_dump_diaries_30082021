--
-- PostgreSQL database dump
--

-- Dumped from database version 13.1
-- Dumped by pg_dump version 13.1

-- Started on 2021-08-30 13:27:09

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

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 201 (class 1259 OID 33232)
-- Name: diary_log; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.diary_log (
    id bigint NOT NULL,
    name character varying NOT NULL,
    date date NOT NULL,
    log text NOT NULL,
    visible smallint,
    user_id bigint
);


ALTER TABLE public.diary_log OWNER TO postgres;

--
-- TOC entry 204 (class 1259 OID 33262)
-- Name: diary_log_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.diary_log ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.diary_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 202 (class 1259 OID 33245)
-- Name: friendship; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.friendship (
    id bigint NOT NULL,
    requester_id bigint,
    addresse_id bigint,
    status smallint
);


ALTER TABLE public.friendship OWNER TO postgres;

--
-- TOC entry 205 (class 1259 OID 33264)
-- Name: friendship_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.friendship ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.friendship_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 200 (class 1259 OID 33224)
-- Name: user; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."user" (
    id bigint NOT NULL,
    username character varying NOT NULL,
    password character varying,
    age bigint,
    sex character(1),
    country character varying,
    city character varying
);


ALTER TABLE public."user" OWNER TO postgres;

--
-- TOC entry 203 (class 1259 OID 33260)
-- Name: user_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public."user" ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 3004 (class 0 OID 33232)
-- Dependencies: 201
-- Data for Name: diary_log; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.diary_log (id, name, date, log, visible, user_id) FROM stdin;
5	Vrijeme	2021-08-25	heheh	1	3
3	Little Perica diary 3	2021-08-23	Lorem ipsum dolor sit amet consectetur adipisicing elit. Nemo, omnis. Culpa a debitis cumque laborum nam enim quos recusandae ullam molestiae expedita saepe illum pariatur nihil, vero et minima quidem.	0	3
4	Little Perica diary 4	2021-08-25	Lorem ipsum dolor sit amet consectetur adipisicing elit. Nemo, omnis. Culpa a debitis cumque laborum nam enim quos recusandae ullam molestiae expedita saepe illum pariatur nihil, vero et minima quidem.	0	1
1	Little Perica diary 2	2021-08-21	Lorem ipsum dolor sit amet consectetur adipisicing elit. Nemo, omnis. Culpa a debitis cumque laborum nam enim quos recusandae ullam molestiae expedita saepe illum pariatur nihil, vero et minima quidem.	1	1
6	Josipa log	2021-08-25	Lorem ipsum dolor sit amet consectetur adipisicing elit. Nemo, omnis. Culpa a debitis cumque laborum nam enim quos recusandae ullam molestiae expedita saepe illum pariatur nihil, vero et minima quidem.Lorem ipsum dolor sit amet consectetur adipisicing elit.	1	4
2	Bruno log	2021-08-22	Bruno keeps logs simple	1	2
\.


--
-- TOC entry 3005 (class 0 OID 33245)
-- Dependencies: 202
-- Data for Name: friendship; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.friendship (id, requester_id, addresse_id, status) FROM stdin;
46	1	5	1
45	5	1	1
48	3	5	0
51	1	4	1
47	4	1	1
50	4	1	1
52	3	2	1
49	2	3	1
37	3	4	1
\.


--
-- TOC entry 3003 (class 0 OID 33224)
-- Dependencies: 200
-- Data for Name: user; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."user" (id, username, password, age, sex, country, city) FROM stdin;
2	Bruno	123	21	M	Croatia	Zagreb
3	Entkeeper17	123	24	M	Croatia	Zagreb
4	Josipa	122	22	W	Croatia	Ivanec
5	Hrvoje	123	27	M	Croatia	Varaždin
1	admin	admin	23	M	Croatia	Samobor
\.


--
-- TOC entry 3014 (class 0 OID 0)
-- Dependencies: 204
-- Name: diary_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.diary_log_id_seq', 6, true);


--
-- TOC entry 3015 (class 0 OID 0)
-- Dependencies: 205
-- Name: friendship_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.friendship_id_seq', 52, true);


--
-- TOC entry 3016 (class 0 OID 0)
-- Dependencies: 203
-- Name: user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.user_id_seq', 5, true);


--
-- TOC entry 2867 (class 2606 OID 33239)
-- Name: diary_log diary_log_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.diary_log
    ADD CONSTRAINT diary_log_pkey PRIMARY KEY (id);


--
-- TOC entry 2869 (class 2606 OID 33249)
-- Name: friendship friendship_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.friendship
    ADD CONSTRAINT friendship_pkey PRIMARY KEY (id);


--
-- TOC entry 2865 (class 2606 OID 33231)
-- Name: user user_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (id);


--
-- TOC entry 2870 (class 2606 OID 33266)
-- Name: diary_log diary_log_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.diary_log
    ADD CONSTRAINT diary_log_user_id_fkey FOREIGN KEY (user_id) REFERENCES public."user"(id) ON UPDATE CASCADE ON DELETE CASCADE NOT VALID;


--
-- TOC entry 2872 (class 2606 OID 33255)
-- Name: friendship friendship_addresse_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.friendship
    ADD CONSTRAINT friendship_addresse_id_fkey FOREIGN KEY (addresse_id) REFERENCES public."user"(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 2871 (class 2606 OID 33250)
-- Name: friendship friendship_requester_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.friendship
    ADD CONSTRAINT friendship_requester_id_fkey FOREIGN KEY (requester_id) REFERENCES public."user"(id) ON UPDATE CASCADE ON DELETE CASCADE;


-- Completed on 2021-08-30 13:27:09

--
-- PostgreSQL database dump complete
--

