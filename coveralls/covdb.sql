PGDMP         4                 x            covdb    12.3    12.3                0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    16393    covdb    DATABASE     �   CREATE DATABASE covdb WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'Russian_Russia.1251' LC_CTYPE = 'Russian_Russia.1251';
    DROP DATABASE covdb;
                postgres    false            �            1259    16407    clothes    TABLE       CREATE TABLE public.clothes (
    clothes_id smallint NOT NULL,
    type_of_clothing character varying(200),
    model character varying(200),
    size smallint,
    suppliers character varying(200),
    article character varying(200),
    job_title_list text
);
    DROP TABLE public.clothes;
       public         heap    postgres    false            �            1259    16402 
   job_titles    TABLE     R   CREATE TABLE public.job_titles (
    job_title character varying(200) NOT NULL
);
    DROP TABLE public.job_titles;
       public         heap    postgres    false            �            1259    16396    users    TABLE     >  CREATE TABLE public.users (
    id integer NOT NULL,
    last_name character varying(30),
    first_name character varying(30),
    patronymic character varying(30),
    job_title character varying(200),
    department character varying(200),
    height smallint,
    clothing_size smallint,
    foot_size smallint
);
    DROP TABLE public.users;
       public         heap    postgres    false            �            1259    16394    users_id_seq    SEQUENCE     �   CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 #   DROP SEQUENCE public.users_id_seq;
       public          postgres    false    203                       0    0    users_id_seq    SEQUENCE OWNED BY     =   ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;
          public          postgres    false    202            �
           2604    16399    users id    DEFAULT     d   ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);
 7   ALTER TABLE public.users ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    203    202    203                      0    16407    clothes 
   TABLE DATA           p   COPY public.clothes (clothes_id, type_of_clothing, model, size, suppliers, article, job_title_list) FROM stdin;
    public          postgres    false    205                    0    16402 
   job_titles 
   TABLE DATA           /   COPY public.job_titles (job_title) FROM stdin;
    public          postgres    false    204   6                 0    16396    users 
   TABLE DATA              COPY public.users (id, last_name, first_name, patronymic, job_title, department, height, clothing_size, foot_size) FROM stdin;
    public          postgres    false    203   S                  0    0    users_id_seq    SEQUENCE SET     ;   SELECT pg_catalog.setval('public.users_id_seq', 1, false);
          public          postgres    false    202            �
           2606    16414    clothes clothes_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.clothes
    ADD CONSTRAINT clothes_pkey PRIMARY KEY (clothes_id);
 >   ALTER TABLE ONLY public.clothes DROP CONSTRAINT clothes_pkey;
       public            postgres    false    205            �
           2606    16406    job_titles job_titles_pkey 
   CONSTRAINT     _   ALTER TABLE ONLY public.job_titles
    ADD CONSTRAINT job_titles_pkey PRIMARY KEY (job_title);
 D   ALTER TABLE ONLY public.job_titles DROP CONSTRAINT job_titles_pkey;
       public            postgres    false    204            �
           2606    16401    users users_pkey 
   CONSTRAINT     N   ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);
 :   ALTER TABLE ONLY public.users DROP CONSTRAINT users_pkey;
       public            postgres    false    203                  x������ � �            x������ � �            x������ � �     