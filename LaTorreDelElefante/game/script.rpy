# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define conan = Character("CONAN", color = "#e9c33c")
define drakos = Character("DRAKOS", color = "#0a0a0a")
define taurus = Character("TAURUS", color = "#643523")
define ladrón = Character("LADRÓN", color = "#0a0a0a")
define yagKosha = Character("YAG KOSHA", color = "#91ef91")
define yara = Character("YARA", color = "#981723")

default conan_esta_solo = True

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
"Un gran chorro de polvo dorado sale por el otro extremo y se extiende instantáneamente formando una densa nube de color verde amarillento que cubre los arbustos, ocultando los resplandecientes ojos."
"Taurus corre apresuradamente hacia el muro. Conan lo mira sin comprender. La densa nube oculta los matorrales y no se oye nada."

conan "¿Qué es ese polvo?"

taurus "¡Es la muerte! Si se levanta viento y sopla en nuestra dirección, tendremos que huir saltando la muralla. Pero no, no se ha levantado viento y la nube se está disipando. Espera hasta que desaparezca del todo. Respirar ese polvo supone la muerte."

"Finalmente quedan flotando solo unas tenues nubecillas amarillentas en el aire; cuando desaparecen, Taurus indica a su compañero con la mano que avance. Se dirigen sigilosamente hacia los arbustos y Conan se queda boquiabierto."
"Tendidos en el suelo entre las sombras yacen cinco cuerpos de color pardo cuya mirada feroz se ha extinguido para siempre. Un olor dulzón y empalagoso persiste en el aire."

conan "¡Murieron sin lanzar un solo rugido! TAURUS, ¿qué era ese polvo?"


#comienzo de la pagina 25 a 32

#"El nemedio agarra firmemente la cuerda, enganchando una rodilla en ella, y comienza a subir con agilidad, como un gato, a pesar de su corpulento cuerpo. El cimmerio lo sigue de cerca. Aunque la cuerda oscila y gira sobre sí misma, ambos hombres continúan escalando sin problemas."
#"Desde lo alto, pueden ver el borde de la torre, sobresaliendo ligeramente de la pared, lo que facilita el ascenso, con la cuerda colgando a unos cincuenta centímetros a los lados."
#"En silencio, siguen subiendo mientras las luces de la ciudad se hacen más pequeñas y el brillo de las estrellas se atenuaba frente al resplandor de las joyas que adornan el borde del edificio. Finalmente, TAURUS extiende su mano, se agarra al borde y, con un rápido impulso, salta al otro lado."
#"CONAN, por su parte, se detiene un momento en el borde, fascinado por las deslumbrantes y frías joyas que lo rodeaban. Diamantes, rubíes, esmeraldas, zafiros, turquesas y piedras de la luna brillan como estrellas incrustadas en un cielo de plata."
#"Desde la distancia, su fulgor se funde en un resplandor blanco, pero, de cerca, cada una de las piedras centellean con millones de matices, hipnotizando al joven con sus destellos."

#conan "Aquí hay una fabulosa fortuna, TAURUS."

#taurus "¡Apresúrate! Si conseguimos el Corazón, esto y todo lo demás será nuestro."

#"CONAN trepa por el resplandeciente borde de la torre. El techo está unos metros más abajo del saliente enjoyado. Es plano y de un material de color azul oscuro, combinado con oro, lo que le da la apariencia de un inmenso zafiro salpicado de polvo dorado."
#"Al otro lado del techo, se alza una especie de habitación hecha del mismo material que las paredes de la torre, adornada con pequeñas gemas. La única puerta visible es de oro macizo, con paneles tallados y piedras preciosas incrustadas que brillan con un resplandor helado."
#"CONAN dirige su mirada hacia el vasto océano de luces a lo lejos, y luego observa a TAURUS, quien está recogiendo la cuerda. El nemedio le muestra el lugar donde el gancho de acero se había asegurado, y vieron que la punta estaba apenas enganchada debajo de una brillante joya en el lado interior del borde."

#taurus "Tuvimos suerte una vez más. Es de imaginar que el peso de ambos podría haber destrozado la piedra. Ahora sígueme, que los verdaderos peligros de nuestra aventura acaban de empezar. Estamos en la guarida de la serpiente, y no sabemos dónde está escondida."
#"Ante el aviso de su compañero, TAURUS voltea para ver a CONAN apuntando con su mano sobre sus cabezas."

