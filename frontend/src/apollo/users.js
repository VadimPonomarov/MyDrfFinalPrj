import {gql} from '@apollo/client';

export const USERS_ALL = gql`
    query Users {
        users {
            id
            lastLogin
            createdAt
            updatedAt
            email
            password
            isSuperuser
            isStaff
            isActive
        }
    }
`;