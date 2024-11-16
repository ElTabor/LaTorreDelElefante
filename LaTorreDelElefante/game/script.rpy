#CHARACTERS
define conan = Character("CONAN", color = "#e9c33c")
define drakos = Character("DRAKOS", color = "#0a0a0a")
define taurus = Character("TAURUS", color = "#643523")
define ladrón = Character("LADRÓN", color = "#0a0a0a")
define yagKosha = Character("YAG KOSHA", color = "#91ef91")
define Yara = Character("YARA", color = "#981723")

#BACKGROUNDS
image cityAlley = "CityAlley.jpg"
image bar = "Bar.jpg"
image cityStreetDrakos = "CityStreet_Drakos.png"
image cityStreetAlone = "CityStreet_Alone.png"
image jardinesInternos = "Fondo.jpg"
image jardinesExternos = "Fondo.jpg"
image ConanVSLeon = "Fondo.jpg"
image TaurusViendoAlLeonEncimaDeConan = "Fondo.jpg"
image LeonMuerto = "Fondo.jpg"
image ConanYTaurusEscalando = "Fondo.jpg"
image ciudadDeFondo = "Fondo.jpg"
image baseDeLaTorre = "Fondo.jpg"
image cimaDeLaTorre = "Fondo.jpg"
image puertaDeOro = "puertaDeOro.png"
image cuartoArania = "CuartoArania.png"
image remacamaraYagKosha = "Fondo.jpg"
image recamaraYara = "Fondo.jpg"
image escaleras= "Fondo.jpg"
image torreDerrumbandoseLejos = "Fondo.jpg"

#CHARACTER SPRITES
image Drakos = "Drakos.png"
image Conan = "Conan.png"
image Ladron = "Ladron.png"
image Taurus = "Taurus.png"
image YagKosha = "YagKosha.png"
image Yara = "Yara.png"
image Corpse = "Corpse.png"
image Arania = "Arania.png"

#SFX
define pasos = "pasos.mp3"
define pasos_concreto = "pasos_concreto.mp3"
define pasos_muchos = "pasos_muchos.mp3"
define pasos_rapidos = "pasos_correr.mp3"
define swordCut = "espadacortando.mp3"
define swordCut2 = "Corte de Espada.mp3"
define swordDraw = "Desenvainar_Espada.mp3"
define windCut = "Wind_Cut.mp3"
define lionRoar = "lion_roar.mp3"
define spiderSound = "SonidodeArania.mp3"
define portazo = "Door_Slam.mp3"
define alertSound = "Sonido-Dealerta.mp3"
define choirSound = "ChoirSoundEffect.mp3"

#MUSICf
define cityAmbience = "audio/city_ambience.mp3"
define forestAmbience = "forest_ambience.mp3"
define tension = "audio/tension_theme.mp3"
define suspense = "suspense_theme.mp3"
define radakan = "radakan-dramaticevent.mp3"

#VARIABLES
default Conan_esta_solo = False
default Conan_esta_herido = False
default Conan_mata_a_Drakos = False


label start:

#COMIENZO NICO
scene cityAlley with fade

play music pasos fadeout 1
"Conan se encuentra caminando en un cajellon de la ciudad dirigiendose hacia lo que seria un bar lleno de personas"

scene bar with fade
stop music fadeout 1

"En la mesa mas poblada, un grupo de delincuentes están atentos a los relatos de un hombre obeso y grosero proveniente de Koth."

show Drakos at center
drakos "Por Bel, dios de los ladrones, que voy a enseñarles cómo se roba una mujer. Estará del otro lado de la frontera de Zamora antes del amanecer, donde habrá una caravana esperándola."
drakos "Un conde de Ofir me prometió trecientas piezas de plata por una joven brithunia de buena familia. Estuve vagando varias semanas por las ciudades fronterizas, donde me hacía pasar por mendigo, hasta que encontré una que valiera la pena."
drakos "¡Ah, qué guapa es esta golfa! Conozco señores de Shem que darían por ella el secreto de la Torre del Elefante."

hide Drakos
"Mientras Drakos vuelve a su cerveza, siente cómo alguien tira de la manga de su túnica."
"Se da vuelta con el entrecejo fruncido y ve a un hombre alto y corpulento"

show Conan at right
conan "Has mencionado la Torre del Elefante. He escuchado muchas cosas acerca de esa torre. ¿Cuál es su secreto?"

show Drakos at left
drakos "¿Y de dónde salus tu, extraño? No pareces de por aquí."

hide Conan
hide Drakos

show Ladron at center
ladrón "No nos gustan los forasteros."

hide Ladron
show Conan at left

conan "Soy Cimerio…"
show Drakos at right
drakos "No me sorprende. Los cimerios son vulgares pero hasta el más tonto de su tipo conocen la leyenda de la torre."

hide Conan
hide Drakos
"A pesar de que el muchacho no tiene una actitud amenazante, Drakos, bajo los efectos del alcohol y la aprobación de su gente, se llena de valor y lo confronta."

show Drakos at right
drakos "¿El secreto de la Torre del Elefante? Bueno, cualquier imbécil sabe que el sacerdote Yara vive allí con la enorme joya llamada Corazón de Elefante; ese es el secreto de su magia."

