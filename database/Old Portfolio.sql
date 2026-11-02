--
-- PostgreSQL database dump
--

\restrict WcVca4cfV8m4D8fnJMLXsFlDavghvYVhjfT79jlnBojhlKXjJxFiesQV59F5uJR

-- Dumped from database version 18.4
-- Dumped by pg_dump version 18.4

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: Old Portfolio; Type: DATABASE; Schema: -; Owner: -
--

CREATE DATABASE "Old Portfolio" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_United States.1252';


\unrestrict WcVca4cfV8m4D8fnJMLXsFlDavghvYVhjfT79jlnBojhlKXjJxFiesQV59F5uJR
\encoding SQL_ASCII
\connect -reuse-previous=on "dbname='Old Portfolio'"
\restrict WcVca4cfV8m4D8fnJMLXsFlDavghvYVhjfT79jlnBojhlKXjJxFiesQV59F5uJR

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: pharmacy2; Type: SCHEMA; Schema: -; Owner: -
--

CREATE SCHEMA pharmacy2;


--
-- Name: portfolio; Type: SCHEMA; Schema: -; Owner: -
--

CREATE SCHEMA portfolio;


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: messages; Type: TABLE; Schema: pharmacy2; Owner: -
--

CREATE TABLE pharmacy2.messages (
    messagetime text NOT NULL,
    content text,
    tom text,
    fromm text
);


--
-- Name: stok; Type: TABLE; Schema: pharmacy2; Owner: -
--

CREATE TABLE pharmacy2.stok (
    karekod text NOT NULL,
    ad text NOT NULL,
    barkod text NOT NULL,
    almatarih text,
    satmatarih text,
    satmahasta text,
    almayer text
);


--
-- Name: takas; Type: TABLE; Schema: pharmacy2; Owner: -
--

CREATE TABLE pharmacy2.takas (
    karekod text NOT NULL,
    ad text,
    tot text,
    fromt text,
    vertarih text,
    altarih text
);


--
-- Name: messages; Type: TABLE; Schema: portfolio; Owner: -
--

CREATE TABLE portfolio.messages (
    messagetime text NOT NULL,
    content text,
    tom text,
    fromm text
);


--
-- Name: stok; Type: TABLE; Schema: portfolio; Owner: -
--

CREATE TABLE portfolio.stok (
    karekod text NOT NULL,
    ad text NOT NULL,
    barkod text NOT NULL,
    almatarih text,
    satmatarih text,
    satmahasta text,
    almayer text
);


--
-- Name: takas; Type: TABLE; Schema: portfolio; Owner: -
--

CREATE TABLE portfolio.takas (
    karekod text NOT NULL,
    ad text,
    tot text,
    fromt text,
    vertarih text,
    altarih text
);


--
-- Name: ajarise_setup; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ajarise_setup (
    version text NOT NULL,
    details jsonb NOT NULL
);


--
-- Data for Name: messages; Type: TABLE DATA; Schema: pharmacy2; Owner: -
--

COPY pharmacy2.messages (messagetime, content, tom, fromm) FROM stdin;
portfolio		x	pharmacy2
261030191716	Yes, we have some available. How many do you need?	portfolio	pharmacy2
261030191916	#give/200000000005	portfolio	pharmacy2
\.


--
-- Data for Name: stok; Type: TABLE DATA; Schema: pharmacy2; Owner: -
--

