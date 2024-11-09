# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define conan = Character("CONAN", color = "#e9c33c")
define drakos = Character("DRAKOS", color = "#0a0a0a")
define taurus = Character("TAURUS", color = "#643523")
define ladrón = Character("LADRÓN", color = "#0a0a0a")
define yagKosha = Character("YAG KOSHA", color = "#91ef91")
define yara = Character("YARA", color = "#981723")


# El juego comienza aquí.

label start:

scene interior_del_bar
"En la mesa mas poblada un grupo de delincuentes están atentos a los relatos de un hombre obeso y grosero proveniente de koth"

drakos "Por Bel, dios de los ladrones, que voy a enseñarles como se roba una mujer; estara del otro lado de la frontera de Zamora antes del amanecer, y allí habrá una caravana esperándola."
drakos "Un conde de Ofir me prometió trecientas piezas de plata por una joven brithunia de buena familia. Estuve vagando varias semanas por las ciudades fronterizas, donde me hacía pasar por mendigo, hasta que encontré una que valiera la pena."
drakos "¡Ah, qué guapa es esta golfa! Conozco señores de Shem que darían por ella el secreto de la Torre del Elefante."

"Mientras Drakos vuelve a su cerveza, siente cómo alguien tira de la manga de su túnica y se da vuelta con el entrecejo fruncido para ver a un hmbre alto y corpulento"

conan "Has mencionado la Torre del Elefante. He escuchado muchas cosas acerca de esa torre.¿Cuál es su secreto?"

drakos "Y ¿De dónde salus tu? extraño, no pareces de por aquí."

ladrón "No nos gustan los forasteros."

conan"Soy Cimerio…"

drakos "No me sorprende, los cimerios son vulgares. Pero hasta el más tonto de su tipo conocen la leyenda de la torre."

"A pesar de que el muchacho no tiene una actitud amenazante, DRAKOS, bajo los efectos del alcohol y la aprobación de su gente, se llena de valor y lo confronta."

drakos "¿El secreto de la Torre del Elefante? Bueno, cualquier imbécil sabe que el sacerdote Yara vive allí con la enorme joya llamada Corazón de Elefante; ese es el secreto de su magia."
    
conan "Yo he visto esa torre. Está en un enorme jardín situado en lo alto de la ciudad y rodeado de elevadas murallas. No he visto guardias. Las murallas parecían fáciles de escalar. ¿Por qué nadie ha robado esa misteriosa piedra preciosa?"

drakos "¡Escuchen a este pagano salvaje!¡Pretende robar la joya de Yara!"

drakos "Entonces presta atención y aprende, muchacho. Debes saber que en Zamora, y especialmente en esta ciudad, hay más intrépidos ladrones que en cualquier otro lugar del mundo, incluido Koth."
drakos "Si algún mortal hubiera sido capaz de robar la piedra preciosa, puedes estar seguro de que habría desaparecido hace mucho tiempo. Tú hablas de escalar las murallas, pero una vez que lo hubieras hecho, desearías irte inmediatamente."
drakos "Por la noche no hay guardias, es decir, guardias humanos, en los jardines por una buena razón."
drakos "Pero en el cuarto de guardia, en la parte inferior de la torre, hay hombres armados, y aun si lograras escabullirte entre los que rondan por los jardines de noche, tendrías que eludir a los soldados, porque la gema está guardada en algún lugar de la parte superior de la torre."

conan "Pero si alguien consiguiera atravesar los jardines, ¿por qué no iba a poder llegar hasta la gema por la parte superior de la torre, eludiendo de ese modo a los soldados?"

drakos "¡Oíd lo que está diciendo! ¡Este bárbaro debe de ser un águila capaz de volar hasta el borde enjoyado de la torre, que se halla a tan solo cincuenta metros de altura, y que tiene las paredes más lisas y resbaladizas que el cristal pulido!"

"Conan, molesto por las carcajadas burlonas de los oyentes y confundido por la falta de cortesía de los locales. Piensa en salir corriendo del lugar pero DRAKOS continúa con su mofa."