show Conan at left
conan "Yo he visto esa torre. Está en un enorme jardín situado en lo alto de la ciudad y rodeado de elevadas murallas. No he visto guardias. Las murallas parecían fáciles de escalar. ¿Por qué nadie ha robado esa misteriosa piedra preciosa?"
hide Conan
drakos "¡Escuchen a este pagano salvaje!"
drakos "¡Pretende robar la joya de Yara!"
drakos "Entonces presta atención y aprende, muchacho. Debes saber que en Zamora, y especialmente en esta ciudad, hay más intrépidos ladrones que en cualquier otro lugar del mundo, incluido Koth."
drakos "Si algún mortal hubiera sido capaz de robar la piedra preciosa, puedes estar seguro de que habría desaparecido hace mucho tiempo. Tú hablas de escalar las murallas, pero una vez que lo hubieras hecho, desearías irte inmediatamente."
drakos "Por la noche no hay guardias, es decir, guardias humanos, en los jardines por una buena razón."
drakos "Pero en el cuarto de guardia, en la parte inferior de la torre, hay hombres armados, y aun si lograras escabullirte entre los que rondan por los jardines de noche, tendrías que eludir a los soldados, porque la gema está guardada en algún lugar de la parte superior de la torre."
show Conan
conan "Pero si alguien consiguiera atravesar los jardines, ¿por qué no iba a poder llegar hasta la gema por la parte superior de la torre, eludiendo de ese modo a los soldados?"

drakos "¡Oíd lo que está diciendo! ¡Este bárbaro debe de ser un águila capaz de volar hasta el borde enjoyado de la torre, que se halla a tan solo cincuenta metros de altura, y que tiene las paredes más lisas y resbaladizas que el cristal pulido!"

hide Conan
hide Drakos
"Conan, molesto por las carcajadas burlonas de los oyentes y confundido por la falta de cortesía de los locales, piensa en salir corriendo del lugar pero Drakos continúa con su mofa."

show Drakos at right
drakos "¡Anda, anda! ¡Cuéntales a estos pobres hombres, que han sido ladrones desde antes que a ti te engendraran, cómo robarías tú la piedra!"

show Conan at left

$ renpy.music.set_volume(0.2, channel='music')
play music tension fadeout 1
conan "Siempre hay alguna manera de hacerlo, si el deseo está unido al valor."

drakos "¡¿Cómo?! ¿Te atreves a enseñarnos nuestro oficio y a insinuar que somos unos cobardes? ¡Vete! ¡Fuera de mi vista!"

"Drakos le da un leve empujón para intimidar a Conan."

menu Matar_a_Drakos:
    "Sí":
        $ Conan_mata_a_Drakos = True
        jump matar_a_Drakos
    "No":
        jump perdonar_a_Drakos

label matar_a_Drakos:
scene bar with fade 
show Conan at center


conan "¿Te atreves a pedirme piedad luego de haberme faltado el respeto?"
stop music

play sound swordCut
"Con un solo movimiento, Conan separa la cabeza del cuerpo de Drakos."
stop music

hide conan

scene cityStreetAlone with fade
"La taberna queda atrás mientras Conan avanza sigilosamente por las calles desiertas, dirigiéndose hacia la Torre del Elefante."
"Con su cuerpo marcado por cicatrices de múltiples batallas, moviéndose con la destreza de un cazador aunque los callejones de Zamora le eran desconocidos."
"A su alrededor, los templos brillan bajo las estrellas, pero las deidades locales no le impresionan. Conan cree en una verdad simple: los dioses, como Crom, son indiferentes y terribles."
"Frente a él, la Torre del Elefante se alza imponente y misteriosa, rodeada de un jardín exótico protegido por altas murallas."
"Aunque las leyendas sobre los peligros de la torre y Yara, su guardián oscuro, le rondan la mente, Conan no teme. Da un gran salto y alcanza la cima de la muralla. Ve unos arbustos y se lanza hacia ellos"

jump Conan_llega_a_la_torre

label perdonar_a_Drakos:
scene bar with fade

show Conan at center
conan "De acuerdo, te voy a dar la oportunidad de redimir tu insolencia acompañándome hacia la torre. Levántate."
hide Conan
"Conan envaina su espada y extiende su mano. Drakos la toma, se para y se sacude el polvo mientras mira a Conan con una expresión de asombro y terror. Después de levantar a Drakos se dirigen hacia las calles de Zamora."

scene cityStreetDrakos with fade
play music cityAmbience fadeout 1

show Drakos at left

drakos "Mi nombre es Drakos, por cierto. Aunque dudo que te importe."

show Conan at right

conan "¿Por qué?"

drakos "¿Qué no eres cimmerio? Tu cultura se reduce a violencia y destrucción. Seguro ni siquiera tienes un nombre propio."

conan "Ja. Claro que tengo un nombre, Conan. Y tus creencias sobre mi cultura no son más que patrañas. Somos fuertes, poderosos y nos cuesta relacionarnos con sus costumbres civilizadas pero te aseguro que uno de nosotros porta más honor que todo un pueblo de ustedes."

drakos "Claro, y por eso estamos yendo a la torre, verdad? No porque quieras robarte una gema."

conan "La gema es lo de menos, imbécil. El verdadero valor está en demostrar mi poder."

"Mientras terminan de discutir sobre sus valores, la imponente torre se asoma en el horizonte."

drakos "Como digas… hasta aquí llego yo. ¿Ya cumplí mi deuda?"

conan "Así es. Gracias por la compañía."

hide Drakos
hide Conan
stop music
"Drakos observa cómo Conan se sumerge en aquella torre de tantos mitos mientras se pregunta si es una simple ilusión o lleva algo de verdad en sus palabras."
"A su vez, Conan salta el muro que resguarda la torre. Una vez dentro, ve unos arbustos y se oculta entre ellos"    
#FIN NICO
#COMIENZO TOMÁS

label Conan_llega_a_la_torre:
scene jardinesExternos with fade

show Conan at center

"En la distancia, Conan ve movimiento detrás de otros arbustos y decide correr hacia ellos empuñando su espada, listo para eliminar cualquier amenaza."

play music pasos_rapidos

