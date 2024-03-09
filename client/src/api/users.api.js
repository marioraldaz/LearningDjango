import axios from 'axios'

const UsersApi=axios.create({
    baseURL: "http://localhost:8000/user/api/v1/user/"
  })
export function getProfileByID(id){
   // const res = axios.get());
}

export function register(user){
  try{
    const { username, password, gender, date_of_birth,email } = user;
    return  UsersApi.post("/",{
      username: username,
      password: password,
      gender: gender,
      date_of_birth: date_of_birth,
      email
    });

  } catch (e) {
    console.log(e);
  }
}

export function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      var cookies = document.cookie.split(';');
      for (var i = 0; i < cookies.length; i++) {
          var cookie = cookies[i].trim();
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}
export async function logIn(formData) {
      const csrftoken = getCookie('csrftoken');
      console.log("csrf",csrftoken);
       console.log(JSON.stringify(formData));
       const response = await axios.post('http://localhost:8000/user/login/', formData, {
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        withCredentials: true // Include cookies in the request
    });
    

      if (response.ok) {
          const data = await response.json();
          console.log('Login successful:', data);
      } else { 
          throw new Error('Login failed with status code ' + response.status);
      }
}


