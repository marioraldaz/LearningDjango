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
  try {
      // Obtain CSRF token from Django cookie
      const csrftoken = getCookie('csrftoken');
      console.log(csrftoken);
       console.log(JSON.stringify(formData));
      // Make POST request with CSRF token included in headers
      const response = await fetch('http://localhost:8000/user/login/', {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json',
              'X-CSRFToken': csrftoken
          },
          body: JSON.stringify(formData),
          credentials: 'include' // Include cookies in the request
      });

      if (response.ok) {
          // Response status is in the range 200-299
          const data = await response.json();
          console.log('Login successful:', data);
      } else { 
          // Response status is not in the range 200-299
          throw new Error('Login failed with status code ' + response.status);
      }
  } catch (error) {
      console.error('Login failed:', error);
  }
}