hide Conan
show Corpse at center

"Al llegar, descubre un cuerpo estrangulado, lo que indica la presencia de alguien."
stop music

hide Corpse
show Taurus at right

"Sigiloso, acecha en la oscuridad hasta que se encuentra con una figura misteriosa que rompe el silencio con un susurro, anticipando lo que está por suceder."

show Conan at left

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

taurus "El novato pretende enseñar su arte al maestro. Si alguien viene a buscarlo ahora y encuentra su cuerpo, irá a comunicarle inmediatamente la noticia a Yara, lo que nos daría tiempo para escapar. Pero si no lo hallaran, rastrearán los arbustos y nos atraparán como a ratas en una trampa."

conan "Tienes razón."

taurus "Así es. Ahora escucha. Estamos perdiendo tiempo con esta maldita discusión.No hay guardianes en el jardín interior, quiero decir guardias humanos, aunque hay centinelas que son mucho más peligrosos aún."
taurus "Es su presencia la que me ha detenido durante tanto tiempo, pero finalmente he descubierto una forma de burlarlos."

conan "¿Y qué me dices de los soldados que vigilan en la parte inferior de la torre?"

taurus "El  viejo Yara vive en las habitaciones superiores. Por ese camino vamos a entrar… y salir, espero. No me preguntes cómo. He planeado una forma de hacerlo."
taurus "Nos introduciremos furtivamente por la parte superior de la torre y estrangularemos al viejo Yara antes de que nos pueda hechizar con alguno de sus condenados maleficios."
taurus "Al menos lo intentaremos; corremos el riesgo de que nos convierta en arañas o en sapos asquerosos, pero por otro lado tenemos la posibilidad de obtener toda la riqueza y el poder del mundo. Un buen ladrón debe saber correr riesgos."

conan "Iré hasta donde sea"

taurus "Entonces sígueme."

"Taurus termina de decir esto y vuelve, toma impulso, se aferra a la muralla y salta. La agilidad de aquel hombre es asombrosa, teniendo en cuenta su tamaño; parece casi deslizarse hacia el borde del muro. Conan lo sigue y cuando están de bruces sobre el ancho paredón, hablan en voz baja."

conan "No veo ninguna luz"

hide Conan
hide Taurus

scene jardinesInternos with fade

"La parte inferior de la torre se parece mucho a la parte que se ve desde fuera del jardín: un cilindro perfecto y brillante, que no parece tener ninguna abertura."

taurus "Hay puertas y ventanas hábilmente construidas. Pero están cerradas. Los soldados respiran el aire que viene de arriba."

"El jardín es un vago conjunto de sombras cubiertas de pequeños árboles donde se balancean sombríamente en la oscuridad ligeros arbustos."
"El cauto espíritu de Conan siente el aura amenazadora que se cierne sobre aquel lugar. Percibe la mirada ardiente de unos ojos invisibles y siente un aroma sutil que le eriza instintivamente el pelo de la nuca como a los sabuesos cuando huelen la presencia de su antiguo enemigo."

show Taurus:
    xalign 0.6
    yalign .75

taurus "Sígueme. Ven detrás de mí, si aprecias tu vida."

show conan behind Taurus:
    xalign .9
    yalign .75

"Taurus extrae de su cinto lo que parece ser un tubo de cobre, el nemedio se deja caer nuevamente encima del césped interior. Conan lo sigue de cerca con la espada preparada, pero Taurus lo empuja hacia atrás, contra la pared, y se queda inmóvil."
"Está en una actitud de tensa expectación y su mirada, al igual que la de Conan, se fija en las sombras de los arbustos que hay cerca de allí. La mata se mueve a pesar de que la brisa deja de soplar."
"En ese momento ven dos enormes ojos resplandecientes entre las ondulantes sombras y detrás de estos pueden ver otros destellos de fuego que centellean en la oscuridad."

show lions:
    xalign 0
    yalign .8

conan "¡Leones!"

taurus "Sí, de día los encierran en unas cavernas subterráneas que hay debajo de la torre. Por eso no hay guardianes en este jardín."

conan "Yo veo cinco, pero quizá haya más en los matorrales. Nos atacarán de un momento a otro."

taurus "¡Silencio!"

"Se oyen ruidos sordos provenientes de las sombras y se ven avanzar los ojos resplandecientes. Conan percibe las inmensas mandíbulas babeantes y las colas que azotan el aire en todas direcciones. La tensión es insoportable."
"El cimmerio empuña la espada, a la espera del inevitable ataque de los gigantescos cuerpos. Entonces, Taurus lleva el extremo del tubo a los labios y sopla con fuerza."
"Un gran chorro de polvo dorado sale por el otro extremo y se extiende instantáneamente formando una densa nube de color verde amarillento que cubre los arbustos, ocultando los resplandecientes ojos."
"Taurus corre apresuradamente hacia el muro. Conan lo mira sin comprender. La densa nube oculta los matorrales y no se oye nada."

conan "¿Qué es ese polvo?"

taurus "¡Es la muerte! Si se levanta viento y sopla en nuestra dirección, tendremos que huir saltando la muralla. Pero no, no se ha levantado viento y la nube se está disipando. Espera hasta que desaparezca del todo. Respirar ese polvo supone la muerte."

"Finalmente quedan flotando solo unas tenues nubecillas amarillentas en el aire; cuando desaparecen, Taurus indica a su compañero con la mano que avance. Se dirigen sigilosamente hacia los arbustos y Conan se queda boquiabierto."
"Tendidos en el suelo entre las sombras yacen cinco cuerpos de color pardo cuya mirada feroz se ha extinguido para siempre. Un olor dulzón y empalagoso persiste en el aire."

hide lions