COPY pharmacy2.stok (karekod, ad, barkod, almatarih, satmatarih, satmahasta, almayer) FROM stdin;
200000000001	parol	9000000000001	2610301843	\N	\N	Demo supplier
200000000003	iburamin cold	9000000000003	2610271903	\N	\N	Demo supplier
200000000004	parol	9000000000001	2610261903	\N	\N	Demo supplier
200000000005	arveles	9000000000002	2610251903	\N	\N	Demo supplier
200000000006	iburamin cold	9000000000003	2610241903	\N	\N	Demo supplier
200000000007	parol	9000000000001	2610231903	\N	\N	Demo supplier
200000000008	arveles	9000000000002	2610221903	\N	\N	Demo supplier
200000000009	iburamin cold	9000000000003	2610211903	\N	\N	Demo supplier
200000000010	parol	9000000000001	2610201903	\N	\N	Demo supplier
200000000011	arveles	9000000000002	2610191903	\N	\N	Demo supplier
200000000012	iburamin cold	9000000000003	2610181903	2610301903	Demo guest 12	Demo supplier
200000000013	parol	9000000000001	2610171903	\N	\N	Demo supplier
200000000014	arveles	9000000000002	2610161903	\N	\N	Demo supplier
200000000015	iburamin cold	9000000000003	2610151903	\N	\N	Demo supplier
200000000016	parol	9000000000001	2610141903	\N	\N	Demo supplier
200000000017	arveles	9000000000002	2610131903	\N	\N	Demo supplier
200000000018	iburamin cold	9000000000003	2610121903	\N	\N	Demo supplier
200000000019	parol	9000000000001	2610111903	\N	\N	Demo supplier
200000000020	arveles	9000000000002	2610101903	\N	\N	Demo supplier
200000000021	iburamin cold	9000000000003	2610091903	\N	\N	Demo supplier
200000000022	parol	9000000000001	2610081903	\N	\N	Demo supplier
200000000023	arveles	9000000000002	2610071903	\N	\N	Demo supplier
200000000024	iburamin cold	9000000000003	2610061903	2610301903	Demo guest 24	Demo supplier
200000000025	parol	9000000000001	2610051903	\N	\N	Demo supplier
200000000026	arveles	9000000000002	2610041903	\N	\N	Demo supplier
200000000027	iburamin cold	9000000000003	2610031903	\N	\N	Demo supplier
200000000028	parol	9000000000001	2610301903	\N	\N	Demo supplier
200000000029	arveles	9000000000002	2610291903	\N	\N	Demo supplier
200000000030	iburamin cold	9000000000003	2610281903	\N	\N	Demo supplier
200000000031	parol	9000000000001	2610271903	\N	\N	Demo supplier
200000000032	arveles	9000000000002	2610261903	\N	\N	Demo supplier
200000000033	iburamin cold	9000000000003	2610251903	\N	\N	Demo supplier
200000000034	parol	9000000000001	2610241903	\N	\N	Demo supplier
200000000035	arveles	9000000000002	2610231903	\N	\N	Demo supplier
200000000036	iburamin cold	9000000000003	2610221903	2610301903	Demo guest 36	Demo supplier
200000000037	parol	9000000000001	2610211903	\N	\N	Demo supplier
200000000038	arveles	9000000000002	2610201903	\N	\N	Demo supplier
200000000039	iburamin cold	9000000000003	2610191903	\N	\N	Demo supplier
200000000040	parol	9000000000001	2610181903	\N	\N	Demo supplier
200000000041	arveles	9000000000002	2610171903	\N	\N	Demo supplier
200000000042	iburamin cold	9000000000003	2610161903	\N	\N	Demo supplier
200000000043	parol	9000000000001	2610151903	\N	\N	Demo supplier
200000000044	arveles	9000000000002	2610141903	\N	\N	Demo supplier
200000000045	iburamin cold	9000000000003	2610131903	\N	\N	Demo supplier
200000000046	parol	9000000000001	2610121903	\N	\N	Demo supplier
200000000047	arveles	9000000000002	2610111903	\N	\N	Demo supplier
200000000048	iburamin cold	9000000000003	2610101903	2610301903	Demo guest 48	Demo supplier
200000000049	parol	9000000000001	2610091903	\N	\N	Demo supplier
200000000050	arveles	9000000000002	2610081903	\N	\N	Demo supplier
200000000051	iburamin cold	9000000000003	2610071903	\N	\N	Demo supplier
200000000052	parol	9000000000001	2610061903	\N	\N	Demo supplier
200000000053	arveles	9000000000002	2610051903	\N	\N	Demo supplier
200000000054	iburamin cold	9000000000003	2610041903	\N	\N	Demo supplier
200000000055	parol	9000000000001	2610031903	\N	\N	Demo supplier
200000000056	arveles	9000000000002	2610301903	\N	\N	Demo supplier
200000000057	iburamin cold	9000000000003	2610291903	\N	\N	Demo supplier
200000000058	parol	9000000000001	2610281903	\N	\N	Demo supplier
200000000059	arveles	9000000000002	2610271903	\N	\N	Demo supplier
200000000060	iburamin cold	9000000000003	2610261903	2610301903	Demo guest 60	Demo supplier
200000000061	parol	9000000000001	2610251903	\N	\N	Demo supplier
200000000062	arveles	9000000000002	2610241903	\N	\N	Demo supplier
200000000063	iburamin cold	9000000000003	2610231903	\N	\N	Demo supplier
200000000064	parol	9000000000001	2610221903	\N	\N	Demo supplier
200000000065	arveles	9000000000002	2610211903	\N	\N	Demo supplier
200000000066	iburamin cold	9000000000003	2610201903	\N	\N	Demo supplier
200000000067	parol	9000000000001	2610191903	\N	\N	Demo supplier
200000000068	arveles	9000000000002	2610181903	\N	\N	Demo supplier
200000000069	iburamin cold	9000000000003	2610171903	\N	\N	Demo supplier
200000000070	parol	9000000000001	2610161903	\N	\N	Demo supplier
200000000071	arveles	9000000000002	2610151903	\N	\N	Demo supplier
200000000072	iburamin cold	9000000000003	2610141903	2610301903	Demo guest 72	Demo supplier
200000000073	parol	9000000000001	2610131903	\N	\N	Demo supplier
200000000074	arveles	9000000000002	2610121903	\N	\N	Demo supplier
200000000075	iburamin cold	9000000000003	2610111903	\N	\N	Demo supplier
200000000076	parol	9000000000001	2610101903	\N	\N	Demo supplier
200000000077	arveles	9000000000002	2610091903	\N	\N	Demo supplier
200000000078	iburamin cold	9000000000003	2610081903	\N	\N	Demo supplier
200000000079	parol	9000000000001	2610071903	\N	\N	Demo supplier
200000000080	arveles	9000000000002	2610061903	\N	\N	Demo supplier
200000000081	iburamin cold	9000000000003	2610051903	\N	\N	Demo supplier
200000000082	parol	9000000000001	2610041903	\N	\N	Demo supplier
200000000083	arveles	9000000000002	2610031903	\N	\N	Demo supplier
200000000084	iburamin cold	9000000000003	2610301903	2610301903	Demo guest 84	Demo supplier
200000000085	parol	9000000000001	2610291903	\N	\N	Demo supplier
200000000086	arveles	9000000000002	2610281903	\N	\N	Demo supplier
200000000087	iburamin cold	9000000000003	2610271903	\N	\N	Demo supplier
200000000088	parol	9000000000001	2610261903	\N	\N	Demo supplier
200000000089	arveles	9000000000002	2610251903	\N	\N	Demo supplier
200000000090	iburamin cold	9000000000003	2610241903	\N	\N	Demo supplier
200000000002	arveles	9000000000002	2610281903	pendingTra	portfolio	Demo supplier
\.


