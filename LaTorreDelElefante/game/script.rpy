# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define Conan = Character("CONAN", color = "#e9c33c")
define Drakos = Character("DRAKOS", color = "#0a0a0a")
define Taurus = Character("TAURUS", color = "#643523")
define ladrón = Character("LADRÓN", color = "#0a0a0a")
define yagKosha = Character("YAG KOSHA", color = "#91ef91")
define Yara = Character("YARA", color = "#981723")

default Conan_esta_solo = False
default Conan_esta_herido = False
default Conan_mata_a_Drakos = False

# El juego comienza aquí.

label start:

scene interior_del_bar
"En la mesa mas poblada un grupo de delincuentes están atentos a los relatos de un hombre obeso y grosero proveniente de koth"

Drakos "Por Bel, dios de los ladrones, que voy a enseñarles como se roba una mujer; estara del otro lado de la frontera de Zamora antes del amanecer, y allí habrá una caravana esperándola."
Drakos "Un conde de Ofir me prometió trecientas piezas de plata por una joven brithunia de buena familia. Estuve vagando varias semanas por las ciudades fronterizas, donde me hacía pasar por mendigo, hasta que encontré una que valiera la pena."
Drakos "¡Ah, qué guapa es esta golfa! Conozco señores de Shem que darían por ella el secreto de la Torre del Elefante."

"Mientras Drakos vuelve a su cerveza, siente cómo alguien tira de la manga de su túnica y se da vuelta con el entrecejo fruncido para ver a un hmbre alto y corpulento"

Conan "Has mencionado la Torre del Elefante. He escuchado muchas cosas acerca de esa torre.¿Cuál es su secreto?"

Drakos "Y ¿De dónde salus tu? extraño, no pareces de por aquí."

ladrón "No nos gustan los forasteros."

Conan"Soy Cimerio…"

Drakos "No me sorprende, los cimerios son vulgares. Pero hasta el más tonto de su tipo conocen la leyenda de la torre."

"A pesar de que el muchacho no tiene una actitud amenazante, Drakos, bajo los efectos del alcohol y la aprobación de su gente, se llena de valor y lo confronta."

Drakos "¿El secreto de la Torre del Elefante? Bueno, cualquier imbécil sabe que el sacerdote Yara vive allí con la enorme joya llamada Corazón de Elefante; ese es el secreto de su magia."
    
    scene bg Conan_Caminando_Por_Un_Callejón_Iluminado_Tenuemente with fade
    
    "Conan se encuentra caminando en un cajellon de la ciudad dirigiendose hacia lo que seria un bar lleno de personas"
    
    scene bg interior_del_bar with fade
    
    
    "En la mesa mas poblada un grupo de delincuentes están atentos a los relatos de un hombre obeso y grosero proveniente de koth"
    
    show drakos at center
    Drakos "Por Bel, dios de los ladrones, que voy a enseñarles como se roba una mujer; estara del otro lado de la frontera de Zamora antes del amanecer, y allí habrá una caravana esperándola."
    Drakos "Un conde de Ofir me prometió trecientas piezas de plata por una joven brithunia de buena familia. Estuve vagando varias semanas por las ciudades fronterizas, donde me hacía pasar por mendigo, hasta que encontré una que valiera la pena."
    Drakos "¡Ah, qué guapa es esta golfa! Conozco señores de Shem que darían por ella el secreto de la Torre del Elefante."
    
    hide drakos
    "Mientras Drakos vuelve a su cerveza, siente cómo alguien tira de la manga de su túnica y se da vuelta con el entrecejo fruncido para ver a un hombre alto y corpulento"
    
    show conan at right
    Conan "Has mencionado la Torre del Elefante. He escuchado muchas cosas acerca de esa torre.¿Cuál es su secreto?"
    
    show drakos at left
    Drakos "Y ¿De dónde salus tu? extraño, no pareces de por aquí."
    
    hide conan
    hide drakos
    
    show ladrón at center
    ladrón "No nos gustan los forasteros."
    
    hide ladrón
    show conan at left
    
    Conan "Soy Cimerio…"
    show drakos at right
    Drakos "No me sorprende, los cimerios son vulgares. Pero hasta el más tonto de su tipo conocen la leyenda de la torre."
    
    hide conan
    hide drakos
    "A pesar de que el muchacho no tiene una actitud amenazante, Drakos, bajo los efectos del alcohol y la aprobación de su gente, se llena de valor y lo confronta."
    
    show drakos at right
    Drakos "¿El secreto de la Torre del Elefante? Bueno, cualquier imbécil sabe que el sacerdote Yara vive allí con la enorme joya llamada Corazón de Elefante; ese es el secreto de su magia."
    
    show conan at left
    Conan "Yo he visto esa torre. Está en un enorme jardín situado en lo alto de la ciudad y rodeado de elevadas murallas. No he visto guardias. Las murallas parecían fáciles de escalar. ¿Por qué nadie ha robado esa misteriosa piedra preciosa?"
    hide conan
    Drakos "¡Escuchen a este pagano salvaje!¡Pretende robar la joya de Yara!"
    Drakos "Entonces presta atención y aprende, muchacho. Debes saber que en Zamora, y especialmente en esta ciudad, hay más intrépidos ladrones que en cualquier otro lugar del mundo, incluido Koth."
    Drakos "Si algún mortal hubiera sido capaz de robar la piedra preciosa, puedes estar seguro de que habría desaparecido hace mucho tiempo. Tú hablas de escalar las murallas, pero una vez que lo hubieras hecho, desearías irte inmediatamente."
    Drakos "Por la noche no hay guardias, es decir, guardias humanos, en los jardines por una buena razón."
    Drakos "Pero en el cuarto de guardia, en la parte inferior de la torre, hay hombres armados, y aun si lograras escabullirte entre los que rondan por los jardines de noche, tendrías que eludir a los soldados, porque la gema está guardada en algún lugar de la parte superior de la torre."
    show conan
    Conan "Pero si alguien consiguiera atravesar los jardines, ¿por qué no iba a poder llegar hasta la gema por la parte superior de la torre, eludiendo de ese modo a los soldados?"
    
    Drakos "¡Oíd lo que está diciendo! ¡Este bárbaro debe de ser un águila capaz de volar hasta el borde enjoyado de la torre, que se halla a tan solo cincuenta metros de altura, y que tiene las paredes más lisas y resbaladizas que el cristal pulido!"
    
    hide conan
    hide drakos
    "Conan, molesto por las carcajadas burlonas de los oyentes y confundido por la falta de cortesía de los locales. Piensa en salir corriendo del lugar pero Drakos continúa con su mofa."
    
    show drakos at right
    Drakos "¡Anda, anda! ¡Cuéntales a estos pobres hombres, que han sido ladrones desde antes que a ti te engendraran, diles cómo robarías tú la piedra!"
    
    show conan at left
    Conan "Siempre hay alguna manera de hacerlo, si el deseo está unido al valor."
    
    Drakos "¡Cómo! ¿Te atreves a enseñarnos nuestro oficio, y a insinuar que somos unos cobardes? ¡Vete! ¡Fuera de mi vista!"
    
    "Drakos le da un leve empujón para intimidar a Conan."
    
    
    
    menu Matar_a_Drakos:
        "Sí":
            $ Conan_mata_a_Drakos = True
            jump matar_a_Drakos
        "No":
            jump perdonar_a_Drakos