conan "¡Murieron sin lanzar un solo rugido! ¿Taurus, qué era ese polvo?"

hide Taurus
hide Conan

#FIN TOMÁS
#COMIENZO FER

scene jardinesInternos with fade
play music forestAmbience fadein 2.0
show Taurus at left with moveinleft

taurus "Están hechas con flores de loto negro, que crecen en las selvas remotas de Khitai, donde solo habitan los monjes de cráneo amarillo de Yun. Esas flores causan la muerte al que las huele."

"Conan se arrodilla al lado de los enormes animales muertos, asegurándose de que no podían hacerle daño. Mueve la cabeza pensando que la magia de las tierras exóticas es terrible y misteriosa a los ojos de los bárbaros del norte."

show Conan at right with moveinright
conan "¿Por qué no matamos a los soldados de la torre de la misma manera?"

show Taurus with dissolve
taurus "Porque ese es todo el polvo que tengo. Su obtención fue una hazaña que hubiera bastado para hacerme famoso entre todos los ladrones del mundo. Lo robé de una caravana que se dirigía a Estigia. ¡Pero, vamos ya, por Bel! ¿Vamos a pasarnos toda la noche hablando?"

scene baseDeLaTorre with fade
stop music fadeout 1.0
play music suspense fadein 2.0
"Taurus y Conan se arrastran silenciosamente hasta la base de la torre. Sin decir una palabra, Taurus desenrolla una cuerda con un gancho de acero en uno de sus extremos."

"¿En que lado de la torre tira Taurus el gancho?"

menu:
    "Lado derecho":
        jump derecho
    "Lado izquierdo":
        jump izquierdo

label derecho:
scene baseDeLaTorre with dissolve
show Conan at leftish
conan "Lánzalo en el lado derecho, veo una saliente allí."

"Mientras que Taurus se prepara para lanzar la soga a la saliente. Conan, atento, apoya su oído en la pared de la torre pero no oye nada, lo que indica que los guardias dentro no se han percatado de su presencia."
"Aun así, el bárbaro siente una inquietud inexplicable. Tal vez por el fuerte olor de los leones que domina el aire."
play sound windCut
"Con un movimiento firme, Taurus lanza la cuerda, y el gancho desaparece sobre el borde de la torre. Tras comprobar que está bien sujeto, tira de ella sin aflojarla."


show Taurus at rightish with dissolve
taurus "¡Buen ojo! Ahora..."

show ConanAlerta with vpunch
play sound lionRoar
"El instinto salvaje de Conan lo hace reaccionar de inmediato, ya que la muerte silenciosa acecha desde arriba. Con una sola mirada, el cimmerio percibe la gigantesca sombra de un león, listo para atacar."
    
scene ConanVSLeon
"Ningún hombre civilizado es tan rápido como el bárbaro. Su espada, brillando bajo las estrellas, se mueve con una fuerza desesperada, y en un instante, el hombre y la bestia ruedan juntos por el suelo."
play sound swordCut2

scene TaurusViendoAlLeonEncimaDeConan
"Taurus, maldiciendo para sus adentros, se agacha y ve a Conan luchando por liberarse del enorme peso del león. Para su asombro, el animal yace muerto, con el cráneo partido. Con su ayuda, Conan aparta el cuerpo y se levanta, aún empuñando su espada ensangrentada."

scene LeonMuerto with fade
show Taurus at right with moveinleft
taurus "¿Estás herido, amigo?"

show Conan at left
conan "¡Por Crom, no! Pero me libre por poco. ¿Por qué esa maldita bestia no ruge en el momento de atacar?"
jump continuacion

label izquierdo:
scene baseDeLaTorre with dissolve
show Conan
conan "Lánzalo en el lado izquierdo, veo una saliente allí."

"Mientras que Taurus se prepara para lanzar la soga a la saliente. Conan, atento, apoya su oído en la pared de la torre, pero no oye nada, lo que indica que los guardias dentro no se han percatado de su presencia."
"Aun así, el bárbaro siente una inquietud inexplicable, tal vez por el fuerte olor de los leones que domina el aire."
play sound windCut
"Con un movimiento firme, Taurus lanza la cuerda, y el gancho desaparece sobre el borde de la torre. Tras comprobar que está bien sujeto, tira de ella sin aflojarla."

show Taurus
taurus "¡Buen ojo! Ahora debemos subir con cuidado"    

show ConanDolorido with vpunch
play sound lionRoar
"El instinto salvaje de Conan lo hace reaccionar con mucha ansiedad y reacción rápido, ya que la muerte silenciosa acecha dentro de los jardines."
    
scene ConanVsLeon
"Intenta desenvainar su espada, pero el enorme felino es mucho más rápido, se mueve con una fuerza desesperada, y en un instante, el hombre y la bestia ruedan juntos por el suelo."
    
scene baseDeLaTorre with dissolve
show TaurusPreocupado
taurus "Oh por dios!. No me esperaba ese enorme león en este lugar de la torre. ¿Estas bien Conan?"

show ConanDolorido
conan "Si, no te preocupes por mí. Sigamos a lo que vinimos, entremos a la torre. No hay tiempo que perder."
hide TaurusPreocupado
jump continuacion

label continuacion:
show Taurus at right
taurus "Todo es extraño en este jardín. Los leones atacan en silencio, al igual que las otras muertes. Pero sigamos; aunque hemos hecho poco ruido en la pelea, los soldados pueden haber oído algo, a menos que estén dormidos o borrachos."
taurus "Esa fiera está en alguna otra parte del jardín y escapa de la muerte de las flores, pero seguramente ya no hay más animales. Ahora debemos trepar por esta cuerda; imagino que no es necesario preguntar a un cimmerio si puede hacerlo."
    
