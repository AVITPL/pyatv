"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import pyatv.protocols.mrp.protobuf.Common_pb2
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _Command:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _CommandEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_Command.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    Unknown: _Command.ValueType  # 0
    Play: _Command.ValueType  # 1
    Pause: _Command.ValueType  # 2
    TogglePlayPause: _Command.ValueType  # 3
    Stop: _Command.ValueType  # 4
    NextTrack: _Command.ValueType  # 5
    PreviousTrack: _Command.ValueType  # 6
    AdvanceShuffleMode: _Command.ValueType  # 7
    AdvanceRepeatMode: _Command.ValueType  # 8
    BeginFastForward: _Command.ValueType  # 9
    EndFastForward: _Command.ValueType  # 10
    BeginRewind: _Command.ValueType  # 11
    EndRewind: _Command.ValueType  # 12
    Rewind15Seconds: _Command.ValueType  # 13
    FastForward15Seconds: _Command.ValueType  # 14
    Rewind30Seconds: _Command.ValueType  # 15
    FastForward30Seconds: _Command.ValueType  # 16
    SkipForward: _Command.ValueType  # 18
    SkipBackward: _Command.ValueType  # 19
    ChangePlaybackRate: _Command.ValueType  # 20
    RateTrack: _Command.ValueType  # 21
    LikeTrack: _Command.ValueType  # 22
    DislikeTrack: _Command.ValueType  # 23
    BookmarkTrack: _Command.ValueType  # 24
    SeekToPlaybackPosition: _Command.ValueType  # 45
    ChangeRepeatMode: _Command.ValueType  # 46
    ChangeShuffleMode: _Command.ValueType  # 47
    EnableLanguageOption: _Command.ValueType  # 53
    DisableLanguageOption: _Command.ValueType  # 54
    NextChapter: _Command.ValueType  # 25
    PreviousChapter: _Command.ValueType  # 26
    NextAlbum: _Command.ValueType  # 27
    PreviousAlbum: _Command.ValueType  # 28
    NextPlaylist: _Command.ValueType  # 29
    PreviousPlaylist: _Command.ValueType  # 30
    BanTrack: _Command.ValueType  # 31
    AddTrackToWishList: _Command.ValueType  # 32
    RemoveTrackFromWishList: _Command.ValueType  # 33
    NextInContext: _Command.ValueType  # 34
    PreviousInContext: _Command.ValueType  # 35
    ResetPlaybackTimeout: _Command.ValueType  # 41
    SetPlaybackQueue: _Command.ValueType  # 48
    AddNowPlayingItemToLibrary: _Command.ValueType  # 49
    CreateRadioStation: _Command.ValueType  # 50
    AddItemToLibrary: _Command.ValueType  # 51
    InsertIntoPlaybackQueue: _Command.ValueType  # 52
    ReorderPlaybackQueue: _Command.ValueType  # 55
    RemoveFromPlaybackQueue: _Command.ValueType  # 56
    PlayItemInPlaybackQueue: _Command.ValueType  # 57
    PrepareForSetQueue: _Command.ValueType  # 58
    SetPlaybackSession: _Command.ValueType  # 59
    PreloadedPlaybackSession: _Command.ValueType  # 60
    SetPriorityForPlaybackSession: _Command.ValueType  # 61
    DiscardPlaybackSession: _Command.ValueType  # 62
    Reshuffle: _Command.ValueType  # 63
    ChangeQueueEndAction: _Command.ValueType  # 135

class Command(_Command, metaclass=_CommandEnumTypeWrapper): ...