Conan "Yo he visto esa torre. Está en un enorme jardín situado en lo alto de la ciudad y rodeado de elevadas murallas. No he visto guardias. Las murallas parecían fáciles de escalar. ¿Por qué nadie ha robado esa misteriosa piedra preciosa?"

Drakos "¡Escuchen a este pagano salvaje!¡Pretende robar la joya de Yara!"

Drakos "Entonces presta atención y aprende, muchacho. Debes saber que en Zamora, y especialmente en esta ciudad, hay más intrépidos ladrones que en cualquier otro lugar del mundo, incluido Koth."
Drakos "Si algún mortal hubiera sido capaz de robar la piedra preciosa, puedes estar seguro de que habría desaparecido hace mucho tiempo. Tú hablas de escalar las murallas, pero una vez que lo hubieras hecho, desearías irte inmediatamente."
Drakos "Por la noche no hay guardias, es decir, guardias humanos, en los jardines por una buena razón."
Drakos "Pero en el cuarto de guardia, en la parte inferior de la torre, hay hombres armados, y aun si lograras escabullirte entre los que rondan por los jardines de noche, tendrías que eludir a los soldados, porque la gema está guardada en algún lugar de la parte superior de la torre."

Conan "Pero si alguien consiguiera atravesar los jardines, ¿por qué no iba a poder llegar hasta la gema por la parte superior de la torre, eludiendo de ese modo a los soldados?"

Drakos "¡Oíd lo que está diciendo! ¡Este bárbaro debe de ser un águila capaz de volar hasta el borde enjoyado de la torre, que se halla a tan solo cincuenta metros de altura, y que tiene las paredes más lisas y resbaladizas que el cristal pulido!"

"Conan, molesto por las carcajadas burlonas de los oyentes y confundido por la falta de cortesía de los locales. Piensa en salir corriendo del lugar pero Drakos continúa con su mofa."

Drakos "¡Anda, anda! ¡Cuéntales a estos pobres hombres, que han sido ladrones desde antes que a ti te engendraran, diles cómo robarías tú la piedra!"

Conan "Siempre hay alguna manera de hacerlo, si el deseo está unido al valor."

Drakos "¡Cómo! ¿Te atreves a enseñarnos nuestro oficio, y a insinuar que somos unos cobardes? ¡Vete! ¡Fuera de mi vista!"

"Drakos le da un leve empujón para intimidar a Conan. "

menu Matar_a_Drakos:
    "Sí":
        $ Conan_mata_a_Drakos = True
        jump matar_a_Drakos
    "No":
        jump perdonar_a_Drakos
    
label matar_a_Drakos:
    scene bg matar_Drakos_escena with fade 
    show conan at center
    Conan "¿Te atreves a pedirme piedad luego de haberme faltado el respeto?"
    
    
    
    "Con un solo movimiento, Conan separa la cabeza del cuerpo de Drakos."
    
    
    hide conan
    
    scene bg exterior_calle_Arenjun__Zamora_Noche with fade
    "La taberna queda atrás mientras Conan avanza sigilosamente por las calles desiertas, dirigiéndose hacia la Torre del Elefante."
    "Con su cuerpo marcado por cicatrices de múltiples batallas, moviéndose con la destreza de un cazador, aunque los callejones de Zamora le eran desconocidos."
    "A su alrededor, los templos brillan bajo las estrellas, pero las deidades locales no le impresionan. Conan cree en una verdad simple: los dioses, como Crom, son indiferentes y terribles."
    "Frente a él, la Torre del Elefante se alza imponente y misteriosa, rodeada de un jardín exótico protegido por altas murallas."
    "Aunque las leyendas sobre los peligros de la torre y Yara, su guardián oscuro, le rondan la mente, Conan no teme. Da un gran salto y alcanza la cima de la muralla. Ve unos arbustos y se lanza hacia ellos"
    
    jump Conan_llega_a_la_torre
    
scene matar_Drakos_escena
Conan "¿Te atreves a pedirme piedad luego de haberme faltado el respeto?"

"Con un solo movimiento, Conan separa la cabeza del cuerpo de Drakos."

scene exterior_calle_Arenjun__Zamora_Noche

"La taberna queda atrás mientras Conan avanza sigilosamente por las calles desiertas, dirigiéndose hacia la Torre del Elefante."
"Con su cuerpo marcado por cicatrices de múltiples batallas, moviéndose con la destreza de un cazador, aunque los callejones de Zamora le eran desconocidos."
"A su alrededor, los templos brillan bajo las estrellas, pero las deidades locales no le impresionan. Conan cree en una verdad simple: los dioses, como Crom, son indiferentes y terribles."
"Frente a él, la Torre del Elefante se alza imponente y misteriosa, rodeada de un jardín exótico protegido por altas murallas."
"Aunque las leyendas sobre los peligros de la torre y Yara, su guardián oscuro, le rondan la mente, Conan no teme. Da un gran salto y alcanza la cima de la muralla. Ve unos arbustos y se lanza hacia ellos"

jump Conan_llega_a_la_torre

label perdonar_a_Drakos:
<<<<<<< HEAD
    scene perdonar_Drakos_escena 
    scene bg interior_bar with fade
    
    show conan at center
    Conan "De acuerdo, te voy a dar la oportunidad de redimir tu insolencia acompañándome hacia la torre. Levántate."
    hide conan
    "Conan envaina su espada y extiende su mano. Drakos la toma, se para y se sacude el polvo mientras mira a Conan con una expresión de asombro y terror. Después de levantar a Drakos se dirigen hacia las calles de Zamora."
    
    
    
    scene bg Calledezamora with fade
    
    
    show drakos at left
    Drakos "Mi nombre es Drakos, por cierto. Aunque dudo que te importe."
    
    show conan at right
    Drakos "Mi nombre es Drakos, por cierto. Aunque dudo que te importe."
=======
scene perdonar_Drakos_escena
>>>>>>> parent of 4c01768 (Update script.rpy)

scene interior_bar

Conan "De acuerdo, te voy a dar la oportunidad de redimir tu insolencia acompañándome hacia la torre. Levántate."

"Conan envaina su espada y extiende su mano. Drakos la toma, se para y se sacude el polvo mientras mira a Conan con una expresión de asombro y terror. Después de levantar a Drakos se dirigen hacia las calles de Zamora."

scene exterior_calle_arenjún_Zamora_noche

Drakos "Mi nombre es Drakos, por cierto. Aunque dudo que te importe."

Conan "¿Por qué?"

Drakos "¿Qué no eres cimmerio? Tu cultura se reduce a violencia y destrucción. Seguro ni siquiera tienes un nombre propio."