--
-- Data for Name: takas; Type: TABLE DATA; Schema: pharmacy2; Owner: -
--

COPY pharmacy2.takas (karekod, ad, tot, fromt, vertarih, altarih) FROM stdin;
200000000002	arveles	portfolio	pharmacy2	261030191047	\N
\.


--
-- Data for Name: messages; Type: TABLE DATA; Schema: portfolio; Owner: -
--

COPY portfolio.messages (messagetime, content, tom, fromm) FROM stdin;
pharmacy2		x	portfolio
261030191616	Hi, do you have any arveles in stock?	pharmacy2	portfolio
261030191816	One box, please. Could you send it over?	pharmacy2	portfolio
\.


--
-- Data for Name: stok; Type: TABLE DATA; Schema: portfolio; Owner: -
--

COPY portfolio.stok (karekod, ad, barkod, almatarih, satmatarih, satmahasta, almayer) FROM stdin;
100000000001	parol	9000000000001	2610301843	\N	\N	Demo supplier
100000000002	arveles	9000000000002	2610301843	\N	\N	Demo supplier
100000000003	iburamin cold	9000000000003	2610301843	\N	\N	Demo supplier
100000000004	parol	9000000000001	2610301843	2610301843	Demo guest	Demo supplier
100000000005	arveles	9000000000002	2610251903	\N	\N	Demo supplier
100000000006	iburamin cold	9000000000003	2610241903	\N	\N	Demo supplier
100000000007	parol	9000000000001	2610231903	\N	\N	Demo supplier
100000000008	arveles	9000000000002	2610221903	\N	\N	Demo supplier
100000000009	iburamin cold	9000000000003	2610211903	\N	\N	Demo supplier
100000000010	parol	9000000000001	2610201903	\N	\N	Demo supplier
100000000011	arveles	9000000000002	2610191903	\N	\N	Demo supplier
100000000012	iburamin cold	9000000000003	2610181903	2610301903	Demo guest 12	Demo supplier
100000000013	parol	9000000000001	2610171903	\N	\N	Demo supplier
100000000014	arveles	9000000000002	2610161903	\N	\N	Demo supplier
100000000015	iburamin cold	9000000000003	2610151903	\N	\N	Demo supplier
100000000016	parol	9000000000001	2610141903	\N	\N	Demo supplier
100000000017	arveles	9000000000002	2610131903	\N	\N	Demo supplier
100000000018	iburamin cold	9000000000003	2610121903	\N	\N	Demo supplier
100000000019	parol	9000000000001	2610111903	\N	\N	Demo supplier
100000000020	arveles	9000000000002	2610101903	\N	\N	Demo supplier
100000000021	iburamin cold	9000000000003	2610091903	\N	\N	Demo supplier
100000000022	parol	9000000000001	2610081903	\N	\N	Demo supplier
100000000023	arveles	9000000000002	2610071903	\N	\N	Demo supplier
100000000024	iburamin cold	9000000000003	2610061903	2610301903	Demo guest 24	Demo supplier
100000000025	parol	9000000000001	2610051903	\N	\N	Demo supplier
100000000026	arveles	9000000000002	2610041903	\N	\N	Demo supplier
100000000027	iburamin cold	9000000000003	2610031903	\N	\N	Demo supplier
100000000028	parol	9000000000001	2610301903	\N	\N	Demo supplier
100000000029	arveles	9000000000002	2610291903	\N	\N	Demo supplier
100000000030	iburamin cold	9000000000003	2610281903	\N	\N	Demo supplier
100000000031	parol	9000000000001	2610271903	\N	\N	Demo supplier
100000000032	arveles	9000000000002	2610261903	\N	\N	Demo supplier
100000000033	iburamin cold	9000000000003	2610251903	\N	\N	Demo supplier
100000000034	parol	9000000000001	2610241903	\N	\N	Demo supplier
100000000035	arveles	9000000000002	2610231903	\N	\N	Demo supplier
100000000036	iburamin cold	9000000000003	2610221903	2610301903	Demo guest 36	Demo supplier
100000000037	parol	9000000000001	2610211903	\N	\N	Demo supplier
100000000038	arveles	9000000000002	2610201903	\N	\N	Demo supplier
100000000039	iburamin cold	9000000000003	2610191903	\N	\N	Demo supplier
100000000040	parol	9000000000001	2610181903	\N	\N	Demo supplier
100000000041	arveles	9000000000002	2610171903	\N	\N	Demo supplier
100000000042	iburamin cold	9000000000003	2610161903	\N	\N	Demo supplier
100000000043	parol	9000000000001	2610151903	\N	\N	Demo supplier
100000000044	arveles	9000000000002	2610141903	\N	\N	Demo supplier
100000000045	iburamin cold	9000000000003	2610131903	\N	\N	Demo supplier
100000000046	parol	9000000000001	2610121903	\N	\N	Demo supplier
100000000047	arveles	9000000000002	2610111903	\N	\N	Demo supplier
100000000048	iburamin cold	9000000000003	2610101903	2610301903	Demo guest 48	Demo supplier
100000000049	parol	9000000000001	2610091903	\N	\N	Demo supplier
100000000050	arveles	9000000000002	2610081903	\N	\N	Demo supplier
100000000051	iburamin cold	9000000000003	2610071903	\N	\N	Demo supplier
100000000052	parol	9000000000001	2610061903	\N	\N	Demo supplier
100000000053	arveles	9000000000002	2610051903	\N	\N	Demo supplier
100000000054	iburamin cold	9000000000003	2610041903	\N	\N	Demo supplier
100000000055	parol	9000000000001	2610031903	\N	\N	Demo supplier
100000000056	arveles	9000000000002	2610301903	\N	\N	Demo supplier
100000000057	iburamin cold	9000000000003	2610291903	\N	\N	Demo supplier
100000000058	parol	9000000000001	2610281903	\N	\N	Demo supplier
100000000059	arveles	9000000000002	2610271903	\N	\N	Demo supplier
100000000060	iburamin cold	9000000000003	2610261903	2610301903	Demo guest 60	Demo supplier
100000000061	parol	9000000000001	2610251903	\N	\N	Demo supplier
100000000062	arveles	9000000000002	2610241903	\N	\N	Demo supplier
100000000063	iburamin cold	9000000000003	2610231903	\N	\N	Demo supplier
100000000064	parol	9000000000001	2610221903	\N	\N	Demo supplier
100000000065	arveles	9000000000002	2610211903	\N	\N	Demo supplier
100000000066	iburamin cold	9000000000003	2610201903	\N	\N	Demo supplier
100000000067	parol	9000000000001	2610191903	\N	\N	Demo supplier
100000000068	arveles	9000000000002	2610181903	\N	\N	Demo supplier
100000000069	iburamin cold	9000000000003	2610171903	\N	\N	Demo supplier
100000000070	parol	9000000000001	2610161903	\N	\N	Demo supplier
100000000071	arveles	9000000000002	2610151903	\N	\N	Demo supplier
100000000072	iburamin cold	9000000000003	2610141903	2610301903	Demo guest 72	Demo supplier
100000000073	parol	9000000000001	2610131903	\N	\N	Demo supplier
100000000074	arveles	9000000000002	2610121903	\N	\N	Demo supplier
100000000075	iburamin cold	9000000000003	2610111903	\N	\N	Demo supplier
100000000076	parol	9000000000001	2610101903	\N	\N	Demo supplier
100000000077	arveles	9000000000002	2610091903	\N	\N	Demo supplier
100000000078	iburamin cold	9000000000003	2610081903	\N	\N	Demo supplier
100000000079	parol	9000000000001	2610071903	\N	\N	Demo supplier
100000000080	arveles	9000000000002	2610061903	\N	\N	Demo supplier
100000000081	iburamin cold	9000000000003	2610051903	\N	\N	Demo supplier
100000000082	parol	9000000000001	2610041903	\N	\N	Demo supplier
100000000083	arveles	9000000000002	2610031903	\N	\N	Demo supplier
100000000084	iburamin cold	9000000000003	2610301903	2610301903	Demo guest 84	Demo supplier
100000000085	parol	9000000000001	2610291903	\N	\N	Demo supplier
100000000086	arveles	9000000000002	2610281903	\N	\N	Demo supplier
100000000087	iburamin cold	9000000000003	2610271903	\N	\N	Demo supplier
100000000088	parol	9000000000001	2610261903	\N	\N	Demo supplier
100000000089	arveles	9000000000002	2610251903	\N	\N	Demo supplier
100000000090	iburamin cold	9000000000003	2610241903	\N	\N	Demo supplier
100000000091	parol	9000000000001	2610231903	\N	\N	Demo supplier
100000000092	arveles	9000000000002	2610221903	\N	\N	Demo supplier
100000000093	iburamin cold	9000000000003	2610211903	\N	\N	Demo supplier
100000000094	parol	9000000000001	2610201903	\N	\N	Demo supplier
100000000095	arveles	9000000000002	2610191903	\N	\N	Demo supplier
100000000096	iburamin cold	9000000000003	2610181903	2610301903	Demo guest 96	Demo supplier
100000000097	parol	9000000000001	2610171903	\N	\N	Demo supplier
100000000098	arveles	9000000000002	2610161903	\N	\N	Demo supplier
100000000099	iburamin cold	9000000000003	2610151903	\N	\N	Demo supplier
100000000100	parol	9000000000001	2610141903	\N	\N	Demo supplier
100000000101	arveles	9000000000002	2610131903	\N	\N	Demo supplier
100000000102	iburamin cold	9000000000003	2610121903	\N	\N	Demo supplier
100000000103	parol	9000000000001	2610111903	\N	\N	Demo supplier
100000000104	arveles	9000000000002	2610101903	\N	\N	Demo supplier
100000000105	iburamin cold	9000000000003	2610091903	\N	\N	Demo supplier
100000000106	parol	9000000000001	2610081903	\N	\N	Demo supplier
100000000107	arveles	9000000000002	2610071903	\N	\N	Demo supplier
100000000108	iburamin cold	9000000000003	2610061903	2610301903	Demo guest 108	Demo supplier
100000000109	parol	9000000000001	2610051903	\N	\N	Demo supplier
100000000110	arveles	9000000000002	2610041903	\N	\N	Demo supplier
100000000111	iburamin cold	9000000000003	2610031903	\N	\N	Demo supplier
100000000112	parol	9000000000001	2610301903	\N	\N	Demo supplier
100000000113	arveles	9000000000002	2610291903	\N	\N	Demo supplier
100000000114	iburamin cold	9000000000003	2610281903	\N	\N	Demo supplier
100000000115	parol	9000000000001	2610271903	\N	\N	Demo supplier
100000000116	arveles	9000000000002	2610261903	\N	\N	Demo supplier
100000000117	iburamin cold	9000000000003	2610251903	\N	\N	Demo supplier
100000000118	parol	9000000000001	2610241903	\N	\N	Demo supplier
100000000119	arveles	9000000000002	2610231903	\N	\N	Demo supplier
100000000120	iburamin cold	9000000000003	2610221903	2610301903	Demo guest 120	Demo supplier
100000000121	parol	9000000000001	2610211903	\N	\N	Demo supplier
100000000122	arveles	9000000000002	2610201903	\N	\N	Demo supplier
100000000123	iburamin cold	9000000000003	2610191903	\N	\N	Demo supplier
100000000124	parol	9000000000001	2610181903	\N	\N	Demo supplier
100000000125	arveles	9000000000002	2610171903	\N	\N	Demo supplier
100000000126	iburamin cold	9000000000003	2610161903	\N	\N	Demo supplier
100000000127	parol	9000000000001	2610151903	\N	\N	Demo supplier
100000000128	arveles	9000000000002	2610141903	\N	\N	Demo supplier
100000000129	iburamin cold	9000000000003	2610131903	\N	\N	Demo supplier
100000000130	parol	9000000000001	2610121903	\N	\N	Demo supplier
100000000131	arveles	9000000000002	2610111903	\N	\N	Demo supplier
100000000132	iburamin cold	9000000000003	2610101903	2610301903	Demo guest 132	Demo supplier
100000000133	parol	9000000000001	2610091903	\N	\N	Demo supplier
100000000134	arveles	9000000000002	2610081903	\N	\N	Demo supplier
100000000135	iburamin cold	9000000000003	2610071903	\N	\N	Demo supplier
100000000136	parol	9000000000001	2610061903	\N	\N	Demo supplier
100000000137	arveles	9000000000002	2610051903	\N	\N	Demo supplier
100000000138	iburamin cold	9000000000003	2610041903	\N	\N	Demo supplier
100000000139	parol	9000000000001	2610031903	\N	\N	Demo supplier
100000000140	arveles	9000000000002	2610301903	\N	\N	Demo supplier
100000000141	iburamin cold	9000000000003	2610291903	\N	\N	Demo supplier
100000000142	parol	9000000000001	2610281903	\N	\N	Demo supplier
100000000143	arveles	9000000000002	2610271903	\N	\N	Demo supplier
100000000144	iburamin cold	9000000000003	2610261903	2610301903	Demo guest 144	Demo supplier
100000000145	parol	9000000000001	2610251903	\N	\N	Demo supplier
100000000146	arveles	9000000000002	2610241903	\N	\N	Demo supplier
100000000147	iburamin cold	9000000000003	2610231903	\N	\N	Demo supplier
100000000148	parol	9000000000001	2610221903	\N	\N	Demo supplier
100000000149	arveles	9000000000002	2610211903	\N	\N	Demo supplier
100000000150	iburamin cold	9000000000003	2610201903	\N	\N	Demo supplier
100000000151	parol	9000000000001	2610191903	\N	\N	Demo supplier
100000000152	arveles	9000000000002	2610181903	\N	\N	Demo supplier
100000000153	iburamin cold	9000000000003	2610171903	\N	\N	Demo supplier
100000000154	parol	9000000000001	2610161903	\N	\N	Demo supplier
100000000155	arveles	9000000000002	2610151903	\N	\N	Demo supplier
100000000156	iburamin cold	9000000000003	2610141903	2610301903	Demo guest 156	Demo supplier
100000000157	parol	9000000000001	2610131903	\N	\N	Demo supplier
100000000158	arveles	9000000000002	2610121903	\N	\N	Demo supplier
100000000159	iburamin cold	9000000000003	2610111903	\N	\N	Demo supplier
100000000160	parol	9000000000001	2610101903	\N	\N	Demo supplier
100000000161	arveles	9000000000002	2610091903	\N	\N	Demo supplier
100000000162	iburamin cold	9000000000003	2610081903	\N	\N	Demo supplier
100000000163	parol	9000000000001	2610071903	\N	\N	Demo supplier
100000000164	arveles	9000000000002	2610061903	\N	\N	Demo supplier
100000000165	iburamin cold	9000000000003	2610051903	\N	\N	Demo supplier
100000000166	parol	9000000000001	2610041903	\N	\N	Demo supplier
100000000167	arveles	9000000000002	2610031903	\N	\N	Demo supplier
100000000168	iburamin cold	9000000000003	2610301903	2610301903	Demo guest 168	Demo supplier
100000000169	parol	9000000000001	2610291903	\N	\N	Demo supplier
100000000170	arveles	9000000000002	2610281903	\N	\N	Demo supplier
100000000171	iburamin cold	9000000000003	2610271903	\N	\N	Demo supplier
100000000172	parol	9000000000001	2610261903	\N	\N	Demo supplier
100000000173	arveles	9000000000002	2610251903	\N	\N	Demo supplier
100000000174	iburamin cold	9000000000003	2610241903	\N	\N	Demo supplier
100000000175	parol	9000000000001	2610231903	\N	\N	Demo supplier
100000000176	arveles	9000000000002	2610221903	\N	\N	Demo supplier
100000000177	iburamin cold	9000000000003	2610211903	\N	\N	Demo supplier
100000000178	parol	9000000000001	2610201903	\N	\N	Demo supplier
100000000179	arveles	9000000000002	2610191903	\N	\N	Demo supplier
100000000180	iburamin cold	9000000000003	2610181903	2610301903	Demo guest 180	Demo supplier
\.


