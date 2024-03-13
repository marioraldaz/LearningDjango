// selectors.js
import { createSelector } from "@reduxjs/toolkit";

export const selectProfileCookie = (state) => state.auth.profileCookie;
export const selectProfile = (state) => state.profile;