<<<<<<< HEAD
    Conan "Así es. Gracias por la compañía."
    
    hide drakos
    hide conan
    
    "Drakos observa cómo Conan se sumerge en aquella torre de tantos mitos mientras se pregunta si es una simple ilusión o lleva algo de verdad en sus palabras."
    "A su vez, Conan salta el muro que resguarda la torre. Una vez dentro, ve unos arbustos y se oculta entre ellos"
=======
Conan "Ja. Claro que tengo un nombre, Conan. Y tus creencias sobre mi cultura no son más que patrañas. Somos fuertes, poderosos y nos cuesta relacionarnos con sus costumbres civilizadas pero te aseguro que uno de nosotros porta más honor que todo un pueblo de ustedes."

Drakos "Claro, y por eso estamos yendo a la torre, ¿verdad? No porque quieras robarte una gema."

Conan "La gema es lo de menos, imbécil. El verdadero valor está en demostrar mi poder."

"Mientras terminan de discutir sobre sus valores se ve la torre a lo lejos."

Drakos "Como digas… hasta aquí llego yo. Ya cumplí mi deuda?"

Conan "Así es. Gracias por la compañía."

"Drakos observa cómo Conan se sumerge en aquella torre de tantos mitos mientras se pregunta si es una simple ilusión o lleva algo de verdad en sus palabras."
"A su vez, Conan salta el muro que resguarda la torre. Una vez dentro, ve unos arbustos y se oculta entre ellos"
>>>>>>> parent of 4c01768 (Update script.rpy)

label Conan_llega_a_la_torre:
scene exterior_jardinesDeLaTorre

"En la distancia, Conan ve movimiento detrás de otros arbustos y decide correr hacia ellos empuñando su espada, listo para eliminar cualquier amenaza."
"Al llegar, descubre un cuerpo estrangulado, lo que indica la presencia de alguien. Sigiloso, acechando en la oscuridad hasta que se encuentra con una figura misteriosa, que rompe el silencio con un susurro, anticipando lo que está por suceder."

Taurus "Tú no eres soldado. Eres un ladrón, igual que yo."

Conan "¿Y tú quién eres?"

Taurus "Soy Taurus de Nemedia."

"Ante ese nombre, Conan relaja ligeramente su agarre en la espada."

Conan "He oído hablar de ti. Todos te llaman el príncipe de los ladrones."

"Una risa suave se escapa de los labios de Taurus. Es tan alto como Conan, pero más corpulento. A pesar de su voluminoso vientre, hay algo magnético y ágil en sus movimientos, una fluidez sutil que delata a un hombre peligroso."
"Sus ojos, brillantes incluso bajo la luz de las estrellas, denotan inteligencia y astucia. Lleva enrollada a su cintura una cuerda fina y fuerte, con nudos distribuidos a intervalos regulares."

Taurus "¿Y tú quién eres?" 

Conan "Soy Conan, el cimmerio. He venido a ver si puedo robar la gema de Yara, la que llaman el Corazón de Elefante"

"Taurus, divertido, ríe en silencio, y aunque Conan puede notar que no era una risa despectiva, le resulta un tanto inesperada."

Taurus "¡Por Bel, dios de los ladrones! Pensaba que era el único con el valor suficiente para intentar este robo. Esos zamorios se creen grandes ladrones, pero tú, Conan... me gusta tu osadía. Nunca he compartido una aventura con nadie, pero por Bel, vamos a intentar esto juntos, si estás de acuerdo."

"Conan observó al hombre con ojos penetrantes antes de hablar." 

Conan "Entonces, ¿tú también buscas la gema?"

Taurus "¿Qué más podría estar buscando? He estado planeando este golpe durante meses. Tú, en cambio, parece que has venido aquí por pura impulsividad, amigo."

Conan "¿Tú mataste al soldado?"

Taurus "Por supuesto. Me arrastré por la muralla cuando él estaba en el extremo opuesto del jardín. Al esconderme entre los matorrales, me escuchó o creyó haber oído algo."
Taurus"Fue su error. Cuando se acercó, fue fácil ponerme detrás de él y estrangularlo antes de que pudiera emitir un sonido. Como la mayoría de los hombres, era medio ciego en la oscuridad."

"Conan frunció el ceño, y tras una breve pausa, añade:"

Conan "Pero cometiste un error."

"Los ojos de Taurus, llenos de orgullo, se encendieron de cólera ante esa afirmación."

Taurus "¿Un error? ¡Imposible!"

Conan "Deberías haber ocultado el cadáver entre los arbustos."

"Taurus lo mira con una mezcla de incredulidad y furia, pero el bárbaro continúa."

Conan "No cambian la guardia hasta pasada la medianoche, lo sé, pero si alguien viene antes y encuentra el cuerpo, nos arriesgamos a que den la alarma."

"Taurus respiró hondo, calmándose, aunque no parecía gustarle la idea de recibir una lección del cimmerio."

Taurus "El novato pretende enseñar su arte al maestro. Si alguien viene a buscarlo ahora y encuentra su cuerpo, irá a comunicarle inmediatamente la noticia a Yara, lo que nos daría tiempo para escapar. Pero si no lo hallaran, rastrearán los arbustos y nos atraparán como a ratas en una trampa."

Conan "Tienes razón."

Taurus "Así es. Ahora escucha. Estamos perdiendo tiempo con esta maldita discusión.No hay guardianes en el jardín interior, quiero decir guardias humanos, aunque hay centinelas que son mucho más peligrosos aún."
Taurus "Es su presencia la que me ha detenido durante tanto tiempo, pero finalmente he descubierto una forma de burlarlos."

Conan "¿Y qué me dices de los soldados que vigilan en la parte inferior de la torre?"

Taurus "El  viejo Yara vive en las habitaciones superiores. Por ese camino vamos a entrar… y salir, espero. No me preguntes cómo. He planeado una forma de hacerlo."
Taurus "Nos introduciremos furtivamente por la parte superior de la torre y estrangularemos al viejo Yara antes de que nos pueda hechizar con alguno de sus condenados maleficios."
Taurus "Al menos lo intentaremos; corremos el riesgo de que nos convierta en arañas o en sapos asquerosos, pero por otro lado tenemos la posibilidad de obtener toda la riqueza y el poder del mundo. Un buen ladrón debe saber correr riesgos."

Conan "Iré hasta donde sea"

Taurus "Entonces sígueme."

"Taurus termina de decir esto y vuelve, toma impulso, se aferra a la muralla y salta. La agilidad de aquel hombre es asombrosa, teniendo en cuenta su tamaño; parece casi deslizarse hacia el borde del muro. Conan lo sigue y cuando están de bruces sobre el ancho paredón, hablan en voz baja."

Conan "No veo ninguna luz"

"La parte inferior de la torre se parece mucho a la parte que se ve desde fuera del jardín: un cilindro perfecto y brillante, que no parece tener ninguna abertura."

Taurus "Hay puertas y ventanas hábilmente construidas. Pero están cerradas. Los soldados respiran el aire que viene de arriba."

