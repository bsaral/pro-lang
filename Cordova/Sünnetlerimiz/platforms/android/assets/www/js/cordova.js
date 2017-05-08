var list = [];
var x;

function getAllZikir(){
	db.transaction(function(tx) {
        tx.executeSql("select * from zikirler ", [], function(tx,res){
        	list = _.toArray(res.rows);
            getZikir();
        });
    }, function(err){
        console.log(err);
        alert("Zikirler Getirelemedi");
    });
}

function getZikir(){
	if(list.length !== 0){
		var num = _.random(list.length - 1)
		document.getElementById("zikirbox").style.display  = "block";
		document.getElementById("zikirname").innerHTML = list[num].name
		document.getElementById("zikirdesc").innerHTML = list[num].desct
		_.pullAt(list,num)
	}else{
		console.log("zikir bitti");
		getAllZikir();
	}
}

function updateSunnahTime(){
    var endtime = new Date(document.getElementById("endtime").value);
    var countDownDate = endtime.getTime();
    var now = new Date().getTime();
    if(countDownDate < now){
        $.simplyToast('Eski Tarihler Seçilemez', 'danger');
    }else{
        db.transaction(function(tx) {
            tx.executeSql("INSERT INTO selectedsunnah (endtime) VALUES (?)", [endtime], function(tx,res){
                console.log("zaman kaydedildi")
                getRandomSunnah();
                $.mobile.changePage("getsunnah.html")
            });
        }, function(err){
            console.log(err);
            alert("Zaman Kaydedilemedi");
        });
    }
}

function getRandomSunnah(){
	db.transaction(function(tx) {
		tx.executeSql("SELECT * FROM selectedsunnah ", [], function(tx,res){
            if(res.rows.length === 1){
            	if(res.rows[0].name === null){
	            	tx.executeSql("SELECT * FROM sunnah ", [], function(tx,res1){
			            if(res1.rows.length !== 0){
			            	var sunnahs = _.toArray(res1.rows);
			            	var num = _.random(sunnahs.length - 1)
			            	tx.executeSql("UPDATE selectedsunnah SET name='"+sunnahs[num].name+"' WHERE name IS NULL", [], function(tx,res2){
					            getTime(res.rows[0].endtime)
					            document.getElementById("getsunnahtext").innerHTML = sunnahs[num].name
					        });
			            }
			        });
	            }else{
	            	getTime(res.rows[0].endtime)
	            	document.getElementById("getsunnahtext").innerHTML = res.rows[0].name
	            }
            }else{
            	if(res.rows[0].name !== null){
            		getTime(res.rows[0].endtime)
            		document.getElementById("getsunnahtext").innerHTML = res.rows[0].name
            	}
            }
        });
    }, function(err){
        console.log(err);
        alert("Sünnet Bulunamadı");
    });
}

function getTime(time){
	var countDownDate = new Date(time).getTime();
	x = setInterval(function() {
	  var now = new Date().getTime();
      var distance = countDownDate - now;

      var days = Math.floor(distance / (1000 * 60 * 60 * 24));
      var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
      var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
      var seconds = Math.floor((distance % (1000 * 60)) / 1000);

      var clock = document.getElementById("clockdiv");
	  var daysSpan = clock.querySelector('.days');
	  var hoursSpan = clock.querySelector('.hours');
	  var minutesSpan = clock.querySelector('.minutes');
	  var secondsSpan = clock.querySelector('.seconds');

	  daysSpan.innerHTML = days;
      hoursSpan.innerHTML = hours
	  minutesSpan.innerHTML = minutes
	  secondsSpan.innerHTML =seconds
	  
	  if (distance < 0) {
	    clearInterval(x);
        $.simplyToast('Süreniz Dolmuştur. Lütfen Yeni Bir Sünnet Seçiniz', 'warning');
        resetSunnah();
	  }
	}, 1000);
}

function getSunnah(){
	db.transaction(function(tx) {
        tx.executeSql("SELECT * FROM selectedsunnah ", [], function(tx,res){
            if(res.rows.length !== 0){
            	$.mobile.changePage("getsunnah.html")
            	setTimeout(function(){getRandomSunnah();}, 500);
            }else{
            	$.mobile.changePage("sunnahtime.html")
            }
        });
    }, function(err){
        console.log(err);
        $.mobile.changePage("sunnahtime.html")
    });
}

function resetSunnah(){
	db.transaction(function(tx) {
        tx.executeSql("DELETE FROM selectedsunnah", [], function(tx,res){
            console.log("seçilen sünnet silindi")
            clearInterval(x);
            $.mobile.changePage("sunnahtime.html")
        });
    }, function(err){
        console.log(err);
        alert("seçilen sünnet silinemedi");
    });
}




