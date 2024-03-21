export const getActivityLevelByNumber = (number) => {
  switch (number) {
    case 1:
      return "sedentary";
    case 2:
      return "lightly_active";
    case 3:
      return "moderately_active";
    case 4:
      return "very_active";
    case 5:
      return "super_active";
    default:
      return "";
  }
};

export const cmToMeters = (heightCm) => {
  return (heightCm / 100).toFixed(2);
};

export const calculateAge = (birthDateString) => {
  const birthDate = new Date(birthDateString);
  const currentDate = new Date();
  const timeDifference = currentDate.getTime() - birthDate.getTime();
  const ageInYears = Math.floor(
    timeDifference / (1000 * 60 * 60 * 24 * 365.25)
  );
  return ageInYears;
};