"El jardín es un vago conjunto de sombras cubiertas de pequeños árboles donde se balancean sombríamente en la oscuridad ligeros arbustos."
"El cauto espíritu de Conan siente el aura amenazadora que se cierne sobre aquel lugar. Percibe la mirada ardiente de unos ojos invisibles y siente un aroma sutil que le eriza instintivamente el pelo de la nuca como a los sabuesos cuando huelen la presencia de su antiguo enemigo."

Taurus "Sígueme. Ven detrás de mí, si aprecias tu vida."

"Taurus extrae de su cinto lo que parece ser un tubo de cobre, el nemedio se deja caer nuevamente encima del césped interior. Conan lo sigue de cerca con la espada preparada, pero Taurus lo empuja hacia atrás, contra la pared, y se queda inmóvil."
"Está en una actitud de tensa expectación y su mirada, al igual que la de Conan, se fija en las sombras de los arbustos que hay cerca de allí. La mata se mueve a pesar de que la brisa deja de soplar."
"En ese momento ven dos enormes ojos resplandecientes entre las ondulantes sombras y detrás de estos pueden ver otros destellos de fuego que centellean en la oscuridad."

Conan "¡Leones!"

Taurus "Sí, de día los encierran en unas cavernas subterráneas que hay debajo de la torre. Por eso no hay guardianes en este jardín."

Conan "Yo veo cinco, pero quizá haya más en los matorrales. Nos atacarán de un momento a otro."

Taurus "¡Silencio!"

"Se oyen ruidos sordos provenientes de las sombras y se ven avanzar los ojos resplandecientes. Conan percibe las inmensas mandíbulas babeantes y las colas que azotan el aire en todas direcciones. La tensión es insoportable."
"El cimmerio empuña la espada, a la espera del inevitable ataque de los gigantescos cuerpos. Entonces, Taurus lleva el extremo del tubo a los labios y sopla con fuerza."
"Un gran chorro de polvo dorado sale por el otro extremo y se extiende instantáneamente formando una densa nube de color verde amarillento que cubre los arbustos, ocultando los resplandecientes ojos."
"Taurus corre apresuradamente hacia el muro. Conan lo mira sin comprender. La densa nube oculta los matorrales y no se oye nada."

Conan "¿Qué es ese polvo?"

Taurus "¡Es la muerte! Si se levanta viento y sopla en nuestra dirección, tendremos que huir saltando la muralla. Pero no, no se ha levantado viento y la nube se está disipando. Espera hasta que desaparezca del todo. Respirar ese polvo supone la muerte."

"Finalmente quedan flotando solo unas tenues nubecillas amarillentas en el aire; cuando desaparecen, Taurus indica a su compañero con la mano que avance. Se dirigen sigilosamente hacia los arbustos y Conan se queda boquiabierto."
"Tendidos en el suelo entre las sombras yacen cinco cuerpos de color pardo cuya mirada feroz se ha extinguido para siempre. Un olor dulzón y empalagoso persiste en el aire."

Conan "¡Murieron sin lanzar un solo rugido! Taurus, ¿qué era ese polvo?"


#comienzo de la pagina 25 a 32

#"El nemedio agarra firmemente la cuerda, enganchando una rodilla en ella, y comienza a subir con agilidad, como un gato, a pesar de su corpulento cuerpo. El cimmerio lo sigue de cerca. Aunque la cuerda oscila y gira sobre sí misma, ambos hombres continúan escalando sin problemas."
#"Desde lo alto, pueden ver el borde de la torre, sobresaliendo ligeramente de la pared, lo que facilita el ascenso, con la cuerda colgando a unos cincuenta centímetros a los lados."
#"En silencio, siguen subiendo mientras las luces de la ciudad se hacen más pequeñas y el brillo de las estrellas se atenuaba frente al resplandor de las joyas que adornan el borde del edificio. Finalmente, Taurus extiende su mano, se agarra al borde y, con un rápido impulso, salta al otro lado."
#"Conan, por su parte, se detiene un momento en el borde, fascinado por las deslumbrantes y frías joyas que lo rodeaban. Diamantes, rubíes, esmeraldas, zafiros, turquesas y piedras de la luna brillan como estrellas incrustadas en un cielo de plata."
#"Desde la distancia, su fulgor se funde en un resplandor blanco, pero, de cerca, cada una de las piedras centellean con millones de matices, hipnotizando al joven con sus destellos."

#Conan "Aquí hay una fabulosa fortuna, Taurus."

#Taurus "¡Apresúrate! Si conseguimos el Corazón, esto y todo lo demás será nuestro."

#"Conan trepa por el resplandeciente borde de la torre. El techo está unos metros más abajo del saliente enjoyado. Es plano y de un material de color azul oscuro, combinado con oro, lo que le da la apariencia de un inmenso zafiro salpicado de polvo dorado."
#"Al otro lado del techo, se alza una especie de habitación hecha del mismo material que las paredes de la torre, adornada con pequeñas gemas. La única puerta visible es de oro macizo, con paneles tallados y piedras preciosas incrustadas que brillan con un resplandor helado."
#"Conan dirige su mirada hacia el vasto océano de luces a lo lejos, y luego observa a Taurus, quien está recogiendo la cuerda. El nemedio le muestra el lugar donde el gancho de acero se había asegurado, y vieron que la punta estaba apenas enganchada debajo de una brillante joya en el lado interior del borde."

#Taurus "Tuvimos suerte una vez más. Es de imaginar que el peso de ambos podría haber destrozado la piedra. Ahora sígueme, que los verdaderos peligros de nuestra aventura acaban de empezar. Estamos en la guarida de la serpiente, y no sabemos dónde está escondida."
#"Ante el aviso de su compañero, Taurus voltea para ver a Conan apuntando con su mano sobre sus cabezas."

#"Atraviesan a rastras la misteriosa y brillante terraza como tigres detrás de su presa y se detienen delante de la puerta de oro. "

#"Voy a entrar a comprobar que sea seguro. Será más sigiloso que entre solo. Tú quédate vigilando la retaguardia."

#menu CONFIAR_EN_Taurus:
 #   "Entrar con el":
  #      $ Conan_esta_solo =False
   #     jump entrar_con_Taurus
    #"Dejer entrar solo a Taurus":
     #   $ Conan_esta_solo =True
        #jump entra_solo_Taurus

#label entrar_con_Taurus:

#Conan "No. Es mejor que entremos juntos. Si es una trampa, necesitarás ayuda."

#Taurus "De acuerdo. Quédate cerca."

#"A la par, los ladrones abren la puerta y se adentran en una habitación oscura, tenebrosa y aparentemente olvidada. Telarañas cuelgan por todas partes y no hay objeto que no esté cubierto de polvo."


scene bg JardinesDeLaTorre with fade
show Taurus at left

Taurus "Están hechas con flores de loto negro, que crecen en las selvas remotas de Khitai, donde solo habitan los monjes de cráneo amarillo de Yun. Esas flores causan la muerte al que las huele."

"Conan se arrodilla al lado de los enormes animales muertos, asegurándose de que no podían hacerle daño. Mueve la cabeza pensando que la magia de las tierras exóticas es terrible y misteriosa a los ojos de los bárbaros del norte."

show Conan
Conan "¿Por qué no matamos a los soldados de la torre de la misma manera?"

