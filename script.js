const API="http://127.0.0.1:5000";

async function scan(){

let res=await fetch(API+"/scan");

let data=await res.json();

document.getElementById("count").innerText=
data.faces_detected;
loadStats();

}

async function loadStats(){

let res=await fetch(API+"/stats");

let stats=await res.json();

let list=document.getElementById("stats");

list.innerHTML="";

stats.forEach(s=>{

let li=document.createElement("li");

li.innerText=s.time+" : "+s.count+" viewers";

list.appendChild(li);

});

loadSuggestion();

}

async function loadSuggestion(){

let res=await fetch(API+"/suggestion");

let data=await res.json();

document.getElementById("suggestion").innerText=
data.suggestion;

}
function bookSlot(name,price){

let advertiser = prompt(
"Enter Advertiser / Brand Name:"
);

if(!advertiser){
alert("Booking cancelled");
return;
}

let duration = prompt(
"How many weeks do you want to book?"
);

if(!duration){
alert("Booking cancelled");
return;
}

let total = parseInt(duration)*parseInt(
price.replace(/\D/g,'')
);

alert(
"Booking Confirmed!\n\n"+
"Advertiser: "+advertiser+"\n"+
"Billboard: "+name+"\n"+
"Duration: "+duration+" weeks\n"+
"Total Cost: ₹"+total
);

}