drakos "¡Anda, anda! ¡Cuéntales a estos pobres hombres, que han sido ladrones desde antes que a ti te engendraran, diles cómo robarías tú la piedra!"

conan "Siempre hay alguna manera de hacerlo, si el deseo está unido al valor."

drakos "¡Cómo! ¿Te atreves a enseñarnos nuestro oficio, y a insinuar que somos unos cobardes? ¡Vete! ¡Fuera de mi vista!"

"Drakos le da un leve empujón para intimidar a Conan. "

menu Matar_a_Drakos:
    "Sí":
        $ matar_drakos = True
        jump matar_a_drakos
    "No":
        $ matar_drakos = False
        jump perdonar_a_drakos
    

label matar_a_drakos:
scene matar_drakos_escena
conan "¿Te atreves a pedirme piedad luego de haberme faltado el respeto?"

"Con un solo movimiento, Conan separa la cabeza del cuerpo de DRAKOS."

scene exterior_calle_Arenjun__Zamora_Noche

"La taberna queda atrás mientras Conan avanza sigilosamente por las calles desiertas, dirigiéndose hacia la Torre del Elefante."
"Con su cuerpo marcado por cicatrices de múltiples batallas, moviéndose con la destreza de un cazador, aunque los callejones de Zamora le eran desconocidos."
"A su alrededor, los templos brillan bajo las estrellas, pero las deidades locales no le impresionan. Conan cree en una verdad simple: los dioses, como Crom, son indiferentes y terribles."
"Frente a él, la Torre del Elefante se alza imponente y misteriosa, rodeada de un jardín exótico protegido por altas murallas."
"Aunque las leyendas sobre los peligros de la torre y Yara, su guardián oscuro, le rondan la mente, Conan no teme. Da un gran salto y alcanza la cima de la muralla. Ve unos arbustos y se lanza hacia ellos"

jump conan_llega_a_la_torre

label perdonar_a_drakos:
scene perdonar_drakos_escena

scene interior_bar

conan "De acuerdo, te voy a dar la oportunidad de redimir tu insolencia acompañándome hacia la torre. Levántate."

"Conan envaina su espada y extiende su mano. DRAKOS la toma, se para y se sacude el polvo mientras mira a Conan con una expresión de asombro y terror. Después de levantar a Drakos se dirigen hacia las calles de Zamora."

scene exterior_calle_arenjún_Zamora_noche

drakos "Mi nombre es Drakos, por cierto. Aunque dudo que te importe."

conan "¿Por qué?"

drakos "¿Qué no eres cimmerio? Tu cultura se reduce a violencia y destrucción. Seguro ni siquiera tienes un nombre propio."

conan "Ja. Claro que tengo un nombre, Conan. Y tus creencias sobre mi cultura no son más que patrañas. Somos fuertes, poderosos y nos cuesta relacionarnos con sus costumbres civilizadas pero te aseguro que uno de nosotros porta más honor que todo un pueblo de ustedes."

drakos "Claro, y por eso estamos yendo a la torre, ¿verdad? No porque quieras robarte una gema."

conan "La gema es lo de menos, imbécil. El verdadero valor está en demostrar mi poder."

"Mientras terminan de discutir sobre sus valores se ve la torre a lo lejos."

drakos "Como digas… hasta aquí llego yo. Ya cumplí mi deuda?"

conan "Así es. Gracias por la compañía."

"Drakos observa cómo Conan se sumerge en aquella torre de tantos mitos mientras se pregunta si es una simple ilusión o lleva algo de verdad en sus palabras."
"A su vez, Conan salta el muro que resguarda la torre. Una vez dentro, ve unos arbustos y se oculta entre ellos"

label conan_llega_a_la_torre:
scene exterior_jardinesDeLaTorre

"En la distancia, Conan ve movimiento detrás de otros arbustos y decide correr hacia ellos empuñando su espada, listo para eliminar cualquier amenaza."
"Al llegar, descubre un cuerpo estrangulado, lo que indica la presencia de alguien. Sigiloso, acechando en la oscuridad hasta que se encuentra con una figura misteriosa, que rompe el silencio con un susurro, anticipando lo que está por suceder."

