// useCookies.js
import { useState } from 'react';

export const useCookies = () => {
  const getCookies = () => {
    return document.cookie.split(';').reduce((cookies, cookie) => {
      const [name, value] = cookie.split('=').map(c => c.trim());
      cookies[name] = value;
      return cookies;
    }, {});
  };

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

  const deleteCookie = (name) => {
    document.cookie = `${name}=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;`;
  };

  return { getCookies, setCookie, deleteCookie };
};
