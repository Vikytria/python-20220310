window.onload = () =>  {
    document.querySelector("#submit_button").onclick = () => { 
        let name = document.querySelector("#name_input").value;
        document.querySelector("#message_p").innerHTML = "Hello " + name + "!";
        return false;
    };
}