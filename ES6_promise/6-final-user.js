import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default async function handleProfileSignup(firstName, lastName, fileName) {
  const array = await Promise.allSettled([signUpUser(firstName, lastName), uploadPhoto(fileName)]);
  return array;
}
