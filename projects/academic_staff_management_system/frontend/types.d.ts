type Person = {
  url: string;
  persian_first_name: string;
  persian_last_name: string;
  gender: string;
  date_of_birth: string;
  nationality: string;
  national_code: string;
  picture: string;
  user: string;
  home_address: string;
  educations: string[];
  phone_numbers: string[];
};

type User = {
  username: string;
  first_name: string;
  last_name: string;
  email: string;
  is_staff: boolean;
  is_active: boolean;
  is_superuser: boolean;
  last_login: string | null;
  date_joined: string;
};
