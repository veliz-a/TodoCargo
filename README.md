# TodoCargo

Prototipo de plataforma de compras mayoristas de frutas a partir de la gestión de carga vehicular. Se adapta a la necesidad del mercado para combatir la informalidad, el desorden de cupos, los problemas de salubridad y el caos vehicular.

**Ubicación / contexto:** Mercados mayoristas de Lima, Perú, incluidas zonas marginales.

## Propuesta

TodoCargo no compra fruta ni posee vehículos. **Ordena lo que ya existe en el mercado:** asigna horarios de llegada (cupos) a los camiones, registra qué carga traen y permite que los compradores mayoristas reserven parte de esa carga antes de que llegue.

> "Ninjacart para los mercados mayoristas de Lima: compra de fruta y programación de carga vehicular en un solo lugar."

## Plataformas comparables

| Plataforma | Qué hace | Transporte |
|---|---|---|
| **Ninjacart** (India) | Conecta agricultores con minoristas y gestiona toda la cadena: centros de acopio, hubs y entregas programadas. Es el modelo más cercano. | Camiones medianos contratados del campo a la ciudad; vans y vehículos de tres ruedas para la última milla. |
| **Twiga Foods** (Kenia) | Frutas y verduras para pequeñas tiendas informales con reparto consolidado. Buen caso para estudiar lo difícil que es la rentabilidad. | Camiones a depósitos; camionetas, vans y motos para la última milla. Mayormente tercerizado. |
| **Frubana** (Colombia, México, Brasil) | Marketplace B2B de productos frescos para restaurantes y bodegas. Es la referencia regional. | Proveedores entregan en almacén central; vans y camiones pequeños contratados reparten al día siguiente. |
| **Liftit / Avancargo / Cargamos** | Marketplaces de carga que conectan a quien envía mercadería con transportistas independientes. Cubren la parte de transporte, no la compraventa. | No tienen flota propia. Van desde vans urbanas hasta tractocamiones. |
| **Citas de camiones en puertos** (ej. Callao) | Asignan horarios a los camiones de contenedores para reducir colas. Es la referencia para el módulo de cupos. | Camiones pesados con horario reservado. |
| **EMMSA / Gran Mercado Mayorista de Lima** | Administra el ingreso y los horarios del mercado. Más que competidor, es un posible aliado o punto de integración. | — |


### Por qué estas plataformas no tienen flota propia

Ninjacart y Frubana trabajan principalmente con transporte tercerizado. La diferencia entre ellas está en **qué parte de la cadena controlan**, no en quién es dueño de los camiones:

- **Ninjacart** controla toda la cadena, desde el agricultor hasta el minorista, con rutas y horarios fijos para transportistas contratados.
- **Frubana** controla el almacén y la última milla, y recibe de proveedores y mayoristas.

Ambas evitan tener flota propia por estas razones:

- **Capital:** los camiones son caros, se deprecian y quedan parados fuera de las horas pico. Los productos frescos se mueven de noche y de madrugada.
- **Volumen variable:** las cosechas y la demanda cambian por temporada, y contratar permite crecer o reducir la flota.
- **Oferta disponible:** hay muchísimos transportistas independientes listos para trabajar.
- **El valor está en otra parte:** datos, rutas, control de calidad y relación con compradores.

**Lección para TodoCargo:** quedarse con la coordinación y la programación, no con los vehículos. En los mercados mayoristas de Lima los camiones y choferes ya existen; lo que falta es orden.

### Transporte en el contexto de Lima

Plataformas comparables a TodoCargo usan dos tramos, que en los mercados de Lima corresponden a:

1. **Llegada:** camiones de provincias (sierra, costa norte, selva) que traen la fruta al mercado.
2. **Salida:** colectivos, camiones pequeños y mototaxis que usan los compradores para llevarse la mercadería.

Ninguna plataforma comparable gestiona **cupos y horarios en la puerta del mercado**. Ese es el diferencial de TodoCargo.

## Primer prototipo: alcance mínimo

1. **Coordinar, no poseer.** Sin vehículos ni inventario propios. Solo se programa y conecta a los camiones y choferes que ya trabajan en el mercado.
2. **Cupos de llegada.** Cada camión reserva un horario antes de llegar. Es la función central.
3. **Datos básicos de carga por cupo.** Producto, cantidad aproximada, origen y placa del vehículo.
4. **Un comprador, un pedido.** Un comprador mayorista reserva fruta de una carga que está por llegar. Sin pagos ni negociación de precios dentro de la app.
5. **Control simple en la puerta.** Marcar llegó, descargó y salió para cada cupo. Esto da los datos para demostrar menos congestión.
6. **Funciona en un celular básico.** Web ligera o flujo tipo WhatsApp; muchos transportistas y comerciantes no instalarán una app.
7. **Un mercado, una línea de producto.** Empezar con un solo mercado mayorista y pocas frutas.

**Fuera del alcance por ahora:** pagos, clasificación de calidad, rutas de reparto, almacén propio y funciones de formalización o tributarias.

**Demo mínima:** un transportista reserva un cupo, un comprador reserva parte de la carga y la puerta registra la entrada y salida del camión a tiempo.