#"Atraviesan a rastras la misteriosa y brillante terraza como tigres detrás de su presa y se detienen delante de la puerta de oro. "

#"Voy a entrar a comprobar que sea seguro. Será más sigiloso que entre solo. Tú quédate vigilando la retaguardia."

#menu CONFIAR_EN_TAURUS:
 #   "Entrar con el":
  #      $ conan_esta_solo =False
   #     jump entrar_con_taurus
    #"Dejer entrar solo a Taurus":
     #   $ conan_esta_solo =True
      #  jump entra_solo_taurus

#label entrar_con_taurus:

#conan "No. Es mejor que entremos juntos. Si es una trampa, necesitarás ayuda."

#taurus "De acuerdo. Quédate cerca."

#"A la par, los ladrones abren la puerta y se adentran en una habitación oscura, tenebrosa y aparentemente olvidada. Telarañas cuelgan por todas partes y no hay objeto que no esté cubierto de polvo."






scene bg JardinesDeLaTorre with fade
show taurus at left

taurus "Están hechas con flores de loto negro, que crecen en las selvas remotas de Khitai, donde solo habitan los monjes de cráneo amarillo de Yun. Esas flores causan la muerte al que las huele."

"CONAN se arrodilla al lado de los enormes animales muertos, asegurándose de que no podían hacerle daño. Mueve la cabeza pensando que la magia de las tierras exóticas es terrible y misteriosa a los ojos de los bárbaros del norte."

show conan
conan "¿Por qué no matamos a los soldados de la torre de la misma manera?"

show taurus
taurus "Porque ese es todo el polvo que tengo. Su obtención fue una hazaña que hubiera bastado para hacerme famoso entre todos los ladrones del mundo. Lo robé de una caravana que se dirigía a Estigia. ¡Pero, vamos ya, por Bel! ¿Vamos a pasarnos toda la noche hablando?"

scene bg BaseDeLaTorre with dissolve
"TAURUS y CONAN se arrastran silenciosamente hasta la base de la torre. Sin decir una palabra, TAURUS desenrolla una cuerda con un gancho de acero en uno de sus extremos."

"¿En que lado de la torre tira TAURUS el gancho?."

menu :
    "Lado derecho":
        jump derecho
    "Lado izquierdo":
        jump izquierdo

label derecho:
scene bg BaseDeLaTorre
show conan
conan "Lánzalo en el lado derecho, veo una saliente allí."

"Mientras que TAURUS se prepara para lanzar la soga a la saliente. CONAN, atento, apoya su oído en la pared de la torre, pero no oye nada, lo que indica que los guardias dentro no se han percatado de su presencia."
"Aun así, el bárbaro siente una inquietud inexplicable, tal vez por el fuerte olor de los leones que domina el aire."
"Con un movimiento firme, TAURUS lanza la cuerda, y el gancho desaparece sobre el borde de la torre. Tras comprobar que está bien sujeto, tira de ella sin aflojarla."

show taurus
taurus "¡Buen ojo! Ahora..."

show conanAlerta
"El instinto salvaje de CONAN lo hace reaccionar de inmediato, ya que la muerte silenciosa acecha desde arriba. Con una sola mirada, el cimmerio percibe la gigantesca sombra de un león, listo para atacar."
scene ConanVsLeon
"Ningún hombre civilizado es tan rápido como el bárbaro. Su espada, brillando bajo las estrellas, se mueve con una fuerza desesperada, y en un instante, el hombre y la bestia ruedan juntos por el suelo."
scene TaurusViendoAlLeonEncimaDeConan
"TAURUS, maldiciendo para sus adentros, se agacha y ve a CONAN luchando por liberarse del enorme peso del león. Para su asombro, el animal yace muerto, con el cráneo partido. Con su ayuda, CONAN aparta el cuerpo y se levanta, aún empuñando su espada ensangrentada."

scene bg LeonMuerto

show taurus at right
taurus "¿Estás herido, amigo?"

show conan at left
conan "¡Por Crom, no! Pero me libre por poco. ¿Por qué esa maldita bestia no ruge en el momento de atacar?"
jump continuacion

label izquierdo:
scene bg BaseDeLaTorre
show conan
conan "Lánzalo en el lado izquierdo, veo una saliente allí."