Unknown: Command.ValueType  # 0
Play: Command.ValueType  # 1
Pause: Command.ValueType  # 2
TogglePlayPause: Command.ValueType  # 3
Stop: Command.ValueType  # 4
NextTrack: Command.ValueType  # 5
PreviousTrack: Command.ValueType  # 6
AdvanceShuffleMode: Command.ValueType  # 7
AdvanceRepeatMode: Command.ValueType  # 8
BeginFastForward: Command.ValueType  # 9
EndFastForward: Command.ValueType  # 10
BeginRewind: Command.ValueType  # 11
EndRewind: Command.ValueType  # 12
Rewind15Seconds: Command.ValueType  # 13
FastForward15Seconds: Command.ValueType  # 14
Rewind30Seconds: Command.ValueType  # 15
FastForward30Seconds: Command.ValueType  # 16
SkipForward: Command.ValueType  # 18
SkipBackward: Command.ValueType  # 19
ChangePlaybackRate: Command.ValueType  # 20
RateTrack: Command.ValueType  # 21
LikeTrack: Command.ValueType  # 22
DislikeTrack: Command.ValueType  # 23
BookmarkTrack: Command.ValueType  # 24
SeekToPlaybackPosition: Command.ValueType  # 45
ChangeRepeatMode: Command.ValueType  # 46
ChangeShuffleMode: Command.ValueType  # 47
EnableLanguageOption: Command.ValueType  # 53
DisableLanguageOption: Command.ValueType  # 54
NextChapter: Command.ValueType  # 25
PreviousChapter: Command.ValueType  # 26
NextAlbum: Command.ValueType  # 27
PreviousAlbum: Command.ValueType  # 28
NextPlaylist: Command.ValueType  # 29
PreviousPlaylist: Command.ValueType  # 30
BanTrack: Command.ValueType  # 31
AddTrackToWishList: Command.ValueType  # 32
RemoveTrackFromWishList: Command.ValueType  # 33
NextInContext: Command.ValueType  # 34
PreviousInContext: Command.ValueType  # 35
ResetPlaybackTimeout: Command.ValueType  # 41
SetPlaybackQueue: Command.ValueType  # 48
AddNowPlayingItemToLibrary: Command.ValueType  # 49
CreateRadioStation: Command.ValueType  # 50
AddItemToLibrary: Command.ValueType  # 51
InsertIntoPlaybackQueue: Command.ValueType  # 52
ReorderPlaybackQueue: Command.ValueType  # 55
RemoveFromPlaybackQueue: Command.ValueType  # 56
PlayItemInPlaybackQueue: Command.ValueType  # 57
PrepareForSetQueue: Command.ValueType  # 58
SetPlaybackSession: Command.ValueType  # 59
PreloadedPlaybackSession: Command.ValueType  # 60
SetPriorityForPlaybackSession: Command.ValueType  # 61
DiscardPlaybackSession: Command.ValueType  # 62
Reshuffle: Command.ValueType  # 63
ChangeQueueEndAction: Command.ValueType  # 135
global___Command = Command

