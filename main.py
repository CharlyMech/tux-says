import os

message = os.environ.get('MSG')
msg_len = len(message)
tux = '''\t _nnnn_      **{up}**
        dGGGGMMb     | {msg} |
       @p~qp~~qMb    |_{down}_|
       M|@||@) M|  _|'
       @,----.JM|
      JS^\__/  qKL
     dZP        qKRb
    dZP          qKKb
   fZP            SMMb
   HZM            MMMM
   FqM            MMMM
 __| ".        |\dS"qML
 |    `.       | `' \Zq
_)      \.___.,|     .'
\____   )MMMMMP|   .'
     `-'       `--' hjm'''.format(up=msg_len*"*", msg=message, down=msg_len*"_")

print(tux)