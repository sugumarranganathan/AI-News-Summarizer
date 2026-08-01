// ===========================================
// AI News Summarizer
// script.js
// ===========================================

const topic = document.getElementById("topic");
const searchBtn = document.getElementById("searchBtn");

const loading = document.getElementById("loading");

const news = document.getElementById("news");
const summary = document.getElementById("summary");
const translation = document.getElementById("translation");

// ===========================================
// Search Button
// ===========================================

searchBtn.addEventListener("click", searchNews);

// ===========================================
// Press Enter
// ===========================================

topic.addEventListener("keypress", function(event){

    if(event.key==="Enter"){

        searchNews();

    }

});

// ===========================================
// Search Function
// ===========================================

async function searchNews(){

    const value = topic.value.trim();

    if(value===""){

        alert("Please enter a news topic.");

        return;

    }

    loading.classList.remove("hidden");

    news.innerHTML="Searching latest news...";
    summary.innerHTML="Generating AI Summary...";
    translation.innerHTML="Translating into Tamil...";

    try{

        const response = await fetch("/summarize",{

            method:"POST",

            headers:{
                "Content-Type":"application/json"
            },

            body:JSON.stringify({

                topic:value

            })

        });

        const data = await response.json();

        news.innerHTML=data.news;

        summary.innerHTML=data.summary;

        translation.innerHTML=data.translation;

    }

    catch(error){

        news.innerHTML="Error fetching news.";

        summary.innerHTML="-";

        translation.innerHTML="-";

        console.log(error);

    }

    loading.classList.add("hidden");

}
