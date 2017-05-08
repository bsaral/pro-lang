var db = null;
var sunnahs = ["Sürekli abdestli durmak","Abdest aldıktan sonra kıble dönüp su içmek.","Cuma günü gusül abdesti almak, tırnak kesmek (Tırnak kesmeye önce sağ el parmaklarının şahadet parmağından başlamak) ve sadaka vermek.",
"Yemekte sağ ayağı dikip sol ayak üzerinde oturmak.","Yemeğe besmele (Bismillahirrahmanirrahim) ile başlayıp hamd (Elhamdülillah) ile bitirmek.","Az gülmek gülünce kahkaha ile değil tebessüm ile gülmek.",
"Elbise ve ayakkabıyı sağdan giyip soldan çıkarmak. ","Gülsuyu kullanmak","Pantolonu katlayıp koymak. ","Aksıranın elhamdülillah demesi. ","Suyu oturarak üç yudumda içmek. ","Yatarken sağ tarafına yatmak. ","Yemeğe tuz ile başlamak. ","Her gün ölümü düşünmek. ","Salavat okumak(Ömründe bir defa okumak farz ,İsmi duyunca vacip, her seferinde ismi duyulunca müstahap). ",
"Bir kapıya gelince kapıyı 3 defa vurur, izin verilirse girmemizi söyler, kapının ya sağ ya sol tarafında durur ve selam verip içeri girerdi. ","Ayakkabıyı giymeden önce ters çevirmek.","Oturarak küçük abdest bozmak (Ayakta bozmak tahrimen mekruhtur; idrarın üste sıçrama ihtimali olduğu gibi bu şekilde abdest bozmak sağlığa da zararlıdır. Ayrıca üstüne idrar ve necaset bulaşanlar, bunu dikkat etmeyerek yapıyorlarsa kabir azabına uğrarlar Allah muhafaza!) ",
"Yemekte güzel şeylerden bahsetmek (Yemekte konuşulmaz lafının aslı yoktur) ","Duş aldıktan sonra çıkarken ayaklarını yıkamak. ","Her gün tövbe etmek. (Tövbe estağfirullah) gibi. ",
"Yolda başı öne eğik yürümek. ","İmanını sık sık tazelemek. -Bunun nasıl olduğunu sahabe-i kiram Efendimiz ((S.A.V)) 'e sorduklarında -La İlahe İllAllah diyerek buyurmuşlardır. (İmam Gazali -Mukafeşetük Kulb) "," Kıymetsiz yerlere girerken sol ayakla girilip, sağ ayakla çıkılması (tuvalet) ","Mubah olan yerlere sağ ayakla girilip sağ ayakla çıkılması. "," Eve girerken, ev boşta olsa selam vermek.","Sofradan doymadan kalkmak.","Ezanı dinlemek.","Yemeğin ortasında dua etmek.","Sofraya oturmadan ellerini yıkamak.",
" Önünde artık bırakmamak ve yemek tabağının dibini sıyırmak","Ekmeği elle bölmek.","Abdestli yatmak","Gömleğin düğmelerini aşağıdan yukarı doğru iliklemek çözerken yukarıdan aşağı doğru çözmek"]