--
-- Data for Name: takas; Type: TABLE DATA; Schema: portfolio; Owner: -
--

COPY portfolio.takas (karekod, ad, tot, fromt, vertarih, altarih) FROM stdin;
200000000002	arveles	portfolio	pharmacy2	261030191047	\N
\.


--
-- Data for Name: ajarise_setup; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.ajarise_setup (version, details) FROM stdin;
postgres-v1	{"pharmacy2": {"stock": 90, "messages": 2}, "portfolio": {"stock": 180, "messages": 2}}
\.


--
-- Name: messages messages_pkey; Type: CONSTRAINT; Schema: pharmacy2; Owner: -
--

ALTER TABLE ONLY pharmacy2.messages
    ADD CONSTRAINT messages_pkey PRIMARY KEY (messagetime);


--
-- Name: stok stok_pkey; Type: CONSTRAINT; Schema: pharmacy2; Owner: -
--

ALTER TABLE ONLY pharmacy2.stok
    ADD CONSTRAINT stok_pkey PRIMARY KEY (karekod);


--
-- Name: takas takas_pkey; Type: CONSTRAINT; Schema: pharmacy2; Owner: -
--

ALTER TABLE ONLY pharmacy2.takas
    ADD CONSTRAINT takas_pkey PRIMARY KEY (karekod);


