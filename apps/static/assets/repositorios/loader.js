

async function auten(){   
     await fetch('http://192.168.2.14:8001/user_unico/')
      .then(response => response.json())
      .then(data => {
          // Aquí se puede hacer algo con los datos obtenidos, como renderizarlos en una tabla o mostrarlos en una lista
          try{ 
   
            var token = localStorage.getItem('token');
            var usuario = JSON.parse(localStorage.getItem('usuario')) 
            if (usuario && token){
               
                Userdb = data.user;
                var usuarioBD = Userdb.find(u => u.username === usuario.username);
                if (usuarioBD.username == usuario.username){
                    document.querySelector('.dropdown-fl').style.display = 'block';
                }
                 else{
                    //window.location.replace(`/login/`);
                    window.location.href = `/login/`
                  
                 }
            }
            else{
               // window.location.replace(`/login/`);
                window.location.href = `/login/`
                
            }
        }
        catch{
            //window.location.replace(`/login/`);
           // window.location.href = `/login/`
            
        }
    })
      .catch(error => console.error(error));

   
    
}
