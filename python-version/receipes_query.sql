create table if not exists users (
  id_user uuid primary key default gen_random_uuid(),
  name varchar(50) not null,
  email varchar(100) unique not null,
  password text not null,
  register_date timestamp default now()
);

create table if not exists receipes (
  id_receipe uuid primary key default gen_random_uuid(),
  id_user uuid references users(id_user) on delete cascade,
  title varchar(255) not null,
  description text,
  instructions text not null,
  dificulty text check(dificulty in ('Easy', 'Mid', 'Hard')),
  creation_date timestamp default now()
);

create table if not exists ingredients(
  id_ingredient uuid primary key default gen_random_uuid(),
  name varchar(100) unique not null
);

create table if not exists ingredients_recipe (
  id_receipe uuid references receipes(id_receipe) on delete cascade,
  id_ingredients uuid references ingredients(id_ingredient) on delete cascade,
  quantity decimal(5,2) not null,
  unidad_medida varchar(50),
  primary key (id_receipe, id_ingredients)
);

create table if not exists categories (
  id_category uuid primary key default gen_random_uuid(),
  name varchar(100) unique not null
);

create table if not exists receipe_categories (
  id_receipe uuid references receipes(id_receipe) on delete cascade,
  id_category uuid references categories(id_category) on delete cascade,
  primary key (id_receipe, id_category)
);

create table if not exists comments (
  id_comments uuid primary key default gen_random_uuid(),
  id_receipe uuid references receipes(id_receipe) on delete cascade,
  id_usuario uuid references users(id_user) on delete cascade,
  comment text not null,
  calification int check (calification between 1 and 5),
  date timestamp default now()
);