show Taurus
Taurus "Porque ese es todo el polvo que tengo. Su obtención fue una hazaña que hubiera bastado para hacerme famoso entre todos los ladrones del mundo. Lo robé de una caravana que se dirigía a Estigia. ¡Pero, vamos ya, por Bel! ¿Vamos a pasarnos toda la noche hablando?"

scene bg BaseDeLaTorre with dissolve
"Taurus y Conan se arrastran silenciosamente hasta la base de la torre. Sin decir una palabra, Taurus desenrolla una cuerda con un gancho de acero en uno de sus extremos."

"¿En que lado de la torre tira Taurus el gancho?."

menu :
    "Lado derecho":
        jump derecho
    "Lado izquierdo":
        jump izquierdo

label derecho:
scene bg BaseDeLaTorre
show Conan
Conan "Lánzalo en el lado derecho, veo una saliente allí."

"Mientras que Taurus se prepara para lanzar la soga a la saliente. Conan, atento, apoya su oído en la pared de la torre, pero no oye nada, lo que indica que los guardias dentro no se han percatado de su presencia."
"Aun así, el bárbaro siente una inquietud inexplicable, tal vez por el fuerte olor de los leones que domina el aire."
"Con un movimiento firme, Taurus lanza la cuerda, y el gancho desaparece sobre el borde de la torre. Tras comprobar que está bien sujeto, tira de ella sin aflojarla."

show Taurus
Taurus "¡Buen ojo! Ahora..."

show ConanAlerta
"El instinto salvaje de Conan lo hace reaccionar de inmediato, ya que la muerte silenciosa acecha desde arriba. Con una sola mirada, el cimmerio percibe la gigantesca sombra de un león, listo para atacar."
scene ConanVsLeon
"Ningún hombre civilizado es tan rápido como el bárbaro. Su espada, brillando bajo las estrellas, se mueve con una fuerza desesperada, y en un instante, el hombre y la bestia ruedan juntos por el suelo."
scene TaurusViendoAlLeonEncimaDeConan
"Taurus, maldiciendo para sus adentros, se agacha y ve a Conan luchando por liberarse del enorme peso del león. Para su asombro, el animal yace muerto, con el cráneo partido. Con su ayuda, Conan aparta el cuerpo y se levanta, aún empuñando su espada ensangrentada."

scene bg LeonMuerto

show Taurus at right
Taurus "¿Estás herido, amigo?"

show Conan at left
Conan "¡Por Crom, no! Pero me libre por poco. ¿Por qué esa maldita bestia no ruge en el momento de atacar?"
jump continuacion

label izquierdo:
scene bg BaseDeLaTorre
show Conan
Conan "Lánzalo en el lado izquierdo, veo una saliente allí."

"Mientras que Taurus se prepara para lanzar la soga a la saliente. Conan, atento, apoya su oído en la pared de la torre, pero no oye nada, lo que indica que los guardias dentro no se han percatado de su presencia."
"Aun así, el bárbaro siente una inquietud inexplicable, tal vez por el fuerte olor de los leones que domina el aire."
"Con un movimiento firme, Taurus lanza la cuerda, y el gancho desaparece sobre el borde de la torre. Tras comprobar que está bien sujeto, tira de ella sin aflojarla."

show Taurus
Taurus "¡Buen ojo! Ahora debemos subir con cuidado"    

"El instinto salvaje de Conan lo hace reaccionar con mucha ansiedad y reacción rápido, ya que la muerte silenciosa acecha dentro de los jardines."
"Apurado, intenta subir rápido pero no logra ver al león que lo está acechando."
scene ConanVsLeon
$ Conan_esta_herido = True
"Intenta desenvainar su espada, pero el enorme felino es mucho más rápido, se mueve con una fuerza desesperada, y en un instante, el hombre y la bestia ruedan juntos por el suelo."
"Taurus, maldiciendo para sus adentros, se agacha y ve a  Conan luchando por liberarse del enorme peso del león. Para su asombro, el animal logra masticar el costado de la costilla izquierda de Conan."
"Luego el bárbaro logra sacar su espada y gracias a la adrenalina que surge dentro de su ser logra clavarle la espada en la parte de atrás del cuello del león y así provocar su muerte."
"Conan aparta el cuerpo y se levanta, aún empuñando su espada ensangrentada."

scene bg BaseDeLaTorre

show TaurusPreocupado
Taurus "Oh por dios!. No me esperaba ese enorme león en este lugar de la torre.¿Estas bien Conan?"

show ConanDolorido
Conan "Si, no te preocupes por mí. Sigamos a lo que vinimos, entremos a la torre. No hay tiempo que perder."
hide TaurusPreocupado
jump continuacion

label continuacion:
show Taurus at right
Taurus "Todo es extraño en este jardín. Los leones atacan en silencio, al igual que las otras muertes. Pero sigamos; aunque hemos hecho poco ruido en la pelea, los soldados pueden haber oído algo, a menos que estén dormidos o borrachos."
Taurus "Esa fiera está en alguna otra parte del jardín y escapa de la muerte de las flores, pero seguramente ya no hay más animales. Ahora debemos trepar por esta cuerda; imagino que no es necesario preguntar a un cimmerio si puede hacerlo."

show ConanDolorido at left
Conan "Si resiste mi peso."

Taurus "Puede aguantar tres veces mi propio peso. Está hecha con trenzas de mujeres muertas, que yo mismo cogí de sus tumbas a medianoche, y que luego sumergí en la mortífera savia del árbol de upas, para hacerlas resistentes."
Taurus "Yo subiré primero, y luego me seguirás tú de cerca."

scene bg ConanYTaurusEscalando

"El nemedio agarra firmemente la cuerda, enganchando una rodilla en ella, y comienza a subir con agilidad, como un gato, a pesar de su corpulento cuerpo. El cimmerio lo sigue de cerca. Aunque la cuerda oscila y gira sobre sí misma, ambos hombres continúan escalando sin problemas."
"Desde lo alto, pueden ver el borde de la torre, sobresaliendo ligeramente de la pared, lo que facilita el ascenso, con la cuerda colgando a unos cincuenta centímetros a los lados."

scene bg ciudadDeFondo
"En silencio, siguen subiendo mientras las luces de la ciudad se hacen más pequeñas y el brillo de las estrellas se atenuaba frente al resplandor de las joyas que adornan el borde del edificio."

scene bg bordeDeLaTorre
"Finalmente, Taurus extiende su mano, se agarra al borde y, con un rápido impulso, salta al otro lado. Conan, por su parte, se detiene un momento en el borde, fascinado por las deslumbrantes y frías joyas que lo rodean y que brillan como estrellas incrustadas en un cielo de plata."
"Desde la distancia, su fulgor se funde en un resplandor blanco, pero, de cerca, cada una de las piedras centellean con millones de matices, hipnotizando al joven con sus destellos."

show Conan at left
Conan "Aquí hay una fabulosa fortuna, Taurus."

show Taurus at right
"¡Apresúrate! Si conseguimos el Corazón, esto y todo lo demás será nuestro."

