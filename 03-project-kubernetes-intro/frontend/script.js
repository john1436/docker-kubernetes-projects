const API_URL=" aba202ecd7456483d9b5dcb84834d53f-404033802.ap-south-1.elb.amazonaws.com";

async function loadTasks(){

    const response=await fetch(`${API_URL}/tasks`);

    const tasks=await response.json();

    const list=document.getElementById("taskList");

    list.innerHTML="";

    tasks.forEach(task=>{

        list.innerHTML+=`<li>${task.title}</li>`;

    });

}

async function addTask(){

    const title=document.getElementById("taskInput").value;

    await fetch(`${API_URL}/tasks`,{

        method:"POST",

        headers:{

            "Content-Type":"application/json"

        },

        body:JSON.stringify({

            title:title

        })

    });

    document.getElementById("taskInput").value="";

    loadTasks();

}

loadTasks();
