"""
The ledger_entry method returns a single ledger
object from the XAH Ledger in its raw format.
See ledger format for information on the
different types of objects you can retrieve.
`See ledger entry <https://xrpl.org/ledger_entry.html>`_
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List, Optional, Union

from typing_extensions import Self

from xahau.models.base_model import BaseModel
from xahau.models.requests.request import LookupByLedgerRequest, Request, RequestMethod
from xahau.models.required import REQUIRED
from xahau.models.utils import KW_ONLY_DATACLASS, require_kwargs_on_init
from xahau.models.xchain_bridge import XChainBridge


class LedgerEntryType(str, Enum):
    """Identifiers for on-ledger objects."""

    ACCOUNT = "account"
    AMENDMENTS = "amendments"
    AMM = "amm"
    CHECK = "check"
    DEPOSIT_PREAUTH = "deposit_preauth"
    DIRECTORY = "directory"
    DID = "did"
    ESCROW = "escrow"
    HOOK = "hook"
    HOOK_STATE = "hook_state"
    HOOK_DEFINITION = "hook_definition"
    FEE = "fee"
    HASHES = "hashes"
    OFFER = "offer"
    ORACLE = "oracle"
    PAYMENT_CHANNEL = "payment_channel"
    SIGNER_LIST = "signer_list"
    STATE = "state"
    TICKET = "ticket"
    NFT_OFFER = "nft_offer"
    URI_TOKEN = "uri_token"


@require_kwargs_on_init
@dataclass(frozen=True, **KW_ONLY_DATACLASS)
class DepositPreauth(BaseModel):
    """
    Required fields for requesting a DepositPreauth if not querying by
    object ID.
    """

    owner: str = REQUIRED  # type: ignore
    """
    This field is required.

    :meta hide-value:
    """

    authorized: str = REQUIRED  # type: ignore
    """
    This field is required.

    :meta hide-value:
    """


@require_kwargs_on_init
@dataclass(frozen=True, **KW_ONLY_DATACLASS)
class Directory(BaseModel):
    """
    Required fields for requesting a DirectoryNode if not querying by
    object ID.
    """

    owner: str = REQUIRED  # type: ignore
    """
    This field is required.

    :meta hide-value:
    """

    dir_root: str = REQUIRED  # type: ignore
    """
    This field is required.

    :meta hide-value:
    """
    sub_index: Optional[int] = None


@require_kwargs_on_init
@dataclass(frozen=True, **KW_ONLY_DATACLASS)
class Escrow(BaseModel):
    """
    Required fields for requesting a Escrow if not querying by
    object ID.
    """

    owner: str = REQUIRED  # type: ignore
    """
    This field is required.

    :meta hide-value:
    """

    seq: int = REQUIRED  # type: ignore
    """
    This field is required.

    :meta hide-value:
    """


@require_kwargs_on_init
@dataclass(frozen=True, **KW_ONLY_DATACLASS)
class Offer(BaseModel):
    """
    Required fields for requesting a Offer if not querying by
    object ID.
    """

    account: str = REQUIRED  # type: ignore
    """
    This field is required.

    :meta hide-value:
    """

    seq: int = REQUIRED  # type: ignore
    """
    This field is required.

    :meta hide-value:
    """


@require_kwargs_on_init
@dataclass(frozen=True, **KW_ONLY_DATACLASS)
class Oracle(BaseModel):
    """
    Required fields for requesting a Price Oracle Ledger Entry, if not querying by
    object ID.
    """

    account: str = REQUIRED  # type: ignore
    """
    This field is required.

    :meta hide-value:
    """

    oracle_document_id: Union[str, int] = REQUIRED  # type: ignore
    """
    This field is required.

    :meta hide-value:
    """


@require_kwargs_on_init
@dataclass(frozen=True)
class RippleState(BaseModel):
    """Required fields for requesting a RippleState if not querying by object ID."""

    accounts: List[str] = REQUIRED  # type: ignore
    """
    This field is required.

    :meta hide-value:
    """

    currency: str = REQUIRED  # type: ignore
    """
    This field is required.

    :meta hide-value:
    """


@require_kwargs_on_init
@dataclass(frozen=True, **KW_ONLY_DATACLASS)
class Ticket(BaseModel):
    """Required fields for requesting a Ticket if not querying by object ID."""

    owner: str = REQUIRED  # type: ignore
    """
    This field is required.

    :meta hide-value:
    """

    ticket_sequence: int = REQUIRED  # type: ignore
    """
    This field is required.

    :meta hide-value:
    """


@require_kwargs_on_init
@dataclass(frozen=True, **KW_ONLY_DATACLASS)
class XChainClaimID(XChainBridge):
    """Required fields for requesting an XChainClaimID if not querying by object ID."""

    xchain_claim_id: Union[int, str] = REQUIRED  # type: ignore
    """
    The `XChainClaimID` associated with a cross-chain transfer, which was created in an
    `XChainCreateClaimID` transaction. This field is required.

    :meta hide-value:
    """


@require_kwargs_on_init
@dataclass(frozen=True, **KW_ONLY_DATACLASS)
class XChainCreateAccountClaimID(XChainBridge):
    """
    Required fields for requesting an XChainCreateAccountClaimID if not querying by
    object ID.
    """

    xchain_create_account_claim_id: Union[int, str] = REQUIRED  # type: ignore
    """
    The `XChainCreateAccountClaimID` associated with a cross-chain account create. This
    field is required.

    :meta hide-value:
    """


@require_kwargs_on_init
@dataclass(frozen=True, **KW_ONLY_DATACLASS)
class Hook(BaseModel):
    """
    Required fields for requesting a Hook if not querying by
    object ID.
    """

    account: str = REQUIRED  # type: ignore
    """
    This field is required.

    :meta hide-value:
    """


@dataclass(frozen=True, **KW_ONLY_DATACLASS)
class HookState(BaseModel):
    """
    Required fields for requesting a Hook if not querying by
    object ID.
    """

    account: str = REQUIRED  # type: ignore
    """
    This field is required.

    :meta hide-value:
    """

    key: str = REQUIRED  # type: ignore
    """
    This field is required.

    :meta hide-value:
    """

    namespace_id: str = REQUIRED  # type: ignore
    """
    This field is required.

    :meta hide-value:
    """


@require_kwargs_on_init
@dataclass(frozen=True, **KW_ONLY_DATACLASS)
class HookDefinition(BaseModel):
    """
    Required fields for requesting a Hook if not querying by
    object ID.
    """

    hook_definition: str = REQUIRED  # type: ignore
    """
    This field is required.

    :meta hide-value:
    """


@dataclass(frozen=True)
class ImportVLSequence(BaseModel):
    """
    Required fields for requesting a ImportVLSequence if not querying by
    object ID.
    """

    public_key: str = REQUIRED  # type: ignore
    """
    This field is required.

    :meta hide-value:
    """


@require_kwargs_on_init
@dataclass(frozen=True, **KW_ONLY_DATACLASS)
class EmittedTxn(BaseModel):
    """
    Required fields for requesting a Hook if not querying by
    object ID.
    """

    emitted_txn: str = REQUIRED  # type: ignore
    """
    This field is required.

    :meta hide-value:
    """


@require_kwargs_on_init
@dataclass(frozen=True, **KW_ONLY_DATACLASS)
class URIToken(BaseModel):
    """
    Required fields for requesting a URIToken if not querying by
    object ID.
    """

    issuer: str = REQUIRED  # type: ignore
    """
    This field is required.

    :meta hide-value:
    """

    uri: str = REQUIRED  # type: ignore
    """
    This field is required.

    :meta hide-value:
    """


@require_kwargs_on_init
@dataclass(frozen=True, **KW_ONLY_DATACLASS)
class LedgerEntry(Request, LookupByLedgerRequest):
    """
    The ledger_entry method returns a single ledger
    object from the XAH Ledger in its raw format.
    See ledger format for information on the
    different types of objects you can retrieve.
    `See ledger entry <https://xrpl.org/ledger_entry.html>`_
    """

    method: RequestMethod = field(default=RequestMethod.LEDGER_ENTRY, init=False)
    index: Optional[str] = None
    account_root: Optional[str] = None
    check: Optional[str] = None
    deposit_preauth: Optional[Union[str, DepositPreauth]] = None
    did: Optional[str] = None
    directory: Optional[Union[str, Directory]] = None
    emitted_txn: Optional[Union[str, EmittedTxn]] = None
    escrow: Optional[Union[str, Escrow]] = None
    hook: Optional[Union[str, Hook]] = None
    hook_definition: Optional[Union[str, HookDefinition]] = None
    hook_state: Optional[Union[str, HookState]] = None
    import_vlseq: Optional[Union[str, ImportVLSequence]] = None
    offer: Optional[Union[str, Offer]] = None
    oracle: Optional[Oracle] = None
    payment_channel: Optional[str] = None
    ripple_state: Optional[RippleState] = None
    ticket: Optional[Union[str, Ticket]] = None
    bridge_account: Optional[str] = None
    bridge: Optional[XChainBridge] = None
    xchain_claim_id: Optional[Union[str, XChainClaimID]] = None
    xchain_create_account_claim_id: Optional[
        Union[str, XChainCreateAccountClaimID]
    ] = None
    uri_token: Optional[Union[str, URIToken]] = None
    ledger_hash: Optional[str] = None
    ledger_index: Optional[Union[str, int]] = None

    binary: bool = False
    nft_page: Optional[str] = None
    """Must be the object ID of the NFToken page, as hexadecimal"""

    def _get_errors(self: Self) -> Dict[str, str]:
        errors = super()._get_errors()
        query_params = [
            param
            for param in [
                self.index,
                self.account_root,
                self.check,
                self.deposit_preauth,
                self.did,
                self.directory,
                self.emitted_txn,
                self.escrow,
                self.hook,
                self.hook_definition,
                self.hook_state,
                self.import_vlseq,
                self.offer,
                self.oracle,
                self.payment_channel,
                self.ripple_state,
                self.ticket,
                self.uri_token,
                self.xchain_claim_id,
                self.xchain_create_account_claim_id,
            ]
            if param is not None
        ]
        if (
            len(query_params) != 1
            and self.bridge is None
            and self.bridge_account is None
        ):
            errors["LedgerEntry"] = "Must choose exactly one data to query"

        if (self.bridge is None) != (self.bridge_account is None):
            # assert that you either have both of these or neither
            errors["Bridge"] = "Must include both `bridge` and `bridge_account`."

        return errors