scene bg laTorreFondoCiudad
"Conan trepa por el resplandeciente borde de la torre. El techo está unos metros más abajo del saliente enjoyado. Es plano y de un material de color azul oscuro, combinado con oro, lo que le da la apariencia de un inmenso zafiro salpicado de polvo dorado."
"Al otro lado del techo, se alza una especie de habitación hecha del mismo material que las paredes de la torre, adornada con pequeñas gemas."
scene bg puertaDeOro
"La única puerta visible es de oro macizo, con paneles tallados y piedras preciosas incrustadas que brillan con un resplandor helado."    
scene bg laTorreFondoCiudad
"Conan dirige su mirada hacia el vasto océano de luces a lo lejos, y luego observa a Taurus, quien está recogiendo la cuerda."
"El nemedio le muestra el lugar donde el gancho de acero se había asegurado, y vieron que la punta estaba apenas enganchada debajo de una brillante joya en el lado interior del borde."

scene bg puertaDeOro
show Taurus at left
"Tuvimos suerte una vez más. Es de imaginar que el peso de ambos podría haber destrozado la piedra. Ahora sígueme, que los verdaderos peligros de nuestra aventura acaban de empezar. Estamos en la guarida de la serpiente, y no sabemos dónde está escondida."

scene bg dentroTerraza
"Atraviesan a rastras la misteriosa y brillante terraza como tigres detrás de su presa y se detienen delante de la puerta de oro. "

scene bg puertaDeOro
show Taurus at right
"Voy a entrar a comprobar que sea seguro. Será más sigiloso que entre solo. Tú quédate vigilando la retaguardia."

hide Taurus
"Conan piensa por dentro"
show Conan
"¿Debo dejar que cruce solo esa puerta?"

menu CONFIAR_EN_Taurus:
    "Entrar con el":
        jump entrar_con_Taurus
    "Dejer entrar a Taurus solo":
        $ Conan_esta_solo = True
        jump entra_solo_Taurus

label entrar_con_Taurus:
show Conan at left
"No. Es mejor que entremos juntos. Si es una trampa, necesitarás ayuda"
show Taurus at right
"De acuerdo. Quédate cerca."

scene puertaDeOro
"A la par, los ladrones abren la puerta y se adentran en una habitación oscura, tenebrosa y aparentemente olvidada. Telarañas cuelgan por todas partes y no hay objeto que no esté cubierto de polvo."

show Conan
"Taurus, cuidado!"

Taurus "Aaagh! Diablos! ¿Qué es esta cosa?"

"Una pegajosa sustancia cubre a Taurus. Pegándolo al suelo e inmovilizándolo."

Conan "Por Crom! ¿De dónde vino eso?"

"Nuevamente, el instinto bárbaro de Conan salva al cimmerio de un nuevo ataque. Una enorme araña intenta embestir desde atrás. Al fallar, la araña continúa hacia Taurus."

Conan "¡NOOO!"

"La araña toma a Taurus por el cuello con sus colmillos y le arrancó la cabeza de un tirón."

Conan "Maldita! ¡Las pagarás!"

"La araña carga hacia Conan nuevamente."

jump Conan_pelea_con_la_araña


#Taurus entra solo
label entra_solo_Taurus:

Conan "Está bien, fijate que hay dentro de ese cuarto."

Taurus "De acuerdo."

"El ladrón abre la puerta y se adentra en una habitación oscura, tenebrosa y aparentemente olvidada. Telarañas cuelgan por todas partes y no hay objeto que no estuviera cubierto de polvo."

Taurus "Diablos… parece que hasta aquí llegas, cimerio…"

"Taurus sale del cuarto"

Taurus "Es seguro, pasa."

"Sin pensarlo mucho, Conan se adentra en el cuarto solo para escuchar un fuerte portazo detrás de él."

Taurus "Debo reconocer que eres muy hábil, bárbaro! Pero te vendría bien un poco de viveza."

Conan "Maldito! ¡Déjame salir!"

Taurus "Lo siento, Conan. No puedo hacer eso si quiero quedarme con la gema. ¡Saluda a mi amiga!"

Conan "¡NO! Abre Taurus, cobarde. ¡Me las vas a pagar!"

"El cimmerio siente como algo cae lentamente del techo, y al darse vuelta ahí la ve. Una enorme araña que vigila la entrada al cuarto de la gema."

"¡Maldita sea! Tendremos que enfrentarnos, asqueroso insecto."

label Conan_pelea_con_la_araña:

menu cómo_atacar_a_la_araña:
    "Atacar de frente":
        jump De_frente
    "Lanzar la espada al candelabro":
        jump Lanzar_espada

label De_frente:
 
"Conan empuña su espada y ataca a la araña de frente."

Conan "¡AAAAH!"

"Justo antes de alcanzarla, el bárbaro se desliza por debajo de ella y la apuñala en el pecho. La araña se desploma y Conan se acerca para recuperar su espada."

if Conan_esta_solo == True :
    jump espera_Taurus #409
else:
    jump recamara_de_yag_kosha #109

label espera_Taurus:

"Se escucha un silencio atroz desde fuera del cuarto por lo que Taurus decide entrar."

Taurus "Espero que esa estúpida araña haya hecho su trabajo."

"Al abrir las puertas ve el cuerpo de la araña en una posición postmortem y ni bien entra siente unos pasos acercándose cada vez más rápido hacia él."

Conan "¡Te dije que me las ibas a pagar, ladrón malnacido!"

"Sin ningún tipo de tapujo Conan corre hacia Taurus y le corta el cuello de una manera limpia dejando que se muera ahogado en su sangre."

jump recamara_de_yag_kosha

label Lanzar_espada:

"Conan esquiva a la araña con mucha agilidad. En sus movimientos, nota que en el medio del cuarto hay un candelabro gigante y se le viene un plan a la cabeza."

Conan "Asquerosa araña, ven ¡Atácame!"

"La araña se va encima del bárbaro sedienta de sangre y con violencia. Cuando está por llegar, el cimmerio anticipa su ataque y tira su espada a la base del candelabro haciendo que se rompa y caiga."
"Para su infortunio, la araña esquiva el enorme candelabro y aprovecha el asombro de Conan para atacar su cuello y romperlo."

if Conan_esta_solo == True :
    jump espera_Taurus_Conan_M #409
else:
    jump Muerte #109

label espera_Taurus_Conan_M:

"Se escucha un silencio atroz desde fuera del cuarto por lo que Taurus decide entrar."

Taurus "Espero que esa estúpida araña haya hecho su trabajo."

"Taurus abre las puertas y ve el cuerpo de Conan tirado en el medio del cuarto. Confiado se fue acercando de a poco hasta percatarse de que tiene el cuello roto, asustado se da media vuelta para salir corriendo de la habitación pero ya era demasiado tarde"
"la araña lo captura con su tela lo deja colgado en el cuarto y aprovecha para devorarlo poco a poco comenzando con su cabeza."

label Muerte:

"Finalmente, los cadáveres de los audaces ladrones que se atrevieron a adentrarse en la famosa torre yacen fríamente en ella. Asesinados por la bestia protectora del secreto de la torre."
jump fin_de_la_partida