show Conan at left with dissolve
conan "Si resiste mi peso..."

taurus "Puede aguantar tres veces mi propio peso. Está hecha con trenzas de mujeres muertas, que yo mismo cogí de sus tumbas a medianoche, y que luego sumergí en la mortífera savia del árbol de upas, para hacerlas resistentes."
taurus "Yo subiré primero, y luego me seguirás tú de cerca."

scene ConanYTaurusEscalando with fade
"El nemedio agarra firmemente la cuerda, enganchando una rodilla en ella, y comienza a subir con agilidad, como un gato, a pesar de su corpulento cuerpo. El cimmerio lo sigue de cerca. Aunque la cuerda oscila y gira sobre sí misma, ambos hombres continúan escalando sin problemas."
"Desde lo alto, pueden ver el borde de la torre, sobresaliendo ligeramente de la pared, lo que facilita el ascenso, con la cuerda colgando a unos cincuenta centímetros a los lados."
    
scene ciudadDeFondo with fade
"En silencio, siguen subiendo mientras las luces de la ciudad se hacen más pequeñas y el brillo de las estrellas se atenuaba frente al resplandor de las joyas que adornan el borde del edificio."

scene cimaDeLaTorre with dissolve
"Finalmente, Taurus extiende su mano, se agarra al borde y, con un rápido impulso, salta al otro lado. Conan, por su parte, se detiene un momento en el borde, fascinado por las deslumbrantes y frías joyas que lo rodean y que brillan como estrellas incrustadas en un cielo de plata."
"Desde la distancia, su fulgor se funde en un resplandor blanco, pero, de cerca, cada una de las piedras centellean con millones de matices, hipnotizando al joven con sus destellos."
    
show Conan at left
conan "Aquí hay una fabulosa fortuna, Taurus."

show Taurus at right
"¡Apresúrate! Si conseguimos el Corazón, esto y todo lo demás será nuestro."

"Conan trepa por el resplandeciente borde de la torre. El techo está unos metros más abajo del saliente enjoyado. Es plano y de un material de color azul oscuro, combinado con oro, lo que le da la apariencia de un inmenso zafiro salpicado de polvo dorado."
"Al otro lado del techo, se alza una especie de habitación hecha del mismo material que las paredes de la torre, adornada con pequeñas gemas."
    
scene puertaDeOro with dissolve
"La única puerta visible es de oro macizo, con paneles tallados y piedras preciosas incrustadas que brillan con un resplandor helado."

show Taurus at left
"Tuvimos suerte una vez más. Es de imaginar que el peso de ambos podría haber destrozado la piedra. Ahora sígueme, que los verdaderos peligros de nuestra aventura acaban de empezar. Estamos en la guarida de la serpiente, y no sabemos dónde está escondida."
"Atraviesan a rastras la misteriosa y brillante terraza como tigres detrás de su presa y se detienen delante de la puerta de oro."

#FIN FER
#COMIENZO SEBA

$ renpy.music.set_volume(0.4, channel='music')
show Taurus at right

taurus "Voy a entrar a comprobar que sea seguro. Será más sigiloso que entre solo. Tú quédate vigilando la retaguardia."

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

conan "No. Es mejor que entremos juntos. Si es una trampa, necesitarás ayuda"

show Taurus at right

taurus"De acuerdo. Quédate cerca."

$ renpy.music.set_volume(0.25, channel='sound')
play music pasos_concreto fadeout 1

"A la par, los ladrones abren la puerta y se adentran en una habitación oscura, tenebrosa y aparentemente olvidada. Telarañas cuelgan por todas partes y no hay objeto que no esté cubierto de polvo."

scene cuartoArania with fade

show Conan

play music radakan fadeout 1

conan "Taurus, cuidado!"
hide Conan

show Taurus
taurus "Aaagh! Diablos! ¿Qué es esta cosa?"

"Una pegajosa sustancia cubre a Taurus. Pegándolo al suelo e inmovilizándolo."

show Conan at left

conan "Por Crom! ¿De dónde vino eso?"

"Nuevamente, el instinto bárbaro de Conan salva al cimmerio de un nuevo ataque. Una enorme araña intenta embestir desde atrás. Al fallar, la araña continúa hacia Taurus."

show Arania right

play sound alertSound

conan "¡NOOO!"

"La araña toma a Taurus por el cuello con sus colmillos y le arrancó la cabeza de un tirón."

hide Taurus

conan "Maldita! ¡Las pagarás!"

play sound pasos_muchos

"La araña carga hacia Conan nuevamente."


jump Conan_pelea_con_la_araña


#Taurus entra solo
label entra_solo_Taurus:

show Conan at left
conan "Está bien, fijate que hay dentro de ese cuarto."

show Taurus 

taurus "De acuerdo."

play music pasos_concreto fadeout 1

hide Conan

"El ladrón abre la puerta y se adentra en la habitación"

scene cuartoArania with fade
stop music fadeout 1

"Esta es oscura, tenebrosa y aparentemente olvidada. Telarañas cuelgan por todas partes y no hay objeto que no estuviera cubierto de polvo."

taurus "Diablos… parece que hasta aquí llegas, cimerio…"

"Taurus vuelve a la puerta y asoma su cabeza"


taurus "Es seguro, pasa."
hide Taurus


$ renpy.music.set_volume(0.15, channel='sound')
play sound portazo
$ renpy.music.set_volume(0.25, channel='sound')

play music radakan fadeout 1

"Sin pensarlo mucho, Conan se adentra en el cuarto solo para escuchar un fuerte portazo detrás de él."
show Conan at left

taurus "Debo reconocer que eres muy hábil, bárbaro! Pero te vendría bien un poco de viveza."


