create table django.api_user_role_list
(
    id        bigint auto_increment
        primary key,
    role_name varchar(100) not null,
    limits    varchar(100) not null,
    descr     varchar(100) not null,
    checks    varchar(5)   not null
);

