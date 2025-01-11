import React, { createContext, useContext, useState, useEffect } from 'react';
import { auth } from '../firebase/firebase'; // Assuming this is your Firebase setup

const FirebaseContext = createContext({
    auth: null,
    user: null
});

export const useFirebase = () => {
    return useContext(FirebaseContext);
};

export const FirebaseProvider = ({ children }) => {
    const [user, setUser] = useState(null);

    useEffect(() => {
        // Listen to the auth state change to update the user when logged in or out
        const unsubscribe = auth.onAuthStateChanged((user) => {
            if (user) {
                setUser(user);
            } else {
                setUser(null);
            }
        });

        // Clean up the listener when the component is unmounted
        return () => unsubscribe();
    }, []);

    const FirebaseValue = {
        auth,
        user
    };

    return (
        <FirebaseContext.Provider value={FirebaseValue}>
            {children}
        </FirebaseContext.Provider>
    );
};
