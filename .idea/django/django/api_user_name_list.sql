create table django.api_user_name_list
(
    id        bigint auto_increment
        primary key,
    username  varchar(150) not null,
    password  varchar(128) not null,
    nickname  varchar(150) not null,
    sex       varchar(50)  not null,
    avatar    varchar(100) null,
    cellphone bigint       null,
    email     varchar(100) null,
    remarks   longtext     null,
    role_id   bigint       not null,
    jointime  datetime(6)  not null,
    constraint role_id
        unique (role_id),
    constraint api_user_name_list_role_id_b2ed1335_fk_api_user_role_list_id
        foreign key (role_id) references django.api_user_role_list (id)
);