taurus "Tú no eres soldado. Eres un ladrón, igual que yo."

conan "¿Y tú quién eres?"

taurus "Soy Taurus de Nemedia."

"Ante ese nombre, Conan relaja ligeramente su agarre en la espada."

conan "He oído hablar de ti. Todos te llaman el príncipe de los ladrones."

"Una risa suave se escapa de los labios de Taurus. Es tan alto como Conan, pero más corpulento. A pesar de su voluminoso vientre, hay algo magnético y ágil en sus movimientos, una fluidez sutil que delata a un hombre peligroso."
"Sus ojos, brillantes incluso bajo la luz de las estrellas, denotan inteligencia y astucia. Lleva enrollada a su cintura una cuerda fina y fuerte, con nudos distribuidos a intervalos regulares."

taurus "¿Y tú quién eres?" 

conan "Soy Conan, el cimmerio. He venido a ver si puedo robar la gema de Yara, la que llaman el Corazón de Elefante"

"Taurus, divertido, ríe en silencio, y aunque Conan puede notar que no era una risa despectiva, le resulta un tanto inesperada."

taurus "¡Por Bel, dios de los ladrones! Pensaba que era el único con el valor suficiente para intentar este robo. Esos zamorios se creen grandes ladrones, pero tú, Conan... me gusta tu osadía. Nunca he compartido una aventura con nadie, pero por Bel, vamos a intentar esto juntos, si estás de acuerdo."

"Conan observó al hombre con ojos penetrantes antes de hablar." 

conan "Entonces, ¿tú también buscas la gema?"

taurus "¿Qué más podría estar buscando? He estado planeando este golpe durante meses. Tú, en cambio, parece que has venido aquí por pura impulsividad, amigo."

conan "¿Tú mataste al soldado?"

taurus "Por supuesto. Me arrastré por la muralla cuando él estaba en el extremo opuesto del jardín. Al esconderme entre los matorrales, me escuchó o creyó haber oído algo."
taurus"Fue su error. Cuando se acercó, fue fácil ponerme detrás de él y estrangularlo antes de que pudiera emitir un sonido. Como la mayoría de los hombres, era medio ciego en la oscuridad."

"Conan frunció el ceño, y tras una breve pausa, añade:"

conan "Pero cometiste un error."

"Los ojos de Taurus, llenos de orgullo, se encendieron de cólera ante esa afirmación."

taurus "¿Un error? ¡Imposible!"

conan "Deberías haber ocultado el cadáver entre los arbustos."

"Taurus lo mira con una mezcla de incredulidad y furia, pero el bárbaro continúa."

conan "No cambian la guardia hasta pasada la medianoche, lo sé, pero si alguien viene antes y encuentra el cuerpo, nos arriesgamos a que den la alarma."

"Taurus respiró hondo, calmándose, aunque no parecía gustarle la idea de recibir una lección del cimmerio."

taurus "El novato pretende enseñar su arte al maestro. Si alguien viene a buscarlo ahora y encuentra su cuerpo, irá a comunicarle inmediatamente la noticia a YARA, lo que nos daría tiempo para escapar. Pero si no lo hallaran, rastrearán los arbustos y nos atraparán como a ratas en una trampa."

conan "Tienes razón."

taurus "Así es. Ahora escucha. Estamos perdiendo tiempo con esta maldita discusión.No hay guardianes en el jardín interior, quiero decir guardias humanos, aunque hay centinelas que son mucho más peligrosos aún."
taurus "Es su presencia la que me ha detenido durante tanto tiempo, pero finalmente he descubierto una forma de burlarlos."

conan "¿Y qué me dices de los soldados que vigilan en la parte inferior de la torre?"

taurus "El  viejo YARA vive en las habitaciones superiores. Por ese camino vamos a entrar… y salir, espero. No me preguntes cómo. He planeado una forma de hacerlo."
taurus "Nos introduciremos furtivamente por la parte superior de la torre y estrangularemos al viejo YARA antes de que nos pueda hechizar con alguno de sus condenados maleficios."
taurus "Al menos lo intentaremos; corremos el riesgo de que nos convierta en arañas o en sapos asquerosos, pero por otro lado tenemos la posibilidad de obtener toda la riqueza y el poder del mundo. Un buen ladrón debe saber correr riesgos."

