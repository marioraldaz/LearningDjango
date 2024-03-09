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



const setCookie = (name, value, options = {}) => {
  const { expires, path } = options;
  let cookieString = `${name}=${value}`;

  if (expires) {
    cookieString += `; expires=${expires.toUTCString()}`;
  }

  if (path) {
    cookieString += `; path=${path}`;
  }

  document.cookie = cookieString;
};