conan "Maldito! ¡Déjame salir!"

taurus "Lo siento, Conan. No puedo hacer eso si quiero quedarme con la gema. ¡Saluda a mi amiga!"

conan "¡NO! Abre Taurus, cobarde. ¡Me las vas a pagar!"

hide Conan 
hide Taurus

show Conan

"El cimmerio siente como algo cae lentamente del techo, y al darse vuelta ahí la ve. Una enorme araña que vigila la entrada al cuarto de la gema."

show Arania at right

play sound spiderSound

"¡Maldita sea! Tendremos que enfrentarnos, asqueroso insecto."

label Conan_pelea_con_la_araña:

stop music fadeout 1

menu cómo_atacar_a_la_araña:
    "Atacar de frente":
        jump De_frente
    "Lanzar la espada al candelabro":
        jump Lanzar_espada

label De_frente:

show Conan 
show Arania

play sound swordDraw

"Conan empuña su espada y ataca a la araña de frente."

conan "¡AAAAH!"

play sound swordCut

"Justo antes de alcanzarla, el bárbaro se desliza por debajo de ella y la apuñala en el pecho. La araña se desploma y Conan se acerca para recuperar su espada."

if Conan_esta_solo == True :
    jump espera_Taurus #409
else:
    jump recamara_de_yag_kosha #109

label espera_Taurus:

hide Conan
hide Arania
scene puertaDeOro

show Taurus

"Se escucha un silencio atroz desde fuera del cuarto por lo que Taurus decide entrar."

scene cuartoArania

show Taurus at left

taurus "Espero que esa estúpida araña haya hecho su trabajo."

play sound portazo

"Al abrir las puertas ve el cuerpo de la araña en una posición postmortem y ni bien entra siente unos pasos acercándose cada vez más rápido hacia él."

show Conan at right

conan "¡Te dije que me las ibas a pagar, ladrón malnacido!"

"Sin ningún tipo de tapujo Conan corre hacia Taurus y le corta el cuello de una manera limpia dejando que se muera ahogado en su sangre."
play sound swordCut2
hide Taurus

jump recamara_de_yag_kosha

label Lanzar_espada:

show Conan
show Arania at right
hide Taurus

"Conan esquiva a la araña con mucha agilidad. En sus movimientos, nota que en el medio del cuarto hay un candelabro gigante y se le viene un plan a la cabeza."

conan "Asquerosa araña, ven ¡Atácame!"

play sound windCut
"La araña se va encima del bárbaro sedienta de sangre y con violencia. Cuando está por llegar, el cimmerio anticipa su ataque y tira su espada a la base del candelabro haciendo que se rompa y caiga."


"Para su infortunio, la araña esquiva el enorme candelabro y aprovecha el asombro de Conan para atacar su cuello y romperlo."

hide Conan
hide Arania

if Conan_esta_solo == True :
    jump espera_Taurus_Conan_M #409
else:
    jump Muerte #109

label espera_Taurus_Conan_M:

scene puertaDeOro

show Taurus

"Se escucha un silencio atroz desde fuera del cuarto por lo que Taurus decide entrar."

scene cuartoArania with fade

taurus "Espero que esa estúpida araña haya hecho su trabajo."

play sound portazo

show Arania at right

"Taurus abre las puertas y ve el cuerpo de Conan tirado en el medio del cuarto. Confiado se fue acercando de a poco hasta percatarse de que tiene el cuello roto, asustado se da media vuelta para salir corriendo de la habitación pero ya era demasiado tarde"
play sound spiderSound
"la araña lo captura con su tela lo deja colgado en el cuarto y aprovecha para devorarlo poco a poco comenzando con su cabeza."

label Muerte:

"Finalmente, los cadáveres de los audaces ladrones que se atrevieron a adentrarse en la famosa torre yacen fríamente en ella. Asesinados por la bestia protectora del secreto de la torre."
jump fin_de_la_partida

#FIN SEBA

#COMIENZO JUAN (ponele)
label recamara_de_yag_kosha:
scene remacamaraYagKosha

show Conan

"Conan entra sigilosamente en una habitación lujosa y exótica, llena de jade y marfil, con un ídolo extraño y aterrador en el centro. El ídolo tiene un cuerpo humanoide verde y una cabeza de pesadilla con colmillos de elefante."

show YagKosha at left

play sound choirSound

yagKosha "¿Quién anda ahí? ¿Has venido a torturarme de nuevo, Yara? ¿No te vas a cansar nunca?"

"Las lágrimas ruedan por sus mejillas, Conan observa las extremidades torturadas de Yag Kosha y siente una profunda compasión por su sufrimiento."

conan "No soy Yara. Soy solamente un ladrón. No te haré daño."

yagKosha "Tú no perteneces a la raza maligna de Yara. Llevas la marca de la fiereza pura y esbelta de las tierras desérticas. Conozco a tu gente desde antiguo."
 
yagKosha "Los conozco con otro nombre hace mucho, mucho tiempo, cuando un mundo distinto alzaba sus brillantes torres hacia las estrellas. Pero... hay sangre en tus manos."

conan "Es de la araña que había en la habitación de arriba y de uno de los leones del jardín."

yagKosha "¡Así es! Muerte en todas partes; lo sé; lo siento. Y la siguiente producirá un efecto mágico que ni el mismo Yara imagina. ¡Oh, hechizo de la liberación, dioses verdes de Yag!"

"Las lágrimas corren por las mejillas de la criatura mientras se estremece bajo intensas emociones. Conan lo observa perplejo hasta que el ser cesa de temblar y sus ojos ciegos se vuelven hacia él, haciéndole una seña."

yagKosha "Escúchame, hombre. Sé que te parezco repugnante y monstruoso, pero tú me parecerías igual de extraño. No soy ni un dios ni un demonio; soy de carne y hueso, aunque diferente. Vengo de Yag, un planeta verde en los confines del universo. Fuimos exiliados de nuestro mundo tras una derrota."

yagKosha "Aquí en la Tierra, nuestras alas se marchitaron. Hemos visto el ascenso y la caída de civilizaciones, desde Valusia hasta Atlantis y Lemuria. Ahora, yo soy el último de mi raza, esclavizado por Yara. Al principio, Yara aprendía de mi magia blanca, pero él ansiaba poder oscuro."

yagKosha "Me engañó para que revelara secretos prohibidos, y me esclavizó. He soportado trescientos años de tormento, obligado a realizar sus malvados deseos. Ahora presiento mi final. Tú eres la mano del destino. Coge la piedra en el altar."

yagKosha "Ahora viene la gran magia. Corta mi corazón y deja que la sangre fluya sobre la piedra. Luego baja a la habitación de Yara, pronuncia su nombre y entrégale la gema. Dile: '¡Atento, viajero del destino! Yag Kosha, el guardián de los arcanos olvidados, se digna a ofrecerte su último y más formidable conjuro.'"
yagKosha"Después, márchate. Mi muerte no es como la tuya; seré libre nuevamente."
hide YagKosha
hide Conan
"Conan se acerca con gesto vacilante, y Yag Kosha le indica dónde debía clavar la hoja. Conan aprieta los dientes y hunde profundamente la espada. La sangre fluye, empapando la hoja y su mano, y la criatura se agita antes de quedar inmóvil."
"Conan, asegurándose de que ya no estaba vivo, extrae lo que parece ser el corazón de Yag Kosha, aunque es distinto a cualquier corazón que hubiera visto. Aprieta la víscera sobre la joya, y sorprendentemente, la sangre fue absorbida por la gema. Con cuidado, Conan sale del recinto y baja por la escalera de plata."
"Siente que el cuerpo de Yag Kosha está sufriendo una transmutación detrás de él, algo que no debe presenciar. Al llegar a la puerta de ébano con la calavera de plata, la abre y ve a Yara, el brujo, en su lecho de seda negra, bajo los efectos del loto amarillo."

scene recamaraYara with fade

show Conan at left
conan "¡Yara! ¡Despierta!"

"Los ojos se abren al instante y se vuelven fríos y crueles como los de un buitre. La negra figura vestida de seda se yergue lúgubre sobre el cimmerio."
show yara at right
Yara "¡Perro! ¿Qué haces aquí?"

"Conan deposita la joya sobre la enorme mesa de ébano."

hide yara
conan "El que envía esta gema me mandó decir:"

menu :
    "¡Atento, viajero del destino! Yag Kosha, el guardián de los arcanos olvidados, se digna a ofrecerte su último y más formidable conjuro.":
        jump Conan_recita_bien_el_hechizo
    "¡Atento, viajero del destino! Yag Kosha, el guardián de los arcanos perdidos, se digna a ofrecerte su último y más fuerte hechizo.":
        jump Conan_recita_mal_el_hechizo


label Conan_recita_mal_el_hechizo:
hide Conan 
show yara at center
Yara "JAJAJA!Eso es todo lo que tienes? Un conjuro que ni siquiera funciona?" 

"Conan, confundido por lo sucedido, decide huir. Pues a pesar de su fuerza, Yara es claramente más poderoso."

Yara "¿A dónde crees que vas?"

"Con un chasquido, Conan se congela en el lugar."

Yara "Crees que puedes cometer tal intrusión y te dejara escapar como si nada hubiera pasado?"

"Conan, incapaz de emitir una palabra, por primera vez, teme por su vida. Entiende que se enfrenta a un poder que no era de su mundo y que su valentía y barbaridad no eran competencia ante tal poder."

Yara "Que pena… siempre creí que quien logre irrumpir en mi torre sería al menos un buen combatiente."

"Con otro chasquido de la mano de Yara, Conan desaparece como si se tratara de la luz al anochecer."
hide yara 
jump fin_de_la_partida


label Conan_recita_bien_el_hechizo:
hide Conan
"Yara retrocede con el rostro pálido mientras la joya, antes cristalina, emite humo de colores cambiantes. Hipnotizado, Yara toma la gema y comienza a encogerse ante los ojos de Conan, primero pareciendo un gigante, luego un niño y finalmente un ser diminuto que corre sobre la mesa aferrando la joya."
"Yara intenta escapar, pero sigue encogiéndose hasta que la joya parece una montaña a su lado, siendo finalmente atraído hacia ella."
show yara at center
Yara "En nombre de Yikk, te maldigo! ¿Cómo te atreves?"
hide yara
"Conan ve en el centro de la gema a una figura alada con cuerpo de hombre y cabeza de elefante, el vengador de Yag Kosha, que persigue a Yara. La joya explota en un destello iridiscente y desaparece, dejando la mesa de ébano y el lecho de mármol vacíos."

menu : 
    "Escapar por la escalera":
        jump escapa_por_escaleras
    "Escapar por donde se entró":
        jump escapa_por_soga


label escapa_por_escaleras:

scene escaleras with fade

"Conan huye, bajando una escalera de plata. Al llegar a una sala con soldados caídos, se da cuenta de que su camino está despejado."

jump Conan_llega_a_PB

label escapa_por_soga:

"Conan atraviesa el mismo camino por el que entró. Cuando llega al cuarto donde combatió a la araña ve el cuerpo frío de Taurus."

scene cuartoArania with fade

if Conan_esta_solo == True:
    show Conan at left
    conan "Te irás al infierno maldito. Esta torre te sepultará, será tu propia tumba"
    hide Conan 