conan "Iré hasta donde sea"

taurus "Entonces sígueme."

"Taurus termina de decir esto y vuelve, toma impulso, se aferra a la muralla y salta. La agilidad de aquel hombre es asombrosa, teniendo en cuenta su tamaño; parece casi deslizarse hacia el borde del muro. CONAN lo sigue y cuando están de bruces sobre el ancho paredón, hablan en voz baja."

conan "No veo ninguna luz"

"La parte inferior de la torre se parece mucho a la parte que se ve desde fuera del jardín: un cilindro perfecto y brillante, que no parece tener ninguna abertura."

taurus "Hay puertas y ventanas hábilmente construidas. Pero están cerradas. Los soldados respiran el aire que viene de arriba."

"El jardín es un vago conjunto de sombras cubiertas de pequeños árboles donde se balancean sombríamente en la oscuridad ligeros arbustos."
"El cauto espíritu de Conan siente el aura amenazadora que se cierne sobre aquel lugar. Percibe la mirada ardiente de unos ojos invisibles y siente un aroma sutil que le eriza instintivamente el pelo de la nuca como a los sabuesos cuando huelen la presencia de su antiguo enemigo."

taurus "Sígueme. Ven detrás de mí, si aprecias tu vida."

"Taurus extrae de su cinto lo que parece ser un tubo de cobre, el nemedio se deja caer nuevamente encima del césped interior. Conan lo sigue de cerca con la espada preparada, pero Taurus lo empuja hacia atrás, contra la pared, y se queda inmóvil."
"Está en una actitud de tensa expectación y su mirada, al igual que la de CONAN, se fija en las sombras de los arbustos que hay cerca de allí. La mata se mueve a pesar de que la brisa deja de soplar."
"En ese momento ven dos enormes ojos resplandecientes entre las ondulantes sombras y detrás de estos pueden ver otros destellos de fuego que centellean en la oscuridad."

conan "¡Leones!"

taurus "Sí, de día los encierran en unas cavernas subterráneas que hay debajo de la torre. Por eso no hay guardianes en este jardín."

conan "Yo veo cinco, pero quizá haya más en los matorrales. Nos atacarán de un momento a otro."

taurus "¡Silencio!"

"Se oyen ruidos sordos provenientes de las sombras y se ven avanzar los ojos resplandecientes. CONAN percibe las inmensas mandíbulas babeantes y las colas que azotan el aire en todas direcciones. La tensión es insoportable."
"El cimmerio empuña la espada, a la espera del inevitable ataque de los gigantescos cuerpos. Entonces, TAURUS lleva el extremo del tubo a los labios y sopla con fuerza."
"Un gran chorro de polvo dorado sale por el otro extremo y se extiende instantáneamente formando una densa nube de color verde amarillento que cubre los arbustos, ocultando los resplandecientes ojos. Taurus corre apresuradamente hacia el muro. Conan lo mira sin comprender. La densa nube oculta los matorrales y no se oye nada."

conan "¿Qué es ese polvo?"

taurus "¡Es la muerte! Si se levanta viento y sopla en nuestra dirección, tendremos que huir saltando la muralla. Pero no, no se ha levantado viento y la nube se está disipando. Espera hasta que desaparezca del todo. Respirar ese polvo supone la muerte."

"Finalmente quedan flotando solo unas tenues nubecillas amarillentas en el aire; cuando desaparecen, Taurus indica a su compañero con la mano que avance. Se dirigen sigilosamente hacia los arbustos y Conan se queda boquiabierto."
"Tendidos en el suelo entre las sombras yacen cinco cuerpos de color pardo cuya mirada feroz se ha extinguido para siempre. Un olor dulzón y empalagoso persiste en el aire."

conan "¡Murieron sin lanzar un solo rugido! TAURUS, ¿qué era ese polvo?"