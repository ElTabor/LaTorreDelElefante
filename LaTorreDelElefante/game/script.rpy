# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define narrador = Character("Narrador")
define conan = Character("Conan")
define drakos = Character("Drakos")
define taurus = Character("Taurus")
define ladrón = Character("Ladrón")
define yag kosha = Character("Yag Kosha")
define yara = Character("Yara")


# El juego comienza aquí.

label start:

scene interior_del_bar:
narrador "En la mesa mas poblada un grupo de delincuentes están atentos a los relatos de un hombre obeso y grosero proveniente de koth"

drakos "Por Bel, dios de los ladrones, que voy a enseñarles como se roba una mujer; estara del otro lado de la frontera de Zamora antes del amanecer, y allí habrá una caravana esperándola. Un conde de Ofir me prometió trecientas piezas de plata por una joven brithunia de buena familia. Estuve vagando varias semanas por las ciudades fronterizas, donde me hacía pasar por mendigo, hasta que encontré una que valiera la pena. ¡Ah, qué guapa es esta golfa! Conozco señores de Shem que darían por ella el secreto de la Torre del Elefante."

narrador "Mientras Drakos vuelve a su cerveza, siente cómo alguien tira de la manga de su túnica y se da vuelta con el entrecejo fruncido para ver a un hmbre alto y corpulento"

conan "Has mencionado la Torre del Elefante. He escuchado muchas cosas acerca de esa torre.¿Cuál es su secreto?"

drakos "Y ¿De dónde salus tu? extraño, no pareces de por aquí".

ladrón "No nos gustan los forasteros."

conan"Soy Cimerio…"

drakos"No me sorprende, los cimerios son vulgares. Pero hasta el más tonto de su tipo conocen la leyenda de la torre."

narrador "A pesar de que el muchacho no tiene una actitud amenazante, DRAKOS, bajo los efectos del alcohol y la aprobación de su gente, se llena de valor y lo confronta."

drakos "¿El secreto de la Torre del Elefante? Bueno, cualquier imbécil sabe que el sacerdote YARA vive allí con la enorme joya llamada Corazón de Elefante; ese es el secreto de su magia."
    
conan "Yo he visto esa torre. Está en un enorme jardín situado en lo alto de la ciudad y rodeado de elevadas murallas. No he visto guardias. Las murallas parecían fáciles de escalar. ¿Por qué nadie ha robado esa misteriosa piedra preciosa?"

drakos "¡Escuchen a este pagano salvaje!¡Pretende robar la joya de YARA!"

drakos "Entonces presta atención y aprende, muchacho. Debes saber que en Zamora, y especialmente en esta ciudad, hay más intrépidos ladrones que en cualquier otro lugar del mundo, incluido Koth. Si algún mortal hubiera sido capaz de robar la piedra preciosa, puedes estar seguro de que habría desaparecido hace mucho tiempo. Tú hablas de escalar las murallas, pero una vez que lo hubieras hecho, desearías irte inmediatamente. Por la noche no hay guardias, es decir, guardias humanos, en los jardines por una buena razón. Pero en el cuarto de guardia, en la parte inferior de la torre, hay hombres armados, y aun si lograras escabullirte entre los que rondan por los jardines de noche, tendrías que eludir a los soldados, porque la gema está guardada en algún lugar de la parte superior de la torre."

conan "Pero si alguien consiguiera atravesar los jardines, ¿por qué no iba a poder llegar hasta la gema por la parte superior de la torre, eludiendo de ese modo a los soldados?"

drakos "¡Oíd lo que está diciendo! ¡Este bárbaro debe de ser un águila capaz de volar hasta el borde enjoyado de la torre, que se halla a tan solo cincuenta metros de altura, y que tiene las paredes más lisas y resbaladizas que el cristal pulido!"

narrador "CONAN, molesto por las carcajadas burlonas de los oyentes y confundido por la falta de cortesía de los locales. Piensa en salir corriendo del lugar pero DRAKOS continúa con su mofa."

drakos "¡Anda, anda! ¡Cuéntales a estos pobres hombres, que han sido ladrones desde antes que a ti te engendraran, diles cómo robarías tú la piedra!"

conan "Siempre hay alguna manera de hacerlo, si el deseo está unido al valor."

drakos "¡Cómo! ¿Te atreves a enseñarnos nuestro oficio, y a insinuar que somos unos cobardes? ¡Vete! ¡Fuera de mi vista!"

narrador "Drakos le da un leve empujón para intimidar a Conan. "

menu: 
"Matar a Drakos?":
    "Sí":
        $ matar_drakos = True
        jump matar_drakos_escena
    "No":
        $ matar_drakos = False
        jump perdonar_drakos_escena
    

label matar_drakos_escena:
conan "¿Te atreves a pedirme piedad luego de haberme faltado el respeto?"