@typing.final
class QueueEndAction(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Enum:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _EnumEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[QueueEndAction._Enum.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        ClearAction: QueueEndAction._Enum.ValueType  # 0
        Reset: QueueEndAction._Enum.ValueType  # 2
        AutoPlay: QueueEndAction._Enum.ValueType  # 3

    class Enum(_Enum, metaclass=_EnumEnumTypeWrapper): ...
    ClearAction: QueueEndAction.Enum.ValueType  # 0
    Reset: QueueEndAction.Enum.ValueType  # 2
    AutoPlay: QueueEndAction.Enum.ValueType  # 3

    def __init__(
        self,
    ) -> None: ...

global___QueueEndAction = QueueEndAction

@typing.final
class DisableReason(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Enum:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _EnumEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[DisableReason._Enum.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        Unknown: DisableReason._Enum.ValueType  # 0
        AdPlayback: DisableReason._Enum.ValueType  # 1
        SkipLimitReached: DisableReason._Enum.ValueType  # 2

    class Enum(_Enum, metaclass=_EnumEnumTypeWrapper): ...
    Unknown: DisableReason.Enum.ValueType  # 0
    AdPlayback: DisableReason.Enum.ValueType  # 1
    SkipLimitReached: DisableReason.Enum.ValueType  # 2

    def __init__(
        self,
    ) -> None: ...

global___DisableReason = DisableReason

@typing.final
class PreloadedPlaybackSessionInfo(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PLAYBACKSESSIONIDENTIFIER_FIELD_NUMBER: builtins.int
    PLAYBACKSESSIONREVISION_FIELD_NUMBER: builtins.int
    PLAYBACKSESSIONPRIORITY_FIELD_NUMBER: builtins.int
    playbackSessionIdentifier: builtins.str
    playbackSessionRevision: builtins.str
    playbackSessionPriority: builtins.int
    def __init__(
        self,
        *,
        playbackSessionIdentifier: builtins.str | None = ...,
        playbackSessionRevision: builtins.str | None = ...,
        playbackSessionPriority: builtins.int | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["playbackSessionIdentifier", b"playbackSessionIdentifier", "playbackSessionPriority", b"playbackSessionPriority", "playbackSessionRevision", b"playbackSessionRevision"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["playbackSessionIdentifier", b"playbackSessionIdentifier", "playbackSessionPriority", b"playbackSessionPriority", "playbackSessionRevision", b"playbackSessionRevision"]) -> None: ...

global___PreloadedPlaybackSessionInfo = PreloadedPlaybackSessionInfo

@typing.final
class CommandInfo(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    COMMAND_FIELD_NUMBER: builtins.int
    ENABLED_FIELD_NUMBER: builtins.int
    ACTIVE_FIELD_NUMBER: builtins.int
    PREFERREDINTERVALS_FIELD_NUMBER: builtins.int
    LOCALIZEDTITLE_FIELD_NUMBER: builtins.int
    MINIMUMRATING_FIELD_NUMBER: builtins.int
    MAXIMUMRATING_FIELD_NUMBER: builtins.int
    SUPPORTEDRATES_FIELD_NUMBER: builtins.int
    LOCALIZEDSHORTTITLE_FIELD_NUMBER: builtins.int
    REPEATMODE_FIELD_NUMBER: builtins.int
    SHUFFLEMODE_FIELD_NUMBER: builtins.int
    PRESENTATIONSTYLE_FIELD_NUMBER: builtins.int
    SKIPINTERVAL_FIELD_NUMBER: builtins.int
    NUMAVAILABLESKIPS_FIELD_NUMBER: builtins.int
    SKIPFREQUENCY_FIELD_NUMBER: builtins.int
    CANSCRUB_FIELD_NUMBER: builtins.int
    SUPPORTEDPLAYBACKQUEUETYPES_FIELD_NUMBER: builtins.int
    SUPPORTEDCUSTOMQUEUEIDENTIFIERS_FIELD_NUMBER: builtins.int
    SUPPORTEDINSERTIONPOSITIONS_FIELD_NUMBER: builtins.int
    SUPPORTSSHAREDQUEUE_FIELD_NUMBER: builtins.int
    UPNEXTITEMCOUNT_FIELD_NUMBER: builtins.int
    PREFERREDPLAYBACKRATE_FIELD_NUMBER: builtins.int
    SUPPORTEDPLAYBACKSESSIONTYPES_FIELD_NUMBER: builtins.int
    CURRENTPLAYBACKSESSIONTYPES_FIELD_NUMBER: builtins.int
    PLAYBACKSESSIONIDENTIFIER_FIELD_NUMBER: builtins.int
    CURRENTQUEUEENDACTION_FIELD_NUMBER: builtins.int
    SUPPORTEDENDQUEUEACTIONS_FIELD_NUMBER: builtins.int
    DISABLEREASON_FIELD_NUMBER: builtins.int
    SUPPORTEDPLAYBACKSESSIONIDENTIFIERS_FIELD_NUMBER: builtins.int
    command: global___Command.ValueType
    enabled: builtins.bool
    active: builtins.bool
    localizedTitle: builtins.str
    minimumRating: builtins.float
    maximumRating: builtins.float
    localizedShortTitle: builtins.str
    repeatMode: pyatv.protocols.mrp.protobuf.Common_pb2.RepeatMode.Enum.ValueType
    shuffleMode: pyatv.protocols.mrp.protobuf.Common_pb2.ShuffleMode.Enum.ValueType
    presentationStyle: builtins.int
    skipInterval: builtins.int
    numAvailableSkips: builtins.int
    skipFrequency: builtins.int
    canScrub: builtins.int
    supportsSharedQueue: builtins.bool
    upNextItemCount: builtins.int
    preferredPlaybackRate: builtins.float
    playbackSessionIdentifier: builtins.str
    currentQueueEndAction: global___QueueEndAction.Enum.ValueType
    disableReason: global___DisableReason.Enum.ValueType
    @property
    def preferredIntervals(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.float]: ...
    @property
    def supportedRates(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.float]: ...
    @property
    def supportedPlaybackQueueTypes(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    @property
    def supportedCustomQueueIdentifiers(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def supportedInsertionPositions(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    @property
    def supportedPlaybackSessionTypes(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def currentPlaybackSessionTypes(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def supportedEndQueueActions(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[global___QueueEndAction.Enum.ValueType]: ...
    @property
    def supportedPlaybackSessionIdentifiers(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___PreloadedPlaybackSessionInfo]: ...
    def __init__(
        self,
        *,
        command: global___Command.ValueType | None = ...,
        enabled: builtins.bool | None = ...,
        active: builtins.bool | None = ...,
        preferredIntervals: collections.abc.Iterable[builtins.float] | None = ...,
        localizedTitle: builtins.str | None = ...,
        minimumRating: builtins.float | None = ...,
        maximumRating: builtins.float | None = ...,
        supportedRates: collections.abc.Iterable[builtins.float] | None = ...,
        localizedShortTitle: builtins.str | None = ...,
        repeatMode: pyatv.protocols.mrp.protobuf.Common_pb2.RepeatMode.Enum.ValueType | None = ...,
        shuffleMode: pyatv.protocols.mrp.protobuf.Common_pb2.ShuffleMode.Enum.ValueType | None = ...,
        presentationStyle: builtins.int | None = ...,
        skipInterval: builtins.int | None = ...,
        numAvailableSkips: builtins.int | None = ...,
        skipFrequency: builtins.int | None = ...,
        canScrub: builtins.int | None = ...,
        supportedPlaybackQueueTypes: collections.abc.Iterable[builtins.int] | None = ...,
        supportedCustomQueueIdentifiers: collections.abc.Iterable[builtins.str] | None = ...,
        supportedInsertionPositions: collections.abc.Iterable[builtins.int] | None = ...,
        supportsSharedQueue: builtins.bool | None = ...,
        upNextItemCount: builtins.int | None = ...,
        preferredPlaybackRate: builtins.float | None = ...,
        supportedPlaybackSessionTypes: collections.abc.Iterable[builtins.str] | None = ...,
        currentPlaybackSessionTypes: collections.abc.Iterable[builtins.str] | None = ...,
        playbackSessionIdentifier: builtins.str | None = ...,
        currentQueueEndAction: global___QueueEndAction.Enum.ValueType | None = ...,
        supportedEndQueueActions: collections.abc.Iterable[global___QueueEndAction.Enum.ValueType] | None = ...,
        disableReason: global___DisableReason.Enum.ValueType | None = ...,
        supportedPlaybackSessionIdentifiers: collections.abc.Iterable[global___PreloadedPlaybackSessionInfo] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["active", b"active", "canScrub", b"canScrub", "command", b"command", "currentQueueEndAction", b"currentQueueEndAction", "disableReason", b"disableReason", "enabled", b"enabled", "localizedShortTitle", b"localizedShortTitle", "localizedTitle", b"localizedTitle", "maximumRating", b"maximumRating", "minimumRating", b"minimumRating", "numAvailableSkips", b"numAvailableSkips", "playbackSessionIdentifier", b"playbackSessionIdentifier", "preferredPlaybackRate", b"preferredPlaybackRate", "presentationStyle", b"presentationStyle", "repeatMode", b"repeatMode", "shuffleMode", b"shuffleMode", "skipFrequency", b"skipFrequency", "skipInterval", b"skipInterval", "supportsSharedQueue", b"supportsSharedQueue", "upNextItemCount", b"upNextItemCount"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["active", b"active", "canScrub", b"canScrub", "command", b"command", "currentPlaybackSessionTypes", b"currentPlaybackSessionTypes", "currentQueueEndAction", b"currentQueueEndAction", "disableReason", b"disableReason", "enabled", b"enabled", "localizedShortTitle", b"localizedShortTitle", "localizedTitle", b"localizedTitle", "maximumRating", b"maximumRating", "minimumRating", b"minimumRating", "numAvailableSkips", b"numAvailableSkips", "playbackSessionIdentifier", b"playbackSessionIdentifier", "preferredIntervals", b"preferredIntervals", "preferredPlaybackRate", b"preferredPlaybackRate", "presentationStyle", b"presentationStyle", "repeatMode", b"repeatMode", "shuffleMode", b"shuffleMode", "skipFrequency", b"skipFrequency", "skipInterval", b"skipInterval", "supportedCustomQueueIdentifiers", b"supportedCustomQueueIdentifiers", "supportedEndQueueActions", b"supportedEndQueueActions", "supportedInsertionPositions", b"supportedInsertionPositions", "supportedPlaybackQueueTypes", b"supportedPlaybackQueueTypes", "supportedPlaybackSessionIdentifiers", b"supportedPlaybackSessionIdentifiers", "supportedPlaybackSessionTypes", b"supportedPlaybackSessionTypes", "supportedRates", b"supportedRates", "supportsSharedQueue", b"supportsSharedQueue", "upNextItemCount", b"upNextItemCount"]) -> None: ...

global___CommandInfo = CommandInfo