"Mientras que TAURUS se prepara para lanzar la soga a la saliente. CONAN, atento, apoya su oído en la pared de la torre, pero no oye nada, lo que indica que los guardias dentro no se han percatado de su presencia."
"Aun así, el bárbaro siente una inquietud inexplicable, tal vez por el fuerte olor de los leones que domina el aire."
"Con un movimiento firme, TAURUS lanza la cuerda, y el gancho desaparece sobre el borde de la torre. Tras comprobar que está bien sujeto, tira de ella sin aflojarla."

show taurus
taurus "¡Buen ojo! Ahora debemos subir con cuidado"    

"El instinto salvaje de CONAN lo hace reaccionar con mucha ansiedad y reacción rápido, ya que la muerte silenciosa acecha dentro de los jardines."
"Apurado, intenta subir rápido pero no logra ver al león que lo está acechando."
scene ConanVsLeon
"Intenta desenvainar su espada, pero el enorme felino es mucho más rápido, se mueve con una fuerza desesperada, y en un instante, el hombre y la bestia ruedan juntos por el suelo."
"TAURUS, maldiciendo para sus adentros, se agacha y ve a  CONAN luchando por liberarse del enorme peso del león. Para su asombro, el animal logra masticar el costado de la costilla izquierda de CONAN."
"Luego el bárbaro logra sacar su espada y gracias a la adrenalina que surge dentro de su ser logra clavarle la espada en la parte de atrás del cuello del león y así provocar su muerte."
"CONAN aparta el cuerpo y se levanta, aún empuñando su espada ensangrentada."

scene bg BaseDeLaTorre

show taurusPreocupado
taurus "Oh por dios!. No me esperaba ese enorme león en este lugar de la torre.¿Estas bien CONAN?"

show conanDolorido
conan "Si, no te preocupes por mí. Sigamos a lo que vinimos, entremos a la torre. No hay tiempo que perder."
hide taurusPreocupado
jump continuacion

label continuacion:
show taurus at right
taurus "Todo es extraño en este jardín. Los leones atacan en silencio, al igual que las otras muertes. Pero sigamos; aunque hemos hecho poco ruido en la pelea, los soldados pueden haber oído algo, a menos que estén dormidos o borrachos."
taurus "Esa fiera está en alguna otra parte del jardín y escapa de la muerte de las flores, pero seguramente ya no hay más animales. Ahora debemos trepar por esta cuerda; imagino que no es necesario preguntar a un cimmerio si puede hacerlo."

show conanDolorido at left
conan "Si resiste mi peso."

taurus "Puede aguantar tres veces mi propio peso. Está hecha con trenzas de mujeres muertas, que yo mismo cogí de sus tumbas a medianoche, y que luego sumergí en la mortífera savia del árbol de upas, para hacerlas resistentes."
taurus "Yo subiré primero, y luego me seguirás tú de cerca."

scene bg conanYTaurusEscalando

"El nemedio agarra firmemente la cuerda, enganchando una rodilla en ella, y comienza a subir con agilidad, como un gato, a pesar de su corpulento cuerpo. El cimmerio lo sigue de cerca. Aunque la cuerda oscila y gira sobre sí misma, ambos hombres continúan escalando sin problemas."
"Desde lo alto, pueden ver el borde de la torre, sobresaliendo ligeramente de la pared, lo que facilita el ascenso, con la cuerda colgando a unos cincuenta centímetros a los lados."

scene bg ciudadDeFondo
"En silencio, siguen subiendo mientras las luces de la ciudad se hacen más pequeñas y el brillo de las estrellas se atenuaba frente al resplandor de las joyas que adornan el borde del edificio."

scene bg bordeDeLaTorre
"Finalmente, TAURUS extiende su mano, se agarra al borde y, con un rápido impulso, salta al otro lado. CONAN, por su parte, se detiene un momento en el borde, fascinado por las deslumbrantes y frías joyas que lo rodean y que brillan como estrellas incrustadas en un cielo de plata."
"Desde la distancia, su fulgor se funde en un resplandor blanco, pero, de cerca, cada una de las piedras centellean con millones de matices, hipnotizando al joven con sus destellos."

show conan at left
conan "Aquí hay una fabulosa fortuna, TAURUS."

show taurus at right
"¡Apresúrate! Si conseguimos el Corazón, esto y todo lo demás será nuestro."