narrador "Con un solo movimiento, CONAN separa la cabeza del cuerpo de DRAKOS."

scene exterior_calle_Arenjún,_Zamora_Noche

narrador "La taberna queda atrás mientras CONAN avanza sigilosamente por las calles desiertas, dirigiéndose hacia la Torre del Elefante. Con su cuerpo marcado por cicatrices de múltiples batallas, moviéndose con la destreza de un cazador, aunque los callejones de Zamora le eran desconocidos. A su alrededor, los templos brillan bajo las estrellas, pero las deidades locales no le impresionan. CONAN cree en una verdad simple: los dioses, como Crom, son indiferentes y terribles. Frente a él, la Torre del Elefante se alza imponente y misteriosa, rodeada de un jardín exótico protegido por altas murallas. Aunque las leyendas sobre los peligros de la torre y YARA, su guardián oscuro, le rondan la mente, CONAN no teme. Da un gran salto y alcanza la cima de la muralla. Ve unos arbustos y se lanza hacia ellos"

label perdonar_drakos_escena:

scene interior_bar:

conan "De acuerdo, te voy a dar la oportunidad de redimir tu insolencia acompañándome hacia la torre. Levántate."

narrador "CONAN envaina su espada y extiende su mano. DRAKOS la toma, se para y se sacude el polvo mientras mira a CONAN con una expresión de asombro y terror. Después de levantar a Drakos se dirigen hacia las calles de Zamora."

scene exterior_calle_arenjún_Zamora_noche:

drakos "Mi nombre es DRAKOS, por cierto. Aunque dudo que te importe."

conan "¿Por qué?"

drakos "¿Qué no eres cimmerio? Tu cultura se reduce a violencia y destrucción. Seguro ni siquiera tienes un nombre propio."

conan "Ja. Claro que tengo un nombre, CONAN. Y tus creencias sobre mi cultura no son más que patrañas. Somos fuertes, poderosos y nos cuesta relacionarnos con sus costumbres civilizadas pero te aseguro que uno de nosotros porta más honor que todo un pueblo de ustedes."

drakos "Claro, y por eso estamos yendo a la torre, ¿verdad? No porque quieras robarte una gema."

conan "La gema es lo de menos, imbécil. El verdadero valor está en demostrar mi poder."

narrador "Mientras terminan de discutir sobre sus valores se ve la torre a lo lejos."

drakos "Como digas… hasta que llego yo, ya cumplí mi deuda?"

conan "Así es. Gracias por la compañía."

narrador "DRAKOS observa cómo CONAN se sumerge en aquella torre de tantos mitos mientras se pregunta si es una simple ilusión o lleva algo de verdad en sus palabras. "


scene exterior_jardinesDeLaTorre:

narrador "En la distancia, ve movimiento detrás de otros arbustos. CONAN decide correr hacia ellos empuñando su espada, listo para eliminar cualquier amenaza. Al llegar, descubre un cuerpo estrangulado, lo que indica la presencia de alguien. Sigiloso, acechando en la oscuridad hasta que se encuentra con una figura misteriosa, que rompe el silencio con un susurro, anticipando lo que está por suceder."

taurus "Tú no eres soldado. Eres un ladrón, igual que yo."

conan "¿Y tú quién eres?"

taurus "Soy TAURUS de Nemedia."

narrador "Ante ese nombre, CONAN relaja ligeramente su agarre en la espada."

conan "He oído hablar de ti. Todos te llaman el príncipe de los ladrones."

narrador "Una risa suave se escapa de los labios de TAURUS. Es tan alto como CONAN, pero más corpulento. A pesar de su voluminoso vientre, hay algo magnético y ágil en sus movimientos, una fluidez sutil que delata a un hombre peligroso. Sus ojos, brillantes incluso bajo la luz de las estrellas, denotan inteligencia y astucia. Lleva enrollada a su cintura una cuerda fina y fuerte, con nudos distribuidos a intervalos regulares."

taurus "¿Y tú quién eres?" 

conan "Soy CONAN, el cimmerio. He venido a ver si puedo robar la gema de YARA, la que llaman el Corazón de Elefante"

narrador "TAURUS, divertido, ríe en silencio, y aunque CONAN puede notar que no era una risa despectiva, le resulta un tanto inesperada."

taurus "¡Por Bel, dios de los ladrones! Pensaba que era el único con el valor suficiente para intentar este robo. Esos zamorios se creen grandes ladrones, pero tú, CONAN... me gusta tu osadía. Nunca he compartido una aventura con nadie, pero por Bel, vamos a intentar esto juntos, si estás de acuerdo."

narrador "Conan observó al hombre con ojos penetrantes antes de hablar." 



show eileen happy

    # Presenta las líneas del diálogo.

    e "Has creado un nuevo juego Ren'Py."

    e "Añade una historia, imágenes y música, ¡y puedes presentarlo al mundo!"

    # Finaliza el juego:

    return
