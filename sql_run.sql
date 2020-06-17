--PAISES
INSERT INTO public.country
(id, "name", codigo, lenguaje, currency)
VALUES(1, 'Ecuador', '593', 'español', 'dolar');
INSERT INTO public.country
(id, "name", codigo, lenguaje, currency)
VALUES(2, 'Peru', '523', 'español', 'peso');
INSERT INTO public.country
(id, "name", codigo, lenguaje, currency)
VALUES(3, 'Colombia', '486', 'español', 'peso');

--provincia
INSERT INTO public.province
(id, "name", region, country_id)
VALUES(1, 'Pichincha', 'Sierra', 1);
INSERT INTO public.province
(id, "name", region, country_id)
VALUES(3, 'Guayas', 'Sierra', 2);
--ciudad
INSERT INTO public.city
(id, "name", province_id)
VALUES(1, 'Quito', 1);
INSERT INTO public.city
(id, "name", province_id)
VALUES(2, 'Cayambe', 1);
INSERT INTO public.city
(id, "name", province_id)
VALUES(3, 'Guayaquil', 3);
-- sector
INSERT INTO public.sector
(id, "name", city_id)
VALUES(1, 'Chimbacalle', 1);
INSERT INTO public.sector
(id, "name", city_id)
VALUES(2, 'Solanda', 1);
INSERT INTO public.sector
(id, "name", city_id)
VALUES(3, 'Bicentenario', 1);
-- direccion
INSERT INTO public.adrerss
(id, "name", line_one, line_two, sector_id)
VALUES(1, 's7295', 'paute', 'sangay', 1);
INSERT INTO public.adrerss
(id, "name", line_one, line_two, sector_id)
VALUES(2, 's2345', 'cutuglagua', 's/a', 2);
---retailer
INSERT INTO public.retailer
(id, "name", description, city_id)
VALUES(1, 'Aki', 'AKi micro mercado', 1);
INSERT INTO public.retailer
(id, "name", description, city_id)
VALUES(5, 'Supermaxi', 'Supermaxi', 2);
INSERT INTO public.retailer
(id, "name", description, city_id)
VALUES(2, 'Oki doki', 'micromercado', 1);
INSERT INTO public.retailer
(id, "name", description, city_id)
VALUES(3, 'Oki doki', 'micromercado', 2);
INSERT INTO public.retailer
(id, "name", description, city_id)
VALUES(4, 'mi comisariato', 'micromercado', 3);

--marcas
INSERT INTO public.brand
(id, "name")
VALUES(1, 'Nike');
INSERT INTO public.brand
(id, "name")
VALUES(2, 'Adidas');
INSERT INTO public.brand
(id, "name")
VALUES(3, 'Rokawear');
INSERT INTO public.brand
(id, "name")
VALUES(4, 'Levis');
INSERT INTO public.brand
(id, "name")
VALUES(5, 'New Era');
--categorias
INSERT INTO public.categorie
(id, "name", description)
VALUES(1, 'ropa', 'ropa');
INSERT INTO public.categorie
(id, "name", description)
VALUES(2, 'cosmeticos', 'cosmeticos');
INSERT INTO public.categorie
(id, "name", description)
VALUES(3, 'electrodomesticos', 'electrodomesticos');
--categoria
INSERT INTO public.subcategorie
(id, "name", description, categorie_id)
VALUES(2, 'hombre', 'hombre', 1);
INSERT INTO public.subcategorie
(id, "name", description, categorie_id)
VALUES(3, 'mujer', 'mujer', 1);
INSERT INTO public.subcategorie
(id, "name", description, categorie_id)
VALUES(4, 'bisuteria', 'bisuteria', 2);
INSERT INTO public.subcategorie
(id, "name", description, categorie_id)
VALUES(5, 'perfumeria', 'perfumeria', 2);
INSERT INTO public.subcategorie
(id, "name", description, categorie_id)
VALUES(6, 'cocina', 'cocina', 3);
INSERT INTO public.subcategorie
(id, "name", description, categorie_id)
VALUES(7, 'educacion', 'educacion', 3);

--clientes
INSERT INTO public.client
(id, "name", last_name, email)
VALUES(1, 'Angel', 'Quingaluisa', 'mail1@gmail.comMegaMaxi');
INSERT INTO public.client
(id, "name", last_name, email)
VALUES(2, 'Juan', 'Rojas', 'mail2@gmail.comMegaMaxi');
INSERT INTO public.client
(id, "name", last_name, email)
VALUES(3, 'Pedro', 'Maldonado', 'mail3@gmail.comMegaMaxi');
INSERT INTO public.client
(id, "name", last_name, email)
VALUES(4, 'Sandra', 'Puliloma', 'mail4@gmail.comMegaMaxi');
INSERT INTO public.client
(id, "name", last_name, email)
VALUES(5, 'Daniela', 'Palomo', 'mail5@gmail.comMegaMaxi');
INSERT INTO public.client
(id, "name", last_name, email)
VALUES(6, 'Geovana', 'Black', 'mail5@gmail.comMegaMaxi');
--prime subcription
INSERT INTO public.prime_suscription
(id, "name", vality_type, enabled, vality)
VALUES(1, 'Prime Oro', 'Oro', true, 1);
INSERT INTO public.prime_suscription
(id, "name", vality_type, enabled, vality)
VALUES(2, 'Prime Plata', 'Plata', true, 1);
--cliente prime subcription
INSERT INTO public.client_prime_suscription
(id, activation_date, suscription_state, client_id, prime_suscription_id)
VALUES(1, '2020-01-01', true, 1, 1);
INSERT INTO public.client_prime_suscription
(id, activation_date, suscription_state, client_id, prime_suscription_id)
VALUES(2, '2020-01-02', true, 3, 2);
