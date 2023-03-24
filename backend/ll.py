for i in range(12):
    print(
        """
        <b-form-file v-model="file{}" class="mt-3" plain></b-form-file>
       <div class="mt-3">教案{}: { { file{} ? file{}.name : '' } }</div>
        """.format(i+1, i+1, i+1, i+1)
    , end='')