var zikir = [
    {name: "Bismillahi Subhanallahi ve Bihamdihi" , description : "Ebu’d-Derdâ radıyallahu anh’tan rivayet edildiğine göre, Rasulullah sallallahu aleyhi ve sellem şöyle buyurdu:“Sizin biriniz her gün sabahladığında Allah için bin hasene (sevap) işlemeyi terketmesin, her kim sabahladığında yüz kere: ‘Bismillahi sübhanallahi ve bihamdihi (Allah’ın ismiyle başlayıp, Allah’ı tesbih ederim ve ona hamd ederim.)’ derse, bu bin hasenedir ki, inşaAllah o gün o kadar (bin tane) günah işleyemez. Bundan başka işlediği hayırlar da bol bol kendisine kalır."},
    {name : " Lâ ilâhe illallâhu vahdehu lâşerîke leh, lehu'l mülkü ve lehu'l hamdü ve hüve alâ külli şey'in kadîr",description : "Hz. Ebû Hüreyre (radıyallâhu anh) anlatıyor: “Resûlullah aleyhissalâtu vesselâm buyurdular ki:“Kim, ‘Lâ ilâhe illallâhu vahdehu lâşerîke leh, lehu’l mülkü ve lehu’l hamdü ve hüve alâ külli şey’in kadîr.’ duasını bir günde yüz kere söylerse, kendisine on köle âzad etmiş gibi sevab verilir, ayrıca lehine yüz sevab yazılır ve yüz günahı da silinir. Bu, ayrıca üç gün akşama kadar onu şeytana karşı muhafaza eder. Bundan daha fazlasını okumayan hiçbir kimse, o adamınkinden daha efdal bir amel de getiremez. Kim de bir günde yüz kere”Sübhânallahi ve bihamdihi” derse hataları dökülür, hatta denizin köpüğü kadar (çok) olsa bile.”"},
    {name : "Lâ ilâhe illallâhu'l Melikül Hakkul Mübin", description : "Hazreti Ali radıyallahu anh’tan rivayet edildiğine göre, Rasulullah aleyhissalatü vesselam Efendimiz Hazretleri şöyle buyurmuştur: “Her kim günde yüz kere ‘Lâ ilâhe illallâhu’l Melikül Hakkul Mübin’ derse, bu zikir kendisi için fakirlikten kurtuluş, kabir yalnızlığında yoldaş olur. Bununla zenginliği celbeder ve cennetin kapısını çalar.”"},
    {name : "Lâ ilâhe illallah", description : "Ebu’d-Derda radıyallahu anh‘tan rivayetle Rasulullah Sallallahu Teala Aleyhi ve Sellem Efendimiz Hazretleri şöyle buyurdu: “ Her kim yüz kere ‘Lâ ilâhe illallah’ derse, Allah(u Teala) onun yüzünü kıyamet gününde ayın ondördü gibi parlatır ve onu dediği günde, onun kadar veya ondan fazla diyenden başka, ondan daha üstün bir amel hiçbir kimse için yükseltilmez.”"},
    {name : "Lâ Havle Velâ Kuvvete İllâ Billâh", description : "Esed İbni Veda’a radıyallahu anh’dan rivayetle, Rasulullah sallallahu aleyhi ve sellem Efendimiz şöyle buyurdular: “Her kim, her gün, yüz kere: ‘Lâ Havle Velâ Kuvvete İllâ Billâh’ derse, fakirlik, ebediyyen ona isabet etmez.”"},
    {name : "Sübhânallâhi velhamdülillâhi velâ ilâhe illallahü vallâhü ekber", description : "Ebû Hüreyre radıyallahu anh’den rivâyet edildiğine göre Resûlullah sallallahu aleyhi ve sellem şöyle buyurdu:“Sübhânallâhi velhamdülillâhi velâ ilâhe illallahü vallâhü ekber demek, benim için, üzerine güneş doğan her şeyden daha kıymetlidir.”"},
    {name : "Estağfirullah", description : "Estağfirullah diyerek istiğfar etmek sürekli devam etmemiz gereken bir ameldir. Allahu Teala’nın çokça tevbe edenleri sevdiği Bakara Suresi 222. Ayetinde geçmektedir. Ayrıca Rasulullah aleyhissalatü vesselam Efendimiz’in şu Hadis-i Şerifleri vardır:“İstiğfara devam edeni, Allahü teâlâ, dertlerden, sıkıntılardan kurtarır. Ummadığı yerden rızıklandırır.”"},
    {name : "Lâ ilâhe illâ ente sübhaneke innî küntü minez-zâlimîn.", description : " Yûnus: Ey Rabbim! Senden başka ilâh yoktur. diye seslendi. Ey Rabbim! Sen, noksanlık ve zalimlikten uzaksın. Ben ise, kendime zulmettim. Şimdi tevbe edip pişman oldum. Bu sıkıntıyı benden gider. Hadiste şöyle buyurulmuştur: 'Sıkıntıya uğrayan her kim bu duayı yaparsa, duası kabul olunur.'" },
    {name : "Allahümme inneke afuvvün kerîmun tuhibbul afve fa'fu anni",description : "Hz. Aişe, Kadir Gecesi'ne ermenin şükrünü ve şevkini idrak etmek için Rasûlullah'a yönelip şöyle bir soru soruyor:Ya Rasûllallah, Kadir Gecesi'ne erme şerefine nail olursam nasıl dua edeyim, dedim: Rasûlullah da şu duayı okumamı söyledi:“Allahümme inneke afuvvün kerîmun tuhibbul afve fa'fu annî.”"},
    {name : "Allahumme Salli Ala Seyyidina Muhammedin Ve Ala Ali Seyyidina Muhammed", description : "Efendimiz (s.a.v.) buyuruyor:<br>“Üzerime Salâvat-ı Şerife getiren kimseleri melekler rahmetle anar, meleklerin rahmetle andıkları kimseyi Allah (c.c.) affeder. Allah’ın affettiği kimse için bütün varlıklar rahmet okurlar.” <br> “Üzerime bir defacık Salâvat-ı Şerife getiren kimse için Allah Teala görevli meleklere:Bu kulumun üç gün içerisinde meydana gelen günahlarını yazmayınız emrini verir.”<br> “Üzerime bin defa Salâvat getiren kimseye Allah (c.c.) narı ile azab etmez.”<br>“Cibril bana: Ya Muhammed (s.a.v.) Sana senden önce hiçbir kimseye getirmedi im bir müjde ile geldim. Allah Teala senin için söyle buyurdu:Ümmetin den kim ayakta iken üç defa Salâvat getirirse, oturmadan önce Allah (c.c.) onu bağışlar. Otururken üç defa getirirse kalkmadan Allah’ın affına mazhar olur, buyurunca efendimiz (s.a.v.) bu müjdeler üzerine şükür secdesine kapandı.”<br>“Kim sabahları üzerime onar defa Salâvat getirirse kırk senelik günahı silinir.”<br>“Cuma günü üzerime yüz defa Salâvat getirenin seksen yıllık hatalarını Allah (c.c.) affeder.”<br>“Üzerime Cuma günü veya gecesi yüz defa Salâvat okuyan kimsenin yüz türlü haceti kabul edilir.”<br>“Bin defa üzerime Salâvat getiren ölmeden önce cennetle müjdelenir.”<br>“Cebrail (a.s.) bana gelerek: Ey Allah’ın Resulü, senin üzerine Salâvat getiren kimse için yetmiş bin melek istiğfar getirir, buyurdu.”<br>“Üzerime getirilen Salâvat sırat üzerinde bir nurdur.”<br>“İnsanların bana en yakını üzerime en çok Salâvat getirenidir.”<br>“Allah’ın yeryüzünde gezen melekleri vardır. Ümmetimin üzerime getirdikleri Salatü selamları bana ulaştırırlar. Getirdikleri Salatü selam bana ulaşır ulaşmaz ben de onlar için isti far ederim.”<br>“Üzerime Salâvat getirenlere kıyamet günü şefaatçi olurum. Salâvat getirmeyenden ise uzağım.”"}
]