label recamara_de_yag_kosha:
scene int recamara de Yag Kosha

"Conan entra sigilosamente en una habitación lujosa y exótica, llena de jade y marfil, con un ídolo extraño y aterrador en el centro. El ídolo tiene un cuerpo humanoide verde y una cabeza de pesadilla con colmillos de elefante."

yagKosha "¿Quién anda ahí? ¿Has venido a torturarme de nuevo, Yara? ¿No te vas a cansar nunca?"

"Las lágrimas ruedan por sus mejillas, Conan observa las extremidades torturadas de Yag Kosha y siente una profunda compasión por su sufrimiento."

Conan "No soy Yara. Soy solamente un ladrón. No te haré daño."

yagKosha "Tú no perteneces a la raza maligna de Yara. Llevas la marca de la fiereza pura y esbelta de las tierras desérticas. Conozco a tu gente desde antiguo."
 
yagKosha "Los conozco con otro nombre hace mucho, mucho tiempo, cuando un mundo distinto alzaba sus brillantes torres hacia las estrellas. Pero... hay sangre en tus manos."

Conan "Es de la araña que había en la habitación de arriba y de uno de los leones del jardín."

yagKosha "¡Así es! Muerte en todas partes; lo sé; lo siento. Y la siguiente producirá un efecto mágico que ni el mismo Yara imagina. ¡Oh, hechizo de la liberación, dioses verdes de Yag!"

"Las lágrimas corren por las mejillas de la criatura mientras se estremece bajo intensas emociones. Conan lo observa perplejo hasta que el ser cesa de temblar y sus ojos ciegos se vuelven hacia él, haciéndole una seña."

yagKosha "Escúchame, hombre. Sé que te parezco repugnante y monstruoso, pero tú me parecerías igual de extraño. No soy ni un dios ni un demonio; soy de carne y hueso, aunque diferente. Vengo de Yag, un planeta verde en los confines del universo. Fuimos exiliados de nuestro mundo tras una derrota."

yagKosha "Aquí en la Tierra, nuestras alas se marchitaron. Hemos visto el ascenso y la caída de civilizaciones, desde Valusia hasta Atlantis y Lemuria. Ahora, yo soy el último de mi raza, esclavizado por Yara."

yagKosha "Al principio, Yara aprendía de mi magia blanca, pero él ansiaba poder oscuro. Me engañó para que revelara secretos prohibidos, y me esclavizó. He soportado trescientos años de tormento, obligado a realizar sus malvados deseos. Ahora presiento mi final. Tú eres la mano del destino. Coge la piedra en el altar."

"Conan vuelve hacia el altar de oro y marfil que le ha señalado el extraño ser y coge una enorme joya redonda, clara como un cristal carmesí, y en ese momento descubre que es el Corazón del Elefante."
"Tú no perteneces a la raza maligna de Yara. Llevas la marca de la fiereza pura y esbelta de las tierras desérticas. Conozco a tu gente desde antiguo. Los conozco con otro nombre hace mucho, mucho tiempo, cuando un mundo distinto alzaba sus brillantes torres hacia las estrellas. Pero... hay sangre en tus manos."

Conan "Es de la araña que había en la habitación de arriba y de uno de los leones del jardín."

yagKosha "¡Así es! Muerte en todas partes; lo sé; lo siento. Y la siguiente producirá un efecto mágico que ni el mismo Yara imagina. ¡Oh, hechizo de la liberación, dioses verdes de Yag!"

"Las lágrimas corren por las mejillas de la criatura mientras se estremece bajo intensas emociones. Conan lo observa perplejo hasta que el ser cesa de temblar y sus ojos ciegos se vuelven hacia él, haciéndole una seña."

yagKosha "Escúchame, hombre. Sé que te parezco repugnante y monstruoso, pero tú me parecerías igual de extraño. No soy ni un dios ni un demonio; soy de carne y hueso, aunque diferente. Vengo de Yag, un planeta verde en los confines del universo. Fuimos exiliados de nuestro mundo tras una derrota."
yagKosha "Aquí en la Tierra, nuestras alas se marchitaron. Hemos visto el ascenso y la caída de civilizaciones, desde Valusia hasta Atlantis y Lemuria. Ahora, yo soy el último de mi raza, esclavizado por Yara. Al principio, Yara aprendía de mi magia blanca, pero él ansiaba poder oscuro."
yagKosha "Me engañó para que revelara secretos prohibidos, y me esclavizó. He soportado trescientos años de tormento, obligado a realizar sus malvados deseos. Ahora presiento mi final. Tú eres la mano del destino. Coge la piedra en el altar."

yagKosha "Ahora viene la gran magia. Corta mi corazón y deja que la sangre fluya sobre la piedra. Luego baja a la habitación de Yara, pronuncia su nombre y entrégale la gema. Dile: '¡Atento, viajero del destino! Yag Kosha, el guardián de los arcanos olvidados, se digna a ofrecerte su último y más formidable conjuro.'"
yagKosha"Después, márchate. Mi muerte no es como la tuya; seré libre nuevamente."

"Conan se acerca con gesto vacilante, y Yag Kosha le indica dónde debía clavar la hoja. Conan aprieta los dientes y hunde profundamente la espada. La sangre fluye, empapando la hoja y su mano, y la criatura se agita antes de quedar inmóvil."
"Conan, asegurándose de que ya no estaba vivo, extrae lo que parece ser el corazón de Yag Kosha, aunque es distinto a cualquier corazón que hubiera visto. Aprieta la víscera sobre la joya, y sorprendentemente, la sangre fue absorbida por la gema. Con cuidado, Conan sale del recinto y baja por la escalera de plata."
"Siente que el cuerpo de Yag Kosha está sufriendo una transmutación detrás de él, algo que no debe presenciar. Al llegar a la puerta de ébano con la calavera de plata, la abre y ve a Yara, el brujo, en su lecho de seda negra, bajo los efectos del loto amarillo."

Conan "¡Yara! ¡Despierta!"

"Los ojos se abren al instante y se vuelven fríos y crueles como los de un buitre. La negra figura vestida de seda se yergue lúgubre sobre el cimmerio."

Yara "¡Perro! ¿Qué haces aquí?"

"Conan deposita la joya sobre la enorme mesa de ébano."

Conan "El que envía esta gema me mandó decir:"

menu :
    "¡Atento, viajero del destino! Yag Kosha, el guardián de los arcanos olvidados, se digna a ofrecerte su último y más formidable conjuro.":
        jump Conan_recita_bien_el_hechizo
    "¡Atento, viajero del destino! Yag Kosha, el guardián de los arcanos perdidos, se digna a ofrecerte su último y más fuerte hechizo.":
        jump Conan_recita_mal_el_hechizo


label Conan_recita_mal_el_hechizo:

Yara "JAJAJA!Eso es todo lo que tienes? Un conjuro que ni siquiera funciona?" 

"Conan, confundido por lo sucedido, decide huir. Pues a pesar de su fuerza, Yara es claramente más poderoso."

Yara "¿A dónde crees que vas?"