scene bg laTorreFondoCiudad
"CONAN trepa por el resplandeciente borde de la torre. El techo está unos metros más abajo del saliente enjoyado. Es plano y de un material de color azul oscuro, combinado con oro, lo que le da la apariencia de un inmenso zafiro salpicado de polvo dorado."
"Al otro lado del techo, se alza una especie de habitación hecha del mismo material que las paredes de la torre, adornada con pequeñas gemas."
scene bg puertaDeOro
"La única puerta visible es de oro macizo, con paneles tallados y piedras preciosas incrustadas que brillan con un resplandor helado."    
scene bg laTorreFondoCiudad
"CONAN dirige su mirada hacia el vasto océano de luces a lo lejos, y luego observa a TAURUS, quien está recogiendo la cuerda."
"El nemedio le muestra el lugar donde el gancho de acero se había asegurado, y vieron que la punta estaba apenas enganchada debajo de una brillante joya en el lado interior del borde."

scene bg puertaDeOro
show taurus at left
"Tuvimos suerte una vez más. Es de imaginar que el peso de ambos podría haber destrozado la piedra. Ahora sígueme, que los verdaderos peligros de nuestra aventura acaban de empezar. Estamos en la guarida de la serpiente, y no sabemos dónde está escondida."

scene bg dentroTerraza
"Atraviesan a rastras la misteriosa y brillante terraza como tigres detrás de su presa y se detienen delante de la puerta de oro. "

scene bg puertaDeOro
show taurus at right
"Voy a entrar a comprobar que sea seguro. Será más sigiloso que entre solo. Tú quédate vigilando la retaguardia."

hide taurus
"Conan piensa por dentro"
show conan
"¿Debo dejar que cruce solo esa puerta?"


menu :
    "Si ":
        jump confiar
    "no":
        jump noConfiar

label noConfiar:
show conan at left
"No. Es mejor que entremos juntos. Si es una trampa, necesitarás ayuda"
show taurus at right
"De acuerdo. Quédate cerca."

scene puertaDeOro
"A la par, los ladrones abren la puerta y se adentran en una habitación oscura, tenebrosa y aparentemente olvidada. Telarañas cuelgan por todas partes y no hay objeto que no esté cubierto de polvo."

show conan
"TAURUS, cuidado!"









taurus "Aaagh! Diablos! ¿Qué es esta cosa?"

"Una pegajosa sustancia cubre a TAURUS. Pegándolo al suelo e inmovilizándolo."

conan "Por Crom! ¿De dónde vino eso?"

"Nuevamente, el instinto bárbaro de CONAN salva al cimmerio de un nuevo ataque. Una enorme araña intenta embestir desde atrás. Al fallar, la araña continúa hacia TAURUS."

conan "¡NOOO!"

"La araña toma a TAURUS por el cuello con sus colmillos y le arrancó la cabeza de un tirón."

conan "Maldita! ¡Las pagarás!"

"La araña carga hacia CONAN nuevamente."

if conan_esta_solo == False:
    jump conan_pelea_con_la_araña

#taurus entra solo
label entra_solo_taurus:

conan "Está bien, fijate que hay dentro de ese cuarto."

taurus "De acuerdo."

"El ladrón abre la puerta y se adentra en una habitación oscura, tenebrosa y aparentemente olvidada. Telarañas cuelgan por todas partes y no hay objeto que no estuviera cubierto de polvo."

taurus "Diablos… parece que hasta aquí llegas, cimerio…"

"TAURUS sale del cuarto"

taurus "Es seguro, pasa."

"Sin pensarlo mucho, CONAN se adentra en el cuarto solo para escuchar un fuerte portazo detrás de él."

taurus "Debo reconocer que eres muy hábil, bárbaro! Pero te vendría bien un poco de viveza."

conan "Maldito! ¡Déjame salir!"

taurus "Lo siento, CONAN. No puedo hacer eso si quiero quedarme con la gema. ¡Saluda a mi amiga!"

conan "¡NO! Abre TAURUS, cobarde. ¡Me las vas a pagar!"

"El cimmerio siente como algo cae lentamente del techo, y al darse vuelta ahí la ve. Una enorme araña que vigila la entrada al cuarto de la gema."

"¡Maldita sea! Tendremos que enfrentarnos, asqueroso insecto."

label conan_pelea_con_la_araña:

menu cómo_atacar_a_la_araña:
    "Atacar de frente":
        jump De_frente
    "Lanzar la espada al candelabro":
        jump Lanzar_espada

label De_frente:
 
"CONAN empuña su espada y ataca a la araña de frente."

conan "¡AAAAH!"