function createDatabaseAndTables(){
	db = window.openDatabase("sunnah", "1.0", "SunnahDB", 1000000);

    db.transaction(function(tx) {
        tx.executeSql("CREATE TABLE IF NOT EXISTS sunnah (name text unique primary key)");
    	loadSunnah();
    }, function(err){
        alert("Sünnet tablosu oluşmadı");
    });

    db.transaction(function(tx) {
        tx.executeSql("CREATE TABLE IF NOT EXISTS selectedsunnah (name text unique primary key, endtime date)");
    	//deleteZikir();
    }, function(err){
        alert("Seçilen Sünnet tablosu oluştu");
    });

    db.transaction(function(tx) {
        tx.executeSql("CREATE TABLE IF NOT EXISTS zikirler (name text, desct text)");
        loadZikir();
    }, function(err){
    	console.log(tx)
        alert("Zikir tablosu oluşmadı");
    });

    db.transaction(function(tx) {
        tx.executeSql("CREATE TABLE IF NOT EXISTS kazalar (name text unique primary key, count number)");
        //deleteKaza();
    }, function(err){
        console.log(tx)
        alert("Kaza tablosu oluşmadı");
    });
}

function loadSunnah(){
	db.transaction(function(tx) {
        tx.executeSql("SELECT * FROM sunnah",[], function(tx,res){
        	if(res.rows.length === 0){
        		sunnahs.forEach(function(sunnah){
					db.transaction(function(tx) {
						tx.executeSql("INSERT INTO sunnah (name) VALUES (?)", [sunnah], function(tx,res){

				        });
				    }, function(err){
				    	alert("Sünnetler Yüklenemedi")
				    });
				})
        	}
        });
    }, function(err){
    	console.log(err);
        alert("Veritabanı Problemi")
    });
}

function deleteKaza(){
	db.transaction(function(tx) {
        tx.executeSql("DROP TABLE kazalar",[], function(tx,res){
        	console.log(res)
        	
        });
    }, function(err){
    	console.log(err);
        alert("Veritabanı Problemi")
    });
}

function loadZikir(){
	db.transaction(function(tx) {
        tx.executeSql("SELECT * FROM zikirler",[], function(tx,res){
        	if(res.rows.length === 0){
        		zikir.forEach(function(z){
					db.transaction(function(tx) {
						tx.executeSql("INSERT INTO zikirler (name,desct) VALUES (?,?)", [z.name,z.description], function(tx,res){

				        });
				    }, function(err){
				    	console.log(err);
				    	alert("Zikirler Yüklenemedi")
				    });
				})
        	}
        });
    }, function(err){
    	console.log(err);
        alert("Veritabanı Problemi")
    });
}



createDatabaseAndTables();