--
-- Name: messages messages_pkey; Type: CONSTRAINT; Schema: portfolio; Owner: -
--

ALTER TABLE ONLY portfolio.messages
    ADD CONSTRAINT messages_pkey PRIMARY KEY (messagetime);


--
-- Name: stok stok_pkey; Type: CONSTRAINT; Schema: portfolio; Owner: -
--

ALTER TABLE ONLY portfolio.stok
    ADD CONSTRAINT stok_pkey PRIMARY KEY (karekod);


--
-- Name: takas takas_pkey; Type: CONSTRAINT; Schema: portfolio; Owner: -
--

ALTER TABLE ONLY portfolio.takas
    ADD CONSTRAINT takas_pkey PRIMARY KEY (karekod);


--
-- Name: ajarise_setup ajarise_setup_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ajarise_setup
    ADD CONSTRAINT ajarise_setup_pkey PRIMARY KEY (version);


--
-- Name: messages_recipient_idx; Type: INDEX; Schema: pharmacy2; Owner: -
--

CREATE INDEX messages_recipient_idx ON pharmacy2.messages USING btree (tom);


--
-- Name: stok_name_idx; Type: INDEX; Schema: pharmacy2; Owner: -
--

CREATE INDEX stok_name_idx ON pharmacy2.stok USING btree (ad);


--
-- Name: messages_recipient_idx; Type: INDEX; Schema: portfolio; Owner: -
--

CREATE INDEX messages_recipient_idx ON portfolio.messages USING btree (tom);


--
-- Name: stok_name_idx; Type: INDEX; Schema: portfolio; Owner: -
--

CREATE INDEX stok_name_idx ON portfolio.stok USING btree (ad);


--
-- PostgreSQL database dump complete
--

\unrestrict WcVca4cfV8m4D8fnJMLXsFlDavghvYVhjfT79jlnBojhlKXjJxFiesQV59F5uJR