"Justo antes de alcanzarla, el bárbaro se desliza por debajo de ella y la apuñala en el pecho. La araña se desploma y CONAN se acerca para recuperar su espada."

if conan_esta_solo == True :
    jump espera_taurus #409
else:
    jump recamara_de_yag_kosha #109

label espera_taurus:

"Se escucha un silencio atroz desde fuera del cuarto por lo que TAURUS decide entrar."

taurus "Espero que esa estúpida araña haya hecho su trabajo."

"Al abrir las puertas ve el cuerpo de la araña en una posición postmortem y ni bien entra siente unos pasos acercándose cada vez más rápido hacia él."

conan "¡Te dije que me las ibas a pagar, ladrón malnacido!"

"Sin ningún tipo de tapujo CONAN corre hacia TAURUS y le corta el cuello de una manera limpia dejando que se muera ahogado en su sangre."

jump recamara_de_yag_kosha

label Lanzar_espada:

"CONAN esquiva a la araña con mucha agilidad. En sus movimientos, nota que en el medio del cuarto hay un candelabro gigante y se le viene un plan a la cabeza."

conan "Asquerosa araña, ven ¡Atácame!"

"La araña se va encima del bárbaro sedienta de sangre y con violencia. Cuando está por llegar, el cimmerio anticipa su ataque y tira su espada a la base del candelabro haciendo que se rompa y caiga."
"Para su infortunio, la araña esquiva el enorme candelabro y aprovecha el asombro de CONAN para atacar su cuello y romperlo."

if conan_esta_solo == True :
    jump espera_taurus_conan_M #409
else:
    jump Muerte #109

label espera_taurus_conan_M:

"Se escucha un silencio atroz desde fuera del cuarto por lo que TAURUS decide entrar."

taurus "Espero que esa estúpida araña haya hecho su trabajo."

"TAURUS abre las puertas y ve el cuerpo de CONAN tirado en el medio del cuarto. Confiado se fue acercando de a poco hasta percatarse de que tiene el cuello roto, asustado se da media vuelta para salir corriendo de la habitación pero ya era demasiado tarde"
"la araña lo captura con su tela lo deja colgado en el cuarto y aprovecha para devorarlo poco a poco comenzando con su cabeza."

label Muerte:

"Finalmente, los cadáveres de los audaces ladrones que se atrevieron a adentrarse en la famosa torre yacen fríamente en ella. Asesinados por la bestia protectora del secreto de la torre."
jump fin_de_la_partida

label recamara_de_yag_kosha:
scene int recamara de yag kosha

"CONAN entra sigilosamente en una habitación lujosa y exótica, llena de jade y marfil, con un ídolo extraño y aterrador en el centro. El ídolo tiene un cuerpo humanoide verde y una cabeza de pesadilla con colmillos de elefante."

yagKosha "¿Quién anda ahí? ¿Has venido a torturarme de nuevo, YARA? ¿No te vas a cansar nunca?"

"Las lágrimas ruedan por sus mejillas, CONAN observa las extremidades torturadas de YAG KOSHA y siente una profunda compasión por su sufrimiento."

conan "No soy YARA. Soy solamente un ladrón. No te haré daño."

yagKosha "Tú no perteneces a la raza maligna de YARA. Llevas la marca de la fiereza pura y esbelta de las tierras desérticas. Conozco a tu gente desde antiguo."
 
yagKosha "Los conozco con otro nombre hace mucho, mucho tiempo, cuando un mundo distinto alzaba sus brillantes torres hacia las estrellas. Pero... hay sangre en tus manos."

conan "Es de la araña que había en la habitación de arriba y de uno de los leones del jardín."

yagKosha "¡Así es! Muerte en todas partes; lo sé; lo siento. Y la siguiente producirá un efecto mágico que ni el mismo YARA imagina. ¡Oh, hechizo de la liberación, dioses verdes de Yag!"

"Las lágrimas corren por las mejillas de la criatura mientras se estremece bajo intensas emociones. CONAN lo observa perplejo hasta que el ser cesa de temblar y sus ojos ciegos se vuelven hacia él, haciéndole una seña."

yagKosha "Escúchame, hombre. Sé que te parezco repugnante y monstruoso, pero tú me parecerías igual de extraño. No soy ni un dios ni un demonio; soy de carne y hueso, aunque diferente. Vengo de Yag, un planeta verde en los confines del universo. Fuimos exiliados de nuestro mundo tras una derrota."