else:
    show Conan at left
    conan "Lo lamento, compañero. Mi misión a cambiado y no he podido completar tu plan."
    hide Conan 
    
"Conan llega al balcón."

scene cimaDeLaTorre

menu :
    "Revisar la soga":
        jump Conan_revisa_la_soga
    "Descender sin revisar la soga":
        jump Conan_no_revisa_la_soga


label Conan_revisa_la_soga:
show Conan at center
conan "Que raro, la soga está floja, la ajuste lo suficiente para poder bajar sin ningún problema de esta torre."
hide Conan

"La soga, firme y bien anudada, soporta su peso sin ceder ni un ápice. Los músculos de Conan se tensan con cada movimiento, pero sus manos expertas se deslizan con precisión sobre la cuerda, controlando el ritmo de su descenso."
"Siente el tirón familiar en los brazos, pero no es nada a lo que su cuerpo curtido no esté acostumbrado. Sus pies tocan la pared del edificio ocasionalmente, pero no pierde el control."
"El guerrero desciende como una sombra, ágil y silencioso, su mirada clavada en el suelo que se aproxima rápidamente. Con un último impulso, Conan aterriza en el empedrado del callejón, flexionando sus rodillas para amortiguar el impacto. No hay pausa en sus movimientos; inmediatamente se pone en pie y suelta la soga sin mirar atrás."

scene baseDeLaTorre with fade

show Conan at center
conan "Suerte que he revisado y ajustado la soga porque si no estaría compartiendo el mismo destino que mi compañero."
hide Conan
jump Conan_llega_a_PB


label Conan_no_revisa_la_soga:
show Conan at center
conan "Tengo que irme rápido sin perder mucho tiempo en revisar si la soga está bien ajustada o no."

"Conan huye, descendiendo rápidamente por la soga que habían tirado Taurus hacia el balcón cuando tenían que subir. Pero a mitad del descenso, algo cambia. La soga, tensa en un principio, comienza a ceder hasta el punto de que se suelta de donde estaba agarrada, por lo que Conan empieza a caer hasta el suelo"
" Por suerte no estaba tan alto, pero aun así quedó medio dolorido tras la caída."
hide Conan
$ Conan_esta_herido = True

scene baseDeLaTorre with fade
show Conan at center 
conan "AAAAH!!! Maldita sea qué suerte tengo, por poco casi me mato, tenía que haber revisado la soga antes, pero aun así sigo vivo pero un poco dolorido."
hide Conan

label Conan_llega_a_PB:
"Sale por una puerta de plata hacia los jardines, donde la brisa del alba lo estremece."

scene jardinesInternos with fade

if Conan_esta_herido == True:
    jump Conan_no_logra_escapar
else:
    jump Conan_logra_escapar


label Conan_no_logra_escapar:

"Conan estando herido, le está costando escapar de la torre del elefante, La torre empieza a temblar y Conan intenta apresurarse."
show Conan at center
conan "Maldita sea, tengo que ser rápido sino no llegaré a escapar de esta torre del infierno. AAAAH!!!"

scene jardinesExternos with fade

"La torre comienza a derrumbarse con Conan dentro."
hide Conan
if Conan_mata_a_Drakos:
    jump Conan_muere_aplastado
else:
    jump Drakos_salva_a_Conan


label Conan_muere_aplastado:

"Conan, herido y exhausto, apenas logra mantenerse en pie mientras la torre del elefante se tambalea violentamente, sus paredes desmoronándose alrededor de él."
show Conan at center
conan "Maldita sea... tengo que salir de aquí... o este será mi final. ¡AAAH!"
hide Conan
"La torre se derrumba por completo, y Conan, atrapado bajo los escombros, no puede escapar. La enorme estructura cae sobre él, aplastando bajo su peso. En sus últimos momentos, sus pensamientos se desvanecen entre la oscuridad y el eco de la destrucción."
"El polvo se asienta lentamente, y el imponente guerrero conocido como Conan encuentra su fin bajo las ruinas de la torre del elefante, su destino sellado en las profundidades de la noche."

jump fin_de_la_partida


label Drakos_salva_a_Conan:

"Pareciendo que Conan muere definitivamente hasta que aparece Drakos en el momento justo para salvarlo y no morir aplastado por la torre."
show Drakos at left
drakos "Maldición Conan, suerte que he llegado en el momento justo para poder rescatarte. No he olvidado nuestra conversación al venir aquí hace unas cuantas horas y también por no haberme matado en el bar, y por eso vengo a ayudarte."
show Conan at right
conan "Muchas gracias… Drakos por haberme salvado, te debo una enorme. Ahora vayámonos de aquí rápidamente antes de que venga una multitud a ver qué pasa."

scene torreDerrumbandoseLejos with fade

"A medida que se iban, tanto Conan como Drakos observaron como la torre se empieza a convertir en una inmensa nube de minúsculas partículas resplandecientes en que ambos se miran muy confundidos y al mismo tiempo muy asombrados por lo que acababa de pasar."
hide Drakos
hide Conan
jump fin_de_la_partida

label Conan_logra_escapar:

scene jardinesExternos with fade

"Conan atraviesa la puerta principal y corre por su vida. El impecable estado físico del bárbaro le permite alejarse lo suficiente para voltear y ver nuevamente la impresionante torre."

Conan "Qué acaba de suceder…? Acaso me han embrujado?"

scene torreDerrumbandoseLejos with fade

"Entre sus dudas, logra observar cómo la estructura comienza a desmoronarse para eventualmente convertirse en una inmensa nube de minúsculas partículas resplandecientes."

label fin_de_la_partida:

#FIN JUAN