"Con un chasquido, Conan se congela en el lugar."

Yara "Crees que puedes cometer tal intrusión y te dejara escapar como si nada hubiera pasado?"

"Conan, incapaz de emitir una palabra, por primera vez, teme por su vida. Entiende que se enfrenta a un poder que no era de su mundo y que su valentía y barbaridad no eran competencia ante tal poder."

Yara "Que pena… siempre creí que quien logre irrumpir en mi torre sería al menos un buen combatiente."

"Con otro chasquido de la mano de Yara, Conan desaparece como si se tratara de la luz al anochecer."

jump fin_de_la_partida


label Conan_recita_bien_el_hechizo:

"Yara retrocede con el rostro pálido mientras la joya, antes cristalina, emite humo de colores cambiantes. Hipnotizado, Yara toma la gema y comienza a encogerse ante los ojos de Conan, primero pareciendo un gigante, luego un niño y finalmente un ser diminuto que corre sobre la mesa aferrando la joya."
"Yara intenta escapar, pero sigue encogiéndose hasta que la joya parece una montaña a su lado, siendo finalmente atraído hacia ella."

Yara "En nombre de Yikk, te maldigo! ¿Cómo te atreves?"

"Conan ve en el centro de la gema a una figura alada con cuerpo de hombre y cabeza de elefante, el vengador de Yag Kosha, que persigue a Yara. La joya explota en un destello iridiscente y desaparece, dejando la mesa de ébano y el lecho de mármol vacíos."

menu : 
    "Escapar por la escalera":
        jump escapa_por_escaleras
    "Escapar por donde se entró":
        jump escapa_por_soga


label escapa_por_escaleras:

"Conan huye, bajando una escalera de plata. Al llegar a una sala con soldados caídos, se da cuenta de que su camino está despejado."

jump Conan_llega_a_PB

label escapa_por_soga:

"Conan atraviesa el mismo camino por el que entró. Cuando llega al cuarto donde combatió a la araña ve el cuerpo frío de Taurus."

if Conan_esta_solo == True:
    Conan "Te irás al infierno maldito. Esta torre te sepultará, será tu propia tumba"
else:
    Conan "Lo lamento, compañero. Mi misión a cambiado y no he podido completar tu plan."

"Conan llega al balcón."

menu :
    "Revisar la soga":
        jump Conan_revisa_la_soga
    "Descender sin revisar la soga":
        jump Conan_no_revisa_la_soga


label Conan_revisa_la_soga:

Conan "Que raro, la soga está floja, la ajuste lo suficiente para poder bajar sin ningún problema de esta torre."

"La soga, firme y bien anudada, soporta su peso sin ceder ni un ápice. Los músculos de Conan se tensan con cada movimiento, pero sus manos expertas se deslizan con precisión sobre la cuerda, controlando el ritmo de su descenso."
"Siente el tirón familiar en los brazos, pero no es nada a lo que su cuerpo curtido no esté acostumbrado. Sus pies tocan la pared del edificio ocasionalmente, pero no pierde el control."
"El guerrero desciende como una sombra, ágil y silencioso, su mirada clavada en el suelo que se aproxima rápidamente. Con un último impulso, Conan aterriza en el empedrado del callejón, flexionando sus rodillas para amortiguar el impacto. No hay pausa en sus movimientos; inmediatamente se pone en pie y suelta la soga sin mirar atrás."

Conan "Suerte que he revisado y ajustado la soga porque si no estaría compartiendo el mismo destino que mi compañero."

jump Conan_llega_a_PB


label Conan_no_revisa_la_soga:

Conan "Tengo que irme rápido sin perder mucho tiempo en revisar si la soga está bien ajustada o no."

"Conan huye, descendiendo rápidamente por la soga que habían tirado Taurus hacia el balcón cuando tenían que subir. Pero a mitad del descenso, algo cambia. La soga, tensa en un principio, comienza a ceder hasta el punto de que se suelta de donde estaba agarrada, por lo que Conan empieza a caer hasta el suelo"
" Por suerte no estaba tan alto, pero aun así quedó medio dolorido tras la caída."

$ Conan_esta_herido = True
Conan "AAAAH!!! Maldita sea qué suerte tengo, por poco casi me mato, tenía que haber revisado la soga antes, pero aun así sigo vivo pero un poco dolorido."


label Conan_llega_a_PB:
"Sale por una puerta de plata hacia los jardines, donde la brisa del alba lo estremece."

if Conan_esta_herido == True:
    jump Conan_no_logra_escapar
else:
    jump Conan_logra_escapar


label Conan_no_logra_escapar:

"Conan estando herido, le está costando escapar de la torre del elefante, La torre empieza a temblar y Conan intenta apresurarse."

Conan "Maldita sea, tengo que ser rápido sino no llegaré a escapar de esta torre del infierno. AAAAH!!!"

"La torre comienza a derrumbarse con Conan dentro."

if Conan_mata_a_Drakos:
    jump Conan_muere_aplastado
else:
    jump Drakos_salva_a_Conan


label Conan_muere_aplastado:

"Conan, herido y exhausto, apenas logra mantenerse en pie mientras la torre del elefante se tambalea violentamente, sus paredes desmoronándose alrededor de él."

Conan "Maldita sea... tengo que salir de aquí... o este será mi final. ¡AAAH!"

"La torre se derrumba por completo, y Conan, atrapado bajo los escombros, no puede escapar. La enorme estructura cae sobre él, aplastando bajo su peso. En sus últimos momentos, sus pensamientos se desvanecen entre la oscuridad y el eco de la destrucción."
"El polvo se asienta lentamente, y el imponente guerrero conocido como Conan encuentra su fin bajo las ruinas de la torre del elefante, su destino sellado en las profundidades de la noche."

jump fin_de_la_partida


label Drakos_salva_a_Conan:

"Pareciendo que Conan muere definitivamente hasta que aparece Drakos en el momento justo para salvarlo y no morir aplastado por la torre."

Drakos "Maldición Conan, suerte que he llegado en el momento justo para poder rescatarte. No he olvidado nuestra conversación al venir aquí hace unas cuantas horas y también por no haberme matado en el bar, y por eso vengo a ayudarte."

Conan "Muchas gracias… Drakos por haberme salvado, te debo una enorme. Ahora vayámonos de aquí rápidamente antes de que venga una multitud a ver qué pasa."

"A medida que se iban, tanto Conan como Drakos observaron como la torre se empieza a convertir en una inmensa nube de minúsculas partículas resplandecientes en que ambos se miran muy confundidos y al mismo tiempo muy asombrados por lo que acababa de pasar."

jump fin_de_la_partida

label Conan_logra_escapar:

"Conan atraviesa la puerta principal y corre por su vida. El impecable estado físico del bárbaro le permite alejarse lo suficiente para voltear y ver nuevamente la impresionante torre."

Conan "Qué acaba de suceder…? Acaso me han embrujado?"

"Entre sus dudas, logra observar cómo la estructura comienza a desmoronarse para eventualmente convertirse en una inmensa nube de minúsculas partículas resplandecientes."

label fin_de_la_partida: