import React from 'react';
import {useQuery} from '@apollo/client';
import {USERS_ALL} from '../apollo/users';

const UserList = () => {
    const {loading, error, data} = useQuery(USERS_ALL);
    if (loading) return <div>...loading</div>;
    if (error) return <div>{error.message}</div>;

    return (
        <div>
            {!!data && data.users.map(({id, email}) => <div>{id} - {email}</div>)}
        </div>
    );
};

export default UserList;