yagKosha "Aquí en la Tierra, nuestras alas se marchitaron. Hemos visto el ascenso y la caída de civilizaciones, desde Valusia hasta Atlantis y Lemuria. Ahora, yo soy el último de mi raza, esclavizado por YARA."

yagKosha "Al principio, YARA aprendía de mi magia blanca, pero él ansiaba poder oscuro. Me engañó para que revelara secretos prohibidos, y me esclavizó. He soportado trescientos años de tormento, obligado a realizar sus malvados deseos. Ahora presiento mi final. Tú eres la mano del destino. Coge la piedra en el altar."

"CONAN vuelve hacia el altar de oro y marfil que le ha señalado el extraño ser y coge una enorme joya redonda, clara como un cristal carmesí, y en ese momento descubre que es el Corazón del Elefante."
"Tú no perteneces a la raza maligna de YARA. Llevas la marca de la fiereza pura y esbelta de las tierras desérticas. Conozco a tu gente desde antiguo. Los conozco con otro nombre hace mucho, mucho tiempo, cuando un mundo distinto alzaba sus brillantes torres hacia las estrellas. Pero... hay sangre en tus manos."

conan "Es de la araña que había en la habitación de arriba y de uno de los leones del jardín."

yagKosha "¡Así es! Muerte en todas partes; lo sé; lo siento. Y la siguiente producirá un efecto mágico que ni el mismo YARA imagina. ¡Oh, hechizo de la liberación, dioses verdes de Yag!"

"Las lágrimas corren por las mejillas de la criatura mientras se estremece bajo intensas emociones. CONAN lo observa perplejo hasta que el ser cesa de temblar y sus ojos ciegos se vuelven hacia él, haciéndole una seña."

yagKosha "Escúchame, hombre. Sé que te parezco repugnante y monstruoso, pero tú me parecerías igual de extraño. No soy ni un dios ni un demonio; soy de carne y hueso, aunque diferente. Vengo de Yag, un planeta verde en los confines del universo. Fuimos exiliados de nuestro mundo tras una derrota. Aquí en la Tierra, nuestras alas se marchitaron. Hemos visto el ascenso y la caída de civilizaciones, desde Valusia hasta Atlantis y Lemuria. Ahora, yo soy el último de mi raza, esclavizado por YARA. Al principio, YARA aprendía de mi magia blanca, pero él ansiaba poder oscuro. Me engañó para que revelara secretos prohibidos, y me esclavizó. He soportado trescientos años de tormento, obligado a realizar sus malvados deseos. Ahora presiento mi final. Tú eres la mano del destino. Coge la piedra en el altar."

yagKosha "Ahora viene la gran magia. Corta mi corazón y deja que la sangre fluya sobre la piedra. Luego baja a la habitación de YARA, pronuncia su nombre y entrégale la gema. Dile: '¡Atento, viajero del destino! YAG KOSHA, el guardián de los arcanos olvidados, se digna a ofrecerte su último y más formidable conjuro.'. Después, márchate. Mi muerte no es como la tuya; seré libre nuevamente."

"CONAN se acerca con gesto vacilante, y YAG KOSHA le indica dónde debía clavar la hoja. CONAN aprieta los dientes y hunde profundamente la espada. La sangre fluye, empapando la hoja y su mano, y la criatura se agita antes de quedar inmóvil. CONAN, asegurándose de que ya no estaba vivo, extrae lo que parece ser el corazón de YAG KOSHA, aunque es distinto a cualquier corazón que hubiera visto. Aprieta la víscera sobre la joya, y sorprendentemente, la sangre fue absorbida por la gema. Con cuidado, CONAN sale del recinto y baja por la escalera de plata. Siente que el cuerpo de YAG KOSHA está sufriendo una transmutación detrás de él, algo que no debe presenciar. Al llegar a la puerta de ébano con la calavera de plata, la abre y ve a YARA, el brujo, en su lecho de seda negra, bajo los efectos del loto amarillo."

conan "¡YARA! ¡Despierta!"

"Los ojos se abren al instante y se vuelven fríos y crueles como los de un buitre. La negra figura vestida de seda se yergue lúgubre sobre el cimmerio."

yara "¡Perro! ¿Qué haces aquí?"

"CONAN deposita la joya sobre la enorme mesa de ébano."

conan "El que envía esta gema me mandó decir:"

label fin_de_la_partida: