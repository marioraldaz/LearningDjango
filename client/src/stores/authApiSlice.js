import { apiSlice} from "../api/apiSlice";

export const authApiSlice = apiSlice.injectEndpoints({
    endpoints: builder =>({
        login: builder.mutation({
            query: credentials => ({
                url: '/auth',
                method: 'POST',
                body: {...credentials}
            }),
            invalidatesTags: ['Users']
        }),
        register: builder.mutation({
            query: (data) => ({
                url: '/register',
                method: 'POST',
                body: JSON.stringify(data)
            }),
            invalidatesTags: ['Users']
        }),
        refresh: builder.mutation({
            query: (data) => ({
                url: '/refresh',
                method: 'POST',
                body: JSON.stringify(data)
            }),
            invalidatesTags: ['Users']
        })
    })
})

export const {
    useLoginMutation
} = authApiSlice